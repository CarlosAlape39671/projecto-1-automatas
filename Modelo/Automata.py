
from graphviz import Digraph

class Automata:
    def __init__(self):
        self.estados = []
        self.alfabeto = []
        self.transiciones = {}
        self.estado_inicial = ''
        self.estados_finales = []