# Assistente de Aprovação: 
while True: 
    print("\nBem-vindo ao Assistente de Aprovação\n") 
 
    # Entrada de dados: 
    while True: 
        try: 
            n1 = float(input("Digite a nota N1 (0.00 a 10.00): ")) 
            if 0 <= n1 <=10: 
                break 
            print("Valor inválido! A nota deve ser entre 0.00 e 10.00.") 
        except ValueError: 
            print("Entrada inválida. Por favor, digite números válidos.") 
    while True: 
        try: 
            n2 = float(input("Digite a nota N2 (0.00 a 10.00): ")) 
            if 0 <= n2 <=10: 
                break 
            print("Valor inválido! A nota deve ser entre 0.00 e 10.00.") 
        except ValueError: 
            print("Entrada inválida. Por favor, digite números válidos.") 
    while True: 
        try: 
            frequencia = float(input("Digite a frequência (0 a 100%): ")) 
            if 0 <= frequencia <= 100: 
                break 
 
            print("Valor inválido! A frequência deve ser entre 0 e 100.") 
        except ValueError: 
            print("Entrada inválida. Por favor, digite números válidos.") 
 
    # Cálculo da média: 
    media = (n1 + n2) / 2 
    print(f"\nMédia final: {media:.2f}") 
    # Apresentação da frequência: 
    print(f"Frequência: {frequencia:,.2f}%\n") 
 
    # Verificação da situação final do aluno: 
    if media >= 7 and frequencia >= 75: 
        print("Situação: Aprovado!") 
    elif 5 <= media < 7 and frequencia >= 75: 
        print("Situação: Recuperação!") 
    elif media < 5 or frequencia < 75: # Poderia ser apenas "else", mas deixei a condição para maior clareza. 
        print("Situação: Reprovado!") 
 
    # Pergunta para o usuário se deseja realizar outra consulta: 
    repetir = input("\nDeseja realizar outra consulta? (s/n): \n") 
    if repetir.lower() != 's': 
        print("\nObrigado por usar o Assistente de Aprovação! Até a próxima!\n") 
        break 