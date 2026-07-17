#importando tkinter
from tkinter import*

#iportar pillow
from PIL import Image, ImageTk

#cores usadas 
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue


#criaçao de janela
janela = Tk ()
janela.title ("")
janela.geometry('350x200')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


#divisao de janela 

frame_logo = Frame(janela, width=350, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


#configurando o frame_logo 
imagem = Image.open('icon-speed.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=20, y=0)
l_logo_nome = Label(frame_logo, text='Speed Test', padx=10, anchor=NE , font=('Ivy 20 bold'), bg=co1, fg=co4)
l_logo_nome.place(x=100, y=15)

l_logo_linha = Label(frame_logo, width=350 , anchor=NW , font=('Ivy 1'), bg=co2)
l_logo_linha.place(x=0, y=57)

#configurando o frame_corpo

l_download = Label(frame_corpo, text='65.7', anchor=NW , font=('arial 28'), bg=co1, fg=co4)
l_download.place(x=44, y=25)
l_download = Label(frame_corpo, text='Mbps download', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
l_download.place(x=30, y=70)

imagem_down = Image.open('down.png')
imagem_down = imagem_down.resize((50,50))
imagem_down = ImageTk.PhotoImage(imagem_down)
l_logo_imagem = Label(frame_corpo, height=60, image=imagem_down, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=130, y=35)


l_upload = Label(frame_corpo, text='65.7', anchor=NW , font=('arial 28'), bg=co1, fg=co4)
l_upload.place(x=235, y=25)
l_upload = Label(frame_corpo, text='Mbps upload', anchor=NW , font=('Ivy 10'), bg=co1, fg=co4)
l_upload.place(x=230, y=70)

imagem_up = Image.open('up.png')
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)
l_logo_imagem = Label(frame_corpo, height=60, image=imagem_up, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=170, y=35)






janela.mainloop ()