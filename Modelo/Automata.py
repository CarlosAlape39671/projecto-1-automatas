
from graphviz import Digraph

class Automata:
    def __init__(self):
        self.estados = []
        self.alfabeto = []
        self.transiciones = {}
        self.estado_inicial = ''
        self.estados_finales = []
        
    def get_estados(self):
        return self.estados
    
    def get_alfabeto(self):
        return self.alfabeto
    
    def get_transiciones(self):
        return self.transiciones
    
    def get_estado_inicial(self):
        return self.estado_inicial
    
    def get_estados_finales(self):
        return self.estados_finales
    
    def set_estados(self, estados):
        self.estados = estados
        
    def set_alfabeto(self, alfabeto):
        self.alfabeto = alfabeto
    
    def set_transiciones(self, transiciones):
        self.transiciones = transiciones
        
    def set_estado_inicial(self, estado_inicial):
        self.estado_inicial = estado_inicial
    
    def set_estados_finales(self, estados_finales):
        self.estados_finales = estados_finales
        
    def graficar(self):
        dot = Digraph(comment='Grafo')
        # Crea un objeto Digraph
        dot = Digraph()

        # Agrega los estados y transiciones al objeto Digraph
        for estado, transiciones in self.afd.items():
            if estado in self.estados_finales:
                dot.node(estado, shape='doublecircle')
            else:
                dot.node(estado)

            for simbolo, siguiente_estado in transiciones.items():
                dot.edge(estado, siguiente_estado, label=simbolo)

        # Agrega la flecha entrante al estado inicial y lo hace invisible
        dot.edge('', self.estado_inicial, arrowhead='vee', style='solid', color='black', headport='e', tailport='n', dir='forward', constraint='false')
        dot.node('', shape='point', style='invis', width='0', height='0')

        # Guarda el grafo en un archivo
        dot.render('automata_afd', format='png', cleanup=True)

        # Opcionalmente, muestra el grafo en una ventana emergente
        # dot.view()
        
    def relacionar_estado(self, estado, caracter, nuevo_estado):
        if estado in self.transiciones:
            if caracter in self.transiciones[estado]:
                self.transiciones[estado][caracter].add(nuevo_estado)
            else:
                self.transiciones[estado][caracter] = {nuevo_estado}
        else:
            self.transiciones[estado] = {caracter: {nuevo_estado}}
