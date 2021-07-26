from art import tprint, art
from random import choice, randint
from time import sleep
import pygame
import os

#Cria variavéis globais que serão usadas no jogo
global moedas, vidas

class Relogio:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
        return self.horas
    
    def atrasado(self):
        return (self.horas > 3 or (self.horas == 3 and self.minutos > 0))

class Personagem():

    def luigi(self):
        #Luigi pode entrar no jogo para ajudar o jogador caso ele escolha SIM
        print()
        print("~.~."*20)
        luigi = input("Deseja acionar o seu irmão Luigi para te ajudar nessa aventura? \nDigite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while luigi not in ["sim","nao","não"]:
            luigi = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        if luigi == "sim":
            print(r"""
████████████████████▀▀Ñ]⌠⌠⌠]└╙▀▀████████████████████████████
█████████████████▀]│[▄╪▓▓▓▄││││││]▀▀████████████████████████
███████████████▀│││▓█]▐█████]│││││││]▀██████████████████████
██████████████l│││#██▄W█▀▀██M│││││││││⌠█████████████████████
█████████████W│││││▀█▌▄▄▄æ█▀││││││││││││▀███████████████████
████████████▌││││││╙└▀└',,,,,,|,└└└││││││▀██████████████████
██████████████▄▄┘└,,^,¡▄▄╗╗m     ╖▄)'└│││⌠██████████████████
██████▀█████▀██▀''`   └▀▓▓▓▄#▒▒▒▓▄▓▓▓n'│││▐█████████████████
██████▀██████▌╓███▄▓▒██▒▓▓▓▓▀▀▀██▓▓▓▓▌ `││▐█████████████████
████████▌█████▀███▓▌██╙╙╢▒▓▓∩7.╠█▓▓▓▓▌  ▓▓▒█████████████████
████▀▀███▌██▀▀████▓▓█▌▄▓▓▓▓▓▓▓▄╠█▒▓▓▓▌ (▒║║╠▒███████████████
█████▌▀██▌████████▓▓█▒▓▓▓▓▓▓▓▓▓▓▒▓▓▓▀▌ ▐▒║║▒▒███████████████
█████████████████▌└▓▓▓▓▓▓▓▓▓▓▓▓▓▀▀└  └▄▓║║║▓████████████████
████████████▀████▒⌐ ╙▀▓▓▓▓▓▓▓▓▓▀      ▓▓▓▓▒█████████████████
███████▀█████████▌∩    ╙▀▓▓▓▀▀-      ╢▒█████████████████████
██████████▀▀Ñ]│││╠▒¿        ▄▄▄▄¬▄╗▓▓▓██████████████████████
████████Ñ││││││││|███M╗╗╗╗░▀▀É▒▒▓▓▓▓▓▒██████████████████████
█████████││││││││││▀██▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓███████████████████████
██████████]│││││││││|▀▀██▒▓▓▓▓▓▓▓▓▓▓▒███████████████████████
███████████▄││││││││││││Ñ▀▀▒▓▓▓▓▓▓▓▀Ñ█▀█████████████████████
████████████▄││││││││││││││░╔|||└└└│││░Wm¡╙▀▀▀▀▀▀███████████
██████████████▄▄││││││││││││││M∩,,,,└└││││M∩└└││││]▀▀███████
            """)
            print("Luigi agora está com você, em algumas situações ele vai conseguir te ajudar.")
            return True
        else:
            print("Você está sozinho nessa aventura, boa sorte!")
            return False

    def donkeyKong(self):
        #Na entrada do castelo o jogador vai precisar enfrentar Donkey Kong, somente se vencer vai entrar no castelo
        print("~.~."*20)
        print("Parabéns! Você chegou na entrada do castelo. O Donkey Kong vai tentar te impedir de entrar, tome cuidado.")
        print("Vamos enfrentar o Donkey Kong para resgatar a Princesa Peach?")
        donkey = input("\nDigite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while donkey not in ["sim", "nao", "não"]:
            donkey = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()

        if donkey == "sim":
            #O resultado da batalha é decidido de acordo com escolhas no jogo
            print("Você enfrentou Donkey Kong com bravura e...")
            musica3 = Mecanica()
            musica3.musicaBatalha()
            load = ["█▒▒▒▒▒▒▒▒▒", "███▒▒▒▒▒▒▒", "█████▒▒▒▒▒", "███████▒▒▒", "█████████▒", "██████████"]
            for i in load:
                sleep(0.83)
                print(i, end=" ", flush=True)
            
            #O resultado da batalha é decidido de acordo com escolhas no jogo
            return "LUTOU"
        else:
            print("Dessa forma você não vai ter a possibilidade de resgatar a Princesa.")
            fugir = input("Deseja mesmo fugir da batalha? \nDigite [SIM] ou [NÃO] ").lower()
            #Retorna inválido e pede novamente o input que está fora dos padrões
            while fugir not in ["sim", "nao", "não"]:
                fugir = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
            #Se o jogador optar por não enfretar Donkey Kong o jogo encerra, pois ele não consegue entrar no Castelo
            if fugir == "sim":
                print("Você não resgatou a Princesa!")
                return "FUGIU"
            else:
                print("Sábia escolha...")
                musica3 = Mecanica()
                musica3.musicaBatalha()
                #O resultado da batalha é decidido de acordo com escolhas no jogo
                print("Você enfrentou Donkey Kong com bravura e...")
                musica3 = Mecanica()
                musica3.musicaBatalha()
                load = ["█▒▒▒▒▒▒▒▒▒", "███▒▒▒▒▒▒▒", "█████▒▒▒▒▒", "███████▒▒▒", "█████████▒", "██████████"]
                for i in load:
                    sleep(0.83)
                    print(i, end=" ", flush=True)
                return "LUTOU"

    def princesa(self):
        #Derrotou o Bowser e chegou para resgatar a princesa
        print(r"""
                  o
                o^\^o
           o\*`'.\|/.'`*/o
            \\\\\\|//////
             {><><@><><}
            }}} _   _ {{{
          }}}}  6   6  {{{
         {{{{{    ^    }}}}}
        {{{{{{\  -=-  /}}}}}}
        {{{{{{{;.___.;}}}}}}}
         {{{{{{{)   (}}}}}}}'
          `""'"':   :'"'"'`
                 `@`
        """)
        print("Você conseguiu encontrar a Princesa Peach, mas isso ainda não acabou...")

class Interativos():

    def cogumelo(self):
        #Quando o jogador encontra  um cogumelo ele tem duas opções para interagir
        print()
        print("~.~."*20)
        print("Os dois me parecem ótimos, um é \033[0;32m [VERDE] \033[0;0m e o outro é \033[1;31m [VERMELHO]\033[0;0m")
        cogumelo = input("Qual você deseja escolher? \nDigite \033[0;32m [VERDE] \033[0;0m ou \033[1;31m [VERMELHO] \033[0;0m").lower() #Colorir a fonte no terminal
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while cogumelo not in ["verde", "vermelho"]:
            cogumelo = input("Você não escolheu uma opção válida. \nDigite [VERDE] ou [VERMELHO] ").lower()
        if cogumelo == "verde":
            print(r"""
📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘
📘📘📘📘📘📘⬛⬛⬛⬛⬛⬛⬛⬛⬛📘📘📘📘📘📘
📘📘📘📘⬛⬛📗📗📗📗📗📗⬜⬜⬜⬛⬛📘📘📘📘
📘📘📘⬛⬜⬜📗📗📗📗📗📗📗⬜⬜⬜⬜⬛📘📘📘
📘📘⬛⬜⬜📗📗📗📗📗📗📗📗📗⬜⬜⬜⬜⬛📘📘
📘📘⬛⬜📗📗⬜⬜⬜⬜📗📗📗📗📗📗⬜⬜⬛📘📘
📘⬛📗📗📗⬜⬜⬜⬜⬜⬜📗📗📗📗📗📗📗📗⬛📘
📘⬛📗📗📗⬜⬜⬜⬜⬜⬜📗📗📗📗📗⬜⬜📗⬛📘
📘⬛⬜⬜📗⬜⬜⬜⬜⬜⬜📗📗📗📗⬜⬜⬜⬜⬛📘
📘⬛⬜⬜📗📗⬜⬜⬜⬜📗📗📗📗📗⬜⬜⬜⬜⬛📘
📘⬛⬜⬜📗📗📗📗📗📗📗📗📗📗📗📗⬜⬜📗⬛📘
📘⬛⬜📗📗⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛📗📗📗⬛📘
📘📘⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛📘📘
📘📘📘⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛📘📘📘
📘📘📘⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛📘📘📘
📘📘📘📘⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛📘📘📘📘
📘📘📘📘📘⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛📘📘📘📘
📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘
            """)
            if vidas >= 2:
                tprint("Voce ganhou 100 moedas!", font="foxy")
                musica2 = Mecanica()
                musica2.musicaUP()
                return "MOEDAS"

            else:
                print("Você ganhou uma vida 💚")
                musica2 = Mecanica()
                musica2.musicaUP()
                return "VIDA"
        else:
            print(r"""
📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘
📘📘📘📘📘📘⬛⬛⬛⬛⬛⬛⬛⬛⬛📘📘📘📘📘📘
📘📘📘📘⬛⬛📕📕📕📕📕📕⬜⬜⬜⬛⬛📘📘📘📘
📘📘📘⬛⬜⬜📕📕📕📕📕📕📕⬜⬜⬜⬜⬛📘📘📘
📘📘⬛⬜⬜📕📕📕📕📕📕📕📕📕⬜⬜⬜⬜⬛📘📘
📘📘⬛⬜📕📕⬜⬜⬜⬜📕📕📕📕📕📕⬜⬜⬛📘📘
📘⬛📕📕📕⬜⬜⬜⬜⬜⬜📕📕📕📕📕📕📕📕⬛📘
📘⬛📕📕📕⬜⬜⬜⬜⬜⬜📕📕📕📕📕⬜⬜📕⬛📘
📘⬛⬜⬜📕⬜⬜⬜⬜⬜⬜📕📕📕📕⬜⬜⬜⬜⬛📘
📘⬛⬜⬜📕📕⬜⬜⬜⬜📕📕📕📕📕⬜⬜⬜⬜⬛📘
📘⬛⬜⬜📕📕📕📕📕📕📕📕📕📕📕📕⬜⬜📕⬛📘
📘⬛⬜📕📕⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛📕📕📕⬛📘
📘📘⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛📘📘
📘📘📘⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛📘📘📘
📘📘📘⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛📘📘📘
📘📘📘📘⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛📘📘📘📘
📘📘📘📘📘⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛📘📘📘📘
📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘📘
            """)
            tprint("Voce cresceu", font="cybermedium")
            musica2 = Mecanica()
            musica2.musicaUP()
            print("\033[1;31mCuidado para não esbarrar nos inimigos!\033[0;0m")
            return "CRESCEU"

    def kart(self):
        #O jogador tem a opção de escolher usar o Mario Kart
        print("~.~."*20)
        print("Olha, você encontrou o Mario Kart!")
        kart = input("Deseja usá-lo para chegar até o Castelo? Digite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while kart not in ["sim", "nao", "não"]:
            kart = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        #Se o jogador escolher sim, ele chega mais rápido ao Castelo
        if kart == "sim":
            print(r"""
             _ _ _ _
    _-_-  _/\______\\__
 _-_-__  / ,-. -M-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'

            """)
            print("Você está correndo de Kart, tome cuidado para não bater em nada.")
            return True
        else:
            print("Parece que você não vai conseguir chegar ao Castelo dessa forma, mas não desista.")
            return False

    def moedas(self, moedas):
        #O jogador se depara com moedas e pode escolher coletar ou ignorar
        print("~.~."*20)
        moeda = input("Oba, apareceram moedas, você deseja coletar? \nDigite [SIM] ou [NÃO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while moeda not in ["sim", "nao", "não"]:
            moeda = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        #Controla o número de moedas coletadas
        if moeda == "sim":
            moedas += 50
            return moedas
        else:
            return moedas

    def goomba(self):
        #O Goomba aparece e é decidido na sorte se o jogador venceu ou perdeu a batalha
        print(r"""

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░░░░░
░░░░░░░░░▄██▄▀░░░░░░░░░░░░▀▄██▄░░░░░░░░░
░░░░░░░░░░░███░░░░░░░░░░░░███░░░░░░░░░░░
░░░░░░░░░░█░▀██░░░░░░░░░░██▀░█░░░░░░░░░░
░░░░░░░░░█░░░▄██▄░░░░░░▄██▄░░░█░░░░░░░░░
░░░░░░░░▄▀░▄▀──▀█▄░░░░▄█▀──▀▄░▀▄░░░░░░░░
░░░░░░░▄▀░▄▀───▄─██░░██─▄───▀▄░▀▄░░░░░░░
░░░░░▄▀░░░█───███─█░░█─███───█░░░▀▄░░░░░
░░░▄▀░░░░░█────▀──█░░█──▀────█░░░░░▀▄░░░
░▄▀░░░░░░░█──────█░░░░█──────█░░░░░░░▀▄░
█░░░░░▄░░░░▀▄▄▄▄▀░░░░░░▀▄▄▄▄▀░░░░▄░░░░░█
█░░░░░▌▀▄░░░░░░░░░░░░░░░░░░░░░░▄▀▐░░░░░█
█░░░░▐▄▄▄█▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄█▄▄▄▌░░░░█
█░░░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀░░░░█
░▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▀░
░░░▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░
░░░░░░░▄▄▀▀▀▀▄░░░░░░░░░░░░▄▀▀▀▀▄▄░░░░░░░
░░░░░▄▀░░░░░░░▀▄▄▄▄▄▄▄▄▄▄▀░░░░░░░▀▄░░░░░
░░░░░█░░░░░░░░░░░▄▀░░▀▄░░░░░░░░░░░█░░░░░
░░░░░░▀▄░░░░░░░▄▀░░░░░░▀▄░░░░░░░▄▀░░░░░░
░░░░░░░░▀▀▀▀▀▀▀░░░░░░░░░░▀▀▀▀▀▀▀░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

""")
        goomba = randint(1,2)
        escolha = int(input("\nCuidado, é um Goomba! Escolha rápido [1] ou [2] para derrotá-lo: "))
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while escolha not in [1, 2]:
            escolha = int(input("Você não escolheu uma opção válida. \nDigite [1] ou [2] apenas: "))
        if goomba == escolha:
            print("Você derrotou o Goomba!")
            return True
        else:
            print("Você não derrotou o Goomba e perdeu 1 vida")
            return False


    def planta(self):
        #A Planta Carnívora aparece e o jogador pode pular ou desviar
        print(r"""
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛🔴🔴⬜🔴🔴⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🔴🔴🔴🔴🔴⬛⬛⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🔴🔴🔴⬜⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬛🔴⬜🔴🔴⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛🔴🔴🔴⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🔴🔴🔴⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🔴⬜⬛⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬛🔴🔴⬛⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬛🔴🔴⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬛🔴🔴⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬛⬜🔴🔴⬛⬛⬛⬛⬛⬛🔴🔴⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🔴🔴🔴🔴🔴🔴🔴🔴🔴⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🔴🔴⬜🔴🔴🔴⬜🔴🔴⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🔴🔴🔴🔴🔴⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬜⬜⬜⬛🍐📗⬛⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬜⬛🍐🍐⬛⬛⬜⬛🍐📗⬛⬜⬛⬛🍐📗⬛⬜⬜
⬜⬜⬛🍐⬛🍐🍐⬛⬛🍐📗⬛⬛🍐🍐⬛📗⬛⬜⬜
⬜⬜⬛🍐⬛📗📗🍐⬛🍐📗⬛🍐📗📗⬛📗⬛⬜⬜
⬜⬜⬛🍐📗⬛📗🍐⬛🍐📗⬛🍐📗⬛📗📗⬛⬜⬜
⬜⬜⬜⬛📗📗⬛📗⬛🍐📗⬛📗⬛📗📗⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛📗⬛📗🍐📗📗⬛📗⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛🍐📗⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬛🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐🍐⬛⬜
⬜⬛📗📗📗📗📗📗📗📗📗📗📗📗📗📗📗📗⬛⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬜⬜⬜⬛🍐🍐📗📗🍐📗🍐📗🍐🍐⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🍐🍐📗📗📗🍐📗🍐🍐🍐⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🍐🍐📗📗🍐📗🍐📗🍐🍐⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛🍐🍐📗📗📗🍐📗🍐🍐🍐⬛⬜⬜⬜⬜
        """)
        escolha = input("\nO que você vai fazer? \nEscolha [BATER] ou [DESVIAR]: ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while escolha not in ["bater","desviar"]:
            escolha = input("Você não escolheu uma opção válida. \nDigite [BATER] ou [DESVIAR] apenas: ")
        if escolha == "bater":
            print("Ops, a planta te mordeu! Você perdeu 1 vida")
            return False
        else:
            print("Você correu da Planta Carnívora e não perdeu muito tempo!")
            musica2 = Mecanica()
            musica2.musicaUP()
            return True

class Mecanica():

    def musicaFundo(self):
        pygame.mixer.init()
        pygame.mixer.music.load('mariobros.mp3')
        pygame.mixer.music.play()

    def musicaGameOver(self):
        pygame.init()
        if os.path.exists('GAMEOVER_MARIO.mp3'):
            pygame.mixer.music.load('GAMEOVER_MARIO.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(10)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')

    def musicaVitoria(self):
        pygame.init()
        if os.path.exists('VENCER_MARIO.mp3'):
            pygame.mixer.music.load('VENCER_MARIO.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)

            clock = pygame.time.Clock()
            clock.tick(10)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()
                clock.tick(10)
        else:
            print('O arquivo musica.mp3 não está no diretório do script Python')

    def musicaBatalha(self):
        pygame.mixer.init()
        pygame.mixer.music.load('BATALHA_MARIO.mp3')
        pygame.mixer.music.play()
    
    def musicaUP(self):
        pygame.mixer.init()
        pygame.mixer.music.load('UP.mp3')
        pygame.mixer.music.play()

    def musicaFinal(self):
        pygame.mixer.init()
        pygame.mixer.music.load('BATALHA_FINAL.mp3')
        pygame.mixer.music.play()


class Castelo():

    def portas(self):
        #Depois de enfrentar e ganhar do Donkey Kong ele finalmente chega até o Castelo
        print("~.~."*20)
        print("Você finalmente entrou no Castelo, agora falta pouco para resgatar a Princesa… escolha uma porta")
        print(r"""
            __________                  ______
           |  __  __  |             ,-'  ;  !  `-.
           | |  ||  | |            / :  !   :   . \
           | |  ||  | |            |_ ;   __:  ;  |
           | |__||__| |            )| .  :)(.  !  |
           |  __  __()|            |"    (##)  _  |
           | |  ||  | |            |  :  ;`'  (_) (
           | |  ||  | |            |  :  :  .     |
           | |  ||  | |            )_ !  ,  ;  ;  |
           | |  ||  | |            || .  .  :  :  |
           | |__||__| |            |" .  |  :  .  |
           |__________|            |_____;----.___|
         Porta de Madeira           Porta de Ferro
        """)

        porta = input("Digite [MADEIRA] ou [FERRO] ").lower()
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while porta not in ["madeira", "ferro"]:
            porta = input("Você não escolheu uma opção válida. \nDigite [MADEIRA] ou [FERRO] ").lower()
        #Indepente da porta que o jogador escolha, ele vai encontrar o Bowser
        if porta == "madeira":
            print("Que pena, a Princesa não está na PORTA DE MADEIRA!")
        else:
            print("Que pena, a Princesa não está na PORTA DE FERRO!")

    def batalhaFinal(self):
        #Batalha final com o Bowser para salvar a Princesa Peach
        print(r"""
───────▄█──────────█─────────█▄───────
─────▐██──────▄█──███──█▄─────██▌─────
────▐██▀─────█████████████────▀██▌────
───▐██▌─────██████████████─────▐██▌───
───████────████████████████────████───
──▐█████──██████████████████──█████▌──
───████████████████████████████████───
────███████▀▀████████████▀▀███████────
─────█████▌──▄▄─▀████▀─▄▄──▐█████─────
───▄▄██████▄─▀▀──████──▀▀─▄██████▄▄───
──██████████████████████████████████──
─████████████████████████████████████─
▐██████──███████▀▄██▄▀███████──██████▌
▐█████────██████████████████────█████▌
▐█████─────██████▀──▀██████─────█████▌
─█████▄─────███────────███─────▄█████─
──██████─────█──────────█─────██████──
────█████────────────────────█████────
─────█████──────────────────█████─────
──────█████────────────────█████──────
───────████───▄────────▄───████───────
────────████─██────────██─████────────
────────████████─▄██▄─████████────────
───────████████████████████████───────
───────████████████████████████───────
────────▀█████████▀▀█████████▀────────
──────────▀███▀────────▀███▀────────── 
        """)
        musica3 = Mecanica()
        musica3.musicaFinal()
        espada = art("sword7")
        print(espada, espada, espada)
        print("Você pode escolher uma das opções a seguir para te ajudar")
        opcoes = ["1- Yoshi", "2- Estrela"]
        for i in opcoes:
            print(i)
        print("Quem vai te ajudar a enfrentar o Bowser? Pense e escolha estrategicamente!")
        chefao = int(input("Escolha sua opção (apenas números): "))
        #Retorna inválido e pede novamente o input que está fora dos padrões
        while chefao not in [1, 2]:
                chefao = int(input("Você não escolheu uma opção válida. \nDigite 1 ou 2: "))
        if chefao == 1:
            print(r"""
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜🍐⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛📗📗⬛⬜⬛⬜⬜🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🍐🍐🍐🍐📗📗⬜⬜⬜🍐🍐⬛⬛⬜⬜⬜
⬜⬜⬜⬛🍐⬛🍐⬛🍐🍐🍐📗⬜📗🍐🍐⬛⬛⬜⬜⬜
⬜⬜⬛🍐🍐🍐🍐🍐🍐🍐🍐📗📗📗🍐🍐🍐⬛⬜⬜⬜
⬜⬜⬛🍐🍐🍐🍐🍐🍐🍐🍐🍐📗📗🍐🍐🍐⬛⬛⬜⬜
⬜⬜⬛🍐🍐🍐🍐🍐🍐🍐🍐📗📗⬜⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬛📗📗🍐🍐🍐🍐🍐📗📗⬛⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬛📗📗🍐🍐🍐📗📗⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛📗📗📗📗⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🍐🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜🍐🍐🍐⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🍐🍐⬛🍐🍐⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛🍐🍐🍐⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛📗⬛⬜⬜⬜⬛🍐🍐🍐🍐⬛⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬛📗⬛⬜⬜⬜⬛📗🍐📗⬛🍐🍐⬛⬛⬛
⬜⬜⬜⬜⬜⬛📗⬛⬜⬜⬜⬛📗📗📗⬛🍐🍐🍐🍐🍐
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬛🍐🍐🍐🍐⬛⬛
⬜⬜⬜⬜⬜⬜⬜⬛🍐⬜⬜⬜🍐🍐🍐🍐🍐⬛⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🍐⬜🍐🍐🍐⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬛🍐⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🔴🔴⬛🔴🔴🔴⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🔴🔴⬛🔴🔴🔴🔴🔴🔴⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🔴🔴⬛🔴🔴🔴🔴🔴🔴⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
            """)
            print("O Yoshi vai lutar com você, ele pode te ajudar a derrotar o seu inimigo")
            return "YOSHI"
       
        else:
            print(r"""
___________✨
_________✨✨
________ ✨✨✨
____✨✨✨✨✨✨✨
______✨✨✨✨✨
_______ ✨✨✨✨
_____✨✨____✨✨
____ ✨__________✨
            """)
            print("Você está invencível por 30 segundos, aproveite!")
            #Inicia a contagem do timer
            timer = 0
            while timer < 30:
                sleep(1)
                timer += 1
                print("-", end=" ", flush=True)
            print("\nFIM DO SEU PODER")
            return "ESTRELA"

#Inicia a contagem das vidas
vidas = 3

#Inicia a contagem de moedas
moedas = 0

while True:
    #Exibe o nome do jogo e menu
    tprint("MARIO", font="block")
    tprint("  A O   R E S G A T E", font="thin")

    #Pergunta para o jogador se deseja iniciar ou não o jogo
    iniciar = input("Você deseja iniciar o jogo? \nDigite [SIM] ou [NÃO] ").lower()

    #Valida a opção digitada e pede novamente, caso seja inválido
    while iniciar not in ["sim","nao","não"]:
        iniciar = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
    #O jogo funciona até o jogador decidir não jogar mais
    if iniciar == "sim":
        #Inicia a música de fundo
        musica1 = Mecanica()
        musica1.musicaFundo()

        #Conta a história para o jogador entender o contexto
        enredo = "Seja bem vindo ao Reino dos Cogumelos!\nO Reino dos Cogumelos foi invadido por criaturas conhecidas como Goombas e, usando a magia de seu rei Bowser, transformaram alguns habitantes em plantas carnívoras..."
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        continuar = input("\nPressione enter para continuar")

        print("~.~."*20)
        enredo = "A Princesa Peach foi sequestrada pois apenas ela detém o poder de desfazer essa magia e salvar o Reino... "
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        print()
        print("~.~."*20)

        enredo = "Cabe a você, Mario, salvar a princesa e libertar o reino de Bowser. Você está pronto?"
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        continuar = input("\nPressione enter para continuar")

        enredo = "Você está pronto para começar essa aventura, porém antes, você tem uma escolha a fazer..."
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)

        #Oferece o Luigi para ser selecionado como ajudante
        luigi = Personagem()
        luigiPersonagem = luigi.luigi()
        continuar = input("Pressione enter para continuar")

        #Informa o jogador que ele vai ter um tempo para concluir o jogo
        print("~.~."*20)
        enredo = "Tome cuidado com o Goomba e com a Planta Carnívora... Eles podem tirar suas vidas... Você começa com 3 vidas. E atenção, você tem no máximo 3 horas para concluir essa missão, você está correndo contra o tempo para resgatar a Princesa!"
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)

        tempo = Relogio()
        print(f"\nInício: {tempo}")
        continuar = input("Pressione enter para continuar")

        #Oferece a opção de coletar moedas
        enredo = "Que incrível, você estava andando pela floresta e encontrou uma caixa misteriora, o que será?"
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)

        #Pergunta para o jogador se deseja abrir ou não a caixa misteriosa
        abrir = input("\nVocê deseja abrir a caixa misteriosa? \nDigite [SIM] ou [NÃO] ").lower()

        #Valida a opção digitada e pede novamente, caso seja inválido
        while abrir not in ["sim","nao","não"]:
            abrir = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        
        #Caso o jogador decida abrir, ele irá encontrar moedas
        if abrir == "sim":
            moeda = Interativos()
            moedas = moeda.moedas(moedas)
            print(f"Você coletou {moedas} moedas")
            tempo.avancaTempo(20)
            print(f"Tempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")               
        
        else:
            print("Tudo bem, que pena...")
            tempo.avancaTempo(10)
            print(f"Tempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        #O Goomba aparece, e o jogador pode derrotar ou perder uma vida na sorte
        enredo = "Você já seguiu bastante pela floresta e uma criatura misteriosa apareceu..."
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)

        goomba = Interativos()
        goombaInterativo = goomba.goomba()
        if goombaInterativo == False:
            vidas -= 1
            print(f"Você tem {vidas} vidas")
            tempo.avancaTempo(30)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        else:
            tempo.avancaTempo(10)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        #Recomeça a música de fundo
        musica1 = Mecanica()
        musica1.musicaFundo()
        enredo = "Deixa eu te contar uma coisa... acho que esqueci de mencionar... Depois de viajar por várias partes do reino e vencer os inimigos ao longo do caminho, você chegará ao Castelo. Cuidado! Apenas após derrotar o Bowser no tempo certo, que a princesa será libertada e o Reino dos Cogumelos será salvo!"
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        
        continuar = input("\nPressione enter para continuar")

        #Oferece a opção de usar o Kart
        enredo = "Já no final da floresta, chegando no caminho das pedras você avistou alguma coisa brilhando que chamou sua atenção..."
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)
        continuar = input("\nPressione enter para se aproximar")

        kart = Interativos()
        marioKart = kart.kart()
        if marioKart == True:
            tempo.avancaTempo(10)
            print(f"Tempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        else:
            tempo.avancaTempo(50)
            print(f"Tempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        
        #Uma planta carnívora aparece, e o jogador pode derrotar ou perder suas moedas ou vida
        enredo = "No carminho das pedras, apareceu uma Planta Carnívora, cuidado!"
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)

        carnivora = Interativos()
        planta = carnivora.planta()
        if planta == False:
            vidas -= 1
            print(f"Você tem {vidas} vidas")
            tempo.avancaTempo(40)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")
        else:
            tempo.avancaTempo(10)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        #Cogumelos aparecem no jardim do Castelo
        enredo = "Hummm... você encontrou dois Cogumelos no Jardim do Castelo"
        for letra in enredo:
            sleep(0.05)
            print(letra, end='', flush=True)

        cogumelo = Interativos()
        cogumeloInterativo = cogumelo.cogumelo()

        if cogumeloInterativo == "MOEDA":
            moedas += 100
            print(f"Você tem {moedas} moedas")
            tempo.avancaTempo(40)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        elif cogumeloInterativo == "VIDA":
            vidas += 1
            print(f"Você tem {vidas} vidas")
            tempo.avancaTempo(60)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        else:
            tempo.avancaTempo(30)
            print(f"\nTempo de jogo: {tempo}")
            continuar = input("\nPressione enter para continuar")

        if marioKart == True:
            #Mario pode escorregar e perder uma vida
            enredo = "Não estava esperando por isso, você estava correndo tanto..."
            for letra in enredo:
                sleep(0.05)
                print(letra, end='', flush=True)
            continuar = input("\nPressione enter para continuar")
            print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⣴⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠛⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢠⠀⡄⠀⣿⠀⢀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠚⠀⠃⠀⣿⣴⠞⠉⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⢀⣸⠇⠀⠀⠀⠀⠈⠀⠀⣀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⠛⢳⣤⣤⡶⠛⠃⠀⣠⠀⠀⠀⠚⣶⡾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⣤⣀⣀⣀⣀⣠⡾⠻⣧⡀⠀⠀⢘⣷⣄⣀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠘⠻⣦⣤⣈⣁⣀⣠⣾⠋⠀⠀⠀⠀
    Poxa, você escorregou em uma banana encantada!⠀⠀⠀⠀⠀⠀
⠀⠀⠀
            """)
            if moedas == 0:
                vidas -= 1
                print("Você não tinha moedas para te proteger, então perdeu 1 vida")
                tempo.avancaTempo(20)
                print(f"Tempo de jogo: {tempo}")
                continuar = input("\nPressione enter para continuar")
            else:
                print("Suas moedas te salvaram, elas foram embora junto com seu Kart... mas você ficou inteiro!")
                tempo.avancaTempo(30)
                print(f"Tempo de jogo: {tempo}")
                continuar = input("\nPressione enter para continuar")
        
        #Mario já consegue visualizar o Castelo e entra em ação o Donkey Kong
        print(r"""
                    |>>>                        |>>>
                    |                           |
                _  _|_  _                   _  _|_  _
               | |_| |_| |                 | |_| |_| |
               \  .      /                 \ .    .  /
                \    ,  /                   \    .  /
                 | .   |_   _   _   _   _   _| ,   |
                 |    .| |_| |_| |_| |_| |_| |  .  |
                 | ,   | .    .     .      . |    .|
                 |   . |  .     . .   .  ,   |.    |
     ___----_____| .   |.   ,  _______   .   |   , |---~_____
_---~            |     |  .   /+++++++\    . | .   |         ~---_
                 |.    | .    |+++++++| .    |   . |              ~-_
              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~
""")
        donkeykong = Personagem()
        donkeyPersonagem = donkeykong.donkeyKong()
        if donkeyPersonagem == "LUTOU":
            #Se no início do jogo, ele escolheu o Luigi para acompanhar, ele vai vencer essa luta e entra no Castelo
            if luigiPersonagem == True:
                print("\nVENCEU pois seu irmão Luigi te ajudou")
                continuar = input("\nPressione enter para entrar no Castelo")
                #No castelo ele vai se deparar com duas portas para procurar a princesa
                print(f"Tempo de jogo: {tempo}")
                porta = Castelo()
                porta.portas()
                #Nenhuma porta escolhida tem a princesa, mas sim, começa a batalha final contra Bowser
                print("Agora você vai enfrentar o Bowser e se vencer vai se encontrar com a Princesa Peach.")
                musica3 = Mecanica()
                musica3.musicaBatalha()
                continuar = input("\nPressione enter para continuar")
                bowser = Castelo()
                final = bowser.batalhaFinal()
                #Após a batalha final, usando os poderes, o jogador derrota Bowser, e tem o grande final decidido pelo tempo que ele conseguiu concluir o jogo
                continuar = input("\nPressione enter para continuar")
                print("~.~."*20)
                print("Você DERROTOU o Bowser!!!!!!!!!!!!!!!!!!")
                print("~.~."*20)
                if final == "ESTRELA":
                    print("Esse tempo que você ficou invencível foi crucial para sua vitória!")
                else:
                    print("Você e Yoshi formam a melhor dupla de todos os tempos, a ajuda dele foi crucial para a sua vitória!")
                peach = Personagem()
                princesa = peach.princesa()
                continuar = input("\nPressione enter para conhecer o final dessa história")

                tempo = tempo.avancaTempo(0)
                if int(tempo) < 3:
                    enredo = "🏆 Chegou no tempo certo e resgatou a Princesa Peach. Bowser foi derrotado, sua magia quebrada e agora todos voltaram a viver felizes no Reino dos Cogumelos! ♥‿♥"
                    for letra in enredo:
                        sleep(0.05)
                        print(letra, end='', flush=True)
                    continuar = input("\nPressione enter para continuar")
                else:
                    print("Xiii... você chegou tarde demais. Peach fugiu com o Wario ╰(◣﹏◢)╯")
                    enredo = "Chegou no tempo certo e resgatou a Princesa Peach. Bowser foi derrotado, sua magia quebrada e agora todos voltaram a viver felizes no Reino dos Cogumelos! ♥‿♥"
                    for letra in enredo:
                        sleep(0.05)
                        print(letra, end='', flush=True)
                    continuar = input("\nPressione enter para continuar")
            #Caso não tenha escolhido o Luigi, o jogador perde a luta
            else:
                print("\nPERDEU pois não estava com seu irmão Luigi")
                tprint("Game Over",font="starwars")
                musica4 = Mecanica()
                musica4.musicaGameOver()
                break
        #Se o jogador escolhe não lutar com Donkey Kong, ele não consegue nem entrar no Castelo e perde o jogo
        else:
            tprint("Game Over",font="starwars")
            musica4 = Mecanica()
            musica4.musicaGameOver()
            break
        
        print(r"""
🚪🚪🚪🚪🚪🚪🚪⬛⬛⬛⬛🚪⬛⬛⬛🚪 
🚪🚪🚪🚪🚪⬛⬛🍎🍎🍎⬛⬛✊✊✊⬛ 
🚪🚪🚪🚪⬛🍎🍎🍎🍎🍎🍎⬛✊✊✊⬛ 
🚪🚪🚪⬛🍎🍎🍎⬛⬛⬛⬛⬛⬛✊✊⬛ 
🚪🚪⬛🍎🍎🍎⬛⬛⬛⬛⬛⬛⬛⬛✊⬛ 
🚪🚪⬛🍎⬛⬛✊✊✊✊✊✊⬛⬛⬛🚪 
🚪⬛⬛⬛⬛✊✊✊⬛✊⬛✊⬛🍎🍎⬛ 
🚪⬛✊⬛⬛✊✊✊⬛✊⬛✊⬛🍎🍎⬛ 
⬛✊✊⬛⬛⬛✊✊✊✊✊✊✊⬛🍎⬛ 
⬛✊✊✊⬛✊✊⬛✊✊✊✊✊⬛🍎⬛ 
🚪⬛✊✊✊✊⬛⬛⬛⬛✊✊⬛⬛⬛🚪 
🚪🚪⬛⬛✊✊✊✊⬛⬛⬛⬛⬛🍎⬛🚪 
🚪🚪🚪⬛⬛⬛✊✊✊✊✊⬛🍎🍎⬛🚪 
🚪🚪⬛🍎🍎⬛⬛⬛⬛⬛⬛⬛🍎⬛🚪🚪 
🚪⬛🍎🍎🍎🍎⬛⬛✊✊✊⬛⬛🚪🚪🚪 
⬛⬛🍎🍎🍎🍎⬛✊✊✊✊✊⬛🚪🚪🚪 
⬛⬛🍎🍎🍎🍎⬛✊✊✊✊✊⬛🚪🚪🚪 
⬛⬛⬛🍎🍎🍎🍎⬛✊✊✊⬛⬛⬛⬛🚪 
🚪⬛⬛⬛🍎🍎🍎⬛⬛⬛⬛⬛⬛⬛⬛🚪 
🚪🚪⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🍎🍎⬛ 
🚪⬛🍎🍎⬛⬛⬛⬛⬛⬛⬛⬛🍎🍎🍎⬛ 
⬛⬛🍎⬛⬛⬛⬛⬛⬛⬛⬛⬛🍎🍎🍎⬛ 
⬛🍎🍎⬛⬛⬛⬛⬛⬛⬛⬛⬛🍎🍎🍎⬛ 
⬛🍎🍎⬛⬛⬛⬛⬛⬛🚪🚪⬛🍎🍎⬛⬛ 
⬛🍎🍎⬛⬛🚪🚪🚪🚪🚪🚪🚪⬛⬛⬛🚪 
🚪⬛⬛🚪🚪🚪🚪🚪🚪🚪🚪🚪🚪🚪🚪🚪
A nossa aventura foi muito boa, até a próxima!
        """)
        #Pergunta para o jogador se deseja jogar novamente
        novamente = input("Você deseja jogar novamente? \nDigite [SIM] ou [NÃO] ").lower()

        #Valida a opção digitada e pede novamente, caso seja inválido
        while novamente not in ["sim","nao","não"]:
            novamente = input("Você não escolheu uma opção válida. \nDigite [SIM] ou [NÃO] ").lower()
        #O jogo encerra se o jogador desejar, ou recomeça
        if novamente != "sim":
            break
        else:
            pass
    #O jogo encerra quando o jogador decide que não quer iniciar
    else:
        tprint("Game Over",font="starwars")
        musica4 = Mecanica()
        musica4.musicaGameOver()
        break