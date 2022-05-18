#Importando tkinter

from tkinter import *
from tkinter import ttk

#Cores
cor1 = '#1d1530' #Roxo Escuro 
cor2 = '#362a52' #Roxo Claro
cor3 = '#ffffff' #Branco
cor4 = '#070133' #Azul Escuro

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config()

#Criação dos Frames
frameTela = Frame(janela, width=235, height=60, bg=cor2)
frameTela.grid(row=0, column=0)

frameCorpo = Frame(janela, width=235, height=313)
frameCorpo.grid(row=1, column=0)

#Variavel de Todos os Valores da Calculadora
todosValores = ''

#Funções da calculadora
def entradaValores(receber):

    global todosValores

    todosValores = todosValores + str(receber)
    
    #Passando valor para tela
    valorTexto.set(todosValores)

#Função de calculo
def calcular():
    global todosValores

    resultado = eval(todosValores)
    
    valorTexto.set(str(resultado))

#Função de limpar a tela
def limparTela():
    global todosValores

    todosValores = ''
    valorTexto.set('')

#Criação de label
valorTexto = StringVar()

appLabel = Label(frameTela, textvariable=valorTexto, width=16, height=2, padx=5, relief='flat', anchor='e', justify='right', font=('Ivy 18'), bg=cor2, fg=cor3)
appLabel.place(x=0, y=0)

#Criação dos Botões
#Primeira Coluna
b1 = Button(frameCorpo, text='Limpar', width=11, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=limparTela)
b1.place(x=0, y=0)

b2 = Button(frameCorpo, text='%', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('%'))
b2.place(x=118, y=0)

b3 = Button(frameCorpo, text='/', width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('/'))
b3.place(x=177, y=0)

#Segunda coluna
b4 = Button(frameCorpo, text='7', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('7'))
b4.place(x=0, y=52)

b5 = Button(frameCorpo, text='8', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('8'))
b5.place(x=59, y=52)

b6 = Button(frameCorpo, text='9', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('9'))
b6.place(x=118, y=52)

b7 = Button(frameCorpo, text='*', width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('*'))
b7.place(x=177, y=52)

#Terceira coluna
b8 = Button(frameCorpo, text='4', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('4'))
b8.place(x=0, y=104)

b9 = Button(frameCorpo, text='5', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('5'))
b9.place(x=59, y=104)

b10 = Button(frameCorpo, text='6', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('6'))
b10.place(x=118, y=104)

b11 = Button(frameCorpo, text='-', width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('-'))
b11.place(x=177, y=104)

#Quarta coluna
b12 = Button(frameCorpo, text='1', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('1'))
b12.place(x=0, y=156)

b13 = Button(frameCorpo, text='2', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('2'))
b13.place(x=59, y=156)

b14 = Button(frameCorpo, text='3', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('3'))
b14.place(x=118, y=156)

b15 = Button(frameCorpo, text='+', width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('+'))
b15.place(x=177, y=156)

#Quinta Coluna
b16 = Button(frameCorpo, text='0', width=11, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('0'))
b16.place(x=0, y=208)

b17 = Button(frameCorpo, text='.', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=lambda: entradaValores('.'))
b17.place(x=118, y=208)

b18 = Button(frameCorpo, text='=', width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', command=calcular)
b18.place(x=177, y=208)



janela.mainloop()

