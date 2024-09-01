import cv2
import pickle
import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk

with open('svm_model.pkl', 'rb') as model_file:
    svm_model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))
    img = img.flatten().reshape(1, -1)
    img = scaler.transform(img)
    return img

def load_and_classify_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((350, 350))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
        
        processed_image = preprocess_image(file_path)
        prediction = svm_model.predict(processed_image)[0]
        
        if prediction == 1:
            result_text = (
                "O **Montreal Cognitive Assessment (MoCA)** é um teste de triagem cognitiva utilizado para avaliar diversas "
                "funções cognitivas, como memória, atenção, linguagem, habilidades visuoespaciais e funções executivas. "
                "O paciente obteve uma pontuação de **26 ou mais** no MoCA Score, o que sugere que ele apresenta uma cognição normal."
            )
        else:
            result_text = (
                "O **Montreal Cognitive Assessment (MoCA)** é um teste de triagem cognitiva utilizado para avaliar diversas "
                "funções cognitivas, como memória, atenção, linguagem, habilidades visuoespaciais e funções executivas. "
                "O paciente obteve uma pontuação inferior a **26** no MoCA Score, o que pode indicar comprometimento cognitivo leve "
                "ou mais significativo. Recomenda-se uma avaliação clínica mais aprofundada."
            )
        
        result_label.config(text=result_text, justify="left", wraplength=750)

root = tk.Tk()
root.title("Classificação de Imagens - MoCA Score")
root.geometry("800x600")
image_label = Label(root)
image_label.pack(pady=20)
load_button = tk.Button(root, text="Carregar Imagem", padx=10, pady=5, fg="white", bg="#263D42", command=load_and_classify_image)
load_button.pack()
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)
root.mainloop()
