CodP = int (input("Digite o Código do Produto:"))
NomP = (input("Digite o Nome do Produto:"))
Desc = (input("Dê uma Descrição do Produto:"))
CP = float (input("Digite o Valor do Custo do Produto:"))
CFp = float (input("Digite o Valor do Custo Fixo/Administrativo do Produto(%):"))
CVp = float (input("Defina o Valor da Comissão de Vendas(%):"))
IVp = float (input("Digite o Valor dos Impostos(%):"))
MLp = float (input("Digite a Rentabilidade Desejada(%):"))

PV = (CP/(1-((CFp+CVp+IVp+MLp)/100)))

RB = (PV-CP)

CPp = (100 * CP/PV)
RBp = (100 * RB/PV)
CF = ((CFp * PV)/100)
CV = ((CVp * PV)/100)
IV = ((IVp * PV)/100)
ML = ((MLp * PV)/100)

print (f"Descriçao:                            Valor:   %")
print (f"A. Preço de Venda                  =  R${PV}   | 100.0%")
print (f"B. Custo de Aquisição (Fornecedor) =  R${CP}   |  {CPp}%") 
print (f"C. Receita Bruta                   =  R${RB}   |  {RBp}%")
print (f"D. Custo Fixo/Administrativo       =  R${CF}  |  {CFp}%")
print (f"E. Comissão de Vendas              =  R${CV}   |   {CVp}%")
print (f"F. Impostos                        =  R${IV}    |  {IVp}%")
print (f"G. Outros Custos (D+E+F)           =  R${CF+CV+IV}   |  {IVp+CVp+CFp}%")
print (f"H. Rentabilidade (C-G)             =  R${ML}   |  {(RBp-(IVp+CVp+CFp))}%")

if MLp > 20:
    print("O Lucro Deste Produto é Alto.")
elif MLp > 10 and MLp <= 20:
    print("O Lucro Deste Produto é Médio.")
elif MLp > 0 and MLp <= 10:
    print("O Lucro Deste Produto é Baixo.")
elif MLp == 0:
    print("Este Produto Não Gera Lucro ou Pejuízo (Equilíbrio).")
elif MLp < 0:
    print("Este Produto Gera Prejuízo.")