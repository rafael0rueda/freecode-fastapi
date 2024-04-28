# README

Project using FastAPI, postgres, psycopg and sqlalquemy.

Remeber create the `.env` file in root of the proyect.

#### Create virtual enviroment py: `py -m venv venv`

#### To active the virtual enviroment use: `source venv/Scripts/activate`

#### Install FastAPI: `pip install fastapi[all]`

#### Install psycopg: `pip install psycopg`

#### Running the app:

Use uvicorn for runnig the app: `uvicorn app.main:app`.

Use reload **Only for development**: `uvicorn app.main:app --reload`.

To stop uvicorn runing in windows use _Ctrl + C_ then _Enter_ or _Ctrl + Break_

### Runing in linux server

Install in the venv of the server uvtool, httptools and gunicorn.

To run the app in the server use:

`gunicorn -w 4 -k uvicorn.wokers.UvicornWorker app.main:app --bind 0.0.0.0:800`

Remenber to change the ip and port.

The other way is creating a service using the file _gunicorn.service_, change the information in the file to macth the server information where the app is going to be deploy, then create a service in the server. 
