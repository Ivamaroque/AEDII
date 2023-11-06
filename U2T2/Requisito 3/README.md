
## Requisitos 3
## Explicação da tabela
- A quantidade de vértices da rede:

  - Isso se refere ao número de nós em um grafo. Em uma rede, os vértices representam entidades, pontos de dados ou elementos que podem estar conectados por arestas. Essa medida indica quantas entidades ou nós fazem parte da rede.
-A quantidade de arestas da rede:

  - As arestas são as conexões entre os nós em um grafo. Essa quantidade se refere ao número de conexões ou relacionamentos entre os nós na rede. Em muitos contextos, as arestas representam interações, relações ou ligações entre as entidades representadas pelos vértices.
-O degree_assortativity_coefficient da rede:

  - O coeficiente de assortatividade de grau (degree assortativity coefficient) é uma medida que descreve como os nós de um grafo estão conectados com base em seus graus (número de conexões). Ele indica se nós com graus semelhantes tendem a se conectar entre si (assortatividade positiva) ou se conectam de forma inversa, ou seja, nós com graus diferentes se conectam (assortatividade negativa).
-O número de componentes conectados da rede:

  - Em um grafo, componentes conectados são grupos de nós que estão ligados por arestas e que não podem ser alcançados a partir de outros grupos de nós dentro do grafo. O número de componentes conectados na rede indica quantos grupos distintos de entidades estão presentes na rede e estão isolados um do outro.
-O tamanho do GCC (Giant Connected Component) da rede:

  - O GCC é o maior componente conectado em um grafo, ou seja, é o maior grupo de nós que estão todos interconectados de alguma forma. O tamanho do GCC é a contagem de nós nesse componente e é uma medida importante para entender a estrutura da rede, especialmente em redes sociais, onde o GCC pode representar a maior parte da população.

## Tabela
| Dados | Qtd de vértices | Qtd de arestas | Coeficiente de assortatividade do grau | Qtd de componentes conectados | Tamanho do GCC | Coeficiente de clustering |
|------|------|------|------|------|------|------|
| web_Google | 685230 | 7600595 | -0.1788553259535877 | 109406 | 334857 | null |
| email_EuAll | 265214 | 420045 | -0.21041150055155367 | 231000 | 34203 | 0.056465531555997504 |
| web_Google | 875713 | 4322051 | -0.05508895972321737 | 2746 | 855802 | 0.5142961475354184 |
| wiki_Rfa | 26255 | 81702 | -0.40334730444192296 | 26255 | 1 | 0.0 |
| amazon0601 | 403394 | 3387388 |-0.04353522746406418 | 1588 | 395234 | 0.3646879271657948 |
