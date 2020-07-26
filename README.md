# Quaker Parser  

## Prerequisites  

* Python3
* pip
* virtualenv

Make sure you have Python3 (>=3.6) to run this app.  
```
$ python3 -V
```  
If you get something like the message below, you can continue the guide. Otherwise, install Python3.  
```
Python 3.6.9
```

You must have pip installed. If you doesn't, install [here](https://pip.pypa.io/en/stable/installing/). Finally, install virtualenv with the command below.  
```
python -m pip install virtualenv
```

## Installation  

Run the command below and everything should be fine.  
**Start a new terminal before running the command.**
```
$ git clone https://github.com/bihellzin/quake-parser.git && cd quake-parser && python3 -m virtualenv .venv && source .venv/bin/activate && python3 -m pip install -r requirements-dev.txt
```  

## Running  

Run the command below and go to the link where uvicorn starts the app (usually http://localhost:8000/).  
```
$ uvicorn main:app --reload
```  
You must pass the parameter through the URL (http://localhost:8000/2).  
To run the script.py just run the command below and you can get the report of all games (that are in the games.log) in the command line.  
```
$ python3 script.py
```
