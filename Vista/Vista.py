from graphviz import Digraph
import os
class Vista:
    def __init__(self):
        pass

    def mostrar_menu(self):
        # Muestra el menú de opciones
        print("Bienvenido al Conversor de Expresiones Regulares a Autómatas")
        print("Seleccione una opción:")
        print("1. Ingresar una expresión regular")
        print("4. Salir")
        
    def leer_opcion(self):
        # Solicita al usuario ingresar una opción y la devuelve
        return input("Ingrese el número de la opción deseada: ")

    def obtener_expresion_regular(self):
        # Solicita al usuario ingresar una expresión regular y la devuelve
        return input("Ingrese la expresión regular: ")
    
    def mostrar_resultado_analisar_expresion(self, resultado):
        # Muestra el resultado del análisis de la expresión regular
        if resultado:
            print("Expresión regular analizada correctamente.")
        else:
            print("Error al analizar la expresión regular.")

    def mostrar_menu_para_expresion(self):
        # Muestra el menú de opciones
        print("2. Mostrar diagrama AFD")
        print("3. Mostrar diagrama AFND")

    def mostrar_saliendo_programa(self):
        # Muestra un mensaje de salida
        print("Saliendo del programa...")
        
    def mostrar_opcion_no_valida(self):
        # Muestra un mensaje de opción no válida
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
    def leer_nombre_archivo(self):
        # Solicita al usuario ingresar el nombre del archivo
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
        dot.render(f'automatas/{nombre_archivo_automata}', format='png', cleanup=True)

        # Opcionalmente, muestra el grafo en una ventana emergente
        # dot.view()
