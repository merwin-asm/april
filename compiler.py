"""
April compiler v 1.0.0

Author : Merwin 
"""


import os
import sys
import json
import random
import hashlib 
from rich import print




base_code = """
##############################################
#Auto-generated code by April compiler v1.0.0
##############################################


from fastapi import FastAPI, Request, Response, status, Depends
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis
from contextlib import asynccontextmanager
import aioredis
import ipaddress
import random
import json
import time
import os


ON_GOING = []

NOT_ALLOWED = []

if ___NOT_ALLOWED_IP___ != None:
    f = open(___NOT_ALLOWED_IP___, "r")
    NOT_ALLOWED = f.read().split("\\n")
    f.close()



def gen_new_id():
    
    global ON_GOING
    
    while True:
        i = random.randint(1000000,900000000000000000000)
        if not i in ON_GOING:
            ON_GOING.append(i)
            return i
        

def wait_for_change(cur_id):
    while True:
        time.sleep(0.005)
        if os.path.exists("." + str(cur_id) + ".output"):
            f = open("." + str(cur_id) + ".output", "r")
            raw_data = f.read()
            
            if raw_data == "":
                continue

            data = json.loads(raw_data)
            
            f.close()
            os.remove("." + str(cur_id) + ".output")
            os.remove("." + str(cur_id) + ".input")

            return data


def check_ip(ip):

    if ___DISALLOW_PRIVATE_IP___:
        return not ipaddress.ip_address(ip).is_private
    
    if ip in NOT_ALLOWED:
        return False

    return True


RATE_LIMIT = ___RATE_LIMIT___
tags_metadata = ___TAGS___

@asynccontextmanager
async def lifespan(_: FastAPI):
    if RATE_LIMIT:
        redis_connection = redis.from_url("redis://localhost:6379", encoding="utf8")
        await FastAPILimiter.init(redis_connection)
        yield
        await FastAPILimiter.close()



app = FastAPI(title= "___TITLE___", version= "___VERSION___", description= "___DESC___", docs_url= "___IF_DOCS___", redoc_url= None,
        openapi_tags=tags_metadata, lifespan=lifespan)




"""


api_code = """


@app.__type__("__end_point__", ___ADD___)
async def __fun_name__(__params__ request: Request, response: Response):
    cli_ip = request.client.host
    if not check_ip(cli_ip):
        return {"err" : "Not Allowed"}

    current_id = gen_new_id()
    f = open("." + str(current_id) + ".input", "w")
    f.write(json.dumps({"request" : dict(request), "input" : __get_params__}))
    f.close()
    os.system(f"__command__ {current_id}")
    data = wait_for_change(current_id)
    try:
        resp = data["output"]
    except:
        resp = ""
    try:
        response.headers = data["headers"]
    except:
        pass
    status = 200
    try:
        if data["status"] != "":
            status = data["status"]
    except:
        pass

    response.status_code = status
    ON_GOING.remove(current_id)
    return resp

"""




def lts(s):
    str1 = ""
 
    for ele in s:
        str1 += ele

    return str1




def get_params(end_point):
    params = []

    e = end_point.split("/")
    
    while True:
        try:
            e.remove("")
        except:
            break

    for x in e:
        if x.startswith("{"):
            x = x.replace("{", "")
            x = x.replace("}", "")
            
            params.append(x)
    
    return params



def format_params(params):
    a = ""
    for e in params:
        a += e + ", "
    
    return a



def get_return_params(params):
    a = "{\n"
    
    for e in params:
        a += f"\t\t '{e}' : {e}, \n"

    a += "}"

    return a



def get_query_params(params):
    query_params = []

    for e in params.split("<"):
        if e.endswith(">"):
            query_params.append(e.replace(">", ""))
    
    return params.split("<")[0] , query_params



def cure_gen_command(command):
    split_ = command.split(":")
    main_part = split_[0]
    cmd = split_[1]

    return main_part.replace(" ", "") + ":" + cmd


def import_apls(commands):
    extras = "\n"
    for e in commands:
        if e.startswith("IMPORT"):
            e = e.replace("IMPORT", "")
            e = e.replace(" ", "")
            e = e.replace("\n", "")
            e = e.replace("\t", "")

            extras = e

            try:
                f = open(extra + ".apl", "r")
                extras += f.read()
                f.close()
            except:
                print(f"WARN : Issue with using '{extra}.apl' ")

    x = ["GEN_DOC","RATE_LIMIT","TITLE","VERSION","DESC","DISALLOW_PRIVATE_IP","NOT_ALLOWED_IP","IMPORT", "//"]
    extras = extras.split("\n")
    for e in extras:
        for z in x:
            if e.startswith(z):
                extras.remove(e)
                break
        
    return extras

def compile(filename, newfilename):
    
    fun_id = 0


    if not os.path.exists(filename):
        print(f"[red]  ERROR :  Compiler - > '{filename}' Not found [/red]")
        return None
    
    f = open(filename)
    commands = f.read().split("\n")
    f.close()
    
    extras = import_apls(commands)

    commands = commands + extras
    
    compiled_code = base_code
    
    
    NAME_DESC = []

    ___IF_DOCS___ = None
    RATE_LIMIT = False
    RATE_LIMIT_PER = None
    TITLE = None
    VERSION = None
    DESC = None
    NOT_ALLOWED_IP = "None"
    DISALLOW_PRIVATE_IP = False

    for e in commands:
        if e.startswith("//"):
            continue

        if "//" in e:
            e = e.split("//")[0]

        if e in ["\n", "\t", " ", ""]:
            continue
                
        if e.startswith("GEN_DOC"):
            e = e.replace("GEN_DOC", "")
            e = e.replace(" ", "")
            e = e.replace("\n", "")
            e = e.replace("\t", "")

            if not e.startswith("/"):
                e = "/" + e

            ___IF_DOCS___ = e
        
            continue


        elif e.startswith("RATE_LIMIT"):
            e = e.replace("RATE_LIMIT", "")
            e = e.replace(" ", "")
            e = e.replace("\n", "")
            e = e.replace("\t", "")


            RATE_LIMIT = True
            RATE_LIMIT_PER = e
            
            continue

        elif e.startswith("TITLE"):
            e = e.replace("TITLE", "")
            e = e.split("'")[1]

            TITLE = e
            
            continue

        elif e.startswith("VERSION"):
            e = e.replace("VERSION", "")
            e = e.replace(" ", "")
            e = e.replace("\n", "")
            e = e.replace("\t", "")

            VERSION = e

            continue

        elif e.startswith("DESC"):
            e = e.replace("DESC", "")
            e = e.split("'")[1]

            DESC = e

            continue

        elif e.startswith("DISALLOW_PRIVATE_IP"):

            DISALLOW_PRIVATE_IP = True

            continue

        elif e.startswith("NOT_ALLOWED_IP"):
            e = e.replace("NOT_ALLOWED_IP", "")
            e = e.replace(" ", "")
            e = e.replace("\n", "")
            e = e.replace("\t", "")

            NOT_ALLOWED_IP = f'"e"'

            continue


        e = cure_gen_command(e)
        
        type_ = e.split("(")[0]
    
        end_point = lts(e.split("(")[1])
        end_point = end_point.split(")")[0]

        end_point , query_params = get_query_params(end_point)

        params = get_params(end_point) + query_params

        formated_params = format_params(params)
        return_params = get_return_params(params)

        command = e.split(":")[1]
        
        LIMIT = None
        
        ## CHecking for '--'

        z = e.split(":")[0]
        z = z.split(")")[1]
        z = z.split("--")
        
        DESC_E = ""
        NAME_E = ""
        NAME_DESC_ = {}

        for e in z:
            if e.startswith("L"):
                LIMIT = e.split("=")[1].replace(" ", "")

            elif e.startswith("N"):
                NAME_E = e.split("=")[1]

            elif e.startswith("D"):
                DESC_E = e.split("=")[1]
        
        if NAME_E != "":
            NAME_DESC_.setdefault("name", NAME_E)
            NAME_DESC_.setdefault("description", DESC_E)

            NAME_DESC.append(NAME_DESC_)


        chunk = api_code.replace("__type__", type_)
        chunk = chunk.replace("__end_point__", end_point)

        chunk = chunk.replace("__fun_name__", f"_{fun_id}")
        fun_id += 1

        chunk = chunk.replace("__params__", formated_params)
        chunk = chunk.replace("__get_params__", return_params)
        chunk = chunk.replace("__command__", command)
        
        if LIMIT != None:
            if NAME_E != "":
                chunk = chunk.replace("___ADD___", f"dependencies=[Depends(RateLimiter(times={LIMIT}, seconds=60))], tags=['{NAME_E}']")
            else:
                chunk = chunk.replace("___ADD___", f"dependencies=[Depends(RateLimiter(times={LIMIT}, seconds=60))]")
        elif RATE_LIMIT:
            if NAME_E != "":
                chunk = chunk.replace("___ADD___", f"dependencies=[Depends(RateLimiter(times={RATE_LIMIT_PER}, seconds=60))], tags=['{NAME_E}']")
            else:
                chunk = chunk.replace("___ADD___", f"dependencies=[Depends(RateLimiter(times={RATE_LIMIT_PER}, seconds=60))]")
        else:
            if NAME_E != "":
                chunk = chunk.replace("___ADD___", f"tags=['{NAME_E}']")
        compiled_code += "\n" + chunk

    
    compiled_code = compiled_code.replace("___IF_DOCS___", ___IF_DOCS___)
    compiled_code = compiled_code.replace("___RATE_LIMIT___", f"{RATE_LIMIT}")
    compiled_code = compiled_code.replace("___TITLE___", TITLE)
    compiled_code = compiled_code.replace("___VERSION___", VERSION)
    compiled_code = compiled_code.replace("___DESC___", DESC)
    compiled_code = compiled_code.replace("___NOT_ALLOWED_IP___", f'{NOT_ALLOWED_IP}')
    compiled_code = compiled_code.replace("___DISALLOW_PRIVATE_IP___", f"{DISALLOW_PRIVATE_IP}")
    compiled_code = compiled_code.replace("___TAGS___", str(NAME_DESC))
    
    runner = f"""

# RUNNING 
import uvicorn
if __name__ == "__main__":
    uvicorn.run("{newfilename.replace(".py", "")}:app")

    """

    compiled_code += runner

    f_ = open(newfilename, "w")
    f_.write(compiled_code)
    f_.close()


try:
    filename = sys.argv[1]
except:
    print("[red]  ERROR : Compiler - > Filename not provided[/red]")
    quit()

print(f"[blue]  MSG : Compiler - > Compiled file's name = {filename.replace('.', '_')}.py [/blue]")
newfilename = filename.replace(".", "_") + ".py"

print("[blue]  MSG : Compiler - > Compiling file[/blue]")

compile(filename, newfilename)



