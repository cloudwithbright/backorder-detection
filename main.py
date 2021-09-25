"""We are going to create an API for our model using 
FastAPI and test this API using Postman. Lets get started."""

#Import Libries
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

#Initialize FastAPI
app = FastAPI()

#Define our model(Input parameters)
class Parameters(BaseModel):
    potencial_issue: float #x0
    desck_risk: float #x1
    ppap_risk: float #x3
    rev_stop: float #x5
    local_bo_qty: float
    perf_6_month_avg: float    
   
#Load in model
model_4 = pickle.load(open("./model_4.pkl","rb"))

#Main Route
@app.get("/")
async def home():
    return {
        "title": "Backorder Detection using machine learning and Deep Learning techniques",
        "type": "API/json",
        "method": "POST",
        "route": "/api/v1/predict",
        "docs": "/docs"
    }
    
#Make prediction route
@app.post("/api/v1/predict")
async def make_prediction(data: Parameters):
    
    #Convert incoming dataset into a dictionary
    data = data.dict()
    
    #Reinitialize variables
    desck_risk = data["desck_risk"]
    ppap_risk = data["ppap_risk"]
    potencial_issue = data["potencial_issue"]
    local_bo_qty = data["local_bo_qty"]
    perf_6_month_avg = data["perf_6_month_avg"]
    rev_stop = data["rev_stop"]
    
    #Make prediction
    make_prediction = model_4.predict([[desck_risk,ppap_risk,
    potencial_issue,local_bo_qty,perf_6_month_avg,rev_stop]])

    #Return custom values
    if make_prediction[0] > 0.5:
        
        return {
            "message": "Product will be in backorder soon"
            }        
    else:
        return {
            "message": "Product will not be in backorder"
            }
    