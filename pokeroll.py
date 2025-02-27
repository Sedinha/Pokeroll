regiao1 = Region(2895,219,391,690)
regiao2 = Region(1933,221,388,690)

pop_up1 = Region(2897,367,389,418)

pop_up2 = Region(1935,334,385,467) 
#Definindo imagem dos elementos a serem clicados
coords = {
    "botao_month": "Month.jpg",
    "botao_7": "Month_choice.jpg",
    "botao_year": "Year.jpg",
    "botao_2023": "Year_choice.jpg",
    "botao_ok": "OK-1.png",
    "botao_terms": "termsPrivacy.png",
    "botao_privacy":"privacyTerms-1.png" ,
    "botao_close": "X%20(button).png",
    "agree_verify": "V%20(confirm%20button).png",
    "create_s_data": "Create_new_save_data.png",
    "not_now": "Not_now.png",
    "next": "next.png",
    "lapis": "lapis.png",
    "campo_name": "campo_nome.png",
    "mewTwo": "genetic_Mewtwo.png",
    "choose": "choose_this_one.png",
    "seta" : "seta.png",
    "seta2" : "seta2.png",
    "maozinha": "maozinha.png",
    "maozinhaLado": "maozinhaLado.png",
    "missions": "missions.png",
    "complete_all": "completeAl.png",
    
}
# Definir as posições iniciais e finais para o deslize do mouse
posicao_inicial = Location(50, 400)  # Ajuste as coordenadas conforme necessário
posicao_final = Location(500, 400)  # Ajuste as coordenadas conforme necessário
# Função para clicar em um botão
def clicar_botao(imagem_botao, regiao):
    if regiao.exists(imagem_botao,10):
        regiao.click(imagem_botao)
    else:
        print("Botao nao encontrado na tela")

# Função para clicar em uma posição relativa
def clicar_relativo(regiao, x_offset=0, y_offset=0):
    loc = regiao.getLastMatch().getTarget()
    new_loc = Location(loc.x + x_offset, loc.y + y_offset)
    click(new_loc)

# Função para digitar texto em um campo
def digitar_texto(imagem_campo, texto, regiao):
    if regiao.exists(imagem_campo, 10):
        regiao.click(imagem_campo)
        type(texto)
    else:
        print("Campo nao encontrado na tela")

# Função para deslizar o mouse horizontalmente em uma região
def deslizar_mouse_horizontalmente(regiao, posicao_inicial, posicao_final):
    # Ajustar as coordenadas de acordo com a região
    posicao_inicial = Location(regiao.x + posicao_inicial.x, regiao.y + posicao_inicial.y)
    posicao_final = Location(regiao.x + posicao_final.x, regiao.y + posicao_final.y)
    
    # Executar o deslize do mouse
    dragDrop(posicao_inicial, posicao_final)
#Funcao para automatizacao
def menu0(regiao,pop_up):
        # Clicar no botão Month
    clicar_botao(coords["botao_month"], regiao)

    # Selecionar o mês '7'
    clicar_botao(coords["botao_7"], regiao)

    # Clicar no botão Year
    clicar_botao(coords["botao_year"], regiao)

    # Selecionar o ano '2023'
    clicar_botao(coords["botao_2023"], regiao)

    #Clicar no botão primeiro Botão OK
    clicar_botao(coords["botao_ok"], regiao)

    # Clicar no botão OK usando a sub-região específica
    clicar_botao(coords["botao_ok"], pop_up)

def accept_TP(regiao):
    # Clicar no botão Terms of Use
    clicar_botao(coords["botao_terms"], regiao)

    # Fechar o pop-up de Terms of Use
    clicar_botao(coords["botao_close"], regiao)

    # Clicar no botão Privacy Notice
    clicar_botao(coords["botao_privacy"], regiao)

    # Fechar o pop-up de Privacy Notice
    clicar_botao(coords["botao_close"], regiao)

    #Clicar no Botão de Aceitar os Termos
    clicar_botao(coords["agree_verify"], regiao)

    # Clicar no segundo botão de confirmação (8-9 pixels abaixo)
    clicar_relativo(regiao, 0, 50)

    # Clicar no primeiro botão de confirmação
    clicar_botao(coords["botao_ok"], regiao)

# Função para abrir pacotes de cartas
def open_cards_package(regiao):
    # Definir as posições iniciais e finais para o deslize do mouse
    # Definir as posições iniciais e finais para o deslize do mouse
    posicao_inicial = Location(50, 400)  
    posicao_final = Location(500, 400)

    giraCarta_inicial =  Location(100, 300)
    giraCarta_final = Location(700, 300)

    # Deslizar o mouse horizontalmente
    deslizar_mouse_horizontalmente(regiao, posicao_inicial, posicao_final)

    # Fazer clique na posição (150, 300) quatro vezes
    for _ in range(4):
        click(Location(regiao.x + 150, regiao.y + 300))
    
    # Finalizar com um deslize do mouse na posição inicial mas sempre na posição final em 300
    deslizar_mouse_horizontalmente(regiao, giraCarta_inicial, giraCarta_final)

def createSave(regiao):
    #clicar_botao(coords["create_s_data"], regiao)
    #clicar_botao(coords["not_now"], regiao)
    clicar_botao(coords["botao_ok"],regiao)
    #clicar de novo o botao ok, porem com clicar relativo
    #clicar_relativo(regiao, 0, 0)
    #clicar no meio da tela
    #clicar no skip
    
def start(regiao,pop_up):
    #clicar_botao(coords["next"],regiao)
    #clicar_botao(coords["botao_ok"],regiao)
    #clicar_botao(coords["lapis"],regiao)
    #digitar_texto(coords["campo_name"], "Gengius***", regiao)
    #clicar_botao(coords["botao_ok"],regiao)
    #clicar_relativo(regiao, 0, 0)
    #clicar_relativo(regiao, 0, 0)
    #clicar_botao(coords["mewTwo"],regiao)
    #clicar_botao(coords["choose"],regiao)
    #deslizar_mouse_horizontalmente(regiao1,posicao_inicial,posicao_final)
    #open_cards_package(regiao)
    #timer
    #deslizar_mouse_horizontalmente(regiao1,swap_inicial,swap_final)
    #clicar_botao(coords["seta"],regiao)
    #clicar_botao(coords["maozinha"],regiao)
    #clicar_botao(coords["botao_ok"],regiao)
    clicar_botao(coords["botao_ok"],pop_up)

def start_screen(regiao):
    #clicar_botao(coords["missions"],regiao)
    #waits
    #clicar_botao(coords["seta"],regiao)
    #clicar_botao(coords["maozinhaLado"],regiao)
    #waits
    #clicar_botao(coords["maozinhaLado"],regiao)
    #clicar_botao(coords["botao_ok"],regiao)
    #clicar_botao(coords["seta2"],regiao)
    #clicar_relativo(regiao, 0, 0)
    clicar_botao(coords["mewTwo"],regiao)
    
    
    
# Executar ações para ambas as instâncias
print("Iniciando automação para a instância 1...")
#menu0(regiao1, pop_up1)
swap_inicial = Location(150, 500)
swap_final = Location(150, 40)
print("Iniciando automação para a instância 2...")
#menu0(regiao2, pop_up2)
#accept_TP(regiao1)
#createSave(regiao1)
#start(regiao1,pop_up1)
start_screen(regiao1)
