import pickle
import os

BASE_DIR = os.path.dirname(__file__)

REGRESSION_MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "regression_model.pkl")
CLASSIFICATION_MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "classification_best_model.pkl")


def load_model(task_type):
    """
    task_type: 'regression' or 'classification'
    """

    if task_type == "regression":
        model_path = REGRESSION_MODEL_PATH

    elif task_type == "classification":
        model_path = CLASSIFICATION_MODEL_PATH

    else:
        raise ValueError(f"Unknown task_type: {task_type}")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    return model
