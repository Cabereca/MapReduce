import threading
import os
from map_regex import map_function_regex
from map_texto import map_function_text
from reduce import reduce_function
from reset import limpar_arquivos

def controller(input_files, output_dir, pattern, is_regex):
     # Apagar arquivos antigos antes de começar
    if os.path.exists(output_dir):
        limpar_arquivos(output_dir)

    map_threads = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if is_regex:
        for file_part in input_files:
            t = threading.Thread(target=map_function_regex, args=(file_part, output_dir, pattern))
            map_threads.append(t)
            t.start()
    else:
         for file_part in input_files:
            t = threading.Thread(target=map_function_text, args=(file_part, output_dir, pattern))
            map_threads.append(t)
            t.start()

    # Espera todas as threads Map terminarem
    for t in map_threads:
        t.join()

# Executa a função Reduce para consolidar os resultados
    reduce_function(output_dir)
