from graphviz import Digraph

# Define el autómata
afd = {
    'q0': {'0': {'q1'}, '1': {'q2'}},
    'q1': {'0': {'q1'}, '1': {'q3'}},
    'q2': {'0': {'q4'}, '1': {'q2'}},
    'q3': {'0': {'q1'}, '1': {'q2'}},
    'q4': {'0': {'q4'}, '1': {'q3'}}
}

estado_inicial = 'q0'
estados_finales = {'q3', 'q4'}

# Crea un objeto Digraph
dot = Digraph()

# Agrega los estados y transiciones al objeto Digraph
for estado, transiciones in afd.items():
    if estado in estados_finales:
        dot.node(estado, shape='doublecircle')
    else:
        dot.node(estado)

    for simbolo, estados_siguientes in transiciones.items():
        for siguiente_estado in estados_siguientes:
            dot.edge(estado, siguiente_estado, label=simbolo)

# Agrega la flecha entrante al estado inicial y lo hace invisible
dot.edge('', estado_inicial, arrowhead='vee', style='solid', color='black', headport='e', tailport='n', dir='forward', constraint='false')
dot.node('', shape='point', style='invis', width='0', height='0')

# Guarda el grafo en un archivo
dot.render('ejemplos/automata_afd', format='png', cleanup=True)

# Opcionalmente, muestra el grafo en una ventana emergente
# dot.view()
