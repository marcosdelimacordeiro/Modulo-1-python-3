# faca um programa em pyhon que abra e reproduza o audio de um arquivo mp3.
#comando para instalar o pygame pip install pygame
#Importa a biblioteca pygame, que permite trabalhar com jogos, sons, eventos
import pygame
#Inicializa todos os módulos do pygame (áudio, vídeo, teclado, etc).É tipo “ligar” o pygame.
pygame.init()
#nicializa somente o módulo de áudio (mixer). Serve para garantir que o som vai funcionar corretamente.
pygame.mixer.init()
#Carrega o arquivo de música na memória.Nada toca ainda — o pygame só “prepara” o áudio.mixer.music → controla músicas longas (mp3, ogg),load() → carrega o arquivo
pygame.mixer.music.load('C:/Users/Windows/Downloads/musica.mp3')
#Começa a tocar a música carregada., sem paramentro  toca somente uma vez
pygame.mixer.music.play()

# verifica se musica esta tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
