avistamentos = ["Colossal", "Anormal", "Pequeno", "Anormal", "Anormal", "Pequeno"]
relatorio = {}

# Para cada titã na lista de avistamentos...
for tita in avistamentos:
    
    # Se o titã JÁ ESTÁ no nosso dicionário de relatório...
    if tita in relatorio:
        # Pega o valor atual dele e SOMA MAIS UM!
        relatorio[tita] += 1
        
    # Se for a PRIMEIRA VEZ que vemos esse titã...
    else:
        # Cria a gaveta dele no dicionário valendo UM!
        relatorio[tita] = 1

print(relatorio)