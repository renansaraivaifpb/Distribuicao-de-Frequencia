# biblioteca para criar o arquivo csv
import csv
# biblioteca para capturar a funcao de raiz quadrada
import math
at = 0;
lista = []
with open("planilha.csv") as arquivo:
    conteudo = csv.reader(arquivo)
    for linha in conteudo:
        lista.append(linha)
print(lista)
lista_formatada = []
for linha in range(0, len(lista)):
    for coluna in range(0,8):
        formatado = float(lista[linha][coluna].replace(",", "."))
        lista_formatada.append(formatado)
maior_numero = 0.0
menor_numero = lista_formatada[0]
for indice in range(0, len(lista_formatada)):
    if(lista_formatada[indice]) > maior_numero:
        maior_numero = lista_formatada[indice]
    if(lista_formatada[indice]) < menor_numero:
        menor_numero = lista_formatada[indice]
at = maior_numero - menor_numero
k = math.floor(math.sqrt(len(lista_formatada)))
ac = round(at / k, 2)
print(f"maior numero: {maior_numero}")
print(f"menor numero: {menor_numero}")
print(f"at: {at}")
print(f"quantidade de dados: {len(lista_formatada)}")
print(f"k: {k}")
print(f"ac: {ac}")
intervalos = [menor_numero]
for i in range(0,k):
    intervalos.append(round(intervalos[i]+ac,2))
fa = []
fa2 = []
quantidade = 0
quantidade_intervalos = 0
intervalo_antecessor = 0
intervalo_sucessor = 1
while(intervalo_sucessor < len(intervalos)):
    for indice in range(0, len(lista_formatada)):
        if lista_formatada[indice] >= intervalos[intervalo_antecessor] and lista_formatada[indice] < intervalos[intervalo_sucessor]:       
            quantidade += 1
    fa.append(quantidade)
    quantidade = 0;
    quantidade_intervalos += 1
    intervalo_antecessor += 1
    intervalo_sucessor += 1
fa[-1] = fa[-1] + 1
faa = []
valor = 0
for i in range(0,k):
    faa.append(round(fa[i] + valor,2))
    valor = faa[i]
fr = []
for i in range(0,k):
    fr.append(round((fa[i] * 100)/len(lista_formatada),2))
soma_fr = 0
for i in range(0,k):
    soma_fr += fr[i]
fra = []
valor = 0
for i in range(0,k):
    fra.append(fr[i] + valor)
    valor = fra[i]



print("")
print("k  |  intervalos  |  f.a         |  f.a.a    |  f.r          |  f.r.a")
print("--------------------------------------------------------------------------------------- ")
for i in range(0,k):
    print(f"{i}  | {intervalos[i]}         |    {fa[i]}         |  {faa[i]}        |    {fr[i]}     |   {fra[i]}")
print("--------------------------------------------------------------------------------------- ")
print(f"-  |  intervalos  |  {len(lista_formatada)}          |  ----      |    {soma_fr}%       |  ----")