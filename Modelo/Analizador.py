class Analizador:

    def analizar_expresion(self, expresion: str) -> bool:
        # Limpiar la expresión regular
        expresion_limpia = expresion.replace(' ', '')
        return self.validar_expresion(expresion_limpia)

    def validar_expresion(self, expresion: str) -> bool:
        # ()
        # | es el o
        # * es el cero o mas
        # + es el uno o mas
        # a, b, c es lenguaje
        
        for caracter in expresion:
            if caracter in ['(', ')', '|', '*', '+']:
                if expresion.index(caracter)+1 <= len(expresion)-1:    
                    if caracter == '|':
                        if expresion[0] == '|' == 0 or expresion[-1] == '|':
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