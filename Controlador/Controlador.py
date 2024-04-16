import re
from Vista.Vista import Vista
from Modelo.Analizador import Analizador
from Modelo.Automata import Automata
class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.analizador = Analizador()
        self.automata = None
        self.expresion_regular = ''

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.leer_opcion()

            if opcion == '1':
                self.automata = Automata()
                self.expresion_regular = self.vista.obtener_expresion_regular()
                respuesta = self.procesar_expresion_regular()
                self.vista.mostrar_resultado_analisar_expresion(respuesta)
                if respuesta:
                    self.vista.mostrar_menu_para_expresion()
                    opcion = self.vista.leer_opcion()
                    if opcion == '2':
                        self.generar_afd()
            elif opcion == '4':
                self.vista.mostrar_saliendo_programa()
                break
            else:
                self.vista.mostrar_opcion_no_valida()
    
    def generar_afd(self):
        self.automata.estado_inicial = self.estado_inicial()
        # self.automata.set_estados_finales(self.automata.estados[-1])
        self.automata.alfabeto = self.alfabeto()
    
    # def generar_transiciones(self):
    #     for i in range(len(self.expresion_regular)):
    #         if self.expresion_regular[i] == '(':

    def procesar_expresion_regular(self):
        return self.analizador.analizar_expresion(self.expresion_regular)
    
    def estado_inicial(self):
        estado_inicial = 'q0'
        return estado_inicial
        
    def alfabeto(self):
        alfabeto = []
        for caracter in self.expresion_regular:
            if caracter not in ['(', ')', '|', '*', '+'] and caracter not in alfabeto:
                alfabeto.append(caracter)
        return alfabeto
    
    def crear_nuevo_estado(self):
        nuevo_estado = 'q' + str(len(self.automata.estados))
        self.establecer_estado(nuevo_estado)
        return nuevo_estado

    def establecer_estado(self, estado):
        self.automata.estados.append(estado)
        
    def mostrar_grafica_automata(self, afd2):
        self.vista.mostrar_automata(afd2)
        # self.vista.mostrar_automata(self.automata.afd, self.automata.estados_finales, self.automata.estado_inicial, self.vista.leer_nombre_archivo())