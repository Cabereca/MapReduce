import os
from controller import controller

if __name__ == "__main__":
    # Diretório onde os arquivos estão localizados
    arquivos_aleatorios_dir = 'arquivos_aleatorios'
    output_dir = 'diretorio_temporario'

    # Obter os arquivos gerados pelo Gerador de Arquivos
    input_files = [os.path.join(arquivos_aleatorios_dir, f) for f in os.listdir(arquivos_aleatorios_dir) if f.endswith('.txt')]

    # Executar o controlador MapReduce com os arquivos gerados
    controller(input_files, output_dir)
