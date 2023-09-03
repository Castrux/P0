import ply.ply.lex as lex
import re
import codecs
import os
import sys


tokens = [
    "ASSIGN",
    "LPARENT",
    "RPARENT",
    "LBRACKED",
    "RBRACKED",
    "COMMA",
    "SEMMICOLON",
    "ID",
    "NUMBER",
]

reserved = {
    "defvar": "DEFVAR",
    "defproc": "DEFPROC",
    "jump": "JUMP",
    "walk": "WALK",
    "leap": "LEAP",
    "turn": "TURN",
    "turnto": "TURNTO",
    "drop": "DROP",
    "get": "GET",
    "grab": "GRAB",
    "letgo": "LETGO",
    "nop": "NOP",
    "facing": "FACING",
    "can": "CAN",
    "not": "NOT",
    "north": "NORTH",
    "south": "SOUTH",
    "west": "WEST",
    "east": "EAST",
    "front": "FRONT",
    "back": "BACK",
    "right": "RIGHT",
    "left": "LEFT",
    "chips": "CHIPS",
    "ballons": "BALLONS",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "repeat": "REPEAT",
    "times": "TIMES",
}

tokens = tokens + list(reserved.values())

t_ignore = r' +'
t_ASSIGN = r'='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKED = r'\{'
t_RBRACKED = r'\}'
t_COMMA = r','
t_SEMMICOLON = r';'

def t_ID(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if token.value.lower() in reserved:
        token.value = token.value.upper()
        token.type = token.value
    return token

def t_NUMBER(token):
    r'\d+'
    token.value = int(token.value)
    return token

def t_newline(token):
    r'\n'
    token.lexer.lineno += len(token.value)

def t_error(token):
    raise Exception(f"caracter ilegal {token.value[0]}")

def generateTokens(pathFile: str):
    fileTest = codecs.open(pathFile, "r", "utf-8")
    contentFileTest = fileTest.read()
    fileTest.close()
    analizer = lex.lex()
    analizer.input(contentFileTest)
    tokens = []
    while True:
        token = analizer.token()
        if not token:
            break
        tokens.append(token)
    return tokens





