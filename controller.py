import threading
import os
from map import map_function
from reduce import reduce_function
from reset import limpar_arquivos

def controller(input_files, output_dir, pattern, is_regex):
     # Apagar arquivos antigos antes de começar
    if os.path.exists(output_dir):
        limpar_arquivos(output_dir)

    map_threads = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Executa a função Map em threads separadas
    for file_part in input_files:
        t = threading.Thread(target=map_function, args=(file_part, output_dir, pattern, is_regex))
        map_threads.append(t)
        t.start()

    # Espera todas as threads Map terminarem
    for t in map_threads:
        t.join()

# Executa a função Reduce para consolidar os resultados
    reduce_function(output_dir)
