# 🧠 Personality Prediction Bot (Introvert vs Extrovert)

This project uses machine learning to predict whether a person is an **Introvert** or **Extrovert** based on behavioral features such as social event frequency, time spent alone, and more.

Built with:
- ✅ **XGBoost Classifier**
- ✅ **Streamlit** for interactive web UI
- ✅ **Python, Pandas, Scikit-learn** for preprocessing and training

---

## 🚀 Live Demo

👉 [Click to try the app](https://introvert-or-extrovert.streamlit.app/)  


---

## 📊 Dataset

Source: [Kaggle - Extrovert vs. Introvert Behavior Data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)  
- Rows: ~2900  
- Cleaned rows after removing nulls: ~2477  
- Target: `personality` (`Introvert`, `Extrovert`)

---

## 📁 Project Structure

📦 personality-predictor
├── app/
│ ├── bot_app.py # Streamlit app
│ ├── model.pkl # Trained XGBoost model
├── model_training.ipynb # Jupyter Notebook for training
├── requirements.txt # Dependencies
└── README.md # Project documentation



---

## ⚙️ Features Used for Prediction

- `time_spent_alone` (hours)
- `stage_fear` (yes/no)
- `social_event_attendance` (0-10 scale)
- `going_outside` (0-10 scale)
- `drained_after_socializing` (yes/no)
- `friend_circle_size` (0-15)
- `post_freq_on_social_media` (0-10)

---

## 🧠 Model Performance

| Model                | Accuracy |
|---------------------|----------|
| Random Forest        | 91%      |
| **XGBoost (chosen)** | **92%**  |

---

## 🛠️ How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/personality-predictor.git
cd personality-predictor/app


Install Dependencies
pip install -r ../requirements.txt

To run APP
streamlit run bot_app.py
