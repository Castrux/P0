import lexer
import productionRules

prodRules = productionRules.productionRules
validParams = [productionRules.ID, productionRules.NUMBER]
validStatements = [
    productionRules.JUMP,
    productionRules.WALK,
    productionRules.LEAP,
    productionRules.TURN,
    productionRules.TURNTO,
    productionRules.DROP,
    productionRules.GET,
    productionRules.GRAB,
    productionRules.LETGO,
    productionRules.NOP,
    productionRules.IF,
    productionRules.WHILE,
    productionRules.REPEAT
]
controlStatements = [
    productionRules.WHILE,
    productionRules.IF,
]
functions = {}
variables = {}
arguments = {}

def ruleMatch(listTokens, rule):
    if listTokens == rule:
        return True
    if productionRules.END in rule and len(listTokens) == 0:
        return True
    return False

def checkListIDs(tokens, fromPos, rule):
    newNextTokens = []
    posibleArgsList = False
    procToken = None
    argsTokens = []
    argsList = []
    argsListIndex = []

    for tokenIndex in range(fromPos, len(tokens)):
        tks = tokens[tokenIndex]
        token = tokens[tokenIndex].type
        
        if token == productionRules.LPARENT:
            procToken = tokens[tokenIndex-1]
            posibleArgsList = True

        elif token == productionRules.RPARENT:
            break

        elif token == productionRules.COMMA:
            try:
                tokenBefore = tokens[tokenIndex-1].type
                tokenAfter = tokens[tokenIndex+1].type
            except:
                raise Exception("ilegal quantity of arguments/parameters")
            
            if tokenBefore not in validParams and tokenAfter not in validParams:
                raise Exception("ilegal value aguments/params")
            
        elif token == productionRules.ID and posibleArgsList:
            argsList.append(token)
            argsTokens.append(tks)
            argsListIndex.append(tokenIndex)
    
    if len(argsList) > 1:
        for tokenIndex in range(fromPos, len(tokens)):
            if len(newNextTokens) < len(rule):
                if tokenIndex == argsListIndex[0]:
                    newNextTokens.append(productionRules.LIST_ID)
                elif argsListIndex[0] < tokenIndex <= argsListIndex[len(argsListIndex)-1]:
                    pass
                else:
                    newNextTokens.append(tokens[tokenIndex].type)

    arguments[procToken.value] = { "args": {}, "proc": procToken }
    for token in argsTokens:
        arguments[procToken.value]["args"][token.value] = token

    return newNextTokens

def checkListStatements(tokens, fromPos, rule):
    newNextTokens = []
    statementsList = []
    statementsListParsed = []
    statementsListIndex = []
    command = []

    for tokenIndex in range(fromPos, len(tokens)):
        token = tokens[tokenIndex]
        tokenType = tokens[tokenIndex].type

        command.append(token)
        statementsListIndex.append(tokenIndex)

        if tokenType == productionRules.ID:
            if token.value in variables or token.value in functions:
                pass
            elif token.value not in arguments.keys():
                for proc,data in arguments.items():
                    args = data["args"].keys()
                    if token.value not in args:
                        raise Exception(f"identificador no existente linea {token.lineno} caracter {token.value}")
            

        if tokenType == productionRules.SEMMICOLON:
            statementsList.append(command)
            command = []
        
        if tokenType ==  productionRules.RBRACKED:
            statementsList.append(command)
            command = []
            break

    for statement in statementsList:
        result, message = parser(statement)
        if result:
            statementsListParsed.append(statement)
        else:
            raise Exception(message)
        
    if len(statementsListParsed) > 0:
        for tokenIndex in range(fromPos, len(tokens)):
            if len(newNextTokens) < len(rule):
                if tokenIndex == statementsListIndex[0]:
                    newNextTokens.append(productionRules.LIST_STATEMENTS)
                elif statementsListIndex[0] < tokenIndex <= statementsListIndex[len(statementsListIndex)-1]:
                    pass
                else:
                    newNextTokens.append(tokens[tokenIndex].type)
    
    return newNextTokens
        
def processFuncsAndVariables(tokens, token, pos):
    if token.type == productionRules.DEFVAR:
        tokenID = tokens[pos]
        if tokenID.type == productionRules.ID:
            variables[tokenID.value] = tokenID
        else:
            raise Exception(f"defincion de variable incorrecta {token.lineno} caracter {token.value}")
    elif token.type == productionRules.DEFPROC:
        tokenID = tokens[pos]
        if tokenID.type == productionRules.ID:
            functions[tokenID.value] = tokenID
        else:
            raise Exception(f"definicion de proc incorrecto {token.lineno} caracter {token.value}")
    elif token.type == productionRules.ID:
        if token.value not in [variables.keys(), functions.keys(), arguments.keys()]:
            raise Exception(f"argumento ilegal {token.lineno} var {token.value}")

def parser(tokens):
    pos = 0
    result = False
    match = False

    while True:
        token = tokens[pos]
        type = token.type
        rules = prodRules.get(type)

        if isinstance(rules, str):
            pos += 1
            if pos >= len(tokens):
                match = True
                result = True
                break
            continue

        for rule in rules:
            lenRule = len(rule)
            fromPos = pos + 1
            untilPos = fromPos + lenRule
            nextTokens = [t.type for t in tokens[fromPos:untilPos]]

            processFuncsAndVariables(tokens, token, fromPos)

            if productionRules.LIST_ID in rule:
                nextTokens = checkListIDs(tokens, fromPos, rule)

            if productionRules.LIST_STATEMENTS in rule:
                nextTokens = checkListStatements(tokens, fromPos, rule)

            if ruleMatch(nextTokens, rule):
                match = True
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
        message = "La cadena es correcta sintacticamente"
    else:
        message = f"Fallo en la linea {token.lineno} cerca de {token.value}"

    return (result, message)


tokens = lexer.generateTokens("programaValido.txt")
try:
    print(parser(tokens)[1])
except Exception as e:
    print(str(e))