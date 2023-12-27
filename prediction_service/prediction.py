import os
import yaml
import json
import joblib
import numpy as np

params_path = "params.yaml"
schema_path = os.path.join("prediction_service","schema_in.json")

class NotInRange(Exception):
    def __init__(self,message="Values not in range"):
        self.message = message
        super().__init__(self.message)

class NotInFeatureColumn(Exception):
    def __init__(self,message="Not part of feature columns"):
        self.message = message
        super().__init__(self.message)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def read_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(request_dict):
    def _validate_cols(col):
        schema = read_schema()
        act_cols = schema.keys()
        if col not in act_cols:
            raise NotInFeatureColumn

    def _validate_values(col,val):
        schema = read_schema()
        if not (schema[col]["min"] <= float(request_dict[col]) <= schema[col]["max"]):
            raise NotInRange

    for col, val in request_dict.items():
        _validate_cols(col)
        _validate_values(col,val)

    return True

def form_response(request_dict):
    if validate_input(request_dict):
        data = [list(map(float,request_dict.values()))]
        response = predict(data)
        return response

def api_response(request_dict):
    try:
        if validate_input(request_dict):
            data = np.array([list(request_dict.values())])
            response = predict(data)
            response = {"response":response}
            return response
    except NotInRange as e:
        response = {"the_expected_range": read_schema(), "response": str(e)}
        return response
    except NotInCols as e:
        response = {"the_exected_cols": get_schema().keys(), "response": str(e) }
        return response
    except Exception as e:
        response = {"response": str(e) }
        return response

def predict(data):
    config = read_params(params_path)
    model_dir= config["webapp_model_dir"]
    model = joblib.load(model_dir)
    prediction= model.predict(data).to_list()[0]
    try:
        if 3 <= prediction <= 8:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected result"

    return prediction[0]