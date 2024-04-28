import oracledb
try:
 conexao = oracledb.connect(
 user="system",
 password="capo1950",
 dsn="localhost/XEPDB1")
except Exception as erro:
 print ('Erro em conexão', erro)
else:
 print ("Conectado", conexao.version)
cursor=conexao.cursor()

#definição das listas
estoque=[]
id_prod=[]
nome_prod=[]
desc_prod=[]
custo_prod=[]
custo_fixo=[]
comissao_vendas=[]
impostos=[]
margem_lucro=[]

cursor.execute("select id_prod from estoque")
id_prod = [row[0] for row in cursor.fetchall()]

cursor.execute("select nome_prod from estoque")
nome_prod = [row[0] for row in cursor.fetchall()]

cursor.execute("select desc_prod from estoque")
desc_prod = [row[0] for row in cursor.fetchall()]

cursor.execute("select custo_prod from estoque")
custo_prod = [row[0] for row in cursor.fetchall()]

cursor.execute("select custo_fixo from estoque")
custo_fixo = [row[0] for row in cursor.fetchall()]

cursor.execute("select comissao_vendas from estoque")
comissao_vendas = [row[0] for row in cursor.fetchall()]

cursor.execute("select impostos from estoque")
impostos = [row[0] for row in cursor.fetchall()]

cursor.execute("select margem_lucro from estoque")
margem_lucro = [row[0] for row in cursor.fetchall()]

estoque.append(id_prod)
estoque.append(nome_prod)
estoque.append(desc_prod)
estoque.append(custo_prod)
estoque.append(custo_fixo)
estoque.append(comissao_vendas)
estoque.append(impostos)
estoque.append(margem_lucro)

cursor.close
conexao.close

print(estoque)
#FAZER ATÉ ADICIONAR OS 6 PRODUTOS
#Calculo da Preço Venda

PV=[]

CP1=custo_prod[0]
CF1=custo_fixo[0]
CV1=comissao_vendas[0]
IMP1=impostos[0]
ML1=margem_lucro[0]

PV.append(CP1/(1-((CF1+CV1+IMP1+ML1)/(100))))

CP2=custo_prod[1]
CF2=custo_fixo[1]
CV2=comissao_vendas[1]
IMP2=impostos[1]
ML2=margem_lucro[1]

PV.append(CP2/(1-((CF2+CV2+IMP2+ML2)/(100))))

CP3=custo_prod[2]
CF3=custo_fixo[2]
CV3=comissao_vendas[2]
IMP3=impostos[2]
ML3=margem_lucro[2]

PV.append(CP3/(1-((CF3+CV3+IMP3+ML3)/(100))))

CP4=custo_prod[3]
CF4=custo_fixo[3]
CV4=comissao_vendas[3]
IMP4=impostos[3]
ML4=margem_lucro[3]

PV.append(CP4/(1-((CF4+CV4+IMP4+ML4)/(100))))

CP5=custo_prod[4]
CF5=custo_fixo[4]
CV5=comissao_vendas[4]
IMP5=impostos[4]
ML5=margem_lucro[4]

PV.append(CP5/(1-((CF5+CV5+IMP5+ML5)/(100))))

CP6=custo_prod[5]
CF6=custo_fixo[5]
CV6=comissao_vendas[5]
IMP6=impostos[5]
ML6=margem_lucro[5]

PV.append(CP6/(1-((CF6+CV6+IMP6+ML6)/(100))))

#Calculo da Renda Bruta

RB1=(PV[0]-CP1)
RB2=(PV[1]-CP2)
RB3=(PV[2]-CP3)
RB4=(PV[3]-CP4)
RB5=(PV[4]-CP5)
RB6=(PV[5]-CP6)

#Calculo Outros Custos

OC1=(PV[0]*(CF1/100)+PV[0]*(CV1/100))+(PV[0]*(IMP1/100))
OC2=(PV[1]*(CF2/100))+(PV[1]*(CV2/100))+(PV[1]*(IMP2/100))
OC3=(PV[2]*(CF3/100))+(PV[2]*(CV3/100))+(PV[2]*(IMP3/100))
OC4=(PV[3]*(CF4/100))+(PV[3]*(CV4/100))+(PV[3]*(IMP4/100))
OC5=(PV[4]*(CF5/100))+(PV[4]*(CV5/100))+(PV[4]*(IMP5/100))
OC6=(PV[5]*(CF6/100))+(PV[5]*(CV6/100))+(PV[5]*(IMP6/100))

#Formula % da Renda Bruta(porcenRB) e Custo de Pordutos

porcenRB1=((RB1*100)/PV[0])
porcenRB2=((RB2*100)/PV[1])
porcenRB3=((RB3*100)/PV[2])
porcenRB4=((RB4*100)/PV[3])
porcenRB5=((RB5*100)/PV[4])
porcenRB6=((RB6*100)/PV[5])

porcenCP1 = (100 * CP1/PV[0])
porcenCP2 = (100 * CP2/PV[1])
porcenCP3 = (100 * CP3/PV[2])
porcenCP4 = (100 * CP4/PV[3])
porcenCP5 = (100 * CP5/PV[4])
porcenCP6 = (100 * CP6/PV[5])

#Valores Brutos de CF, CV, IMP e ML

bCF1 = ((CF1 * PV[0])/100)
bCF2 = ((CF2 * PV[1])/100)
bCF3 = ((CF3 * PV[2])/100)
bCF4 = ((CF4 * PV[3])/100)
bCF5 = ((CF5 * PV[4])/100)
bCF6 = ((CF6 * PV[5])/100)

bCV1 = ((CV1 * PV[0])/100)
bCV2 = ((CV2 * PV[1])/100)
bCV3 = ((CV3 * PV[2])/100)
bCV4 = ((CV4 * PV[3])/100)
bCV5 = ((CV5 * PV[4])/100)
bCV6 = ((CV6 * PV[5])/100)

bIMP1 = ((IMP1 * PV[0])/100)
bIMP2 = ((IMP2 * PV[1])/100)
bIMP3 = ((IMP3 * PV[2])/100)
bIMP4 = ((IMP4 * PV[3])/100)
bIMP5 = ((IMP5 * PV[4])/100)
bIMP6 = ((IMP6 * PV[5])/100)

bML1 = ((ML1 * PV[0])/100)
bML2 = ((ML2 * PV[1])/100)
bML3 = ((ML3 * PV[2])/100)
bML4 = ((ML4 * PV[3])/100)
bML5 = ((ML5 * PV[4])/100)
bML6 = ((ML6 * PV[5])/100)


#Saída

#p1
print (f"Produto:{nome_prod[0]}   Especifcacão:{desc_prod[0]}")
print (" ")
print (f"Descriçao:                            Valor:   %")
print (f"A. Preço de Venda                  =  R${PV[0]}   | 100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP1}   |  {porcenCP1}%") 
print (f"C. Receita Bruta                   =  R${RB1}   |  {porcenRB1}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF1}  |  {CF1}%")
print (f"E. Comissão de Vendas              =  R${bCV1}   |   {CV1}%")
print (f"F. Impostos                        =  R${bIMP1}    |  {IMP1}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC1}   |  {IMP1+CV1+CF1}%")
print (f"H. Rentabilidade (C-G)             =  R${bML1}   |  {ML1}%")

if ML1 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML1 > 10 and ML1 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML1 > 0 and ML1 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML1 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML1 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p2
print (f"Produto:{nome_prod[1]}   Especifcacão:{desc_prod[1]}")
print (" ")
print (f"Descriçao:                            Valor:   %")
print (f"A. Preço de Venda                  =  R${PV[1]}   | 100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP2}   |  {porcenCP2}%") 
print (f"C. Receita Bruta                   =  R${RB2}   |  {porcenRB2}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF2}  |  {CF2}%")
print (f"E. Comissão de Vendas              =  R${bCV2}   |   {CV2}%")
print (f"F. Impostos                        =  R${bIMP2}    |  {IMP2}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC2}   |  {IMP2+CV2+CF2}%")
print (f"H. Rentabilidade (C-G)             =  R${bML2}   |  {ML2}%")

if ML2 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML2 > 10 and ML2 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML2 > 0 and ML2 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML2 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML2 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p3
print (f"Produto:{nome_prod[2]}   Especifcacão:{desc_prod[2]}")
print (" ")
print (f"Descriçao:                            Valor:   %")
print (f"A. Preço de Venda                  =  R${PV[2]}   | 100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP3}   |  {porcenCP3}%") 
print (f"C. Receita Bruta                   =  R${RB3}   |  {porcenRB3}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF3}  |  {CF3}%")
print (f"E. Comissão de Vendas              =  R${bCV3}   |   {CV3}%")
print (f"F. Impostos                        =  R${bIMP3}    |  {IMP3}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC3}   |  {IMP3+CV3+CF3}%")
print (f"H. Rentabilidade (C-G)             =  R${bML3}   |  {ML3}%")

if ML3 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML3 > 10 and ML3 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML3 > 0 and ML3 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML3 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML3 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p4
print (f"Produto:{nome_prod[3]}   Especifcacão:{desc_prod[3]}")
print (" ")
print (f"Descriçao:                            Valor:   %")
print (f"A. Preço de Venda                  =  R${PV[3]}   | 100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP4}   |  {porcenCP4}%") 
print (f"C. Receita Bruta                   =  R${RB4}   |  {porcenRB4}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF4}  |  {CF4}%")
print (f"E. Comissão de Vendas              =  R${bCV4}   |   {CV4}%")
print (f"F. Impostos                        =  R${bIMP4}    |  {IMP4}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC4}   |  {IMP4+CV4+CF4}%")
print (f"H. Rentabilidade (C-G)             =  R${bML4}   |  {ML4}%")

if ML4 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML4 > 10 and ML4 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML4 > 0 and ML4 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML4 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML4 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p5
print (f"Produto:{nome_prod[4]}   Especifcacão:{desc_prod[4]}")
print (" ")
print (f"Descriçao:                            Valor:   %")
print (f"A. Preço de Venda                  =  R${PV[4]}   | 100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP5}   |  {porcenCP5}%") 
print (f"C. Receita Bruta                   =  R${RB5}   |  {porcenRB5}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF5}  |  {CF5}%")
print (f"E. Comissão de Vendas              =  R${bCV5}   |   {CV5}%")
print (f"F. Impostos                        =  R${bIMP5}    |  {IMP5}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC5}   |  {IMP5+CV5+CF5}%")
print (f"H. Rentabilidade (C-G)             =  R${bML5}   |  {ML5}%")

if ML5 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML5 > 10 and ML5 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML5 > 0 and ML5 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML5 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML5 < 0:
    print("Este Produto Gera Prejuízo.")

print (" ")
print (" ")

#p6
print (f"Produto:{nome_prod[5]}   Especifcacão:{desc_prod[5]}")
print (" ")
print (f"Descriçao:                            Valor:   %")
print (f"A. Preço de Venda                  =  R${PV[5]}   | 100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP6}   |  {porcenCP6}%") 
print (f"C. Receita Bruta                   =  R${RB6}   |  {porcenRB6}%")
print (f"D. Custo Fixo/Administrativo       =  R${bCF6}  |  {CF6}%")
print (f"E. Comissão de Vendas              =  R${bCV6}   |   {CV6}%")
print (f"F. Impostos                        =  R${bIMP6}    |  {IMP6}%")
print (f"G. Outros Custos (D+E+F)           =  R${OC6}   |  {IMP6+CV6+CF6}%")
print (f"H. Rentabilidade (C-G)             =  R${bML6}   |  {ML6}%")

if ML6 > 20:
    print("O Lucro Deste Produto é Alto.")
elif ML6 > 10 and ML6 <= 20:
    print("O Lucro Deste Produto é Médio.")
elif ML6 > 0 and ML6 <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif ML6 == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif ML6 < 0:
    print("Este Produto Gera Prejuízo.")
