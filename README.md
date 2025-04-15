### Nomes: Lucas Mendes Israel, Gustavo Henrique Costa, Gabriel D. kasten, Luis Felipe Mondini, Gustavo Larsen


## Fibonacci com Recursividade e Memoization
Este projeto implementa uma solução otimizada para calcular o n-ésimo número da sequência de Fibonacci utilizando recursividade com memoization (programação dinâmica). A interface gráfica foi desenvolvida com Tkinter, permitindo ao usuário inserir o valor de n, visualizar o cálculo passo a passo e também gerar um gráfico de tempo de execução.
</br></br>
### Como funciona o código:

A função fibonacci(n) é recursiva e usa um dicionário memo como cache, que funciona como uma hashtable para armazenar os resultados já calculados.

Antes de calcular qualquer valor, a função verifica se ele já está em memo. Se estiver, reutiliza o valor (evitando recálculo).

Cada chamada imprime no terminal se o valor está sendo calculado ou se está vindo do cache.

A interface gráfica foi feita com Tkinter, permitindo:

Entrada do valor de n;

Execução do cálculo;

Exibição do resultado e do cache final;

Geração de um gráfico mostrando o tempo de execução para valores de 1 até n.
</br></br>
### Vantagens do uso de memoization:

Performance otimizada: sem memoization, a complexidade é exponencial. Com memoization, cai para O(n).

Evita chamadas duplicadas: cada valor de Fibonacci é calculado uma única vez.
