import random
import os
from reset import deletar_arquivos

class FileGenerator:
    def __init__(self, split, n, alphabet, min_size, max_size):
        self.split = split  # Número de arquivos a serem gerados
        self.n = n  # Número de palavras a serem geradas
        self.alphabet = alphabet  # Alfabeto de caracteres permitidos
        self.min_size = min_size  # Tamanho mínimo das palavras
        self.max_size = max_size  # Tamanho máximo das palavras

    def _gerar_palavras_aleatorias(self):
        palavras = []
        for _ in range(self.n):
            palavras_length = random.randint(self.min_size, self.max_size)
            palavra = ''.join(random.choice(self.alphabet) for _ in range(palavras_length))
            palavras.append(palavra)
        return palavras

    def gerar_arquivos(self, output_dir):
        # Se o diretório já existe, apagamos seu conteúdo (se houver arquivos antigos)
        if os.path.exists(output_dir):
            # Apagar os arquivos antigos dentro do diretório
            deletar_arquivos(output_dir)
        else:
            # Se o diretório não existe, criamos ele
            os.makedirs(output_dir)

        # Gera palavras aleatórias e as divide em arquivos
        palavras = self._gerar_palavras_aleatorias()
        palavras_por_arquivo = len(palavras) // self.split

        for i in range(self.split):
            part_words = palavras[i*palavras_por_arquivo: (i+1)*palavras_por_arquivo]
            with open(os.path.join(output_dir, f'arquivo{i+1}.txt'), 'w') as f:
                f.write(' '.join(part_words))
              
#Exemplo de Uso              
if __name__ == "__main__":
    # Parâmetros de configuração
    gerador_de_arquivos = FileGenerator(
        split=1,              # Dividir o texto em 3 arquivos
        n=100,                # Gerar 100 palavras
        alphabet=['a', 'b', 'c', 'd', 'e'],  # Definir as letras permitidas
        min_size=3,           # Tamanho mínimo de palavras: 4 letras
        max_size=6            # Tamanho máximo de palavras: 8 letras
    )

    # Criar e executar o gerador de arquivos
    arquivos_aleatorios_dir = 'arquivos_aleatorios'
    gerador_de_arquivos.gerar_arquivos(arquivos_aleatorios_dir)              
