import os
import time

def limparTela():
  os.system("cls")

def aguarde(segundos=1):
  time.sleep(segundos)

def lerInteiro(mensagem):
  while True:
    try:
      variavel = int(input(mensagem))
      return variavel
    except:
      print("Valor informado incorreto")

def lerString(mensagem):
  while True:
    variavel = input(mensagem)
    if len(variavel)>1:
      return variavel
    else:
      print("Valor informado incorretamente")