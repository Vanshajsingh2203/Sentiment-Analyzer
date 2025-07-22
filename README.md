# 🎬 Movie Review Sentiment Analyzer

## 📝 Overview

The Movie Review Sentiment Analyzer is a machine learning-powered application that classifies movie reviews as **Positive, Negative, or Neutral** based on sentiment analysis.Using a trained **Recurrent Neural Network (RNN)**, the app predicts the sentiment of user-inputted text and provides a confidence Score.

## ✨ Features

- 📝 Text-based Sentiment Analysis
- 📊 Confidence Score for Sentiment Prediction
- 🎭 Emoji-based Sentiment Representation
- 🎨 Modern, User-Friendly UI with Streamlit
- 📉 Visual Progress Bar for Sentiment Strength

## 🛠 Technology Stack

- Python
- Streamlit
- TensorFlow/Keras
- NumPy & Pandas
- RNN

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- TensorFlow installed
- Pretrained model (`SimpleRnn_imdb.h5`)
- Tokenizer file (`tokenizer.pkl`)

### Installation

1. Clone the repository
```bash
git clone https://github.com/taskmaster-1/sentiment-analyzer.git
cd sentiment-analyzer
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

## 📦 Requirements File

Create a `requirements.txt` with:
```txt
streamlit
tensorflow
numpy
pandas
pickle-mixin
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔒 Security

- Never commit your model files (`SimpleRnn_imdb.h5`) or tokenizer files (`tokenizer.pkl`) to public repositories
- Use `.gitignore` to exclude sensitive files

## 📊 How It Works

1. Enter a movie review in the text box
2. Click the "Analyze Sentiment" button
3. The model predicts the sentiment (**Positive, Negative, or Neutral**)
4. The confidence score is displayed
5. A visual progress bar shows sentiment strength

## 📈 Future Roadmap

- [ ] Improve model accuracy with advanced NLP techniques
- [ ] Deploy as a web app using Streamlit Sharing or Render
- [ ] Support for multiple languages
- [ ] Live API for sentiment prediction

## 🏷️ Versioning

Current Version: 1.0.0

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🌐 Deployed Application

### 🔗 Live 
- **Render**: [https://sentiment-analyzer-rncf.onrender.com]

## 📞 Contact

Gmail - [vivekyad5223@gmail.com](mailto:vivekyad5223@gmail.com)

Project Link: [https://github.com/taskmaster-1/sentiment-analyzer](https://github.com/taskmaster-1/sentiment-analyzer)

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [IMDB Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)
- [Python](https://www.python.org/)
