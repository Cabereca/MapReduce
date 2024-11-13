import os

def limpar_arquivos(output_dir='diretorio_temporario'):
    # Apagar arquivo temporário se existir
    tmp_file = os.path.join(output_dir, 'arquivo_temporario.tmp')
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
        os.rmdir(output_dir)

    # Apagar o arquivo final se existir
    final_file = 'resultado.txt'
    if os.path.exists(final_file):
        os.remove(final_file)

if __name__ == "__main__":
    deletar_arquivos()