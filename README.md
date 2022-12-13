# FastApi-BackendApi + Mongodb..
Python-FastApi  Rest Api 

install pip pipenv
activate enviroment
pipenv shell.
___________________________________________________________________________________________________________________________________________________________
Required dependencies fastapi:

# Fastening light Python Framework for API build
fastapi == 0.88.0

# Fast ASGI server implementation which helps in the interaction between your application and the backend 
uvicorn == 0.20.0

# Motor is a full-featured, non-blocking IO MongoDB driver for Python 
motor == 2.4.0
___________________________________________________________________________________________________________________________________________________________
run server 
# uvicorn main:app --reload

# http://127.0.0.1:8000/

After hit on browser you will get this response 

{
"status": "Success",
"message": "Success"
}



you can also test via swagger Ui and PostMan.

http://127.0.0.1:8000/docs

Request Body 

default
GET
/
Read Root

GET
/api/todo
Get Todo

GET
/api/todo/{title}
Get Todo By Title

DELETE
/api/todo/{title}
Delete Todo

POST
/api/todo/
Post Todo

PUT
/api/todo/{title}/
Put Todo

