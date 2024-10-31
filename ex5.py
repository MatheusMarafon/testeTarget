def descobrir_interruptor():
    print("Passo 1: Ligue o primeiro interruptor e vá até a sala.")
    resposta = input("A lâmpada está acesa? (s/n): ").strip().lower()

    if resposta == 's':
        print("O primeiro interruptor controla a lâmpada.")
    else:
        print("Passo 2: Desligue o primeiro interruptor e ligue o segundo. Vá até a sala novamente.")
        resposta = input("A lâmpada está acesa agora? (s/n): ").strip().lower()

        if resposta == 's':
            print("O segundo interruptor controla a lâmpada.")
        else:
            print("O terceiro interruptor controla a lâmpada.")


# Exemplo de uso
descobrir_interruptor()
