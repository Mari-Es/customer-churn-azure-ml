from sklearn.metrics import accuracy_score
import json

def evaluate_model(model, X_test, y_test, metrics_path):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)


    with open(metrics_path, "w") as f:
        json.dump({"accuracy": acc}, f) 


    return acc