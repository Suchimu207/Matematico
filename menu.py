from colorama import Fore, Style
from enum import Enum

class Menu:
    def __init__(self, estados_jogo):
        self.estados = estados_jogo
    
    def menuInicial(self):
        print("")
        print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
        print(Fore.GREEN + Style.BRIGHT+"           Matemático!"+Style.NORMAL)
        print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
        print(Fore.GREEN + Style.BRIGHT+"Desenvolvido por Carlos S. Rehem"+Style.NORMAL)
        print(Fore.GREEN + Style.BRIGHT+"Versão: 0.0.3"+Style.NORMAL)
    
        print("")
        print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
        for estado in self.estados:
            if estado != self.estados.PRINCIPAL:
                print(f"{Fore.WHITE}{Style.BRIGHT}{estado.value}. {estado.name}{Style.NORMAL}")
        print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
        print("")
    
    def nomeEstado(self, estadoAtual):
        print("")
        print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
        print(Fore.GREEN + Style.BRIGHT+estadoAtual.name+Style.NORMAL)
        print(Fore.WHITE + Style.BRIGHT+"================================"+Style.NORMAL)
        print("")