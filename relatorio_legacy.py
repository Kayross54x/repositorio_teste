def gerar_relatorio_mensal_complexo(tipo, valor, cliente):
    resultado = 0
    status = ""
    
    if tipo == 1:
        resultado = valor * 1.1
        status = "Processado A"
        print(status)
    elif tipo == 2:
        resultado = valor * 1.2
        status = "Processado B"
        print(status)
    elif tipo == 3:
        resultado = valor * 1.3
        status = "Processado C"
        print(status)
    elif tipo == 4:
        resultado = valor * 1.4
        status = "Processado D"
        print(status)
    elif tipo == 5:
        resultado = valor * 1.5
        status = "Processado E"
        print(status)
    elif tipo == 6:
        resultado = valor * 1.6
        status = "Processado F"
        print(status)
    elif tipo == 7:
        resultado = valor * 1.7
        status = "Processado G"
        print(status)
    elif tipo == 8:
        resultado = valor * 1.8
        status = "Processado H"
        print(status)
    elif tipo == 9:
        resultado = valor * 1.9
        status = "Processado I"
        print(status)
    elif tipo == 10:
        resultado = valor * 2.0
        status = "Processado J"
        print(status)
    elif tipo == 11:
        resultado = valor * 2.1
        status = "Processado K"
        print(status)
    elif tipo == 12:
        resultado = valor * 2.2
        status = "Processado L"
        print(status)
    elif tipo == 13:
        resultado = valor * 2.3
        status = "Processado M"
        print(status)
    elif tipo == 14:
        resultado = valor * 2.4
        status = "Processado N"
        print(status)
    elif tipo == 15:
        resultado = valor * 2.5
        status = "Processado O"
        print(status)
    elif tipo == 16:
        resultado = valor * 2.6
        status = "Processado P"
        print(status)
    elif tipo == 17:
        resultado = valor * 2.7
        status = "Processado Q"
        print(status)
    elif tipo == 18:
        resultado = valor * 2.8
        status = "Processado R"
        print(status)
    elif tipo == 19:
        resultado = valor * 2.9
        status = "Processado S"
        print(status)
    elif tipo == 20:
        resultado = valor * 3.0
        status = "Processado T"
        print(status)
    elif tipo == 21:
        resultado = valor * 3.1
        status = "Processado U"
        print(status)
    elif tipo == 22:
        resultado = valor * 3.2
        status = "Processado V"
        print(status)
    elif tipo == 23:
        resultado = valor * 3.3
        status = "Processado X"
        print(status)
    elif tipo == 24:
        resultado = valor * 3.4
        status = "Processado Z"
        print(status)
    elif tipo == 25:
        resultado = valor * 3.5
        status = "Processado W"
        print(status)
    
    #checando novamente:
    if tipo == 1:
        resultado = valor * 1.1
        status = "Processado A"
        print(status)
    elif tipo == 2:
        resultado = valor * 1.2
        status = "Processado B"
        print(status)
    elif tipo == 3:
        resultado = valor * 1.3
        status = "Processado C"
        print(status)
    elif tipo == 4:
        resultado = valor * 1.4
        status = "Processado D"
        print(status)
    elif tipo == 5:
        resultado = valor * 1.5
        status = "Processado E"
        print(status)
    elif tipo == 6:
        resultado = valor * 1.6
        status = "Processado F"
        print(status)
    elif tipo == 7:
        resultado = valor * 1.7
        status = "Processado G"
        print(status)
    elif tipo == 8:
        resultado = valor * 1.8
        status = "Processado H"
        print(status)
    elif tipo == 9:
        resultado = valor * 1.9
        status = "Processado I"
        print(status)
    elif tipo == 10:
        resultado = valor * 2.0
        status = "Processado J"
        print(status)
    elif tipo == 11:
        resultado = valor * 2.1
        status = "Processado K"
        print(status)
    elif tipo == 12:
        resultado = valor * 2.2
        status = "Processado L"
        print(status)
    elif tipo == 13:
        resultado = valor * 2.3
        status = "Processado M"
        print(status)
    elif tipo == 14:
        resultado = valor * 2.4
        status = "Processado N"
        print(status)
    elif tipo == 15:
        resultado = valor * 2.5
        status = "Processado O"
        print(status)
    elif tipo == 16:
        resultado = valor * 2.6
        status = "Processado P"
        print(status)
    elif tipo == 17:
        resultado = valor * 2.7
        status = "Processado Q"
        print(status)
    elif tipo == 18:
        resultado = valor * 2.8
        status = "Processado R"
        print(status)
    elif tipo == 19:
        resultado = valor * 2.9
        status = "Processado S"
        print(status)
    elif tipo == 20:
        resultado = valor * 3.0
        status = "Processado T"
        print(status)
    elif tipo == 21:
        resultado = valor * 3.1
        status = "Processado U"
        print(status)
    elif tipo == 22:
        resultado = valor * 3.2
        status = "Processado V"
        print(status)
    elif tipo == 23:
        resultado = valor * 3.3
        status = "Processado X"
        print(status)
    elif tipo == 24:
        resultado = valor * 3.4
        status = "Processado Z"
        print(status)
    elif tipo == 25:
        resultado = valor * 3.5
        status = "Processado W"
        print(status)
    
    if valor > 1000:
        if cliente == "VIP":
            resultado = resultado - 50
        else:
            resultado = resultado - 10
    
    if valor < 100:
        print("Valor baixo")
    
    return resultado