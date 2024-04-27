# README

Project using FastAPI, postgres, psycopg.

Remeber create the `.env` file in root of the proyect.

#### Create virtual enviroment py: `py -m venv venv`

#### To active the virtual enviroment use: `source venv/Scripts/activate`

#### Install FastAPI: `pip install fastapi[all]`

#### Install psycopg `pip install psycopg`

#### Running the server:

Use uvicorn for runnig the service `uvicorn app.main:app`.
Use to reload **Only use for development** `uvicorn app.main:app --reload`. 

To stop uvicorn for runing in windows use _Ctrl + C_ then _Enter_ or _Ctrl + Break_
