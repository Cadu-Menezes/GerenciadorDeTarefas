import psutil 
import pygame


def mostra_uso_memoria():    
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20 
    tela.fill(preto)
    pygame.draw.rect(s1, azul, (20, 50, largura_tela-2*20, 70))
    larg = larg*mem.percent/100      
    pygame.draw.rect(s1, vermelho, (20, 50, larg, 70))
    tela.blit(s1, (0, 0))
    total = round(mem.total/(1024**3), 1) 
    texto_barra = "Uso de memória (Total: " + str(total) + "GB): "  
    text = font.render(texto_barra, 1, branco) 
    tela.blit(text, (20, 10)) 


def mostra_uso_cpu ():   
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela -2*20
    pygame.draw.rect(s2, azul, (20, 50, largura_tela-2*20, 70))
    larg = larg*capacidade/100
    pygame.draw.rect(s2, vermelho, (20, 50, larg, 70))
    tela.blit(s2, (0, altura_tela/3))
    text = font.render ("Uso da CPU:", 1, branco )     
    tela.blit(text, (20, 200)) 


def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela -2*20
    pygame.draw.rect(s3, azul, (20, 50, largura_tela-2*20, 70)) 
    larg = larg*disco.percent/100
    pygame.draw.rect(s3, vermelho, (20, 50, larg, 70))
    tela.blit(s3, (0, 2*altura_tela/3))
    total =  round(disco.total/(1024**3), 2)
    texto_barra = "Uso de Disco: (Total: " +str(total) + " GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 400))  


def endereço ():
    dic_interfaces = psutil.net_if_addrs()
    ip = dic_interfaces["Ethernet"][1].address
    larg = largura_tela -2*20
    texto_ip = f"Endereço IP: {ip}" 
    text = font.render(texto_ip, 1, branco)
    tela.blit(text, (20, 550))


azul = (0, 0, 255)  
vermelho = (255, 0, 0)  
branco = (255, 255, 255) 
preto = (0, 0, 0)


pygame.font.init()
font = pygame.font.Font(None, 32)


largura_tela = 800   
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Gerenciador de Tarefas ")   
pygame.display.init()


s1 = pygame.surface.Surface((largura_tela, altura_tela/3))
s2 = pygame.surface.Surface((largura_tela, altura_tela/3))
s3 = pygame.surface.Surface((largura_tela, altura_tela/3))


pygame.draw.rect(s1, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(s1, (0, 0))
pygame.draw.rect(s2, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(s2, (0, altura_tela/3))
pygame.draw.rect(s3, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(s3, (0, 2*altura_tela/3))


clock = pygame.time.Clock()


cont = 30 
terminou = False 
while not terminou:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            terminou = True    


    if cont == 30: 
        mostra_uso_memoria()
        mostra_uso_cpu()    
        mostra_uso_disco()  
        endereço () 
        cont = 0   
   

    pygame.display.update()  
    clock.tick(60) 
    cont = cont + 1  
pygame.display.quit()