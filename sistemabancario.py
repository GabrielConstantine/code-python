#Criar um sistema bancario  com as operações: sacar, depositar e visualizar extrato bancario.

def main():
    saldo = 0.0
    qtd_saque = 0
    qtd_deposito = 0
    
    while True:
        
        optionsMenu = input("""
                Bem-vindo ao banco Constantine.
                Digite a operação que deseja realizar:
                
                Para sacar digite s
                Para depositar digite d
                Para visualizar o extrato bancário digite e
                Para sair digite q
                
                Opção: """)
        
        if optionsMenu == 's':
            
            if qtd_saque >= 3:
                print("\nSaque inválido.")
                
            else:
                valor_saque = float(input("\nDigite o valor que deseja sacar: "))
                
                if valor_saque > 500.00:
                    print("\nValor de saque acima do limite permitido.")
                    
                else:
                    saldo -= valor_saque
                    qtd_saque += 1
                    print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
        
        elif optionsMenu == 'd':
            
            if qtd_deposito >= 3:
                print("\Deposito inválido.")
            
            if (qtd_deposito < 3):
                valor_deposito = float(input("\nDigite o valor que deseja depositar: "))

                if valor_deposito > 500.00:
                    print("Valor de depósito acima do limite permitido.")
                
                else:
                    saldo += valor_deposito
                    qtd_deposito += 1
                    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
        
        elif optionsMenu == 'e':
            print(f"""
                  ***********************************
                    Seu saldo atual é de R${saldo:.2f}.
                     Quantidade de saque feitos: {qtd_saque:}
                   Quantidade de depositos feito: {qtd_deposito:}
                  ***********************************""")
        
        elif optionsMenu == 'q':
            print("\nObrigado por utilizar o banco Constantine.")
            break
        
        else:
            print("\nOpção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()
