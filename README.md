# Simulador de Memória cache
O simulador foi desenvolvido na linguagem de programação Python, por ser uma linguagem de programação de alto nível, com tipagem dinâmica e uma liberdade muito grande para a manipulação de strings. Para organizar o desenvolvimento do código em equipe, utilizamos o Google Colaboratory, uma ferramenta que facilita o compartilhamento de códigos por meio de uma lista de células que podem conter textos explicativos ou códigos executáveis e até mesmo suas respectivas saídas.

## Instalação
O único pré-requisito do simulador é que sua máquina tenha instalado o python 3.7 ou superior. Para saber a sua versão do python basta abrir o terminal de comando e digitar:

    python --version
 
O resultado obtido deverá ser algo semelhante a isso:

    Python 3.7.0
Após confirmar a sua versão do python basta navegar pelo prompt de comando ate a pasta na qual foram salvos tanto os arquivos de teste quanto os scripts e executar o seguinte código para iniciar o simulador:

    python main.py -h
Então aparecerão as instruções abaixo:

    +--------- PARAMETROS ACEITOS ---------+
    | 1-Numero total de linhas da memoria: |
    |    -um numero inteiro                |
    | 2-Numero de palavras por linha       |
    |    -um numero inteiro                |
    | 3-Tipo de mapeamento:                |
    |    -"d" para mapeamento direto       |
    |    -"a" para mapeamento associativo  |
    |    -"c" para associativo por conjunto|
    | 4-Politica de escrita:               |
    |    -"t" para write through           |
    |    -"b" para write back              |
    | 5-Algoritimo de substituicao:        |
    |    -"r" para um escolha randomica    |
    |    -"p" para pri a entrar, pri a sair|
    |    -"l" para LFU                     |
    |    -"n" para mapeamento direto       |
    | 6-Arquivo de texto:                  |
    |    -arquivo.txt                      |
    | FORMATO FINAL:                       |
    |     -"1,2,345-6"                     |
    +--------------------------------------+
## O que foi implementado
1.  Tipos de Mapeamento:
    
	-   Mapeamento Direto
    
	-   Mapeamento Associativo
    
	-   Mapeamento Associativo por Conjunto
    
2.  Política de substituição:
    
	-   Escolha aleatória​
   
	-   FIFO (“primeiro a entrar, primeiro a sair”)
    
	-   LFU (saí o bloco menos utilizado)
  
3.  Política de escrita:
    
	-   Write Thought
	
    ## 1 - Mapeamento Direto
    Sobre o mapeamento direto ele é a técnica mais simples, visto que mapeia cada bloco da memória principal a apenas uma linha de cache possível.

Aplicando o mapeamento direto no arquivo ''t4.trace'':

    16,2,dtn-t4.trace
A saída será:

    +-------+-------------------------------+
    | INDEX |              TAG              |
    +-------+-------------------------------+
    |   0   |             10016             |
    |   1   |             10017             |
    |   2   |             10016             |
    |   3   |            3fc000e            |
    |   4   |            3fc000e            |
    |   5   |             10015             |
    |   6   |            3fc000e            |
    |   7   |             1802a             |
    |   8   |             1802a             |
    |   9   |             10015             |
    |  10   |             10015             |
    |  11   |             10015             |
    |  12   |             10015             |
    |  13   |             10015             |
    |  14   |             10015             |
    |  15   |             10015             |
    +-------+-------------------------------+
    MISS: 280
    HIT: 316
    ACESSOS A MEMORIA: 280
    MAPEAMENTO DIRETO
    POLITICA DE ESCRITA WRITE THROUGH
## Mapeamento Associativo
O mapeamento associativo compensa a desvantagem do mapeamento direto, permitindo que cada bloco da memória principal seja carregado em qualquer linha da cache. Nesse caso, a lógica de controle da cache interpreta um endereço de memória simplesmente como um campo Tag e um campo Palavra. O campo Tag identifica o bloco da memória principal. Para determinar se um bloco está na cache, a lógica de controle da cache precisa comparar simultaneamente a tag de cada linha. Observe que nenhum campo no endereço corresponde ao número de linha, de modo que o número de linhas na cache não é determinado pelo formato do endereço.

Aplicando o mapeamento associativo e politica de substituição FIFO no arquivo ''t4.trace'':

    16,2,atp-t4.trace

A saída será:

        +-------+-------------------------------+
        | INDEX |              TAG              |
        +-------+-------------------------------+
        |   0   |            1802a7             |
        |   1   |            10015d             |
        |   2   |            10015e             |
        |   3   |            10015f             |
        |   4   |            100160             |
        |   5   |            100161             |
        |   6   |           3fc000e4            |
        |   7   |            100162             |
        |   8   |           3fc000e6            |
        |   9   |            100171             |
        |  10   |            1802a8             |
        |  11   |            100159             |
        |  12   |           3fc000e1            |
        |  13   |            10015a             |
        |  14   |            10015b             |
        |  15   |            10015c             |
        +-------+-------------------------------+
        MISS: 411
        HIT: 185
        ACESSOS A MEMORIA: 411
        MAPEAMENTO ASSOCIATIVO
        POLITICA DE ESCRITA WRITE THROUGH
        SUBSTITUIÇAO DOS PRIMEIROS A ENTRAR
    ## Mapeamento Associativo por Conjunto
    O mapeamento associativo em conjunto é um meio-termo que realça os pontos fortes das técnicas direta e associativa, enquanto reduz suas desvantagens. Neste caso, a cache é uma série de conjuntos, cada um consistindo em uma série de linhas.
    
    Aplicando o mapeamento associativo por conjunto, politica de substituição
    LFU  ''t4.trace'':
    
        16,2,ctl-t4.trace
    Em seguida o simulador ira pedir para o usuário inserir o numero de linhas por conjunto:
    
        Numero de Linhas por conjunto:
        4
    
    A saída será:
    
    +-------+-------------------------------+
    | INDEX |              TAG              |
    +-------+-------------------------------+
    |   0   |             600aa             |
    |   1   |             4005c             |
    |   2   |            ff00039            |
    |   3   |             40052             |
    |   4   |             4005b             |
    |   5   |             40052             |
    |   6   |            ff00038            |
    |   7   |             40058             |
    |   8   |             4005b             |
    |   9   |            ff00039            |
    |  10   |            ff00037            |
    |  11   |             40052             |
    |  12   |             40051             |
    |  13   |             40053             |
    |  14   |             40054             |
    |  15   |             4005c             |
    +-------+-------------------------------+
    MISS: 432
    HIT: 173
    ACESSOS A MEMORIA: 441
    MAPEAMENTO ASSOCIATIVO POR CONJUNTOS
    TAMANHO DO CONJUNTO = 4
    POLITICA DE ESCRITA WRITE THROUGH
    SUBSTITUIÇAO LFU

    






