import os
import random

def map_function(arquivo, output_dir):
    contador_de_palavras = {}

    # Abrir a parte do arquivo e contar as palavras
    with open(arquivo, 'r') as f:
        for linha in f:
            palavras = linha.split()
            for palavra in palavras:
                if palavra not in contador_de_palavras:
                    contador_de_palavras[palavra] = 1
                else:
                    contador_de_palavras[palavra] += 1

    # Gravar o resultado em um arquivo temporário
    with open(os.path.join(output_dir, 'arquivo_temporario.tmp'), 'a') as f_out:
        for palavra, count in contador_de_palavras.items():
            f_out.write(f"{palavra} {count}\n")
