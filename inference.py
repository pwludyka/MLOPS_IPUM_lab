import joblib
import numpy as np

flowers_names = {0: "setosa", 1: "versicolor", 2: "virginica"}


def load_model():
    with open("model.joblib", "rb") as file:
        trained_model = joblib.load(file)
    return trained_model["model"], trained_model["scaler"]


def predict(features: dict):
    model, scaler = load_model()
    dimensions = np.array(
        [
            [
                features["sepal_length"],
                features["sepal_width"],
                features["petal_length"],
                features["petal_width"],
            ]
        ]
    )
    dimensions_std = scaler.transform(dimensions)
    prediction = model.predict(dimensions_std)
    return flowers_names[prediction[0]]
