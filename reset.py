import os

def deletar_arquivos(output_dir='arquivos_aleatorios'):
    if os.path.exists(output_dir):
        for file_name in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(output_dir)

def limpar_arquivos(output_dir='diretorio_temporario'):
    # Apagar arquivo temporário se existir
    tmp_file = os.path.join(output_dir, 'arquivo_temporario.tmp')
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
        os.rmdir(output_dir)

    # Apagar o arquivo final se existir
    final_file = 'contagem_final'
    if os.path.exists(final_file):
        os.remove(final_file)

if __name__ == "__main__":
    limpar_arquivos()
    deletar_arquivos()