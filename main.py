import os, sys
from colorama import just_fix_windows_console, Fore, Back, Style
from enum import Enum, auto
from pygame import mixer

"""
Autor: Carlos S. Rehem
Versão: 0.0.1

Calculadora simples com música de fundo.

"""

just_fix_windows_console()

mixer.init()
mixer.music.load("BGM\CastleFunk.mp3")
mixer.music.set_volume(0.6)

class EstadosJogo(Enum):
    PRINCIPAL = 0
    ADIÇÃO = auto()
    SUBTRAÇÃO = auto()
    MULTIPLICAÇÃO = auto()
    DIVISÃO = auto()
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

def menuInicial():
    print("")
    print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
    print(Fore.GREEN + Style.BRIGHT+"           Matemático!"+Style.NORMAL)
    print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
    print(Fore.GREEN + Style.BRIGHT+"Desenvolvido por Carlos S. Rehem"+Style.NORMAL)
    print(Fore.GREEN + Style.BRIGHT+"Versão: 0.0.1"+Style.NORMAL)
    
    print("")
    print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
    for estado in EstadosJogo:
        if estado != EstadosJogo.PRINCIPAL:
            print(f"{Fore.WHITE}{Style.BRIGHT}{estado.value}. {estado.name}{Style.NORMAL}")
    print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
    print("")

def menuOperação(estadoAtual):
    valor1 = 0
    valor2 = 0
    resultado = 0
    
    print("")
    print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
    print(Fore.GREEN + Style.BRIGHT+estadoAtual.name+Style.NORMAL)
    print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
    print("")
    
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
    elif estadoAtual == EstadosJogo.DIVISÃO:
        if valor2 > 0:
            resultado = valor1//valor2
        else: 
            resultado = 0
 
    print("")
    print(Fore.GREEN + Style.BRIGHT+"Resultado:", resultado)
    print(Fore.WHITE + Style.BRIGHT+"\nDeseja voltar para o menu inicial? S/N"+Style.NORMAL)
    entradaTexto = inputTexto((Fore.WHITE + Style.BRIGHT+"> "+Style.NORMAL))
    
    if "S" in entradaTexto or "s" in entradaTexto:
        return EstadosJogo.PRINCIPAL
    else:
        return estadoAtual
    
if __name__ == "__main__":
    estadoAtual = EstadosJogo.PRINCIPAL
    mixer.music.play(-1)
    rodando = True
    
    while rodando:
        if estadoAtual != EstadosJogo.PRINCIPAL:
            limpaTela()
            estadoAtual = menuOperação(estadoAtual)
            
        if estadoAtual == EstadosJogo.PRINCIPAL:
            limpaTela()
            menuInicial()
            try:
                entrada = inputNúmero((Fore.WHITE + Style.BRIGHT+"> "+Style.NORMAL))
        
                if entrada == EstadosJogo.ADIÇÃO.value:
                    estadoAtual = EstadosJogo.ADIÇÃO
                elif entrada == EstadosJogo.SUBTRAÇÃO.value:
                    estadoAtual = EstadosJogo.SUBTRAÇÃO
                elif entrada == EstadosJogo.MULTIPLICAÇÃO.value:
                    estadoAtual = EstadosJogo.MULTIPLICAÇÃO
                elif entrada == EstadosJogo.DIVISÃO.value:
                    estadoAtual = EstadosJogo.DIVISÃO
                elif entrada == estadoAtual.SAIR.value:
                    limpaTela()
                    rodando = False
                    mixer.music.stop()
                    sys.exit(0)
            except ValueError:
                print(Fore.RED + Style.BRIGHT+"Comando inválido!"+Style.NORMAL)
                input(Fore.WHITE + Style.BRIGHT+"Pressione ENTER..."+Style.NORMAL)