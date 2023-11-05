class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        new_root.height = max(self._height(new_root.left), self._height(new_root.right)) + 1

        return new_root

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        node.height = max(self._height(node.left), self._height(node.right)) + 1

        balance = self._balance(node)

        # Left Heavy
        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right Heavy
        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _find_words_with_prefix(self, node, prefix):
        if node is None:
            return []

        if node.key.startswith(prefix):
            return [node.key] + \
                   self._find_words_with_prefix(node.left, prefix) + \
                   self._find_words_with_prefix(node.right, prefix)
        elif prefix < node.key:
            return self._find_words_with_prefix(node.left, prefix)
        else:
            return self._find_words_with_prefix(node.right, prefix)

    def find_words_with_prefix(self, prefix):
        return self._find_words_with_prefix(self.root, prefix)


# Função para pré-processar o corpus
def preprocess_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c.isalnum() or c.isspace()])
    words = text.split()
    return words


# Exemplo de uso
if __name__ == "__main__":
    corpus = """
A Revolução da Inteligência Artificial: Máquinas que Aprendem e Transformam o Mundo

A inteligência artificial (IA) é uma das inovações mais empolgantes e transformadoras do século XXI. Trata-se de um campo da ciência da computação que busca criar sistemas capazes de realizar tarefas que, até pouco tempo atrás, só podiam ser executadas por seres humanos, como raciocinar, tomar decisões, aprender e compreender linguagem natural. A IA representa a capacidade de as máquinas não apenas processarem dados, mas também de interpretá-los e tomar ações com base nessa interpretação.

Um dos principais catalisadores desse avanço tecnológico é o aprendizado de máquina (machine learning), um subcampo da IA que permite que os sistemas aprendam e melhorem a partir da experiência. Isso significa que, em vez de serem programadas para executar tarefas específicas, as máquinas podem aprender com dados e se adaptar a novas situações, tornando-se cada vez mais eficientes em suas operações.

A IA está presente em muitos aspectos da nossa vida cotidiana, mesmo que muitas vezes não a percebamos. Os mecanismos de recomendação em serviços de streaming, como Netflix e Spotify, são alimentados por algoritmos de IA que analisam nossas preferências e sugerem conteúdos relevantes. Os assistentes virtuais, como Siri, Google Assistant e Alexa, são exemplos de IA que podem responder a perguntas, realizar tarefas e até mesmo manter conversas naturais com os usuários.

Além do entretenimento e da assistência virtual, a IA tem uma ampla gama de aplicações em setores como medicina, finanças, transporte, manufatura e muito mais. Na medicina, por exemplo, a IA pode ser usada para diagnosticar doenças, analisar imagens médicas, prever surtos de epidemias e personalizar tratamentos com base nos dados do paciente. Nas finanças, os algoritmos de IA são usados para detecção de fraudes, previsões de mercado e gerenciamento de portfólio.

No entanto, a crescente influência da IA também levanta questões éticas e sociais importantes. Questões sobre privacidade de dados, viés algorítmico e o impacto da automação no emprego são apenas alguns dos desafios que a sociedade enfrenta à medida que a IA se torna cada vez mais onipresente. É essencial encontrar um equilíbrio entre a inovação tecnológica e a responsabilidade ética para garantir que a IA beneficie a humanidade como um todo.

À medida que a IA continua a evoluir, é emocionante pensar no que o futuro reserva. A IA promete revolucionar a maneira como vivemos, trabalhamos e interagimos com o mundo ao nosso redor. No entanto, é crucial que continuemos a estudar, debater e regulamentar o uso da IA para garantir que seus benefícios sejam maximizados e que os riscos sejam minimizados. Com a combinação certa de inovação e responsabilidade, a inteligência artificial tem o potencial de moldar um futuro mais inteligente e promissor para todos nós.
"""

    prefix = "rev"

    words = preprocess_text(corpus)
    avl_tree = AVLTree()

    for word in set(words):
        avl_tree.insert(word)

    completions = avl_tree.find_words_with_prefix(prefix)
    print("Lista de Palavras:", completions)
