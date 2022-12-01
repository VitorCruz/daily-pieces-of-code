import csv

## QUANTIDADE DE ARQUIVOS PARA JUNTAR
arquivos = 6

## DELIMITADOR DO ARQUIVO
delimiter = ';'

## PATTERN DOS ARQUIVOS DE ENTRADA SEM O ".CSV" NOMEAR OS ARQUIVOS COM PATTERN +1,2,3,4,5,6 (ex: teste1.csv, teste2.csv, teste3.csv)
filepattern = 'C:\\Users\\vitorc\\Desktop\\Celcoin\\ArquivosJuntar\\teste'

## ARQUIVO DE SAÍDA
arquivo_saida = 'C:\\Users\\vitorc\\Desktop\\Celcoin\\ArquivosJuntar\\tudojunto.csv'


f = open(f'{filepattern}1.csv', 'r')
headers = f.readline().strip().split(delimiter)
result = []

for i in range(1,arquivos+1):    
    with open(f'{filepattern}{str(i)}.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            row_dict = {}
            for h in headers:
                row_dict[h] = row[h]
            result.append(row_dict) 
            
with open(arquivo_saida, 'w', newline='') as csvfile:
    fieldnames = [*headers]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()
    for r in result:
        writer.writerow(r)        