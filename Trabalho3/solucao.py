from typing import Iterable, Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:Nodo, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        

def calc_acao(estado:str, indice:int, acao:str)->Tuple[str,str]:
    match acao:
        case "acima":
            mod = -3
        case "abaixo":
            mod = 3
        case "esquerda":
            mod = -1
        case "direita":
            mod = 1
    num_troca = estado[indice + mod]
    estado = estado.replace(estado[indice + mod],'_')
    estado = estado.replace(estado[indice],num_troca)
    return [acao,estado]

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    list_acoes = []
    indice = 1
    for i in estado:
        if i == '_':
            break
        else:
            indice += 1
    
    match indice:
        case 1:
            list_acoes.append(calc_acao(estado,indice,"direita"))
            list_acoes.append(calc_acao(estado,indice,"abaixo"))
        case 2:
            list_acoes.append(calc_acao(estado,indice,"direita"))
            list_acoes.append(calc_acao(estado,indice,"abaixo"))
            list_acoes.append(calc_acao(estado,indice,"esquerda"))
        case 3:
            list_acoes.append(calc_acao(estado,indice,"esquerda"))
            list_acoes.append(calc_acao(estado,indice,"abaixo"))
        case 4:
            list_acoes.append(calc_acao(estado,indice,"direita"))
            list_acoes.append(calc_acao(estado,indice,"abaixo"))
            list_acoes.append(calc_acao(estado,indice,"acima"))
        case 5:
            list_acoes.append(calc_acao(estado,indice,"direita"))
            list_acoes.append(calc_acao(estado,indice,"abaixo"))
            list_acoes.append(calc_acao(estado,indice,"esquerda"))
            list_acoes.append(calc_acao(estado,indice,"acima"))
        case 6:
            list_acoes.append(calc_acao(estado,indice,"esquerda"))
            list_acoes.append(calc_acao(estado,indice,"abaixo"))
            list_acoes.append(calc_acao(estado,indice,"acima"))
        case 7:
            list_acoes.append(calc_acao(estado,indice,"direita"))
            list_acoes.append(calc_acao(estado,indice,"acima"))
        case 8:
            list_acoes.append(calc_acao(estado,indice,"esquerda"))
            list_acoes.append(calc_acao(estado,indice,"direita"))
            list_acoes.append(calc_acao(estado,indice,"acima"))
        case 9:
            list_acoes.append(calc_acao(estado,indice,"esquerda"))
            list_acoes.append(calc_acao(estado,indice,"acima"))
    return list_acoes     
    #raise NotImplementedError


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
