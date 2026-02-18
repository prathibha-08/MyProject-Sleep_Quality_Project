import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("dataset.csv")

# Encode categorical columns
le_caffeine = LabelEncoder()
le_interruptions = LabelEncoder()
le_quality = LabelEncoder()

df["Caffeine"] = le_caffeine.fit_transform(df["Caffeine"])
df["Sleep_Interruptions"] = le_interruptions.fit_transform(df["Sleep_Interruptions"])
df["Quality"] = le_quality.fit_transform(df["Quality"])

# Features and Target
X = df.drop("Quality", axis=1)
y = df["Quality"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "model.pkl")
joblib.dump(le_caffeine, "le_caffeine.pkl")
joblib.dump(le_interruptions, "le_interruptions.pkl")
joblib.dump(le_quality, "le_quality.pkl")

print("✅ Model trained and saved successfully!")
