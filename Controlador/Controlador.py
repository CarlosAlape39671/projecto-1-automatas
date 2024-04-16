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
        estado_inicial = self.estado_inicial()
        alfabeto = self.alfabeto()
        # transiciones = self.crear_transiciones()
        subexpresiones = self.dividir_expresion(self.expresion_regular)
        afd2 = self.generar_afd(subexpresiones)
        self.mostrar_grafica_automata(afd2)
        
        # print(subexpresiones)
        # self.establecer_estado_inicial(estado_inicial)
        # self.establecer_alfabeto(alfabeto)
        # self.establecer_transiciones(transiciones)
        # print(transiciones)
        # self.mostrar_grafica_automata()

    def procesar_expresion_regular(self):
        return self.analizador.analizar_expresion(self.expresion_regular)
    
    def estado_inicial(self):
        estado_inicial = 'q0'
        self.establecer_estado(estado_inicial)
        return estado_inicial
    
    def establecer_estado_inicial(self, estado_inicial):
        self.automata.set_estado_inicial(estado_inicial)
        
    def alfabeto(self):
        alfabeto = []
        for caracter in self.expresion_regular:
            if caracter not in ['(', ')', '|', '*', '+']:
                alfabeto.append(caracter)
                
    def establecer_alfabeto(self, alfabeto):
        self.automata.set_alfabeto(alfabeto)
        
    def generar_afd(self, subexpresiones):
        afd2 = {}
        estado = "q"
        numero = 0
        for expresion in subexpresiones:
            estado1 = estado + str(numero)
            estado2 = estado + str(numero+1)
            if "*" in expresion and "|" in expresion:
                expresion_sin_asterisco = expresion.strip("*")
                expresion_sin_parentesis = expresion_sin_asterisco.strip("()")
                print(f"Estado {estado1} va con {expresion_sin_parentesis} hacia {estado2}")
                print(f"Estado {estado2} va con {expresion_sin_parentesis} hacia {estado2}")
                opciones = self.obtener_caracteres(expresion)
                print(f"Estado {estado1} va con {opciones[0]} hacia {estado2}")
                print(f"Estado {estado1} va con {opciones[1]} hacia {estado2}")
                afd2[estado1] = {opciones[0]: estado2, opciones[1]: estado2}
                afd2[estado1] = {expresion_sin_parentesis: estado2}
                afd2[estado2] = {expresion_sin_parentesis: estado2}
            elif "|" in expresion:
                opciones = self.obtener_caracteres(expresion)
                if (afd2[estado1]) != None:  # Verifica si el estado ya existe en afd2
                    clav = ""
                    val = ""
                    transiciones = afd2[estado1].copy()  # Crea una copia de las transiciones existentes
                    print(f"copia: {transiciones}")
                    for clave, valor in transiciones.items():
                        clav = clave
                        val = valor
                    afd2[estado1] = {opciones[0]: estado2, opciones[1]: estado2, clav:val}  # Actualiza afd2 con las transiciones combinadas
                else:
                    afd2[estado1] = {opciones[0]: estado2, opciones[1]: estado2}  # Si no existe, crea las transiciones directamente
                print(f"Estado {estado1} va con {opciones[0]} hacia {estado2}")
                print(f"Estado {estado1} va con {opciones[1]} hacia {estado2}")
                #afd2[estado1] = {opciones[0]: estado2, opciones[1]: estado2}
            elif "*" in expresion:
                expresion_sin_asterisco = expresion.strip("*")
                expresion_sin_parentesis = expresion_sin_asterisco.strip("()")
                print(f"Estado {estado1} va con {expresion_sin_parentesis} hacia {estado2}")
                print(f"Estado {estado2} va con {expresion_sin_parentesis} hacia {estado2}")
                afd2[estado1] = {expresion_sin_parentesis: estado2}    
                afd2[estado2] = {expresion_sin_parentesis: estado2}
            elif "*" not in expresion:
                expresion_sin_parentesis = expresion.strip("()")
                print(f"Estado {estado1} va con {expresion_sin_parentesis} hacia {estado2}")
                afd2[estado1] = {expresion_sin_parentesis: estado2}
            estado_final = estado1
            
            
            numero += 1
            estado = "q"
        return afd2
    
    def obtener_caracteres(self, expresion):
        # Busca todos los caracteres entre paréntesis
        caracteres_entre_parentesis = re.findall(r'\((.*?)\)', expresion)
        
        # Divide los caracteres y los une en una sola lista
        caracteres = ''.join(caracteres_entre_parentesis).split('|')
        
        return caracteres
        
    def dividir_expresion(self, expresion):
        subexpresiones = []
        subexpresion_actual = ''
        nivel = 0

        for char in expresion:
            if char == '(':
                nivel += 1
                subexpresion_actual += char
            elif char == ')':
                nivel -= 1
                subexpresion_actual += char
                if nivel == 0:
                    subexpresiones.append(subexpresion_actual)
                    subexpresion_actual = ''
            elif char == '*' and nivel == 0:
                subexpresiones[-1] += char
            else:
                subexpresion_actual += char

        return subexpresiones

    # def obtener_caracteres(expresion):
    #     subexpresiones = self.dividir_expresion(expresion)
    #     print(subexpresiones)
    
    def crear_nuevo_estado(self):
        nuevo_estado = 'q' + str(len(self.automata.estados))
        self.establecer_estado(nuevo_estado)
        return nuevo_estado

    def establecer_estado(self, estado):
        self.automata.estados.append(estado)
        
    def establecer_transiciones(self, transiciones):
        self.automata.set_transiciones(transiciones)
        
    def mostrar_grafica_automata(self, afd2):
        self.vista.mostrar_automata(afd2)
        # self.vista.mostrar_automata(self.automata.afd, self.automata.estados_finales, self.automata.estado_inicial, self.vista.leer_nombre_archivo())