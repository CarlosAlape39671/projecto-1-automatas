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
        # a, b, c es lenguaj
        
        for posicion in range(len(expresion)):
            if expresion[posicion] in ['(', ')', '|', '*', '+']:
                if expresion[posicion] == '|':
                    if posicion == 0 or posicion == len(expresion)-1:
                        return False
                    if posicion+1 < len(expresion) and expresion[posicion+1] == ')':
                        return False
                if expresion[posicion] == '(':
                    if posicion+1 < len(expresion) and expresion[posicion+1] == ')':
                        return False
                if expresion[posicion] == '*':
                    if posicion+1 < len(expresion) and expresion[posicion+1] == '+':
                        return False
                    if posicion+1 < len(expresion) and expresion[posicion+1] == '*':
                        return False
                    if posicion == 0 or expresion[posicion-1] != ')':
                        return False
                if expresion[posicion] == '+':
                    if posicion+1 < len(expresion) and expresion[posicion+1] == '*':
                        return False
                    if posicion+1 < len(expresion) and expresion[posicion+1] == '+':
                        return False
                    if posicion == 0 or expresion[posicion-1] != ')':
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