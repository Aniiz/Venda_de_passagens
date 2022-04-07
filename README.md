# Venda de Passagens

### Sobre:

Trabalho Final da disciplina de Estrutura de Dados.

##### Status: Finalizado.

### Proposta:


&nbsp;&nbsp;&nbsp;&nbsp;A empresa de transporte terrestre interestadual Expresso Vai-e-Vem adquiriu uma nova frota de ônibus com 2 andares. Com a nova aquisição,
a Vai-eVem deseja implementar uma nova funcionalidade no seu programa de vendas de passagens para que atenda a sua nova demanda. Os novos
ônibus possuem capacidade para 63 passageiros divididos nos dois andares. Além disso, os ônibus possuem uma fileira leito (cadeira que reclina
até virar uma cama) e outra fileira semi-leito (cadeira com reclinação mais confortável).</br>
&nbsp;&nbsp;&nbsp;&nbsp;No andar superior, o lado direito possui 8 cadeiras do tipo Leito, enquanto no lado esquerdo há 30 cadeiras do tipo semi-leito, sendo duas
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
