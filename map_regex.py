import re
import os

def map_function_regex(file_part, output_dir, pattern):
    with open(file_part, 'r') as f:
        with open(os.path.join(output_dir, 'arquivoTemporario.tmp'), 'a') as f_out:
            regex = re.compile(pattern)

            for line in f:
                if regex.search(line):
                    f_out.write(f'{file_part}: {line}')
