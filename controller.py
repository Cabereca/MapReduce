import threading
import os
from map import map_function
from reduce import reduce_function

def limpar_arquivos(output_dir):
    # Apagar arquivo temporário se existir
    tmp_file = os.path.join(output_dir, 'arquivo_temporario.tmp')
    if os.path.exists(tmp_file):
        os.remove(tmp_file)

    # Apagar o arquivo final se existir
    final_file = 'contagem_final'
    if os.path.exists(final_file):
        os.remove(final_file)

def controller(input_files, output_dir):
     # Apagar arquivos antigos antes de começar
    limpar_arquivos(output_dir)

    map_threads = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Executa a função Map em threads separadas
    for file_part in input_files:
        t = threading.Thread(target=map_function, args=(file_part, output_dir))
        map_threads.append(t)
        t.start()

    # Espera todas as threads Map terminarem
    for t in map_threads:
        t.join()

    # Agrupar os resultados do arquivo temporário
    agrupamento = {}
    tmp = open(os.path.join(output_dir, 'arquivo_temporario.tmp'), 'r')
    for line in tmp:
        key, value = line.split()
        if key in agrupamento:
            agrupamento[key].append(int(value))
        else:
            agrupamento[key] = [int(value)]

    tmp.close()

    # Executar a função Reduce em threads separadas para cada chave
    reduce_threads = []
    for key in agrupamento.keys():
        t = threading.Thread(target=reduce_function, args=(key, agrupamento[key]))
        reduce_threads.append(t)
        t.start()

    # Espera todas as threads Reduce terminarem
    for t in reduce_threads:
        t.join()
