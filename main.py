import os
import re
import sys
from controller import controller

if __name__ == "__main__":

    # Pega o padrão de expressão regular ou texto simples como argumento
    if len(sys.argv) < 4:
        print("Uso: python main.py <padrão> <diretório_entrada> <regex|texto>")
        sys.exit(1)

    # Padrão de expressão regular ou texto simples fornecido pelo usuário
    pattern = sys.argv[1]

    # Tipo de padrão: 'regex' ou 'texto'
    pattern_type = sys.argv[3].lower()

    # Verifica se o tipo de padrão é válido
    if pattern_type not in ['regex', 'texto']:
        print("O tipo de padrão deve ser 'regex' ou 'texto'.")
        sys.exit(1)

    # Define se o padrão é regex ou texto
    is_regex = pattern_type == 'regex'

    # Diretório com os arquivos de entrada (divididos)
    input_dir = sys.argv[2]

    # Diretório para armazenar os arquivos temporários e o resultado final
    output_dir = 'diretorio_temporario'

    # Coleta os arquivos de entrada (parte de cada arquivo)
    input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.txt')]

    # Chama o controlador para executar o Map e o Reduce
    controller(input_files, output_dir, pattern, is_regex)
