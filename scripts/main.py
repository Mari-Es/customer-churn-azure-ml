import yaml
from pathlib import Path
from preprocessing import preprocess_data
from train import train_model
from evaluate import evaluate_model


ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT_DIR / 'config' / 'config.yaml'

with open(CONFIG_PATH, 'r') as f:
    cfg = yaml.safe_load(f)


X_train, X_test, y_train, y_test = preprocess_data(
    cfg['data']["path"],
    cfg["data"]["target"],
    cfg["training"]["test_size"],
    cfg["training"]["random_state"]

)

model = train_model(X_train, y_train, "outputs/model.pkl")
acc = evaluate_model(model, X_test, y_test, "outputs/metrics.json")

print(f"Training complete. Accuracy: {acc:3f}")