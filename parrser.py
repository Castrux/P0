import lexer
import productionRules

prodRules = productionRules.productionRules
tokens = lexer.generateTokens("programaPrueba.txt")

def parser():
    pos = 0
    result = False
    match = False

    while True:
        token = tokens[pos]
        type = token.type
        rules = prodRules.get(type)

        if isinstance(rules, str):
            continue
        
        for rule in rules:
            lenRule = len(rule)
            fromPos = pos + 1
            untilPos = fromPos + lenRule
            nextTokens = tokens[fromPos:untilPos]
            nextTypes = [t.type for t in nextTokens]
            
            if nextTypes == rule:
                match = True
                pos += lenRule
                break
            
        if match == False:
            result = False
            break
        else:
            result = True
            match = False
            pos += 1

        if pos >= len(tokens):
            break

    if result:
        print("La cadena es correcta sintacticamente")
    else:
        print(f"Fallo en la linea {token.lineno} caracter {token.lexpos}")

parser()