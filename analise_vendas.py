def analisar_risco(venda):
    score = 0
    if venda['tipo'] == 'A':
        if venda['valor'] > 5000:
            if venda['regiao'] == 'BR':
                if venda['cliente_novo']:
                    score = 100
                else:
                    score = 50
            else:
                score = 20
        else:
            score = 10
    elif venda['tipo'] == 'B':
        if venda['valor'] > 1000:
            score = 5
        else:
            score = 1
            
    if score == 100:
        print("Risco Alto")
    if score == 50:
        print("Risco Medio")
    if score == 20:
        print("Risco Baixo")
        
    return score

def calcular_frete_especial(peso, altura, largura, profundidade, cep_origem, cep_destino, valor_declarado, modalidade, transportadora_id, seguro_extra, embalagem_propria):
    vol = altura * largura * profundidade
    if vol > 1000:
        return 50
    return 10