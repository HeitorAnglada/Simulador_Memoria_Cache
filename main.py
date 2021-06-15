import math
import random
import funcoes as f

f.mensagem_de_entrada()

entrada = input('->')
print(entrada)

posicao_virgulai = entrada.find(',')
numero_linhas = int(entrada[:posicao_virgulai])
print(numero_linhas)

posicao_virgulaf = entrada.find(',', posicao_virgulai + 1)
tamanho_palavra = int(entrada[posicao_virgulai + 1: posicao_virgulaf])
print(tamanho_palavra)

tipo_de_mapeamento = entrada[posicao_virgulaf + 1]
print(tipo_de_mapeamento)

politica_de_escrita = entrada[posicao_virgulaf + 2]
print(politica_de_escrita)

algoritimo_de_substituicao = entrada[posicao_virgulaf + 3]
print(algoritimo_de_substituicao)

posicao_menos = entrada.find('-')
arquivoi = entrada[posicao_menos + 1:]
print(arquivoi)

arquivo = open(arquivoi, 'r')

bit_linha = int(math.log2(numero_linhas))

cache = []
while len(cache) < numero_linhas:
    cache.append('-1')

hit = 0
miss = 0
acesso_memoria = 0
b = 0
freq = []
while len(freq) < numero_linhas:
    freq.append(1)
if tipo_de_mapeamento == 'c':
    print('Numero de Linhas por conjunto:')
    X = int(input())
    k = int(numero_linhas / X)
print('AGUARDE')

for palavra in arquivo:

    if palavra[0] == ' ':
        instrucao = palavra[1]

    else:
        instrucao = palavra[0]

    endereco = palavra[3:palavra.find(',')]


    if len(endereco) < 8:
        t = 8 - len(endereco)
        endereco = t * '0' + endereco

    elif len(endereco) > 8:
        while len(endereco) > 8: endereco = endereco[1:]

    convert = f.any2any(endereco, 16, 2)
    t = len(32 * '0') - len(convert)
    enderecamento = '0' * t + convert

    if tipo_de_mapeamento == 'd':

        linha_cache = enderecamento[32 - tamanho_palavra - bit_linha:32 - tamanho_palavra]

        tag = enderecamento[0:32 - tamanho_palavra - bit_linha]
        tagHex = f.any2any(tag, 2, 16)

        linha_cache_decimal = int(f.any2dec(linha_cache, 2))



        if instrucao == 'L' or 'I':

            if cache[linha_cache_decimal] == tagHex:
                hit += 1

            else:

                miss += 1
                acesso_memoria += 1
                #  adiciona o endereço na posição r
                cache[linha_cache_decimal] = tagHex

        elif instrucao == 'S':

            if politica_de_escrita == 't':

                if cache[linha_cache_decimal] == tagHex:
                    hit += 1
                    acesso_memoria = acesso_memoria + 1

                else:
                    miss += 1
                    acesso_memoria = acesso_memoria + 1
                    cache[linha_cache_decimal] = tagHex

        elif instrucao == 'M':

            if cache[linha_cache_decimal] == tagHex:
                hit += 1

            else:
                miss += 1
                acesso_memoria += 1
                cache[linha_cache_decimal] = tagHex

            hit += 1
            acesso_memoria += 1

    if tipo_de_mapeamento == 'a':

        tag = enderecamento[0:32 - tamanho_palavra]
        tagHex = f.any2any(tag, 2, 16)
        a = random.randrange(0, numero_linhas - 1)
        i = 0

        if instrucao == 'L' or 'I':

            if '-1' in cache:

                for palavra in cache:

                    if cache[i] == '-1':

                        miss = miss + 1
                        cache[i] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        break

                    elif cache[i] != tagHex and cache[i] != '-1':
                        i = i + 1

                    elif cache[i] == tagHex and cache[i] != '-1':

                        hit = hit + 1
                        freq[i] += 1
                        break

            else:

                if algoritimo_de_substituicao == 'r':

                    for palavra in cache:

                        if tagHex in cache:

                            hit = hit + 1
                            break

                        else:

                            miss = miss + 1
                            cache[a] = tagHex
                            acesso_memoria = acesso_memoria + 1
                            break

                elif algoritimo_de_substituicao == 'p':

                    for palavra in cache:

                        if tagHex in cache:
                            hit = hit + 1

                            break

                        else:

                            miss = miss + 1
                            cache[b] = tagHex
                            acesso_memoria = acesso_memoria + 1
                            b += 1
                            break

                elif algoritimo_de_substituicao == 'l':

                    for palavra in cache:

                        if tagHex in cache:

                            hit = hit + 1
                            H = cache.index(tagHex)
                            freq[H] += 1

                            break

                        else:

                            p = 0
                            c = 0
                            min = freq[c]

                            while c < numero_linhas:

                                if freq[c] < min:
                                    min = freq[c]
                                    p = c

                                c += 1

                            miss += 1
                            acesso_memoria += 1
                            cache[p] = tagHex

        elif instrucao == 'S':

            if '-1' in cache:

                for palavra in cache:

                    if cache[i] == '-1':
                        miss = miss + 1
                        cache[i] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        break

                    elif cache[i] != tagHex and cache[i] != '-1':
                        i = i + 1

                    elif cache[i] == tagHex and cache[i] != '-1':

                        hit = hit + 1
                        acesso_memoria += 1
                        freq[i] += 1
                        break

            else:

                if algoritimo_de_substituicao == 'r':

                    for palavra in cache:

                        if tagHex in cache:

                            hit = hit + 1
                            acesso_memoria += 1
                            break

                        else:

                            miss = miss + 1
                            cache[a] = tagHex
                            acesso_memoria = acesso_memoria + 1
                            break

                elif algoritimo_de_substituicao == 'p':

                    for palavra in cache:

                        if tagHex in cache:
                            hit = hit + 1

                            break
                        else:

                            miss = miss + 1
                            cache[b] = tagHex
                            acesso_memoria = acesso_memoria + 1
                            b += 1
                            break

                elif algoritimo_de_substituicao == 'l':

                    for palavra in cache:

                        if tagHex in cache:

                            hit = hit + 1
                            H = cache.index(tagHex)
                            freq[H] += 1

                            break

                        else:

                            p = 0
                            c = 0
                            min = freq[c]

                            while c < numero_linhas:

                                if freq[c] < min:
                                    min = freq[c]
                                    p = c

                                c += 1

                            miss += 1
                            acesso_memoria += 1
                            cache[p] = tagHex

        elif instrucao == 'M':

            if '-1' in cache:

                for palavra in cache:

                    if cache[i] == '-1':

                        miss = miss + 1
                        cache[i] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        break

                    elif cache[i] != tagHex and cache[i] != '-1':
                        i = i + 1

                    elif cache[i] == tagHex and cache[i] != '-1':

                        hit = hit + 1
                        freq[i] += 1

                        break

            else:

                if algoritimo_de_substituicao == 'r':

                    for palavra in cache:

                        if tagHex in cache:
                            hit = hit + 1

                            break
                        else:

                            miss = miss + 1
                            cache[a] = tagHex
                            acesso_memoria = acesso_memoria + 1
                            break

                elif algoritimo_de_substituicao == 'p':

                    for palavra in cache:

                        if tagHex in cache:
                            hit = hit + 1

                            break
                        else:

                            miss = miss + 1
                            cache[b] = tagHex
                            acesso_memoria = acesso_memoria + 1
                            b += 1
                            break

                elif algoritimo_de_substituicao == 'l':

                    for palavra in cache:

                        if tagHex in cache:

                            hit = hit + 1
                            H = cache.index(tagHex)
                            freq[H] += 1

                            break
                        else:

                            p = 0
                            c = 0
                            min = freq[c]

                            while c < numero_linhas:

                                if freq[c] < min:
                                    min = freq[c]
                                    p = c

                                c += 1

                            miss += 1
                            acesso_memoria += 1
                            cache[p] = tagHex

            acesso_memoria += 1
            hit += 1

        if b == numero_linhas:
            b = 0

    elif tipo_de_mapeamento == 'c':

        bit_conjunto = int(math.log2(k))

        conjunto = enderecamento[32 - tamanho_palavra - bit_conjunto:32 - tamanho_palavra]
        conjunto_decimal = int(f.any2dec(conjunto, 2))

        tag = enderecamento[0:32 - tamanho_palavra - bit_conjunto]
        tagHex = f.any2any(tag, 2, 16)
        a = random.randrange(0 + (X * conjunto_decimal), (X) + (X * conjunto_decimal))
        c  = []
        while len(c) < k:
            c.append(-1)

        min = []
        while len(min) < k:
            min.append(freq[X * conjunto_decimal])
        j = 0
        Z = 0


        if instrucao == ('L' or 'I'):

            while (Z <= X):

                if Z < X:

                    if cache[j + (X * conjunto_decimal)] == '-1':

                        cache[j + (X * conjunto_decimal)] = tagHex
                        miss += 1
                        acesso_memoria += 1
                        break

                    elif cache[j + (X * conjunto_decimal)] == tagHex:

                        hit += 1
                        freq[j + (X * conjunto_decimal)] += 1

                        if freq[j + (X * conjunto_decimal)] < min[conjunto_decimal]:
                            min[conjunto_decimal] = freq[j + (X * conjunto_decimal)]
                            c[conjunto_decimal] = j + (X * conjunto_decimal)

                        break
                    elif cache[j + (X * conjunto_decimal)] != '-1' and tagHex:
                        j += 1

                    Z += 1

                elif Z == X:

                    if algoritimo_de_substituicao == 'r':
                        miss += 1
                        cache[a] = tagHex
                        acesso_memoria += 1
                        Z += 1

                    elif algoritimo_de_substituicao == 'p':
                        miss = miss + 1
                        cache[b + (X * conjunto_decimal)] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        b += 1
                        Z += 1

                    elif algoritimo_de_substituicao == 'l':
                        miss = miss + 1
                        cache[c[conjunto_decimal]] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        Z += 1

        if instrucao == 'S':

            while (Z <= X):

                if Z < X:

                    if cache[j + (X * conjunto_decimal)] == '-1':

                        cache[j + (X * conjunto_decimal)] = tagHex
                        miss += 1
                        acesso_memoria += 1
                        break

                    elif cache[j + (X * conjunto_decimal)] == tagHex:

                        hit += 1
                        freq[j + (X * conjunto_decimal)] += 1
                        acesso_memoria += 1

                        if freq[j + (X * conjunto_decimal)] < min[conjunto_decimal]:
                            min[conjunto_decimal] = freq[j + (X * conjunto_decimal)]
                            c[conjunto_decimal] = j + (X * conjunto_decimal)

                        break
                    elif cache[j + (X * conjunto_decimal)] != '-1' and tagHex:
                        j += 1

                    Z += 1

                elif Z == X:

                    if algoritimo_de_substituicao == 'r':
                        miss += 1
                        cache[a] = tagHex
                        acesso_memoria += 1
                        Z += 1

                    elif algoritimo_de_substituicao == 'p':

                        miss = miss + 1
                        cache[b + (X * conjunto_decimal)] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        b += 1
                        Z += 1

                    elif algoritimo_de_substituicao == 'l':

                        miss = miss + 1
                        cache[c] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        Z += 1

        if instrucao == 'M':

            while (Z <= X):

                if Z < X:

                    if cache[j + (X * conjunto_decimal)] == '-1':

                        cache[j + (X * conjunto_decimal)] = tagHex
                        miss += 1
                        acesso_memoria += 1
                        break

                    elif cache[j + (X * conjunto_decimal)] == tagHex:

                        hit += 1
                        acesso_memoria += 1
                        freq[j + (X * conjunto_decimal)] += 1

                        if freq[j + (X * conjunto_decimal)] < min[conjunto_decimal]:
                            min[conjunto_decimal] = freq[j + (X * conjunto_decimal)]
                            c[conjunto_decimal] = j + (X * conjunto_decimal)

                        break

                    elif cache[j + (X * conjunto_decimal)] != '-1' and tagHex:
                        j += 1

                    Z += 1

                elif Z == X:

                    if algoritimo_de_substituicao == 'r':

                        miss += 1
                        cache[a] = tagHex
                        acesso_memoria += 1
                        Z += 1

                    elif algoritimo_de_substituicao == 'p':

                        miss = miss + 1
                        cache[b + (X * conjunto_decimal)] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        b += 1
                        Z += 1

                    elif algoritimo_de_substituicao == 'l':

                        miss = miss + 1
                        cache[c] = tagHex
                        acesso_memoria = acesso_memoria + 1
                        Z += 1

                hit += 1
                acesso_memoria += 1

        if b == X:
            b = 0

cont = 0
print(cache)
print('+-------+-------------------------------+')
print('| {: ^5} | {: ^29} |'.format('INDEX', 'TAG'))
print('+-------+-------------------------------+')

for palavra in cache:
    print('| {: ^5} | {: ^29} |'.format(cont, cache[cont]))
    cont = cont + 1

print('+-------+-------------------------------+')

print(f'MISS: {miss}')
print(f'HIT: {hit}')
print(f'ACESSOS A MEMORIA: {acesso_memoria}')

if tipo_de_mapeamento == 'd':
    print(f'MAPEAMENTO DIRETO')

elif tipo_de_mapeamento == 'a':
    print(f'MAPEAMENTO ASSOCIATIVO')

elif tipo_de_mapeamento == 'c':
    print(f'MAPEAMENTO ASSOCIATIVO POR CONJUNTOS')
    print(f'TAMANHO DO CONJUNTO = {X}')

if politica_de_escrita == 't':
    print(f'POLITICA DE ESCRITA WRITE THROUGH')

elif politica_de_escrita == 'b':
    print(f'POLITICA DE ESCRITA WRITE BACK')

if algoritimo_de_substituicao == 'l':
    print(f'SUBSTITUIÇAO LFU')

elif algoritimo_de_substituicao == 'r':
    print(f'SUBSTITUIÇAO ALEATORIA')

elif algoritimo_de_substituicao == 'p':
    print(f'SUBSTITUIÇAO DOS PRIMEIROS A ENTRAR')


if tipo_de_mapeamento is 'd':
    arquivo = 'tracos_mDireto_' + arquivoi[:-6] + '.txt'

elif tipo_de_mapeamento is 'a':

    if algoritimo_de_substituicao is 'r':
        arquivo = 'tracos_MapAssociativo_SubAleat_' + arquivoi[:-6] + '.txt'

    elif algoritimo_de_substituicao is 'p':
        arquivo = 'tracos_MapAssociativo_SubFIFO_' + arquivoi[:-6] + '.txt'

    elif algoritimo_de_substituicao is 'l':
        arquivo = 'tracos_MapAssociativo_SubLFU_' + arquivoi[:-6] + '.txt'

elif tipo_de_mapeamento is 'c':

    if algoritimo_de_substituicao is 'r':
        arquivo = 'tracos_MapConjunto_SubAleat_' + arquivoi[:-6] + '.txt'

    elif algoritimo_de_substituicao is 'p':
        arquivo = 'tracos_MapConjunto_SubFIFA_' + arquivoi[:-6] + '.txt'

    elif algoritimo_de_substituicao is 'l':
        arquivo = 'tracos_MapConjunto_SubLFU_' + arquivoi[:-6] + '.txt'

memoria = open(arquivo, 'w')

cont = 0
for palavra in cache:
    memoria.write(f'{cache[cont]}\n')
    cont = cont + 1

memoria.write(f'\nENTRADA: {entrada}\n')
memoria.write(f'MISS: {miss}\n')
memoria.write(f'HIT: {hit}\n')
memoria.write(f'ACESSOS A MEMORIA: {acesso_memoria}\n')

if tipo_de_mapeamento == 'd':
    memoria.write(f'MAPEAMENTO DIRETO\n')

elif tipo_de_mapeamento == 'a':
    memoria.write(f'MAPEAMENTO ASSOCIATIVO\n')

elif tipo_de_mapeamento == 'c':
    memoria.write(f'MAPEAMENTO ASSOCIATIVO POR CONJUNTOS\n')
    memoria.write(f'LINHAS POR CONJUNTO = {X}\n')

if politica_de_escrita == 't':
    memoria.write(f'POLITICA DE ESCRITA WRITE THROUGH\n')

elif politica_de_escrita == 'b':
    memoria.write(f'POLITICA DE ESCRITA WRITE BACK\n')

if algoritimo_de_substituicao == 'l':
    memoria.write(f'SUBSTITUIÇAO LFU\n')

elif algoritimo_de_substituicao == 'r':
    memoria.write(f'SUBSTITUIÇAO ALEATORIA\n')

elif algoritimo_de_substituicao == 'p':
    memoria.write(f'SUBSTITUIÇAO DOS PRIMEIROS A ENTRAR\n')
