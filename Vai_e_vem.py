'''A empresa de transporte terrestre interestadual Expresso Vai-e-Vem adquiriu uma nova frota de ônibus com 2 andares. Com a nova aquisição,
a Vai-eVem deseja implementar uma nova funcionalidade no seu programa de vendas de passagens para que atenda a sua nova demanda. Os novos
ônibus possuem capacidade para 63 passageiros divididos nos dois andares. Além disso, os ônibus possuem uma fileira leito (cadeira que reclina
até virar uma cama) e outra fileira semi-leito (cadeira com reclinação mais confortável).
   No andar superior, o lado direito possui 8 cadeiras do tipo Leito, enquanto no lado esquerdo há 30 cadeiras do tipo semi-leito, sendo duas
por fileira. No andar inferior do ônibus, do lado direito, há 5 cadeiras do tipo leito, já do lado esquerdo, há 23 cadeiras do tipo semi-leito,
sendo também duas por fileira. O valor da passagem varia do trecho do percurso, sendo que o valor da passagem leito é 30% a mais que a do 
semi-leito. Uma novidade nessa nova atualização são os status:Ocupado e Livre. O status Ocupado pode ter dois sub-estados Reservado e Comprado.
O status Reservado destina-se a uma pré-venda que não foi confirmada, a qual pode ser efetivada ou não. Já o status Ocupado significa que o
assento foi comprado. Por fim, o Livre designa os assentos livres. O sistema deve ter os seguintes relatórios:

 - Total de assentos livres e ocupados por ônibus, especificando o quantitativo por andar.

 - Total de assentos ocupados por estado, Reservado e Comprado por ônibus, especificando o quantitativo por andar.

 - Total de passagens compradas por tipo de ônibus, especificando o quantitativo por andar.

 - Especificar qual o ônibus da frota teve mais passagens vendidas.

 - Especificar qual o ônibus da frota teve menos passagens vendidas.
'''
 
def criarmenu(OP):  # <-- Gera Menu principal:
    c = 0
    print('\n----------------------------------------------------')
    print('Digite o número correspondente a ação desejada:')
    for q1 in OP:
        c = c + 1
        print('[{}] - {}'.format(c, q1))
    print('----------------------------------------------------')
    Esc = int(input('\nOpção: '))
    while Esc <= 0 or Esc > c:
        Esc = int(input('Digite uma opção correta: '))
    return Esc

class trecho:
    def __init__(self) -> None:
        self.__trechos = []
        self.__listaonibus = []
        arquivo = open('Trechos.txt', 'r', encoding='utf8') #lê o .txt que comtem o nome e o preço dos trechos
        for linhas in arquivo:
            self.__trechos.append(linhas.split())
        

    def gettrechos(self):
        return self.__trechos
    def getlistaonibus(self):
        return self.__listaonibus

    def trechos(self): #Pega os nomes dos trechos
        c = 0
        print(f'\nTemos os trechos:\n')
        for x in self.gettrechos():
            c = c + 1
            print(f'{c} - {x[0]}')
    
    def rodaronibus(self, Ntrecho, totalonibus): #Pega as info do .txt e cria os ônibus na rota
        c = len(self.getlistaonibus()) #Sempre conta quantos onibus existem, para que sempre que for criar um o numero de ID nunca se repita
        opção = Ntrecho
        qtonibus = totalonibus
        for buzao in range(qtonibus): #Realiza o tanto de vezes informado pelo usuário
            c = c + 1
            trecho = self.gettrechos()[opção-1] #Pega o valor e o nome dotrecho
            moldeonibus = onibus(int(trecho[1])) #Seta o valor do trecho no onibus
            moldeonibus.setnumeroonibus(c) #Passa o numero para o onibus
            moldeonibus.settrechos(trecho[0]) #Seta o nome do trecho no onibus
            for andares in moldeonibus.getandares(): #pega os andares do onibus
                for poltronas in andares.getpoltronas(): #Pega as poltrona dos andares
                    poltronas.setonibus(c) #Seta o numero do onibus na poltrona (Aqui só usado para o comando tostring la na classe poltrona, para ficar mais organizado.)
            self.getlistaonibus().append(moldeonibus)
    
    def tostring(self): #exibe as info do onibus
        for buzao in self.getlistaonibus():
            print(f'O ônibus numero {buzao.getnumeroonibus()} está no trecho {buzao.gettrecho()} com valor de R$ {buzao.getpreçosemileito()} para semi-leito e R$ {round(buzao.getpreçosemileito()*1.3,2)} para leito.')
    
    def onibustrecho(self, trecho): #Informa os onibus que estão rodando no  trecho escolhido
        numerosonibus = []
        for buzao in self.getlistaonibus(): #Pega os onibus
            if buzao.gettrecho() == trecho: #verifica se o trecho passado é o mesmo que onibus roda
                numerosonibus.append(buzao.getnumeroonibus()) #Adiciona o numero do onibus na lista
        if numerosonibus != []: #Só realiza esse passo caso exista onibus no trecho informado
            print(f'\nNo trecho {buzao.gettrecho()} temos os onibus: ',end='') 
            for x in numerosonibus:
                print(f'{x}; ',end='') #passa os numeros dos onibus
            print('\n')
        return numerosonibus #Retorna a lista contendo os numeros dos onibus no trecho informado.

    # O método comprar() e reservar() fazem a mesma coisa. Note que o comprar() não utiliza o método de busca binária
    #consequnentemente ele acaba sendo mais confudo e longo.

    def comprar(self, trecho, nonibus, superior, npoltrona): #compra uma poltrona
        for onibus in self.getlistaonibus(): #pega o onibus
            if trecho.upper() == onibus.gettrecho().upper(): #verifica se o trecho do onibus bate com o da compra
                if nonibus == int(onibus.getnumeroonibus()): #Verifica se o numero do onibus bate com o da compra
                    for andares in onibus.getandares(): #Pega os andares do onibus
                        if superior == andares.getsuperior(): #Verifica se o andar é o mesmo do passado na compra
                            for poltronas in andares.getpoltronas(): #Pega a poltrona
                                if npoltrona == poltronas.getnumero(): #Verifica se a poltrona é a informada na compra
                                    if poltronas.getstatus() != True: #Verifica se a poltrona está ocupada
                                        print(f'A poltrona numero {poltronas.getnumero()} está no status {poltronas.getstatus()}\n') #informa o subestado da poltrona
                                    else: #Realiza a compra da poltrona
                                        poltronas.setstatus('Comprada') #Altera o estado para ocupado, subestado comprada
                                        onibus.passagemcomprada() #Aumenta 1 unidade de passagem comprada no onibus
                                        poltronas.tostring() #informa os dados da poltrona comprada.
                                        print(' ')
    
    def reservar(self, trecho, nonibus, superior, npoltrona): #Reserva uma poltrona
        onibus = self.buscabináriaonibus(nonibus) #Pega o onibus
        for andares in onibus.getandares(): #Pega os andares do onibus
            if superior == andares.getsuperior(): # Verificar se o andar (superior/inferior) bate com o informado na reserva
                poltronas = self.buscabináriapoltrona(andares,npoltrona) #Peg a poltrona
                if poltronas.getstatus() != True: # Verifica se a poltrona está livre
                    print(f'A poltrona numero {poltronas.getnumero()} está no status {poltronas.getstatus()}\n') #Se estiver ocupada, informa o subestado da poltrona
                else: #Realiza a reserva da poltrona
                    poltronas.setstatus('Reservada') #Altera o status da poltrona para ocupado, subestado Reservada.
                    poltronas.tostring() #Informa os dados da poltrona que foi reservada
                    print(' ')                         
    
    def statusassentos(self, nonibus): #Passa o estado das poltronas do onibus informado
        for onibus in self.getlistaonibus(): #Pega o onibus
            if nonibus == onibus.getnumeroonibus(): #verifica se é o onibus escolhido
                print(f'\nStatus do Onibus {onibus.getnumeroonibus()}:\n')
                onibus.assSuperior() #Informa o estado do andar superior
                onibus.assinferior() #Informa o estado do andar inferior

    def assentosocupados(self, nonibus): # Infomra o subestado da poltrona (Reservada/Comprada)
        Reservados = 0
        Comprados = 0
        for buzao in self.getlistaonibus(): #Pega o onibus
            if nonibus == buzao.getnumeroonibus(): #Verifica se é este onibus que desejamos verificar
                for andares in buzao.getandares(): #Pegar os andares do onibus
                    if andares.getsuperior(): #Verifica se é o superior
                        print(F'\nAssentos ocupados do onibus {buzao.getnumeroonibus()}:\n')
                        for polt in andares.getpoltronas(): #Pega as poltronas do andar
                            if polt.getstatus() == 'Reservada': #Verifica se a poltrona está reservada
                                Reservados = Reservados + 1
                            if polt.getstatus() == 'Comprada': #Verifica se a poltrona está comprada
                                Comprados = Comprados + 1
                        print(f'No andar superior do onibus {buzao.getnumeroonibus()} temos, comprados: \033[1;34m{Comprados}\033[0;0m  reservados: \033[1;34m{Reservados}\033[0;0m')
                        Reservados = 0
                        Comprados = 0
                    else:   # Aqui sobra o andar inferior
                        for polt in andares.getpoltronas(): #Pega as poltronas
                            if polt.getstatus() == 'Reservada': #Verifica se está reservada
                                Reservados = Reservados + 1
                            if polt.getstatus() == 'Comprada': #verifica se está comprada
                                Comprados = Comprados + 1
                        print(f'No andar Inferior do onibus {buzao.getnumeroonibus()} temos, comprados: \033[1;34m{Comprados}\033[0;0m  reservados: \033[1;34m{Reservados}\033[0;0m')
                        Reservados = 0
                        Comprados = 0
    
    def passagenscompradas(self, nonibus): #Mostra o tipo das passagens que foram compradas em algum onibus
        leito = 0
        semileito = 0
        for buzao in self.getlistaonibus(): # Pega o onibus
            if buzao.getnumeroonibus() == nonibus: # Verifica se o onibus é o que desejamos verificar
                for andares in buzao.getandares(): # Pega o andar do onibus
                    if andares.getsuperior(): # Pega o andar superior
                        print(f'\nAssentos comprados no onibus {buzao.getnumeroonibus()}:\n')
                        for assento in andares.getpoltronas(): #Pega as poltronas
                            if assento.getstatus() == 'Comprada': # Verifica se a poltrona está com status comprado
                                if assento.getespecial() == True: #Verifica se a poltrona é Leito
                                    leito = leito + 1
                                else: # Poltrona semi-leito
                                    semileito = semileito + 1
                        print(f'Comprados no andar superior:  leito-> \033[1;34m{leito}\033[0;0m, semi-leito-> \033[1;34m{semileito}\033[0;0m')
                        leito = 0
                        semileito = 0
                    else:
                        for assento in andares.getpoltronas(): #Pega andar inferior
                            if assento.getstatus() == 'Comprada': # Verifica se poltrona está com status comprado
                                if assento.getespecial() == True: # Verifica se a poltrona é leito
                                    leito = leito + 1
                                else: # Poltrona semi-leito
                                    semileito = semileito + 1
                        print(f'Comprados no andar inferior:  leito-> \033[1;34m{leito}\033[0;0m, semi-leito-> \033[1;34m{semileito}\033[0;0m\n')
                        leito = 0
                        semileito = 0
    
    def MaiseMenosVendido(self): #Mostra o onibu que mais vendeu e o que menos vendeu passagens.
        primeiro = True
        menor = 0
        maior = 0
        for buzao in self.getlistaonibus(): #Pega todos os onibus criados.
            if primeiro:
                menor = buzao #Declara o primeiro onibus lido como menor
                maior = buzao #Declara o primeiro onibus lido como maior
                primeiro = False
            else:
                if buzao.getvendidos() > maior.getvendidos(): #Compara o onibus que mais vendeu com o atual
                    maior = buzao
                if buzao.getvendidos() < menor.getvendidos(): #Compara o onibus que menos vendeu com o atual
                    menor = buzao 
        print(f'O onibus \033[1;34m{maior.getnumeroonibus()}\033[0;0m teve mais passagens vendidas.')
        print(f'O onibus \033[1;34m{menor.getnumeroonibus()}\033[0;0m teve menos passagens vendidas.')
    
    def buscabináriaonibus(self,item):
        lista = self.getlistaonibus()
        primeiro = 0
        ultimo = len(lista)-1
        encontrado = False
        
        while primeiro <= ultimo and not encontrado:
            meio = (primeiro + ultimo) // 2
            if lista[meio].getnumeroonibus() == item:
                encontrado = True
            else:
                if item < lista[meio].getnumeroonibus():
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return lista[meio]
    
    def buscabináriapoltrona(self,lista,item):
        lista = lista.getpoltronas()
        primeiro = 0
        ultimo = len(lista)-1
        encontrado = False
        
        while primeiro <= ultimo and not encontrado:
            meio = (primeiro + ultimo) // 2
            if lista[meio].getnumero() == item:
                encontrado = True
            else:
                if item < lista[meio].getnumero():
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return lista[meio]

class onibus:
    def __init__(self, preço) -> None:
        self.__numero = None
        self.__andares = []
        self.__Trecho = None
        self.__PreçoSemiLeito = preço
        self._vendidos = 0
        self.criaronibus() #Cria o onibus xD
        for andares in self.getandares(): #Pega os andares deste onibus
            for poltronas in andares.getpoltronas(): #pega as poltronas do andar
                poltronas.setvalor(preço) #Seta o preço da passagem para essa poltrona

    def getvendidos(self):
        return self._vendidos
    def getnumeroonibus(self):
        return self.__numero
    def getandares(self):
        return self.__andares
    def gettrecho(self):
        return self.__Trecho
    def getpreçosemileito(self):
        return self.__PreçoSemiLeito

    def setvendidos(self, valor):
        self._vendidos = valor
    def setnumeroonibus(self,valor):
        self.__numero = valor
    def setandares(self, valor):
        self.__andares = valor
    def settrechos(self, valor):
        self.__Trecho = valor
    
    def passagemcomprada(self):
        self.setvendidos(self.getvendidos()+1) # Guarda quantas passagens foram vendidas neste onibus

    def criaronibus(self): #Cria  o andar superior e inferior do onibus
        moldesuperior = andar() #Cria um molde da classe andar
        moldesuperior.setsuperior(True) #declara ela como andar superior
        moldesuperior.criarsuperior() #Cria o andar seguindo a distribuição de poltronas
        self.getandares().append(moldesuperior)

        moldeinferior = andar() #Cria um molde da classe andar
        moldeinferior.setsuperior(False) #declara ela como andar inferior
        moldeinferior.criarinferior() #Cria o andar seguindo a distribuição de poltronas
        self.getandares().append(moldeinferior)

    def assSuperior(self): #Informa os acentos livres e ocupados do andar superior
        ocupados = []
        livres = []
        for andares in self.getandares(): #Pega os andares presentes no onibus
            if andares.getsuperior() == True: #Pega o andar superior
                for poltronas in andares.getpoltronas(): #Pega as poltronas
                    if poltronas.getstatus() == True: #Verifica se está livre
                        livres.append(poltronas) #Adiciona na lista de poltronas livres
                    else: 
                        ocupados.append(poltronas) #Adiciona na lista de poltronas ocupadas
            
                print(f'No andar superior do ônibus {self.getnumeroonibus()} temos {len(livres)} poltronas livres.')
                for poltronas in livres: #printa o numero de todas as poltronas livres do andar superior
                    print(f'\033[1;32m{poltronas.getnumero()} - \033[0;0m',end='')
                
                print(f'\nNo andar superior do ônibus {self.getnumeroonibus()} temos {len(ocupados)} poltronas ocupadas.')
                for poltronas in ocupados: #printa o numero de todas as poltronas ocupadas do andar superior
                    print(f'\033[31m{poltronas.getnumero()} - \033[0;0m',end='')
    
    def assinferior(self): #Informa os acentos livres e ocupados do andar inferior
        ocupados = []
        livres = []
        for andares in self.getandares(): #Pega os andares presentes no onibus
            if andares.getsuperior() != True: #Pega o andar inferior
                for poltronas in andares.getpoltronas(): #Pega as poltronas
                    if poltronas.getstatus() == True: #Verifica se está livre
                        livres.append(poltronas) #Adiciona na lista de poltronas livres
                    else: 
                        ocupados.append(poltronas) #Adiciona na lista de poltronas ocupadas
            
                print(f'\n\nNo andar inferior do ônibus {self.getnumeroonibus()} temos {len(livres)} poltronas livres: ')
                for poltronas in livres: #printa o numero de todas as poltronas livres do andar inferior
                    print(f'\033[1;32m{poltronas.getnumero()} - \033[0;0m',end='')
                print(f'\n\nNo andar inferior do ônibus {self.getnumeroonibus()} temos {len(ocupados)} poltronas ocupadas:')
                for poltronas in ocupados: #printa o numero de todas as poltronas ocupadas do andar inferior
                    print(f'\033[31m{poltronas.getnumero()} - \033[0;0m',end='')

class andar:
    def __init__(self) -> None:
        self.__superior = None
        self.__poltronas = []

    def criarsuperior(self):
        contador = 0
        for x in range(38): #Quantidade de poltronas no andar superior
            contador = contador + 1 
            moldepoltrona = poltrona() #Cria um molde da classe poltrona
            moldepoltrona.setnumero(x+1) #Declara o numero da poltrona
            moldepoltrona.setandar('Superior') #Declara a poltrona como andar superior
            if contador == 3: #Essa regra que distribui os numeros de uma forma que faça sentido com a lógica da disposição das poltronas no andar.
                moldepoltrona.setespecial(True) #Declara poltrona como Leito
            else:
                moldepoltrona.setespecial(False) #Delcara poltrona como semi-leito
            if contador == 5:
                contador = 0
            self.getpoltronas().append(moldepoltrona) #Adiciona a poltrona na lista 
    
    def criarinferior(self): 
        contador = 0
        for x in range(28): #Quantidade de poltronas no andar inferior
            contador = contador + 1 #controla se a poltrona vai ser especial ou não. (imagem)
            moldepoltrona = poltrona() #Cria um molde da classe poltrona
            moldepoltrona.setnumero(x+1) #Declara o numero da poltrona
            moldepoltrona.setandar('Inferior') #Declara a poltrona como andar inferior
            if contador%5 == 0: #Essa regra que distribui os numeros de uma forma que faça sentido com a lógica da disposição das poltronas no andar.
                moldepoltrona.setespecial(True) #Declara poltrona como Leito
            else:
                moldepoltrona.setespecial(False) #Delcara poltrona como semi-leito
            self.getpoltronas().append(moldepoltrona) #Adiciona a poltrona na lista 

    def getsuperior(self):
        return self.__superior
    def getpoltronas(self):
        return self.__poltronas
    
    def setsuperior(self, valor):
        self.__superior = valor
    def setpoltronas(self, valor):
        self.__poltronas = valor
    
    def tostring(self): #Informa as poltronas do andar.
        if self.getsuperior() == True:
            print('\nAndar Superior: \n')
            for poltronas in self.getpoltronas():
                poltronas.tostring()
        else:
            print('\nAndar inferior: \n')
            for poltronas in self.getpoltronas():
                poltronas.tostring()

class poltrona:
    def __init__(self) -> None:
        self.__numero = None # Número é dado na classe andar
        self.__especial = None #Determina se é leito ou não na classe andar
        self.__livre = True #Sempre cria as poltronas em estado livre
        self.__valor = 0 #valor é dado na classe onibus
        self.__andar = None #valor será dado na classe andar
        self.__onibus = None #valor é dado na classe trecho
    
    def getonibus(self):
        return self.__onibus
    def getnumero(self):
        return self.__numero
    def getespecial(self):
        return self.__especial
    def getvalor(self):
        return self.__valor
    def getstatus(self):
        return self.__livre
    def getandar(self):
        return self.__andar
    
    def setonibus(self, valor):
        self.__onibus = valor
    def setnumero(self, valor):
        self.__numero = valor
    def setespecial(self, valor):
        self.__especial = valor
    def setvalor(self, valor):
        if self.getespecial() == True:
            self.__valor = round(valor * 1.3,2)
        else:
            self.__valor = valor
    def setstatus(self, valor):
        self.__livre = valor
    def setandar(self, valor):
        self.__andar = valor

   
    def poltronatipo(self):
        if self.getespecial() == True:
            tipo = 'Leito'
        else:
            tipo = 'Semi-leito'
        return tipo

    def tostring(self):
        if int(self.getnumero()) < 10:
            if self.getespecial() == True:
                print(f'\nOnibus {self.getonibus()} - Andar {self.getandar()} - Poltrona numero:  {self.getnumero()} - Tipo: {self.poltronatipo()} - Valor: R$ {self.getvalor()} - Status: {self.getstatus()}')
            else:
                print(f'\nOnibus {self.getonibus()} - Andar {self.getandar()} - Poltrona numero:  {self.getnumero()} - Tipo: {self.poltronatipo()} - Valor: R$ {self.getvalor()} - Status: {self.getstatus()}')
        else:
            if self.getespecial() == True:
                print(f'\nOnibus {self.getonibus()} - Andar {self.getandar()} - Poltrona numero: {self.getnumero()} - Tipo: {self.poltronatipo()} - Valor: R$ {self.getvalor()} - Status: {self.getstatus()}')
            else:
                print(f'\nOnibus {self.getonibus()} - Andar {self.getandar()} - Poltrona numero: {self.getnumero()} - Tipo: {self.poltronatipo()} - Valor: R$ {self.getvalor()} - Status: {self.getstatus()}')


Roteiro = trecho()
loop = 1

#Aqui abaixo eu crio os onibus. (alguns estão comentados para mostrar que se não tiver onibus rodando no trecho não será possivel comprar passagem)
Roteiro.rodaronibus(1, 3) #Cria três onibus no trecho 1 - AB
#Roteiro.rodaronibus(2, 2) #Cria dois onibus no trecho 2 - AC
#Roteiro.rodaronibus(3, 2) #Cria dois onibus no trecho 3 - BC

#Abaixo compro algumas passagens manualmente só para ter alguns dados nos objetos, possibilitando visualizar melhor como o funionamento geral.

#Passagem comprada no trecho AB, do onibus 1, no piso superior, na poltrona 1
Roteiro.comprar('AB', 1, True, 1) # (Trecho, Numero do Onibus, Superior ou não, Numero da poltrona)
#Passagem reservada no trecho AB, do onibus 1, no piso inferior, na poltrona 1
Roteiro.reservar('AB', 1, False, 1)
#passagem comprada no trecho AB, do onibus 2, no piso inferior, na poltrona 1
Roteiro.comprar('AB', 2, False, 1)

while loop == 1:
    opção = criarmenu(['Verificar status das poltronas.', 'Verificar poltronas ocupadas.', 'Verificar tipo de passagem vendida.', 'Verificar maior e menor vendedor.', 'Comprar passagem','Fazer reserva', 'Encerrar'])
    if opção == 1:
        numeroonibus = int(input(f'\nInforme o numero do onibus que deseja consultar {Roteiro.getlistaonibus()[0].getnumeroonibus()} ~ {Roteiro.getlistaonibus()[len(Roteiro.getlistaonibus())-1].getnumeroonibus()} : '))
        Roteiro.statusassentos(numeroonibus) #Mostra o status das poltronas de um onibus
    if opção == 2:
        numeroonibus = int(input(f'\nInforme o numero do onibus que deseja consultar {Roteiro.getlistaonibus()[0].getnumeroonibus()} ~ {Roteiro.getlistaonibus()[len(Roteiro.getlistaonibus())-1].getnumeroonibus()} : '))
        Roteiro.assentosocupados(numeroonibus) #Informa o sub estado as poltronas ocupadas
    if opção == 3:
        numeroonibus = int(input(f'\nInforme o numero do onibus que deseja consultar {Roteiro.getlistaonibus()[0].getnumeroonibus()} ~ {Roteiro.getlistaonibus()[len(Roteiro.getlistaonibus())-1].getnumeroonibus()} : '))
        Roteiro.passagenscompradas(numeroonibus) #Verifica o tipo das passagens que foram vendendias
    if opção == 4:
        Roteiro.MaiseMenosVendido() #mostra os onibus com mais passagens vendidas, e os com menos também
    if opção == 5:
        Roteiro.trechos() #Motra os trechos
        trechoescolhido = int(input(f'\nInfome o trecho para pronsseguir: '))
        onibusdisponivel = Roteiro.onibustrecho(Roteiro.gettrechos()[trechoescolhido-1][0]) #motra os onibus no trecho escolhido
        if onibusdisponivel != []:
            numerodoonibus = int(input('Infome o numero do onibus: '))
            andarescolhido = int(input(f'Informe o andar desejado:\n \n[1] - Superior\n[2] - Inferior\nOpção: '))
            if andarescolhido == 1:
                andarescolhido = True
            if andarescolhido == 2:
                andarescolhido = False
            numerocadeira = int(input('Infome o numero da poltrona: '))
            Roteiro.comprar(Roteiro.gettrechos()[trechoescolhido-1][0], numerodoonibus, andarescolhido, numerocadeira) #Passa todas as info e realiza a compra da passagem
        else:
            print('\nNão temos onubis rodando nesse trecho.')
    if opção == 6:
        Roteiro.trechos()
        trechoescolhido = int(input(f'\nInfome o trecho para pronsseguir: '))
        onibusdisponivel = Roteiro.onibustrecho(Roteiro.gettrechos()[trechoescolhido-1][0])
        if onibusdisponivel != []:
            numerodoonibus = int(input('Infome o numero do onibus: '))
            andarescolhido = int(input(f'Informe o andar desejado:\n \n[1] - Superior\n[2] - Inferior\nOpção: '))
            if andarescolhido == 1:
                andarescolhido = True
            if andarescolhido == 2:
                andarescolhido = False
            numerocadeira = int(input('Infome o numero da poltrona: '))
            Roteiro.reservar(Roteiro.gettrechos()[trechoescolhido-1][0], numerodoonibus, andarescolhido, numerocadeira)
        else:
            print('\nNão temos onubis rodando nesse trecho.')
    if opção == 7:
        loop = 0
