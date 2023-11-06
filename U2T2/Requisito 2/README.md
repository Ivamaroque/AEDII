## Requisito 2
No requisito 2 foi desenvolvido 5 gráficos que ajudam a ter uma noção visual de como funciona a assotividade de cada rede escolhida. O código usado para demostrar isso pode ser encontrado aqui no repositório ou acessando diretamente o [link](https://colab.research.google.com/drive/1JTCx9ttGMdfrS1EXVfedC3Np8JI8JfNB?usp=sharing).

## Funcionamento dos gráficos
O gráfico que está sendo plotando é chamado de "Gráfico de Assortatividade" ou "Assortatividade de Grau". Ele é usado para visualizar como os nós de um grafo estão conectados com base em seus graus em relação aos graus de seus vizinhos.
- Eixo X (Grau dos Nós):
  - No eixo X, você tem os graus dos nós. Cada ponto no gráfico representa um nó no grafo e seu grau, que é o número de conexões que o nó possui.
- Eixo Y (Média dos Graus dos Nós Vizinhos):
  - No eixo Y, você tem a média dos graus dos nós vizinhos. Para cada nó no grafo, seus vizinhos são os nós diretamente conectados a ele. A média dos graus dos nós vizinhos é calculada para cada nó e representa a média dos graus dos nós aos quais esse nó está conectado.
 
O gráfico mostra a relação entre o grau de um nó (X) e a média dos graus dos nós vizinhos desse nó (Y). Cada ponto no gráfico representa um nó, e a posição do ponto no gráfico revela informações sobre a topologia da rede. Aqui estão algumas interpretações comuns do gráfico:
- Se os pontos no gráfico estão distribuídos de forma crescente, isso indica uma rede "disassortativa". Isso significa que nós com graus mais altos tendem a se conectar a nós com graus mais baixos e vice-versa.
- Se os pontos no gráfico estão distribuídos de forma decrescente, isso indica uma rede "assortativa". Isso significa que nós com graus semelhantes tendem a se conectar entre si.
- Se os pontos estão distribuídos aleatoriamente ou não seguem uma tendência clara, a rede pode ser considerada "neutra" em relação à assortatividade.

Essa visualização ajuda a entender como os nós na rede estão organizados em termos de seus graus e como os nós de alta conectividade se relacionam com os nós de baixa conectividade. Isso é útil em diversas aplicações, como análise de redes sociais, análise de redes de computadores e estudo de fenômenos complexos em sistemas de rede.
