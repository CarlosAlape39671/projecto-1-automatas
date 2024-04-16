from graphviz import Digraph
import os
class Vista:
    def __init__(self):
        pass

    def mostrar_menu(self):
        print("Bienvenido al Conversor de Expresiones Regulares a Autómatas")
        print("Seleccione una opción:")
        print("1. Ingresar una expresión regular")
        print("4. Salir")
        
    def leer_opcion(self):
        return input("Ingrese el número de la opción deseada: ")

    def obtener_expresion_regular(self):
        return input("Ingrese la expresión regular: ")
    
    def mostrar_resultado_analisar_expresion(self, resultado):
        if resultado:
            print("Expresión regular analizada correctamente.")
        else:
            print("Error al analizar la expresión regular.")

    def mostrar_menu_para_expresion(self):
        print("2. Mostrar diagrama AFD")
        print("3. Mostrar diagrama AFND")

    def mostrar_saliendo_programa(self):
        print("Saliendo del programa...")
        
    def mostrar_opcion_no_valida(self):
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
    def leer_nombre_archivo(self):
        return input("Ingrese el nombre del archivo para el automata: ")

    def mostrar_automata(self, automata, estados_finales, estado_inicial, nombre_archivo_automata):
        # Crea un objeto Digraph
        dot = Digraph()

        # Agrega los estados y transiciones al objeto Digraph
        for estado, transiciones in automata.items():
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
        dot.render(f'ejemplos/{nombre_archivo_automata}', format='png', cleanup=True)

        # Opcionalmente, muestra el grafo en una ventana emergente
        # dot.view()

