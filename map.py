import re
import os

def map_function(file_part, output_dir, pattern, is_regex):
    with open(file_part, 'r') as f:
        with open(os.path.join(output_dir, 'arquivoTemporario.tmp'), 'a') as f_out:
            # Se for regex, compila a expressão regular
            if is_regex:
                regex = re.compile(pattern)

            for line in f:
                if is_regex:
                    # Se for regex, usa search para encontrar o padrão na linha
                    if regex.search(line):
                        f_out.write(f'{file_part}: {line}')
                else:
                    # Se for texto simples, usa 'in' para verificar se o padrão está na linha
                    if pattern in line:
                        f_out.write(f'{file_part}: {line}')  
