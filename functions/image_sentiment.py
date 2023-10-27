import keras
import numpy
from PIL import Image

classes = ["happy", "sad", "angry", "surprised", "disgusted", "fearful", "neutral"]

def predict(image: Image):
    model = keras.models.load_model("./model/model.keras")
    # X = Image.open("test1.jpg")
    X = image.convert("RGB")
    X = X.resize((128, 128))
    pred = model.predict(numpy.asarray([numpy.asarray(X)])).argmax(axis=1)
    # print(pred)
    # print(classes[pred[0]])
    return classes[pred[0]]