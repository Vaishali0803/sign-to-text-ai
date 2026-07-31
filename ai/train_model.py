import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

folder = "dataset/custom_dataset"

data = []

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path, header=None)

        print(f"{file}: shape = {df.shape}")
        print(df.tail(2))
        print("----------------")

        data.append(df)

dataset = pd.concat(data, ignore_index=True)

print("Dataset shape:", dataset.shape)
print(dataset.isna().sum())

# Features
X = dataset.iloc[:, :-1]

# Labels
y = dataset.iloc[:, -1]

print(dataset.iloc[:, -1].isna().sum())
print(dataset.iloc[:, -1].value_counts())

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training model...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy : {accuracy*100:.2f}%")

joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")