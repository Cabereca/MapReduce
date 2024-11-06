# Projeto MapReduce com Threads 

## Objetivo 

Este projeto implementa um processo básico de MapReduce para contagem de palavras em arquivos de texto. O objetivo principal é aplicar o conceito de MapReduce em um ambiente multithreaded, dividindo o trabalho de contagem de palavras em várias partes (map) e agregando os resultados (reduce), utilizando threads para paralelização.

Este trabalho foi desenvolvido como parte da disciplina Sistemas Distribuídos, com o objetivo de demonstrar o uso de MapReduce em sistemas distribuídos e paralelização usando threads em Python.

## Arquitetura do Sistema
A implementação do MapReduce segue a arquitetura clássica:

#### Map: Divide a tarefa de contar as palavras em vários arquivos de entrada, processando-os em paralelo por meio de threads.
#### Reduce: Consolida os resultados de contagem das palavras em um único arquivo de saída, também usando threads para paralelização.

## Funcionalidades
- Geração de Arquivos: Gera arquivos de texto com palavras aleatórias (usando o módulo FileGenerator).
- MapReduce Paralelizado: Utiliza threads para paralelizar tanto a fase de mapeamento quanto a de redução.
- Limpeza de Arquivos Anteriores: Antes de iniciar o processamento, os arquivos de saída anteriores (se existirem) são apagados, garantindo um ambiente limpo para cada execução.

## Tecnologias Utilizadas
- Python 3.x
- Multithreading (via módulo threading)

## Como Executar
### Requisitos:
Python 3.x: Certifique-se de que o Python 3 esteja instalado no seu ambiente.
### Passos:
Baixe ou Clone o Repositório: Se ainda não tiver o repositório, clone-o ou baixe-o para sua máquina local.

```
git clone https://github.com/Cabereca/MapReduce.git
cd MapReduce
```
Prepare os Arquivos de Entrada O projeto inclui um diretório /aquivos_aleatorios onde os arquivos de texto com palavras serão armazenados. Os arquivos podem ser gerados com o módulo Gerador de Arquivos. Certifique-se de que o diretório aquivos_aleatorios contenha arquivos de texto com palavras geradas aleatoriamente.

Execute o Código Para rodar o código, basta executar o arquivo main.py. Este arquivo irá gerar os arquivos de entrada e executar o processo de MapReduce.

```
python main.py
```
Verifique a Saída Após a execução, os resultados da contagem de palavras serão armazenados em contagem_final, que será gerado durante a execução.

## Possíveis Melhorias
Este projeto é uma implementação simples de MapReduce com paralelização usando threads. Algumas melhorias futuras podem incluir:

- Distribuição Real de Tarefas: Em um ambiente real de sistemas distribuídos, seria interessante distribuir o trabalho entre diferentes máquinas ou processos, possivelmente utilizando ferramentas como Apache Hadoop ou Spark.
- Persistência em Banco de Dados: Em vez de escrever em arquivos, seria interessante persistir as contagens de palavras em um banco de dados.
- Mais Tipos de Processamento: O projeto pode ser expandido para outras operações do MapReduce, como filtragem ou agregações mais complexas.

