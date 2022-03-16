from flask import (
    Flask,
    request
)
from datetime import datetime
from app.database import (user, 
    vehicle, 
    report
)

app = Flask(__name__)
VERSION = "1.0.0"


@app.get("/ping")
def ping():
    resp = {
        "status": "ok",
        "message": "success",
    }
    return resp



@app.get("/verison")
def version():
    resp = {
        "status": "ok",
        "message": "success",
        "verison": VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:S")
    }
    return resp


@app.get("/users/<int:pk>")
def get_user_by_id(pk):
    target_user = user.select_by_id(pk)
    resp = {
        "status": "ok",
        "message": "success",
        "user" : target_user
    }
    return resp




@app.get("/users/")
def get_all_users():
    user_list = user.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "users": user_list
    }
    return resp



@app.post("/users/")
def create_user():
    user_data = request.json
    user.insert(user_data)
    return "", 204



@app.put("/users/<int:pk>")
def update_user(pk):
    user_data = request.json
    user.update(pk, user_data)
    return "", 204



@app.put("/deactivate/<int:pk>")
def deactivate_user(pk):
    user.deactivate_user(pk)
    return "", 204

@app.get("/vehicles/users/<int:pk>")
def get_vehicles_by_user_id(pk):
    vehicle_list = vehicle.select_by_user_id(pk)
    resp = {
        "status": "ok",
        "message": "success",
        "vehicle" : vehicle_list
    }
    return resp

@app.get("/reports/users/vehicles")
def get_users_and_vehicles_report():
    output = report.get_users_and_vehicles_join()
    resp = {
        "status": "ok",
        "message": "success",
        "report_data" : output
    }
    return resp


@app.get("/vehicles/")
def get_all_vehicles():
    vehicle_list = vehicle.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "vehicle": vehicle_list
    }
    return resp



@app.post("/vehicle/")
def create_vehicle():
    vehicle_data = request.json
    vehicle.insert(vehicle_data)
    return "", 204



@app.put("/vehicle/<int:pk>")
def update_vehicle(pk):
    vehicle_data = request.json
    vehicle.update(pk, vehicle_data)
    return "", 204



@app.put("/deactivate/<int:pk>")
def deactivate_vehicle(pk):
    vehicle.deactivate_vehicle(pk)
    return "", 204



