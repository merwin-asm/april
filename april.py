def main():
    a = """
April v 1.0.0

A language for programming API's

# Some cool features : 

 - Maskes use Of FastAPI
 
 - Show API Statistics (If required)
 - Support Multiple Languages
 
 - Generate Documentation ( 'GEN_DOC {eg : /e/e/doc }' )
 - Rate Limiting ( 'RATE_LIMIT {how many per min}' )
 - Disallow Private IP ( 'DISALLOW_PRIVATE_IP' )
 - Not Allowed IP ( 'NOT_ALLOWED_IP {textfile.txt each ip sep by \n}' )
 
 - Other keywords:
    - TITLE '{}'
    - VERSION {}
    - DESC '{}'

 - Use '--':
    - --L = {call-per-min} (set limiting for a single endpoint)
    - --N = {Name for the end point} (to put in docs)
    - --D = {Desc for the end point} (to put in docs)


# Installng Redis and running manually
- sudo apt-get install redis-server
- Using uvicorn = uvicorn main:app --host 0.0.0.0 --port 80

Auther : Merwin
    """
    help_ = """
\t-h Help 
\t-a About
\t-c Compile eg: april -c <file.apl> | Compiles \n\t   the code to python saved in name file_apl.py (if the og name was file.apl)
\t-r Run eg: april -r <file.apl> <host:port> 
\t-v Version
    """

    import sys
    import os

    sys =  sys.argv

    if len(sys) == 1:
        print(help_)
        exit()

    if sys[1] == "-c":
        os.system(f"python3 compiler.py {sys[2]}")

    elif sys[1] == "-a":
        print(a)

    elif sys[1] == "-h":
        print(help_)

    elif sys[1] == "-r":
        nn = sys[2].split(".")[0:-1]
        n = ""
        for e in nn:
            n += e
        n += "_apl"

        os.system(f"python3 compiler.py {sys[2]}")
        os.system(f"uvicorn {n}:app --host {sys[3].split(':')[0]} --port {sys[3].split(':')[1]}")

    elif sys[1] == "-v":
        print("1.0.0")

    else:
        print("Command Not Found")

if __name__ == '__main__':
    main()


