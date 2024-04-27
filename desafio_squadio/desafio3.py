capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril

resultado = capacidade_atual + (capacidade_atual * (aumento_percentual / 100))

# TODO: Imprima a nova capacidade
print("Dado de entrada:"
      f"\n{capacidade_atual} {aumento_percentual}"
      "\nSaída esperada:"
      f"\n{resultado}")
