class node:
    def __init__(self, num): #Inicializa o construtor definindo valor, esquerda, direita e altura
        self.valor = num
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.root = None
    # A altura das subárvores detodo nó nunca deve diferir em mais de 1.
    def altura(self, Node):
        if Node is None:
            return 0
        else:
            return Node.altura
# A função fator_balanceamento calcula o valor do fator de balanceamento. fb = altEsq – altDir
# Está balanceada se o valor estiver entr 1 e -1.
    def fator_balanceamento(self, Node):
        if Node is None:
            return 0
        else:
            return self.altura(Node.esquerda) - self.altura(Node.direita)

    def MinimumValueNode(self, Node):
        if Node is None or Node.esquerda is None:
            return Node
        else:
            return self.MinimumValueNode(Node.esquerda)
# Função para rotar a arvore para a direira
    def rotacionaDireita(self, Node):
        a = Node.esquerda
        b = a.direita
        a.direita = Node
        Node.esquerda = b
        Node.altura = 1 + max(self.altura(Node.esquerda), self.altura(Node.direita))
        a.altura = 1 + max(self.altura(a.esquerda), self.altura(a.direita))
        return a

    # Função para rotar a arvore para a esquerda
    def rotacionaEsquerda(self, Node):
        a = Node.direita
        b = a.esquerda
        a.esquerda = Node
        Node.direita = b
        Node.altura = 1 + max(self.altura(Node.esquerda), self.altura(Node.direita))
        a.altura = 1 + max(self.altura(a.esquerda), self.altura(a.direita))
        return a
# Função para inserir valores na árvore
    def inserir(self, val, root):
        if root is None:
            return node(val)
        elif val <= root.valor:
            root.esquerda = self.inserir(val, root.esquerda)
        elif val > root.valor:
            root.direita = self.inserir(val, root.direita)
        root.altura = 1 + max(self.altura(root.esquerda), self.altura(root.direita))
        fator_balanceamento = self.fator_balanceamento(root)
        if fator_balanceamento > 1 and root.esquerda.valor > val:
            return self.rotacionaDireita(root)
        if fator_balanceamento < -1 and val > root.direita.valor:
            return self.rotacionaEsquerda(root)
        if fator_balanceamento > 1 and val > root.esquerda.valor:
            root.esquerda = self.rotacionaEsquerda(root.esquerda)
            return self.rotacionaDireita(root)
        if fator_balanceamento < -1 and val < root.direita.valor:
            root.direita = self.rotacionaDireita(root.direita)
            return self.rotacionaEsquerda(root)
        return root

    def busca(self, val):
        if self.root:
            return self.busca_data(val, self.root)
        return False

    def busca_data(self, val, Node):
        if val == Node.valor:
            return True
        elif val < Node.valor and Node.esquerda:
            return self.busca_data(val, Node.esquerda)
        elif val > Node.valor and Node.direita:
            return self.busca_data(val, Node.direita)
        return False

#ordena a arvore
    def ordenar(self, root):
        if root is None:
            return
        print(root.valor)
        self.ordenar(root.esquerda)
        self.ordenar(root.direita)
# Função pra deletar elementos.
    def deletar(self, val, Node):
        if Node is None:
            return Node
        elif val < Node.valor:
            Node.esquerda = self.deletar(val, Node.esquerda)
        elif val > Node.valor:
            Node.direita = self.deletar(val, Node.direita)
        else:
            if Node.esquerda is None:
                lt = Node.direita
                Node = None
                return lt
            elif Node.direita is None:
                lt = Node.esquerda
                Node = None
                return lt
            rgt = self.MinimumValueNode(Node.direita)
            Node.valor = rgt.valor
            Node.direita = self.deletar(rgt.valor, Node.direita)
        if Node is None:
            return Node
        Node.altura = 1 + max(self.altura(Node.esquerda), self.altura(Node.direita))
        fator_balanceamento = self.fator_balanceamento(Node)
        if fator_balanceamento > 1 and self.fator_balanceamento(Node.esquerda) >= 0:
            return self.rotacionaDireita(Node)
        if fator_balanceamento < -1 and self.fator_balanceamento(Node.direita) <= 0:
            return self.rotacionaEsquerda(Node)
        if fator_balanceamento > 1 and self.fator_balanceamento(Node.esquerda) < 0:
            Node.esquerda = self.rotacionaEsquerda(Node.esquerda)
            return self.rotacionaDireita(Node)
        if fator_balanceamento < -1 and self.fator_balanceamento(Node.direita) > 0:
            Node.direita = self.rotacionaDireita(Node.direita)
            return self.rotacionaEsquerda(Node)
        return Node


Tree = AVL()
r = None
#Inserção

r = Tree.inserir(4, r)
r = Tree.inserir(6, r)
r = Tree.inserir(7, r)
r = Tree.inserir(8, r)
r = Tree.inserir(9, r)
print("Arvore após inserção:")
Tree.ordenar(r)
# Exclusão
rt = Tree.deletar(8,r)
print("Arvore após deletar um valor:")
Tree.ordenar(r)
# Pesquisa
print("\nPesquisa:")
resultado = Tree.busca(3)
if resultado:
    print("Valor encontrado")
else:
    print("Valor não encontrado")
