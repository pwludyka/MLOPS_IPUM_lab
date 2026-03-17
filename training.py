from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import joblib


def load_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y


def train_model():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1, stratify=y
    )

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
    ppn.fit(X_train_std, y_train)

    y_pred = ppn.predict(X_test_std)
    print("Accuracy: ", accuracy_score(y_test, y_pred))

    return ppn, sc


def save_model():
    trained_model, scaler = train_model()
    joblib.dump({"model": trained_model, "scaler": scaler}, "model.joblib")
    print("Model saved as model.joblib")


if __name__ == "__main__":
    save_model()
