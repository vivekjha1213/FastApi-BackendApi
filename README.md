# FastApi-BackendApi + Mongodb..


author @Vivek kumar jha 
Python-FastApi  Rest Api

For mac os use Pip3.

pip install fastapi

pip install "uvicorn[standard]"

install pip pipenv
activate Local environment

pipenv shell
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
/![Screenshot 2022-12-13 at 1 17 25 PM](https://user-images.githubusercontent.com/67068290/208139526-9aa142a1-abd5-43c9-8c1f-fe918b334a3b.png)

Request Body 

default
GET

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
-----------------------------------------------------------------------------------------------------------------------------------------------------------
![Screenshot 2022-12-13 at 1 16 10 PM](https://user-images.githubusercontent.com/67068290/208139668-5b648c61-1a94-4312-abf0-e699b2150bf6.png)


for Frontend Ui.

npm install node
npm start 

