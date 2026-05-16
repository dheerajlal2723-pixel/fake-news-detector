import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add labels
fake["label"] = "FAKE"
true["label"] = "REAL"

# Combine datasets
data = pd.concat([fake, true])

# Input and output
x = data["text"]
y = data["label"]

# Convert text into numbers
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

# Transform text
x_train = vectorizer.fit_transform(x_train)
x_test = vectorizer.transform(x_test)

# Train AI model
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(x_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("AI Model Trained Successfully")