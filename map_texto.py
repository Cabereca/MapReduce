import os

def map_function_text(file_part, output_dir, pattern):
    with open(file_part, 'r') as f:
        with open(os.path.join(output_dir, 'arquivoTemporario.tmp'), 'a') as f_out:
            for line in f:
                if pattern in line:
                    f_out.write(f'{file_part}: {line}')  
