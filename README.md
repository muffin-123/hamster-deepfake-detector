# 🐹 Hamster - Deepfake Detection Library

`Hamster` is a lightweight Python library built around the MesoNet architecture for detecting deepfakes at the **frame level**. It provides an easy-to-use interface to load a trained model and predict whether an image is real or fake based on subtle mesoscopic features.

---

## 🔍 What is Hamster?

Hamster wraps a pre-trained [MesoNet](https://arxiv.org/abs/1809.00888) model and provides a simple API to:

* Load the model
* Predict the authenticity of a face image (Real or Fake)
* Use in local projects or backend APIs

---

## 📦 What's Inside

* ✅ `hamster/` - Python package folder
* ✅ `predictor.py` - Loads the model and makes predictions
* ✅ `mesonet_model.h5` - Trained model file (optional, hosted or downloadable)
* ✅ `requirements.txt` - Required dependencies
* ✅ `README.md` - Documentation

---

## 🚀 Installation & Setup

### 🔁 Clone the Repository

```bash
git clone https://github.com/muffin-123/hamster.git
cd hamster
pip install .

```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Usage Example

```python
from hamster import model_loader

# Predict an image
result = model_loader.predict_image("sample_image.jpg")
print(result)
```

Output:

```python
{'label': 'Fake', 'confidence': 0.9421}
```

---

## 📥 Pretrained Model

This library includes the pretrained MesoNet model (`mesonet_model.h5`) for deepfake detection.

📁 You can also find and download this model separately from its own repository here:  
🔗 [mesonet-trained-model (GitHub Repo)](https://github.com/muffin-123/mesonet-trained-model)

---
## 🏗️ How It Works

* The model is a CNN trained using the Meso-4 architecture.
* Takes a 256×256 image as input
* Returns a confidence score:

  * Closer to 1 → Fake
  * Closer to 0 → Real

---

## 📁 Library Folder Structure

```
hamster/
├── __init__.py
├── model_loader.py     # loads model + inference
├── predictor.py         # optional CLI or API utilities
├── mesonet_model.h5     # pretrained weights
├── requirements.txt
├── setup.py
└── README.md
```


