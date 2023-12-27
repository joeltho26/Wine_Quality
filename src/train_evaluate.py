import os
import pandas as pd
import sys
import warnings
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from get_data import read_params
import argparse
import joblib
import json

def train_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]
    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    target = config["base"]["target_col"]
    scores = config["reports"]["scores"]
    params = config["reports"]["params"]

    train = pd.read_csv(train_data_path, sep=",", )
    test = pd.read_csv(test_data_path, sep=",", )

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target,axis=1)
    test_x = test.drop(target,axis=1)

    lr = ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_state)
    lr.fit(train_x,train_y)

    pred = lr.predict(test_x)
    (rmse,mae,r2) = eval_metrics(test_y,pred)

    print("ElasticNet model (alpha=%f, l1_ratio=%f):" %(alpha,l1_ratio))
    print("RMSE:{}", rmse)
    print("MAE:{}", mae)
    print("R2 Score:{}", r2)

    with open(scores,"w") as f:
        score = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        json.dump(score, f, indent=4)

    with open(params,"w") as f:
        param = {
            "alpha": alpha,
            "l1_ratio": l1_ratio
        }
        json.dump(param, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir,"model.joblib")
    joblib.dump(lr,model_path)

def eval_metrics(actual,pred):
    rmse = np.sqrt(mean_squared_error(actual,pred))
    mae = mean_absolute_error(actual,pred)
    r2 = r2_score(actual,pred)
    return rmse, mae, r2

if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument("--config",default="params.yaml")
    parsed_args = arg.parse_args()
    train_evaluate(config_path=parsed_args.config)