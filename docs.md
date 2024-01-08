
# April 1.0.0

## About
This language was made for making API's great ease and more efficiency.

The language connects each API endpoint to a specific program/command, in case you want to write the code for the endpoint '/home' in python and '/generate' in Cpp - this can be done.

The language have packages for multiple languages for adapting april to the wanted language (some packages are made by the community too!!) . In case you dont find the required package for utilizing april in your wanted language - don't worry its easy to make a package for your own.


#### Note 
- You need python3, redis server and pip3 installed on your system
- You can install april via pip
- The file extention for april is .apl 


##

## Features

- Easy install
- Simple
- Efficient
- Inbuild ratelimiting features (if req)
- Auto-Generated API Docs (if req)
- Banned IPs
- Disallow Private IPs (if req)
- Cross platform

## Installation

WIndows :
```sh
pip install aprillang
```

Linux / MacOs:
```sh
pip3 install aprillang
```
## Commandline examples

Get the list of allowed commands
```sh
april -h
```

Get info of the language
```sh
april -a
```

Compile an .apl file (april file):
- This converts the april code to python3 code
- Compiled file is saved as filename without extention apl + '_apl.py'

```sh
april -c file.apl
```

Run an .apl file (start the API server):
- Format for the command is - april -r <filename> <host:port>

```sh
april -r file.apl 0.0.0.0:8080
```

Get the version of april:

```sh
april -v
```

## Code examples

### Keyword commands

- Generate Documentation ( 'GEN_DOC {eg : /e/e/doc }' )
- Rate Limiting ( 'RATE_LIMIT {how many per min}' )
- Disallow Private IP ( 'DISALLOW_PRIVATE_IP' )
- Not Allowed IP ( 'NOT_ALLOWED_IP {textfile.txt each ip sep by \n}' )
 
- Other keywords:
    - TITLE '{}'
    - VERSION {}
    - DESC '{}'

### General Commands

- General format : 

<request_type eg: get,post..>(<the api endpoint, use '{var-name}' when there is a variable in the endpoint url eg: '/home/page/{}') : <the code execute the program which handle the endpoint eg: python3 home.py>


example:
Making a Get endpoint:
```py
get('/home') : python3 home.py
```
Making a Get endpoint with 1/more variables:
```py
get('/home/page/{x}/para/{y}') : python3 home.py
```

Then the rest is done with the help of packages made for integrating april with them.
You can find the list of packages in the [home page](https://github.com/merwin-asm/april) .

### Properties

These are attributes which can be added to general commands

Uses '--'

- --L = {call-per-min} (set limiting for a single endpoint)
- --N = {Name for the end point} (to put in docs)
- --D = {Desc for the end point} (to put in docs)
## Support

For support, join our discord server https://discord.gg/PXMSPJXhXd.


## License

[MIT](https://choosealicense.com/licenses/mit/)

