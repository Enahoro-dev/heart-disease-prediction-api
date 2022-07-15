from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app=FastAPI()
origins= ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

class model_input(BaseModel):
    Age: int
    Sex:int
    ChestPainType:int
    RestingBloodPressure:int
    SerumCholesterol:int
    FastingBloodSugar:int
    RestingElectrocardiogram:int
    MaximumHeartRate:int
    Angina:int
    OldPeak:float
    STSlope:int
    MajorVessels:int
    Thal:int

heart_model = pickle.load(open('heart_model.sav','rb'))

@app.post('/heart_prediction')
def heart_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    age=input_dictionary['Age']
    sex=input_dictionary['Sex']
    chest=input_dictionary['ChestPainType']
    bp=input_dictionary['RestingBloodPressure']
    chol=input_dictionary['SerumCholesterol']
    fbs=input_dictionary['FastingBloodSugar']
    ecg=input_dictionary['RestingElectrocardiogram']
    rate=input_dictionary['MaximumHeartRate']
    angina=input_dictionary['Angina']
    peak=input_dictionary['OldPeak']
    slope=input_dictionary['STSlope']
    vessels=input_dictionary['MajorVessels']
    thal=input_dictionary['Thal']

    input_list = [age, sex, chest, bp, chol, fbs, ecg, rate, angina, peak, slope, vessels, thal]
    prediction= heart_model.predict([input_list])

    if prediction[0]==0:
        return 'You are unlikely to have heart disease'
    else:
        return 'You may have heart disease'