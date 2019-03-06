import json

from bottle import get,request,response,post

from BottleServer.DB.Model.AdminModel import AdminModel


@post("/Admin/Login")
def LoginAdmin():
    data = request.json
    detail = dict()
    try:
        username = data["username"]
        password = data["password"]
        response.headers["Content-Type"] = "application/json"

        if username == "" or password == "":
            detail["message"] = "Username and Password Invalid"
        else:
            admObj = AdminModel()
            result = admObj.Login(username,password)
            if len(result) == 0:
                detail["message"] = "Username and Password Invalid"
            else :
                detail["message"] = "Login Succesfull"
    except:
        detail["message"] = "Username and Password Invalid"
    return json.dumps(detail)

@post("/Admin/AddNew")
def AddAdmin():
    data = request.json
    detail = dict()
    try:
        username = data["username"]
        password = data["password"]
        response.header["Content-Type"] = "application/json"

        admObj = AdminModel()
        result = admObj.AddAdmin(username,password)
        if result == True:
            detail["message"] = True
        else:
            detail["message"] = False
    except:
        detail["message"] = False
    return json.dumps(detail)