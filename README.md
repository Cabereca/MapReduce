# Projeto MapReduce com Threads 

## Objetivo 

Este projeto implementa um processo básico de MapReduce para realizar um grep em arquivos de texto, filtrando as linhas que correspondem ao texto ou à expressão regular fornecida. O objetivo principal é aplicar o conceito de MapReduce em um ambiente multithreaded, dividindo o trabalho de busca (map) e consolidando os resultados (reduce), utilizando threads para paralelização.

Este trabalho foi desenvolvido como parte da disciplina Sistemas Distribuídos, com o intuito de demonstrar o uso de MapReduce para filtragem de texto em sistemas distribuídos e paralelização utilizando threads em Python.

## Arquitetura do Sistema
A implementação do MapReduce segue a arquitetura clássica:

#### Map:  Divide a tarefa de filtrar as linhas que correspondem ao padrão de busca (texto ou expressão regular) em vários arquivos de entrada, processando-os em paralelo por meio de threads.
#### Reduce: Consolida os resultados das linhas que coincidem com o padrão de todos os arquivos

## Funcionalidades
- MapReduce Paralelizado: Utiliza threads para paralelizar tanto a fase de mapeamento quanto a de redução, otimizando o tempo de execução ao processar grandes volumes de dados.
- Busca por Texto ou Regex: Permite filtrar as linhas dos arquivos que contêm o texto ou correspondem à expressão regular informada.
- Limpeza de Arquivos Anteriores: Antes de iniciar o processamento, os arquivos de saída anteriores (se existirem) são apagados, garantindo um ambiente limpo para cada execução.

## Tecnologias Utilizadas
- Python 3.x
- Multithreading (via módulo threading)
- Expressões Regulares (via módulo re)

## Como Executar
### Requisitos:
Python 3: Certifique-se de que o Python 3 esteja instalado no seu ambiente.
### Passos:
Baixe ou Clone o Repositório: Se ainda não tiver o repositório, clone-o ou baixe-o para sua máquina local.

```
git clone https://github.com/Cabereca/MapReduce.git
cd MapReduce
git checkout grep
```
Prepare os Arquivos de Entrada O projeto inclui um diretório /arquivos_entrada onde os arquivos de texto com palavras serão armazenados.Certifique-se de que o diretório arquivos_aleatorios contenha arquivos de texto com palavras geradas aleatoriamente.

O código nessecita de alguns argumentos de linha de comando, com base no exemplo abaixo:

```
python main.py <padrão> <diretório_entrada> <regex|texto>
```

- Com o padrão sendo o texto ou exressão regular buscada
- O dirertório de entrada sendo a pasta onde os arquivos alvos da busca estão localizados
- E se o padrão buscado foi regex ou texto

### Exemplo de Execução

Imagine que você deseja filtrar todas as linhas que contenham a palavra "erro". Você pode executar o seguinte comando:

```
python main.py 'erro' ./arquivos_entrada texto
```
Ou, se deseja buscar por uma expressão regular mais complexa, como por exemplo todas as linhas que contêm números seguidos de uma palavra, pode executar:

```
python main.py '\d+\s+\w+' ./arquivos_entrada regex
```

Verifique a Saída Após a execução, os resultados da contagem de palavras serão armazenados em um aruivo resultado, que será gerado durante a execução.

## Possíveis Melhorias
Este projeto é uma implementação simples de MapReduce com paralelização usando threads. Algumas melhorias futuras podem incluir:

- Distribuição Real de Tarefas: Em um ambiente real de sistemas distribuídos, seria interessante distribuir o trabalho entre diferentes máquinas ou processos, possivelmente utilizando ferramentas como Apache Hadoop ou Spark.
- Persistência em Banco de Dados: Em vez de escrever em arquivos, seria interessante persistir as contagens de palavras em um banco de dados.


