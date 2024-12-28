from tkinter import *
import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def transformar():
    link = inputt.get()
    if not link.strip():
        resultado.config(text="Por favor, insira um link válido.")
        return
    
    qr_imagem = qrcode.make(link)
    caminho_imagem = "qrcode.png"
    qr_imagem.save(caminho_imagem)
    
    img = Image.open(caminho_imagem)
    img = img.resize((150, 150))  
    qr_code_img = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_code_img)
    qr_label.image = qr_code_img
    
    resultado.config(text="QR Code gerado com sucesso!")


janela = Tk()
janela.title("Gerador de QR Code")


orientacao = Label(janela, text="Coloque o link desejado para gerar um QR Code:")
orientacao.grid(column=0, row=0, columnspan=2, padx=10, pady=5)

inputt = tk.Entry(janela, width=30)
inputt.grid(column=0, row=1, padx=10, pady=5, columnspan=2)

botao = Button(janela, text="Gerar", command=transformar)
botao.grid(column=0, row=2, columnspan=2, pady=10)

resultado = Label(janela, text="")
resultado.grid(column=0, row=3, columnspan=2, pady=5)

qr_label = Label(janela)
qr_label.grid(column=0, row=4, columnspan=2, pady=10)

janela.mainloop()
