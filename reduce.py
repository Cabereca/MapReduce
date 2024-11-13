def reduce_function(output_dir):
    # Ler o arquivo temporário contendo todas as linhas que passaram no filtro
    with open(os.path.join(output_dir, 'arquivoTemporario.tmp'), 'r') as temp_file:
        result_lines = temp_file.readlines()

    # Grava o resultado final no arquivo de saída
    with open('resultado.txt', 'w') as final_output:
        for line in result_lines:
            final_output.write(line)