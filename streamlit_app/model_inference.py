from model_loader import load_model
import numpy as np


def model_prediction(X, task_type):
    model = load_model(task_type)

    if task_type == "regression":
        pred = model.predict(X)
        return float(pred[0])

    elif task_type == "classification":
        pred = model.predict(X)
        return int(pred[0]), None
