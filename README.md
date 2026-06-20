Web-based Disease Prediction & Recommendation System built with [Streamlit](https://streamlit.io).

## Features

- **Heart Disease** — Logistic Regression model with 13 clinical parameters
- **Pneumonia** — VGG16 CNN model for chest X-ray classification
- **Skin Cancer** — CNN model classifying 7 types of skin lesions
- **Multidisease** — Naive Bayes model predicting 41 diseases from symptoms

## Setup

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Project Structure

```
WBDPRS/
├── streamlit_app.py          # Entrypoint with st.navigation
├── pages/
│   ├── heart.py              # Heart disease prediction
│   ├── pneumonia.py          # Pneumonia detection
│   ├── skin.py               # Skin cancer detection
│   └── multidisease.py       # Multi-disease prediction
├── model_vgg16.h5            # VGG16 model for pneumonia
├── best_model.h5             # CNN model for skin cancer
├── Training.csv              # Training data for multidisease
├── Testing.csv               # Testing data for multidisease
├── requirements.txt
└── LICENSE
```

## License

MIT

