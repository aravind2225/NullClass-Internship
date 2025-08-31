from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import numpy as np
import pickle

# Load model
with open("xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Mapping function
def get_vehicle_type_numeric(vehicle_type: str):
    mapping = {"Premium": 1, "Economy": 0}
    return mapping.get(vehicle_type)

# Prediction API
@app.post("/predict")
async def predict(data: dict):
    number_of_riders = data.get("number_of_riders")
    number_of_drivers = data.get("number_of_drivers")
    vehicle_type = data.get("vehicle_type")
    Expected_Ride_Duration = data.get("Expected_Ride_Duration")

    vehicle_type_numeric = get_vehicle_type_numeric(vehicle_type)
    if vehicle_type_numeric is None:
        return {"error": "Invalid vehicle type"}

    input_data = np.array([[number_of_riders, number_of_drivers, vehicle_type_numeric, Expected_Ride_Duration]])
    predicted_price = model.predict(input_data)
    return {"prediction": float(predicted_price[0])}
