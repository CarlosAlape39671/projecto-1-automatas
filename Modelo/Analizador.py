class Analizador:

    def analizar_expresion(self, expresion: str):
        # Limpiar la expresión regular
        expresion_limpia = expresion.replace(' ', '')

        # Validar si la expresión regular es válida
        if not self.validar_expresion(expresion_limpia):
            return False
        return True

    def validar_expresion(self, expresion: str) -> bool:
        # Verificar si la expresión regular es válida
        # Esto es una implementación básica y puede necesitar ajustes según los requisitos exactos
        
        # ()
        # | es el o
        # * es el cero o mas
        # + es el uno o mas
        # a, b, c es lenguaje
        
        for caracter in expresion:
            if caracter in ['(', ')', '|', '*', '+']:
                if expresion.index(caracter)+1 <= len(expresion)-1:    
                    if caracter == '|':
                        if expresion.index(caracter) == 0:
                            return False
                        if expresion[expresion.index(caracter)+1] == ')':
                            return False
                    if caracter == '(':
                        if expresion[expresion.index(caracter)+1] == ')':
                            return False
                    if caracter == '*':
                        if expresion[expresion.index(caracter)+1] == '+':
                            return False
                        if expresion[expresion.index(caracter)+1] == '*':
                            return False
                    if caracter == '+':   
                        if expresion[expresion.index(caracter)+1] == '*':
                            return False
                        if expresion[expresion.index(caracter)+1] == '+':
                            return False
                else:
                    if caracter == '|':
                        return False
        
        parentesis_abiertos = 0
        parentesis_cerrados = 0
        for caracter in expresion:
            if caracter == '(':
                parentesis_abiertos += 1
            if caracter == ')':
                parentesis_cerrados += 1
        
        if parentesis_abiertos != parentesis_cerrados:
            return False
        
        return True