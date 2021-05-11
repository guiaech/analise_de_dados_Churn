#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

tabela_cliente = pd.read_csv(r"C:\Users\guilh\Downloads\telecom_users.csv")
#nomeie uma variável e solicitei ao pandas ler um arquivo csv
tabela_cliente = tabela_cliente.drop(["Unnamed: 0"], axis=1)
tabela_cliente = tabela_cliente.drop(["IDCliente"], axis=1)
tabela_cliente = tabela_cliente.drop(["Codigo"], axis = 1)
#aqui foi retirado da tabela os dados desnecessários 
display(tabela_cliente)
#para demosntrar a tabela


# In[18]:


tabela_cliente["TotalGasto"] = pd.to_numeric(tabela_cliente["TotalGasto"], errors = "coerce")
#Aqui transformamos o TotalGasto de object para numerico e acrescentamos errors = "coerce" para que o programa ignore algum que dê erro
tabela_cliente = tabela_cliente.dropna()
#Aqui removemos as linhas vazias caso queira exlcuir alguma coluna vazia deve se usar tabela_cliente.dropna(how='all', axis=1) 


print (tabela_cliente.info())
#comando faz a leitura das informações da tabela 


# In[26]:


display(tabela_cliente["Churn"].value_counts())
#Comando para ler os valores na tabela de Churn
display(tabela_cliente["Churn"].value_counts(normalize=True).map("{:.1%}".format))
#Comando para formartar a tabela em porcentagem (normaliza=True) e o map("{:.1%}".format) para formatar em casa decimal e porcentagem


# In[29]:


import plotly.express as px
#importação da biblioteca de gráficos 

for coluna in tabela_cliente:
    grafico = px.histogram(tabela_cliente , x = coluna , color="Churn")
    grafico.show()
#Aqui usei o comando de repetição para que fizesse todos graficos das colunas e colorisse os Churns que é relevante para analise dos dados



# Conclusão:
# 
# - Clientes que possuem dependentes tendem a não cancelar
# 
# - Clientes tendem a sair mais nos 5 primeiros meses
#     Assim podemos estar com clientes não qualificados ou não estamos suprindo as necessidades dos clientes
#     Após 8 meses na empresa o cliente tende a não cancelar
#     
# - Estamos com algum problema sério no nosso serviço de fibra pois temos um alto indice de cancelamento para usuarios desse serviço. Fazer uma analise deste serviço
# 
# - Clientes com maior número de serviços tendem a não cancelar.
#   Fazer promoções para compra de mais serviços
#   
# - Clientes com contratos mensais tendem a não ficar na empresa
#   Ter incentivos para se fazer contratos maiores.
#   
# - Clientes com pagamento de boleto eletronico tendem a não continuar na empresa
#   Criar descontos para formas de pagamento pelo cartão ou débito automático 
#   
# - Clientes com gastos menores mensal tendem a cancelar mais o contrato
#   Criando um laço com cliente com vários produtos o valor tende a subir e assim diminuindo a porcentagem de churn.
