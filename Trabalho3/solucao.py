from typing import Iterable, Set, Tuple
from heapq import heappush, heappop
from collections import deque #opcional,extra (BFS)

OBJECTIVE = "12345678_"

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __lt__(self, other):
        return self.custo < other.custo
    
    def __eq__(self, other):
        return isinstance(other, Nodo) and self.estado == other.estado
    
    def __hash__(self):
        return hash(self.estado)
    
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
        case _:
            raise ValueError(f"Acao invalida: {acao}")
    estado_list = list(estado)
    num_troca = estado_list[indice + mod]
    estado_list[indice + mod] = '_'
    estado_list[indice] = num_troca
    novo_estado = ''.join(estado_list)
    return (acao,novo_estado)

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    acoes_set = set()

    indice = estado.index('_')
    
    if indice > 2:
        acoes_set.add(calc_acao(estado,indice,"acima"))
    if indice < 6:
        acoes_set.add(calc_acao(estado,indice,"abaixo"))
    if indice % 3 > 0:
        acoes_set.add(calc_acao(estado,indice,"esquerda"))
    if indice % 3 < 2:
        acoes_set.add(calc_acao(estado,indice,"direita"))
    return acoes_set

def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    nodos = set()
    # substituir a linha abaixo pelo seu codigo
    sucessores = sucessor(nodo.estado)
    for suc in sucessores:
        nodos.add(Nodo(suc[1], nodo, suc[0], nodo.custo + 1))
    return nodos

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    X = set()
    F = []
    heappush(F, (0, Nodo(estado, None, None, 0)))
    nos_expandidos = 0

    while F:
        _, v = heappop(F)
        if v.estado == OBJECTIVE:
            sequencia = []
            nodo = v
            while nodo is not None:
                if nodo.acao is not None:
                    sequencia.insert(0, nodo.acao)
                nodo = nodo.pai
            return sequencia#, nos_expandidos
        
        if v.estado not in X:
            X.add(v.estado)
            nos_expandidos += 1
            for nodo in expande(v):
                if nodo not in X:
                    heappush(F, (nodo.custo + hamming_distance(nodo.estado, OBJECTIVE), nodo))
    return None#, nos_expandidos

def hamming_distance(string1, string2): 
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i] and string1[i] != "_":
            distance += 1
    return distance

def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    X = set()
    F = []
    heappush(F, (0, Nodo(estado, None, None, 0)))
    nos_expandidos = 0

    while F:
        _, v = heappop(F)
        if v.estado == OBJECTIVE:
            sequencia = []
            nodo = v
            while nodo is not None:
                if nodo.acao is not None:
                    sequencia.insert(0, nodo.acao)
                nodo = nodo.pai
            return sequencia#, nos_expandidos
        
        if v.estado not in X:
            X.add(v.estado)
            nos_expandidos += 1
            for nodo in expande(v):
                if nodo not in X:
                    heappush(F, (nodo.custo + manhattan_distance(nodo.estado, OBJECTIVE), nodo))
    return None#, nos_expandidos

def manhattan_distance(string1, string2, grid_size = 3): 
    distance = 0
    L = len(string1)
    for i in range(L):
        char = string1[i]
        if char != '_':
            matching_pos = string2.index(char)
            x1,y1 = divmod(i, grid_size)
            x2,y2 = divmod(matching_pos, grid_size)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

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
    
    X = set()
    F = deque()
    F.append(Nodo(estado, None, None, 0))
    nos_expandidos = 0

    while F:
        v = F.popleft()
        if v.estado == OBJECTIVE:
            sequencia = []
            nodo = v
            while nodo is not None:
                if nodo.acao is not None:
                    sequencia.insert(0, nodo.acao)
                nodo = nodo.pai
            return sequencia#, nos_expandidos
        
        if v.estado not in X:
            X.add(v.estado)
            nos_expandidos += 1
            for nodo in expande(v):
                if nodo not in X:
                    F.append(nodo)
    return None#, nos_expandidos
    

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
    #F é uma pilha!

    X = set()
    F = []
    F.append(Nodo(estado, None, None, 0))
    nos_expandidos = 0

    while F:
        v = F.pop()
        if v.estado == OBJECTIVE:
            sequencia = []
            nodo = v
            while nodo is not None:
                if nodo.acao is not None:
                    sequencia.insert(0, nodo.acao)
                nodo = nodo.pai
            return sequencia#, nos_expandidos
        
        if v.estado not in X:
            X.add(v.estado)
            nos_expandidos += 1
            for nodo in expande(v):
                if nodo not in X:
                    F.append(nodo)
    

    return None#, nos_expandidos


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
   
    X = set()
    F = []
    heappush(F, (0, Nodo(estado, None, None, 0)))
    nos_expandidos = 0

    new_heuristic = lambda x, y: manhattan_distance(x, y) + hamming_distance(x, y)

    while F:
        _, v = heappop(F)
        if v.estado == OBJECTIVE:
            sequencia = []
            nodo = v
            while nodo is not None:
                if nodo.acao is not None:
                    sequencia.insert(0, nodo.acao)
                nodo = nodo.pai
            return sequencia#, nos_expandidos
        
        if v.estado not in X:
            X.add(v.estado)
            nos_expandidos += 1
            for nodo in expande(v):
                if nodo not in X:
                    heappush(F, (nodo.custo + new_heuristic(nodo.estado, OBJECTIVE), nodo))
   
    return None#, nos_expandidos

    raise NotImplementedError
