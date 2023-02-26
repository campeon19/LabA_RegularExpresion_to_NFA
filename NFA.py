from graphviz import Digraph
EPSILON = 'ε'
CONCAT = "."
UNION = "|"
STAR = "*"
QUESTION = "?"
PLUS = "+"


class Simbolo:
    def __init__(self, simbolo):
        self.c_id = simbolo
        self.id = ord(simbolo)


class Trancision:
    def __init__(self, simbolo, estado):
        self.simbolo = simbolo
        self.estado = estado


class Estado:
    def __init__(self, id, es_final=False):
        self.id = id
        self.es_final = es_final
        self.trancisiones = {}

    def agregar_trancision(self, simbolo, estado):
        if simbolo in self.trancisiones:
            self.trancisiones[simbolo].append(estado)
        else:
            self.trancisiones[simbolo] = [estado]

    def get_trancisiones(self, simbolo):
        if simbolo in self.trancisiones:
            return self.trancisiones[simbolo]
        else:
            return []

    def borra_trancision(self, simbolo):
        if simbolo in self.trancisiones:
            del self.trancisiones[simbolo]


class AFN:
    def __init__(self, estado_inicial, estado_final):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

    def __repr__(self):
        return f"AFN({self.estado_inicial}, {self.estado_final})"

    def get_estados(self):
        estados = set()
        self._get_estados(self.estado_inicial, estados)
        return estados

    def _get_estados(self, estado, estados):
        if estado in estados:
            return
        estados.add(estado)
        for simbolo in estado.trancisiones:
            for next_estado in estado.get_trancisiones(simbolo):
                self._get_estados(next_estado, estados)

    def print_afn(self):
        dot = Digraph()
        dot.attr('node', shape='doublecircle')
        dot.node(str(self.estado_final.id))
        dot.attr('node', shape='circle')
        dot.node('start', style='invis')
        dot.edge('start', str(self.estado_inicial.id))
        for estado in self.get_estados():
            for simbolo in estado.trancisiones:
                for next_estado in estado.get_trancisiones(simbolo):
                    dot.edge(str(estado.id), str(
                        next_estado.id), label=str(simbolo))
        dot.format = 'png'
        return dot


def postfix_to_afn(postfix):
    stack = []
    id = 0
    for simbolo in postfix:
        if simbolo == CONCAT:
            afn2 = stack.pop()
            afn1 = stack.pop()
            afn1.estado_final.es_final = False
            af2SegundoEstado = afn2.estado_inicial
            afn1.estado_final.agregar_trancision(
                afn2.estado_inicial.trancisiones, afn2.estado_inicial)

        elif simbolo == UNION:
            afn2 = stack.pop()
            afn1 = stack.pop()
            estado_inicial = Estado(id)
            id += 1
            estado_final = Estado(id)
            id += 1
            estado_inicial.agregar_trancision(EPSILON, afn1.estado_inicial)
            estado_inicial.agregar_trancision(EPSILON, afn2.estado_inicial)
            afn1.estado_final.es_final = False
            afn1.estado_final.agregar_trancision(EPSILON, estado_final)
            afn2.estado_final.es_final = False
            afn2.estado_final.agregar_trancision(EPSILON, estado_final)
            stack.append(AFN(estado_inicial, estado_final))
        elif simbolo == STAR:
            afn = stack.pop()
            estado_inicial = Estado(id)
            id += 1
            estado_final = Estado(id)
            id += 1
            estado_inicial.agregar_trancision(EPSILON, afn.estado_inicial)
            estado_inicial.agregar_trancision(EPSILON, estado_final)
            afn.estado_final.es_final = False
            afn.estado_final.agregar_trancision(EPSILON, afn.estado_inicial)
            afn.estado_final.agregar_trancision(EPSILON, estado_final)
            stack.append(AFN(estado_inicial, estado_final))
        elif simbolo == QUESTION:
            afn = stack.pop()
            estado_inicial = Estado(id)
            id += 1
            estado_final = Estado(id)
            id += 1
            estado_inicial.agregar_trancision(EPSILON, afn.estado_inicial)
            estado_inicial.agregar_trancision(EPSILON, estado_final)
            afn.estado_final.es_final = False
            afn.estado_final.agregar_trancision(EPSILON, estado_final)
            stack.append(AFN(estado_inicial, estado_final))
        elif simbolo == PLUS:
            afn = stack.pop()
            estado_inicial = Estado(id)
            id += 1
            estado_final = Estado(id)
            id += 1
            estado_inicial.agregar_trancision(EPSILON, afn.estado_inicial)
            afn.estado_final.es_final = False
            afn.estado_final.agregar_trancision(EPSILON, afn.estado_inicial)
            afn.estado_final.agregar_trancision(EPSILON, estado_final)
            stack.append(AFN(estado_inicial, estado_final))
        else:
            estado_inicial = Estado(id)
            id += 1
            estado_final = Estado(id, True)
            id += 1
            estado_inicial.agregar_trancision(simbolo, estado_final)
            stack.append(AFN(estado_inicial, estado_final))
    return stack.pop()


postfix = "ab|*a.b.b."
afn = postfix_to_afn(postfix)
dot = afn.print_afn()
dot.render('afn', view=True)
