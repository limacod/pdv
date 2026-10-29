bruto=0
totaldesconto=0
final=0

x=[]

while True:
    VC = float(input("Digite '0' para encerrar ou informe o total da compra: R$ "))
    
    if VC == 0:
        break
    
    if VC<0:
        print("O VALOR INFORMADO É INVALIDO! DIGITE NOVAMENTE")
        continue
    
    ID=int(input("informe a idade do cliente: "))
    
    VD=VC
    
    if ID>=65:
        VD=VD*0.80
   
    if VD>100:
        VF=VD*0.90
    
    else:
        VF=VD
    desconto=VC-VF
    
    x.append([VC,desconto,VF])
    
    print(f"Valor original: R$ {VC:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {VF:.2f}")
    
    bruto+=VC
    totaldesconto += desconto
    final+=VD


print("\n===== RESUMO DO DIA =====")
print(f"Quantidade de compras: {len(x)}")
print(f"Total bruto: R$ {bruto:.2f}")
print(f"Total de descontos: R$ {totaldesconto:.2f}")
print(f"Total final: R$ {final:.2f}")


        
    