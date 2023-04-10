x_exato = 0.5672
x_aproximado = 0.55

erro_absoluto = abs(x_exato - x_aproximado)
erro_relativo = abs(x_exato - x_aproximado) / abs(x_exato)

print(f"Erro absoluto: {erro_absoluto:.4f}")
print(f"Erro relativo: {erro_relativo:.4f}")
