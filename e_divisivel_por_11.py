def e_divisivel_por_11(numero):
    numero = abs(numero)
    numero_para_string = str(numero)

    if len(numero_para_string) == 2 and numero_para_string[0] == numero_para_string[1]:
        return True

    if int(numero) >= 100 and int(numero) <= 200:
        primeiro_digito = int(numero_para_string[0])
        segundo_digito = int(numero_para_string[1])
        terceiro_digito = int(numero_para_string[2])

        return primeiro_digito + terceiro_digito == segundo_digito

    if int(numero) > 200:
        soma = 0
        sinal = '+'

        for n in numero_para_string:
            if sinal == '+':
                soma += int(n)
                sinal = '-'
            else:
                soma -= int(n)
                sinal = '+'

        return soma == 0 or e_divisivel_por_11(soma)
    
    return False