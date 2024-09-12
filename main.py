#Bibliotecas
import pygame

#Inicialização
pygame.init()
pygame.font.init()

#Tela
tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Jogo de Detetive')
fonte = pygame.font.Font(None, 40)

#Imagens
largura_tela, altura_tela = tela.get_size()
ini = pygame.image.load("./assets/inicio.png")
introduc = pygame.image.load("./assets/introducao1.png")
introduc1 = pygame.image.load("./assets/introducao2.png")
regra = pygame.image.load("./assets/regras.png")
cenario = pygame.image.load("./assets/cena.png")
sus = pygame.image.load("./assets/suspeitos.jpeg")
dica = pygame.image.load("./assets/dicas.png")
premisa = pygame.image.load("./assets/premisas.png")
final = pygame.image.load("./assets/ganhou.png")

#Dimenção imagem
inicio = pygame.transform.scale(ini, (largura_tela, altura_tela))
regras = pygame.transform.scale(regra, (largura_tela, altura_tela))
introducao = pygame.transform.scale(introduc, (largura_tela, altura_tela))
introducao1 = pygame.transform.scale(introduc1, (largura_tela, altura_tela))
suspeitos = pygame.transform.scale(sus, (largura_tela, altura_tela))
dicas = pygame.transform.scale(dica, (largura_tela, altura_tela))
premisas = pygame.transform.scale(premisa, (largura_tela, altura_tela))
ganhou = pygame.transform.scale(final, (largura_tela, altura_tela))

#Variaveis
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = (135, 206, 235)
color_passive = (177, 188, 85)
branco = (255, 255, 255)
preto = (0, 0, 0)
active = False
LEFT = 1
RIGHT = 3
input_rect.x +=355
input_rect.y +=425
input_rect.width *= 2
input_rect.height *= 2



#Cenas
loop = True
cena = "inicial"

#Principal
while loop:
    #Inicio
    if cena == "inicial":#Anthony
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "regras"

            tela.blit(inicio, (0 , 0))

    #Regras
    if cena == "regras":#Rafa
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "introducao"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "inicial"
            tela.blit(regras,(0, 0))

    #Introducao
    elif cena == "introducao":#Gustavo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              loop = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "introducao1"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "regras"
        tela.blit(introducao, (0 , 0))

    #Introducao1
    elif cena == "introducao1":#Gustavo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              loop = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
              cena = "jogo"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "introducao"
        tela.blit(introducao1, (0 , 0))
  
    #Cenario
    elif cena == "jogo":#Rafa
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
              
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "suspeitos"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "introducao1"
            tela.blit(cenario, (0, 0))

    #Suspeitos
    elif cena == "suspeitos":#Gustavo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "dicas"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "jogo"
            tela.blit(suspeitos, (0, 0))

    #Dicas
    elif cena == "dicas":#Anthony
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                cena = "premisas"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "suspeitos"
            tela.blit(dicas, (0, 0))

    #Premisas
    elif cena == "premisas":#Anthony
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if input_rect.collidepoint(event.pos):
                  active = True
                else:
                  active = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                cena = "dicas"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_text == "U":
                  cena = "ganhou"
                # Verifica Backspace
                if event.key == pygame.K_BACKSPACE:
                  # Apaga o texto
                  user_text = user_text[:-1]

                # Texto do usuario
                else:
                  user_text += event.unicode
            #Fundo
            tela.blit(premisas, (0, 0))
            if active:
              color = color_active
            else:
              color = color_passive

            #Desenha a caixa de resposta
            pygame.draw.rect(tela, color, input_rect)

            text_surface = fonte.render(user_text, True, (0))

            #Desenha o texto
            tela.blit(text_surface, (input_rect.x+5, input_rect.y+5))

            #Limitar o texto dentro da caixa de resposta
            input_rect.w = max(100, text_surface.get_width()+10)


    elif cena == "ganhou":#Geral
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False
      tela.blit(ganhou, (0, 0))
              



    pygame.display.flip()

'''
1.Milton foi morto por uma Serra*
2.Joaquim ou Judite estavam na cozinha*
3.Se o Marco estava no quarto, então Rodolfo atirou no Milton*
4.Se Joaquim estava na cozinha, então Judite matou o milton
5.Se Marco não estava no quarto, então Joaquim não estava na cozinha
6.Se Judite estava na cozinha, então Peter matou Milton *
7.Judite ou Marco tinham uma faca
8.Se Rodolfo atirou no Milton, então estava na sala
9.Se Rodolfo estava na sala, então Marco tinha uma faca


Q. Judite estava na cozinha*
P. Joaquim estava na cozinha*
R. Marco estava no quarto*
S. Rodolfo atirou no milton*
T. Judite matou Milton
U. Peter matou o milton*
X. Judite tinha uma faca
W. Marco tinha uma faca
Z. Rodolfo estava na sala
(dedução lógica = ~S)*


1.Z => W - Hipotese
2.P V Q - Hipotese
3.R => S - Hipotese
4.P => T - Hipotese
5.~R => ~P - Hipotese
6.Q => U - Hipotese
7.X V W - Hipotese
8.S => Z - Hipotese

9.~S - Hipotese(dedução)
10.~R modus tolens(3)
11.~P modus ponens(5)
12.Q silogismo disjuntivo(2)
13.Conclusão:U  modus ponens(6)

'''
