## Basic Implementation 

``` javascript
import json
import requests

url = 'https://heart-ml-api.herokuapp.com/heart_prediction'

input_data_for_model = {
    'Age': int
    'Sex':int
    'ChestPainType':int
    'RestingBloodPressure':int
    'SerumCholesterol':int
    'FastingBloodSugar':int
    'RestingElectrocardiogram':int
    'MaximumHeartRate':int
    'Angina':int
    'OldPeak':float
    'STSlope':int
    'MajorVessels':int
    'AverageHeartRate':int
}

input_json = json.dumps(input_data_for_models)
response = requests.post(url, data=input_json)
print(response.text)
```
