import random
import time
lista = [0, 0]

class Jogo():
    def __int__(self):
        self.opcoes = ["pedra", "papel", "tesoura"]
        self.pc = random.choice(self.opcoes)


    def pedra_papel_tesoura(self):
        while True:
            jogador = str(input("""Esse é o Pedra, Papel e Tesoura da Lari! 
    Você tem três opções:
Pedra
Papel
Tesoura
Escreva sua opção: """)).lower()
            while jogador != "pedra" and jogador != "papel" and jogador != "tesoura":
                jogador = int(input("Digite uma opção válida: "))
                if jogador == "pedra" or jogador == "papel" or jogador == "tesoura":
                    break
            if self.pc == jogador:
                print(f"O computador escolheu {self.opcoes} e você escolheu {jogador}. ")
                time.sleep(1.5)
                print("Empatou! Vamos jogar de novo.")
                print(f"Placar: \nJogador = {lista[0]} X Computador = {lista[1]}")
                time.sleep(1.5)
            if self.pc == "pedra" and jogador == "papel":
                print(f"O computador escolheu {self.opcoes} e você escolheu {jogador}. ")
                time.sleep(1.5)
                print("Você ganhou!")
                lista[0] = lista[0] + 1
                print(f"Placar: \nJogador = {lista[0]} X Computador = {lista[1]}")
                time.sleep(1.5)
                if lista[0] == 2:
                    print("Você ganhou duas rodadas! Fim de jogo.")
                    break
            if self.pc == "pedra" and jogador == "tesoura":
                print(f"O computador escolheu {self.opcoes} e você escolheu {jogador}. ")
                time.sleep(1.5)
                print("O computador ganhou!")
                lista[1] = lista[1] + 1
                print(f"Placar: \nJogador = {lista[0]} X Computador = {lista[1]}")
                time.sleep(1.5)
                if lista[1] == 2:
                    print("O computador ganhou duas rodadas! Fim de jogo.")
                    break
            if self.pc == "papel" and jogador == "pedra":
                print(f"O computador escolheu {self.opcoes} e você escolheu {jogador}. ")
                time.sleep(1.5)
                print("O computador ganhou!")
                lista[1] = lista[1] + 1
                print(f"Placar: \nJogador = {lista[0]} X Computador = {lista[1]}")
                time.sleep(1.5)
                if lista[1] == 2:
                    print("O computador ganhou duas rodadas! Fim de jogo.")
                    break
            if self.pc == "tesoura" and jogador == "pedra":
                print(f"O computador escolheu tesoura e você escolheu pedra. ")
                time.sleep(1)
                print("Você ganhou!")
                lista[0] = lista[0] + 1
                print(f"Placar: \nJogador = {lista[0]} X Computador = {lista[1]}")
                time.sleep(1.5)
                if lista[0] == 2:
                    print("Você ganhou duas rodadas! Fim de jogo.")
                    break
            if self.pc == "tesoura" and jogador == "papel":
                print(f"O computador escolheu tesoura e você escolheu papel. ")
                time.sleep(1.5)
                print("O computador ganhou!")
                lista[1] = lista[1] + 1
                print(f"Placar: \nJogador = {lista[0]} X Computador = {lista[1]}")
                time.sleep(1.5)
                if lista[1] == 2:
                    print("O computador ganhou duas rodadas! Fim de jogo.")
                    break
            if self.pc == "papel" and jogador == "tesoura":
                print(f"O computador escolheu {self.opcoes} e você escolheu {jogador}. ")
                time.sleep(1.5)
                print("Você ganhou!")
                lista[0] = lista[0] + 1
                print(f"Placar: \nJogador = {lista[0]} X Computador = {lista[1]}")
                time.sleep(1.5)
                if lista[0] == 2:
                    print("Você ganhou duas rodadas! Fim de jogo.")
                    break

class Jogador():
    def jogador(self):
        usuario = str(input("Digite seu nome: "))
        jogo = Jogo()
        jogo.pedra_papel_tesoura()


if __name__ == "__main__":
    jogador = Jogador()
    jogador.jogador()

