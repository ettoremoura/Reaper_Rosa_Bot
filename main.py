# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 23:25:59 2019

@author: Ettore
"""

import telegram
import configparser
import redis
import random
import requests
from telegram.ext import Updater, CommandHandler
from datetime import date
from datetime import timedelta

# Configuring bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

# Connecting to Telegram API
# Updater retrieves information and dispatcher connects commands
updater = Updater(token=config['DEFAULT']['token'])
dispatcher = updater.dispatcher

# Connecting to Redis db
db = redis.StrictRedis(host=config['DB']['host'],
                       port=config['DB']['port'],
                       db=config['DB']['db'])

def start(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()

    # Welcome message
    msg = "Olá\n"
    msg += "Eu sou o {0} xD\n".format(me.first_name)
    msg += "O que você quer?\n\n"
    msg += "/ettore - Sorteia uma frase aleatória do Ettore\n"
    msg += "/saitama - Oh não Saitama acaba de Saitamar mais uma vez\n"
    msg += "/marilia - Marilialia não está com sorte hoje\n"
    msg += "/roraimense - É\n"
    msg += "/iron - Você está sendo atacado\n"
    msg += "/draude - Pagando bem que mal tem?\n"
    msg += "/irmao - Irmão do Saitama chegando\n"
    msg += "/aleatorio - Uma curiosidade aleatória na língua da rainha\n"
    msg += "/nasa - Uma foto aleatória que a nasa tirou\n"
    msg += "/piada - Uma piada aleatória na língua da rainha\n"
    

    # Commands menu
    main_menu_keyboard = [[telegram.KeyboardButton('/ettore')],
                           [telegram.KeyboardButton('/saitama')],
                           [telegram.KeyboardButton('/marilia')],
                           [telegram.KeyboardButton('/roraimense')],
                           [telegram.KeyboardButton('/iron')],
                           [telegram.KeyboardButton('/draude')],
                           [telegram.KeyboardButton('/irmao')],
                           [telegram.KeyboardButton('/aleatorio')],
                           [telegram.KeyboardButton('/nasa')],
                           [telegram.KeyboardButton('/piada')]]
                            
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
######################################
def ettore(bot, update):
    horas = str(random.randrange(19,24,1))
    minutos = str(random.randrange(0,61,1))
    if len(minutos) == 1:
            while minutos == '0' or minutos == '5':
                minutos = str(random.randrange(0,61,1))
            minutos= '0'+minutos
    else:
        while minutos[1] == '0' or minutos[1] == '5':
                minutos = str(random.randrange(10,61,1))
    lista_ettores =["WoW hoje às "+horas+":"+minutos+"?",'WoW é show!','Refém não é nem gente :P','Vou pro Rocket League.','Eu sou um anjo']
    i=random.randrange(0,len(lista_ettores),1)
    string=lista_ettores[i]
    bot.send_message(chat_id=update.message.chat_id,text=string)

ettore_handler = CommandHandler('ettore', ettore)
dispatcher.add_handler(ettore_handler)
######################################
def Saitama(bot, update):
    Saitamagem=str(random.randrange(1000,1000000,1))
    string='Saitama acaba de Saitamar pela '+Saitamagem+'ª vez !!!!'
    bot.send_message(chat_id=update.message.chat_id,text=string)

Saitama_handler = CommandHandler('Saitama', Saitama)
dispatcher.add_handler(Saitama_handler)
######################################
def marilia(bot, update):
    erro=str(random.randrange(100,1000000,1))
    string='Mas bah errei tiro pela '+erro+'ª vez :('
    bot.send_message(chat_id=update.message.chat_id,text=string)

marilia_handler = CommandHandler('marilia', marilia)
dispatcher.add_handler(marilia_handler)
######################################
def roraimense(bot, update):
    nivel=random.randrange(1,20,1)
    i=0
    string='e' 
    while i<nivel:
        string+='h'
        i+=1
    bot.send_message(chat_id=update.message.chat_id,text=string)
    
roraimense_handler = CommandHandler('roraimense', roraimense)
dispatcher.add_handler(roraimense_handler)
######################################
def iron(bot, update):
    objetos=['Balança de cozinha', 'Batedeira de bolo', 'Espremedor de fruta elétrico', 'Faca elétrica', 'Filtro de água', 'Forninho elétrico', 'Liquidificador para cozinha', 'Micro-ondas', 'Processador de alimentos', 'Um jogo de panelas em aço inox, que vem com frigideira sem tampa e três caçarolas com tampa (16, 20 e 24 cm)', 'Uma cozi-vapore de 20 cm', 'Panela de pressão de 5 litros, da melhor marca que tiver no mercado', 'Frigideira pequena de teflon', 'Grelha de ferro para bifes', 'Caneca guardadora de óleo usado com filtro', 'Chaleira com apito', 'Leiteira de inox ou aço esmaltado ou de plástico', 'Forma média de banho-maria para pudim', 'Forma média de bolo com furo no meio', 'Assadeiras retangulares (pequena, média e grande)', 'Forma média com aro removível', 'Latas para mantimento', 'Espagueteira', 'Dois jogos de tigelas plásticas com três tamanhos e cores diferentes', 'Bacias para lavar verdura', 'Centrífuga de folhas', 'Escorredor de arroz', 'Potes plásticos de vários tamanhos e profundidade com tampa', 'Secador de salada', 'Uma lata de lixo grande', 'Utensílios para pia: ','Escorredor de louça', 'Lixeira pequena para colocar sobre a pia', 'Panos de pia', 'Plástico protetor de pia, para não lascar a louça', 'Porta- detergente', 'Porta- fósforos', 'Porta- papel', 'Porta- sabão de pia, e esponja', 'Rodo para pia', 'Saleiro', 'Abridores de garrafas, de lata, e saca-rolha', 'Batedor de carne', 'Boleador', 'Caneca com as medidas dos ingredientes impressas', 'Colheres de pau', 'Colheres medidoras', 'Concha', 'Descascador de legumes', 'Escumadeira', 'Espátula', 'Garfão (garfo longo)', 'Jarra medidora', 'Jogo de facas para cozinha (dois tamanhos)', 'Luva térmica', 'Pão duro pequeno e médio', 'Pincel', 'Ralador triangular de inox para cebola, queijo, e fatias finas', 'Três tábuas para carne, legumes, e frutas', 'Três peneiras de tamanhos e espessuras de trama variados', 'Caldeirão', 'Cortador de ovos cozidos', 'Cortador de pastel', 'Cortador de pizza', 'Cuscuzeiro', 'Descaroçador de azeitonas', 'Descaroçador de maçã', 'Foie', 'Porta- condimentos', 'Ralador e fatiador de legumes', 'Rolo de abrir massa', 'Tesoura trinchante de frango', 'Descansos de panela', 'Funil', 'Porta- condimento', 'Porta- sal', 'Saco de confeiteiro', 'Tesoura para embalagens, papel manteiga, verduras', 'Saiba agora onde guardar todos os utensílios em sua cozinha', '1 açucareiro', '1 bandeja grande', '1 bandeja pequena', '1 cesto para pão', '1 coador pequeno para leite', '1 concha para sorvete', '1 cortador de queijo', '1 espremedor simples de laranja', '1 faca de pão', '1 garrafa de vidro para colocar água na geladeira', '1 garrafa térmica branca para leite', '1 garrafa térmica preta para café', '1 jogo de facas pequenas de serra', '1 manteigueira', '1 porta- adoçante de saquinho', '1 portal- mel', '1 porta- queijo ralado', '1 tesoura', '1 torradeira', '1 tostex de tefal', 'Formas de plástico para gelo', 'Pegador de frios', 'Porta- frios', 'Prato para pudim / bolo', 'Prato para rocambole', 'Quebra-nozes', 'Queijadeira com tampa', 'Toalhas de mesa e jogos americanos', '1 aparelho de chá completo', '1 aparelho de jantar completo', '1 bandeja pequena', '1 dúzia de copos de água inquebráveis', '1 faqueiro', '1 molheira', '1 pegador de macarrão', '1 pegador de salada', '1 pote pequeno para o sal', '1 prato de vidro para colocar 1 pudim ou frutas', '1 tigela de vidro para colocar a salada de frutas ou doce em calda', '1 vidro pequeno para o vinagre', 'Suportes de travessa (madeira ou inox)', 'Vasilhas pequenas de vidro para a sobremesa', 'Copos para whisky', 'Copos para cerveja', 'Copos para caipirinha', 'Copos para champagne', 'Copos para refrigerante', 'Descansa copos', 'Porta-vinho', 'Panos de prato só para o bar', 'Réchaud para conhaque', '1 dosador de whisky ', '1 coqueteleira', '1 pilão para caipirinhas', '1 copo para mexer coquetéis que não possam ser agitados', '2 bastões para mexer coquetéis de cabo longo', '2 colheres de mexer coquetéis, de cabo longo e cabo curto', '1 espremedor de frutas', '1 coador ', '1 faca pequena de serra', '1 tábua para cortar frutas', '1 máquina de moer gelo', '1 balde de gelo', '1 pegador de gelo', '1 concha pequena para pegar gelo moído', '1 balde para gelo', '1 saca-rolha para vinhos e abridor de garrafa', '1 jarra pequena ', '1 jarra grande ', '1 lixeira pequena para pia', 'Marcador de copo', 'Termômetro para medir a temperatura do vinho', 'Colarinho de garrafa', 'Tampa para fechamento hermético', 'Cesta para torradas', 'Espetos de cabo curto para pegar aperitivos', 'Faca para cortar queijo', 'Faquinhas para aperitivo', 'Garfinhos para aperitivo', 'Guardanapo pequeno de tecido', 'Porta- guardanapos de papel', 'Tábua para cortar queijo', 'Vasilhas para aperitivos', '1 aparelho de jantar para churrasco', '2 toalhas', 'Acendedor de churrasqueira', 'Assadeira de borda baixa para derreter queijo', 'Cestas para pão', 'Conjunto para churrasco cabo longo duas peças (garfão e faca comprida)', 'Espátula', 'Espeto para churrasco', 'Faqueiro de cabo de madeira', 'Grelha fixa para churrasqueira', 'Pegador de carnes', 'Puxador de brasa', 'Tábua para cortar churrasco com coletor de suco da carne', 'Travessas de madeira para colocar o churrasco', 'Braseiro pequeno de ferro', 'Carrinho para churrasco', 'Gira-grill', 'Aparelho de barbear elétrico', 'Cesto para roupa suja', 'Cestos de lixo para a pia e para a bacia', 'Espelho de parede com luz e aumento', 'Porta-maquiagem', 'Porta- pasta e escova de dente', 'Porta- toalhas', 'Porta-xampu', 'Recipientes para algodão, cotonete e lenços de papel', 'Saboneteira para o Box', 'Saboneteira sobre a pia', 'Secador de cabelos', 'Tapete na saída do Box e em frente a pia', 'Aramados para objetos de uso junto ao tanque', 'Bacia grande para roupa de cama e banho', 'Bacia média para roupa íntima', 'Balde de alumínio para ferver roupa', 'Balde para roupas em geral', 'Balde para toalhas de mesa e panos de prato', 'Cabides de plástico', 'Cesto arejado para roupa suja esperando lavagem', 'Cesto de roupas suja e limpa', 'Cesto para roupa passada', 'Cesto para roupa seca a passar', 'Dois ferros de passar roupas', 'Forração para a tabua de passar, macia e branca', 'Forros térmicos', 'Borrifador de água para roupa', 'Panos brancos de tecido de algodão fino para passar roupa sem que elas brilhem', 'Porta-ferro', 'Porta-prendedor de roupa', 'Prendedores de roupa', 'Varais de teto ou de armar', 'Máquina de lavar roupas ou um tanquinho', 'Secadora', 'Tábua de passar roupa', 'Tanque', 'Amaciante ou vinagre branco', 'Escova para lavar roupa', 'Sabão em pedra e em pó', '1 pá de lixo', '2 Rodos um para a cozinha e outro para o banheiro', 'Balde de cor escura para limpeza', 'Enceradeira', 'Espanador de pó', 'Flanelas', 'Lixeira', 'Lixeira para lixo reciclável', 'Pano de saco ','Panos de limpeza para o chão', 'Vassoura de pelo só para varrer a sala e os quartos', 'Vassoura de piaçava', 'Vassoura mágica ou aspirador de pó', 'Recipiente Plástico para organizar o material de lavar banheiro', 'Escova para limpar dentro de bacia', 'Esponja multiuso', 'Pano de chão', 'Pano de limpeza para secar as pias', 'Flanela para lustrar as torneiras', 'Produtos necessários para a higienização', 'Cera de carnaúba', 'Escova de limpar estofados', 'Esponja e sabão de coco para limpar móveis laqueados e parede', 'Flanela', 'Lustra móvel', 'Pano de limpeza branco', 'Recipiente Plástico para organizar o material para limpar salas e quartos', 'Álcool ou produtos industrializados', 'Flanela limpa e seca para tirar o pó', 'Jornal', 'Pano seco (que não solte pelo)', 'Recipiente Plástico para organizar os produtos', 'Removedor', 'Algodão industrial','Estopa', 'Flanela', 'Polidor de metal', 'Polidor de prata', 'Recipiente plástico para organizar os produtos','Abajur Octo Gota De Madeira Chocolate C/ Cúpula De Tecido Bege 48cm']
    i=random.randrange(0,len(objetos),1)
    string=['Estou sendo atacado por '+objetos[i]+'!!!!!!!!','Não posso estou na minha '+str(i)+'ª mesa de RPG']
    i=random.randrange(0,len(string),1)
    bot.send_message(chat_id=update.message.chat_id,text=string[i])
    
iron_handler = CommandHandler('iron', iron)
dispatcher.add_handler(iron_handler)
######################################
def draude(bot, update):
    string='Você está pagando e ainda exige que seja maior de idade????'
    bot.send_message(chat_id=update.message.chat_id,text=string)
    
draude_handler = CommandHandler('draude', draude)
dispatcher.add_handler(draude_handler)
######################################
def aleatorio(bot, update):
    curiosidade=requests.get('https://uselessfacts.jsph.pl//random.json?language=en').json()
    l=requests.get('https://api.mymemory.translated.net/get?q='+curiosidade['text']+'&langpair=en|pt-br')
    string=l.json()['responseData']['translatedText'].replace('&quot','"')
    bot.send_message(chat_id=update.message.chat_id,text=string)
    
aleatorio_handler = CommandHandler('aleatorio', aleatorio)
dispatcher.add_handler(aleatorio_handler)
######################################
def irmao(bot, update):
    chance = str(random.randrange(0,101,1))
    string = 'Com ' + chance + '% de chance o irmão do Saitama irá usar o PC hj'
    if int(chance) >= 51:
        string+='\n F'
    elif int(chance) == 50:
        string+=' :| \n F?'
    else:
        string+=' :) \n'
    bot.send_message(chat_id=update.message.chat_id,text=string)
    
irmao_handler = CommandHandler('irmao', irmao)
dispatcher.add_handler(irmao_handler)
#####################################
def nasa(bot,update):
    i=random.randrange(0,20)
    data=str(date.today()-timedelta(days=i))
    k=requests.get('https://api.nasa.gov/planetary/apod?api_key=6pTOzj7m7XrNuEcbgxFuZI7Ja0qdB6NX7RqSs3cB&date='+data)
    k=k.json()
    print(k)
    bot.sendPhoto(update.message.chat_id,k['url'])
     
nasa_handler = CommandHandler('nasa', nasa)
dispatcher.add_handler(nasa_handler)
#####################################
def piada(bot,update):
    k=requests.get('https://icanhazdadjoke.com/', headers={'Accept':'application/json'})
    l=requests.get('https://api.mymemory.translated.net/get?q='+k.json()['joke']+'&langpair=en|pt-br')
    text1=l.json()['responseData']['translatedText'].replace('&quot','"')
    bot.send_message(chat_id=update.message.chat_id,text = text1)
     
piada_handler = CommandHandler('piada', piada)
dispatcher.add_handler(piada_handler)