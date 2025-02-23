# Sentiment-Analyzer
🎬 Sentiment Analyzer – Movie Review Analysis App Sentiment Analyzer is a powerful and intuitive web app that helps users determine the sentiment of their movie reviews. 

A simple and elegant sentiment analysis web app built with **Streamlit** and **TensorFlow**. This app predicts whether a given movie review is **Positive**, **Negative**, or **Neutral** using a pre-trained RNN model.

## 🚀 Features
- 📌 User-friendly interface with a modern design
- 🎭 Sentiment prediction with confidence score
- 🎯 Emoji-based sentiment visualization
- 📊 Progress bar indicating confidence level

## 📂 Project Structure
```
📦 Sentiment-Analyzer
├── 📄 app.py                # Main Streamlit app
├── 📄 requirements.txt      # Dependencies list
├── 📄 Dockerfile            # Docker setup
├── 📄 tokenizer.pkl         # Tokenizer for text preprocessing
├── 📄 SimpleRnn_imdb.h5     # Pre-trained RNN model
├── 📄 .env                  # Environment variables
└── 📄 README.md             # Project documentation
```

## 📥 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/taskmaster-1/sentiment-analyzer.git
cd sentiment-analyzer
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
streamlit run app.py
```

## 🐳 Running with Docker

### 1️⃣ Build the Docker Image
```sh
docker build -t sentiment-analyzer .
```

### 2️⃣ Run the Docker Container
```sh
docker run -p 8501:8501 sentiment-analyzer
```

## 🛠️ Technologies Used
- **Streamlit** (UI Framework)
- **TensorFlow/Keras** (Deep Learning)
- **NumPy & Pickle** (Data Processing)
- **Docker** (Containerization)

## 🤝 Contributing
Feel free to fork this repository and submit pull requests with improvements!

## 📄 License
This project is licensed under the **MIT License**.

---

💡 *Developed with ❤️ using AI and Machine Learning.*
