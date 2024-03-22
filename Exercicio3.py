def construir_piramide(base):
    niveis = []
    niveis.append(base)

    while len(base) > 1:
        novo_nivel = []
        for i in range(len(base) - 1):
            novo_nivel.append(base[i] + base[i + 1])
        niveis.append(novo_nivel)
        base = novo_nivel

    return niveis

def imprimir_piramide(piramide):
    for nivel in piramide:
        print(" ".join(map(str, nivel)))

def main():
    try:
        entrada = input("Digite os valores da base da pirâmide separados por espaço: ")
        valores_base = list(map(int, entrada.split()))
        piramide = construir_piramide(valores_base)
        imprimir_piramide(piramide)
    except ValueError:
        print("Por favor, insira valores inteiros separados por espaço.")

if __name__ == "__main__":
    main()
