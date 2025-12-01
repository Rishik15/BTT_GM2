from model_loader import load_model

def model_prediction(X):

    model = load_model()

    pred = model.predict(X)

    return int(pred)