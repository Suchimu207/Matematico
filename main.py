import os, sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame import mixer, key
from colorama import just_fix_windows_console, Fore, Back, Style
from enum import Enum, auto
from menu import Menu

"""
Autor: Carlos S. Rehem
Versão: 0.0.3

Calculadora simples com música de fundo.

"""

just_fix_windows_console()

mixer.init()
mixer.music.load(r"BGM\CastleFunk.mp3")
mixer.music.play(loops=-1, fade_ms=3000)
mixer.music.set_volume(0.6)

class EstadosJogo(Enum):
    PRINCIPAL = 0
    ADIÇÃO = auto()
    SUBTRAÇÃO = auto()
    MULTIPLICAÇÃO = auto()
    EXPONENCIAÇÃO = auto()
    DIVISÃO = auto()
    DIVISÃO_INTEIRA = auto()
    SAIR = auto()

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def inputNúmero(valor):
    while True:
        numero = input(valor).replace(',', '.')
        try:
            return float(numero)
        except ValueError:
            print(Fore.RED + Style.BRIGHT+"\nSomente números.\n"+Style.NORMAL)

def inputTexto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto and not texto.replace(' ', '').isnumeric():
            return texto
        print(Fore.RED + Style.BRIGHT+"\nTexto inválido.\n"+Style.NORMAL)

def menuOperação(estadoAtual):
    print(Fore.WHITE + Style.BRIGHT+"Insira o primeiro valor:"+Style.NORMAL)
    valor1 = inputNúmero((Fore.WHITE + Style.BRIGHT+"> "+Style.NORMAL))
    
    print("")
    
    print(Fore.WHITE + Style.BRIGHT+"Insira o segundo valor:")
    valor2 = inputNúmero((Fore.WHITE + Style.BRIGHT+"> "+Style.NORMAL))
   
    if estadoAtual == EstadosJogo.ADIÇÃO:
        resultado = valor1 + valor2
    elif estadoAtual == EstadosJogo.SUBTRAÇÃO:
        resultado = valor1 - valor2
    elif estadoAtual == EstadosJogo.MULTIPLICAÇÃO:
        resultado = valor1 * valor2
    elif estadoAtual == EstadosJogo.EXPONENCIAÇÃO:
        resultado = valor1 ** valor2
    elif estadoAtual == EstadosJogo.DIVISÃO:
        if valor2 > 0:
            resultado = valor1/valor2 
        else: 
            resultado = 0
    elif estadoAtual == EstadosJogo.DIVISÃO_INTEIRA:
        if valor2 > 0:
            resultado = valor1//valor2
        else: 
            resultado = 0
    
    print("")
    print(Fore.GREEN + Style.BRIGHT+"Resultado:", resultado)
    print(Fore.WHITE + Style.BRIGHT+"_________________________________________"+Style.NORMAL)
    print(Fore.WHITE + Style.BRIGHT+"\nDeseja voltar para o menu inicial? S/N"+Style.NORMAL)
    entradaTexto = inputTexto((Fore.WHITE + Style.BRIGHT+"> "+Style.NORMAL))
    
    if entradaTexto.upper() == "S":
        return EstadosJogo.PRINCIPAL
    else:
        return estadoAtual

if __name__ == "__main__":
    estadoAtual = EstadosJogo.PRINCIPAL
    gui = Menu(EstadosJogo)
    rodando = True
    
    while rodando:
        if estadoAtual != EstadosJogo.PRINCIPAL:
            limpaTela()
            gui.nomeEstado(estadoAtual)
            estadoAtual = menuOperação(estadoAtual)           
        
        if estadoAtual == EstadosJogo.PRINCIPAL:
            limpaTela()
            gui.menuInicial()
            try:
                entrada = inputNúmero((Fore.WHITE + Style.BRIGHT+"> "+Style.NORMAL))
                
                if entrada == EstadosJogo.ADIÇÃO.value:
                    estadoAtual = EstadosJogo.ADIÇÃO
                elif entrada == EstadosJogo.SUBTRAÇÃO.value:
                    estadoAtual = EstadosJogo.SUBTRAÇÃO
                elif entrada == EstadosJogo.MULTIPLICAÇÃO.value:
                    estadoAtual = EstadosJogo.MULTIPLICAÇÃO
                elif entrada == EstadosJogo.EXPONENCIAÇÃO.value:
                    estadoAtual = EstadosJogo.EXPONENCIAÇÃO
                elif entrada == EstadosJogo.DIVISÃO.value:
                    estadoAtual = EstadosJogo.DIVISÃO
                elif entrada == EstadosJogo.DIVISÃO_INTEIRA.value:
                    estadoAtual = EstadosJogo.DIVISÃO_INTEIRA
                elif entrada == estadoAtual.SAIR.value: 
                    mixer.music.fadeout(2000)
                    limpaTela()
                    rodando = False
                    sys.exit(0)
            except ValueError:
                print(Fore.RED + Style.BRIGHT+"Comando inválido!"+Style.NORMAL)
                input(Fore.WHITE + Style.BRIGHT+"Pressione ENTER..."+Style.NORMAL)