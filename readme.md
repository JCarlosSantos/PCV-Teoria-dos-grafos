# Projeto PCV - Teoria a grafos 100% atualizado

# Descrição

No momento consta nesse projeto, um algoritmo desenvolvido para receber bases de dados em formato de matriz (onde se espera que trate-se da representação de distâncias de cidades), e organizar em uma lista de vetores.

# Instalação

Instale o Python com versão minima 3.11.2, disponivel em: https://www.python.org/downloads/.
Baixe os arquivos do repositorio e salve em uma pasta de sua preferência, com o python instalado, abra a pasta de origem do projeto no cmd, em seguida, no prompt de comando, digite o comando: `python main.py` para executar o algoritmo.

# Como usar

O algoritmo principal inicialmente realiza apenas a leitura das [bases de dados](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html) fornecidas para solução do problema, são elas ATT48, DANTZIG42, FRI26, GR17 e P01.

Abaixo, veja um exemplo de um dos base de dados sem tratamento:

![image](https://github.com/JCarlosSantos/PCV-Teoria-dos-grafos/assets/134893104/25342bf0-7a26-4c7c-8a5c-1d65f4705bee)

Os nomes das bases de dados que serão lidas estão inclusas na lista `file_names`, que podem ser alteradas ao gosto do usuário:
![image](https://github.com/JCarlosSantos/PCV-Teoria-dos-grafos/assets/134893104/0f224f3c-f1e3-4882-a1f5-cf18d6af3721)

Ao executar o algoritmo, no terminal serão exibidos os valores das bases de dados que estarão formatados para lista de vetores. 

Exemplo de base de dados após tratamento:

![image](https://github.com/JCarlosSantos/PCV-Teoria-dos-grafos/assets/134893104/bd48a91a-bf55-4250-8151-0a49748b7c32)



# Licença

Este projeto é licenciado sob a [Licença MIT](https://opensource.org/license/mit/)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# Contato dos desenvolvedores

Desenvolvido por: 
José Carlos Silva Santos - jose.santos5@arapiraca.ufal.br

# Hardware sugerido

Para realizar a implementação e os testes dos algoritmos acima mencionados recorreu-se a um computador com processador AMD Ryzen™ 7 5800H 3.20 GHz, tendo 16GB 3200 MHz DDR4 (2 × 8GB) de memória RAM SODDIM, SSD PCIe NVME de 1TB e SSD PCIe NVME de 512 GB, com sistema operacional Windows 11 Home.
A execução dos algoritmos deve ser realizada com uma configuração mínima necessária: processador Intel i3-3220 3.30 GHz, com 8 GB 1666 MHz DDR4 (1 × 8GB) de memória RAM, HD de 500GB, e sistema operacional Ubuntu Linux.

# Sofware necessário

Python 3.11.2
