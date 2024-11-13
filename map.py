import os
import random

def map_function(arquivo, output_dir):
    with open(arquivo, 'r') as f:
        with open(os.path.join(output_dir, 'arquivo_temporario.tmp'), 'a') as f_out:
            # Itera sobre cada linha do arquivo
            for linha in f:
                # Divide a linha em palavras
                palavras = linha.split()
                # Conta as ocorrências das palavras e escreve diretamente no arquivo temporário
                for palavra in palavras:
                    f_out.write(f"{palavra} 1\n")
