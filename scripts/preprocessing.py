from sklearn.model_selection import train_test_split
import pandas as pd


def preprocess_data(data_path,target,test_size,random_state):

    df=pd.read_csv(data_path)

    df["target"] = df["gender"].map({"Male": 1, "Female": 0})
    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    
    df = df.drop(columns=["customerID"],errors="ignore")
    df = df.dropna()


    X = df.drop(columns=[target])
    X = pd.get_dummies(X, drop_first=True)
    y=df[target]

    return train_test_split(X, y, test_size=test_size, random_state=random_state)