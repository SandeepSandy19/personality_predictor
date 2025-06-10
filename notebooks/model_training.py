
#  Data Loading
import pandas as pd

# Load the dataset
df = pd.read_csv("../data/personality_data.csv")

# Drop rows with missing values
df = df.dropna()

# Preview the data
df.head()

#  Data Preprocessing
from sklearn.preprocessing import LabelEncoder

# Encode yes/no columns
yes_no_cols = ["stage_fear", "drained_after_socializing"]
le = LabelEncoder()
for col in yes_no_cols:
    df[col] = le.fit_transform(df[col])  # yes=1, no=0

# Encode target label
personality_map = {"introvert": 0, "extrovert": 1}
df["personality"] = df["personality"].map(personality_map)

#  Exploratory Data Analysis (EDA)
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x="personality", data=df)
plt.title("Personality Distribution")
plt.show()

# Model Training
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Features and target
X = df.drop("personality", axis=1)
y = df["personality"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

#  Model Evaluation
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#  Save the Model
import joblib
joblib.dump(model, "../app/model.pkl")

