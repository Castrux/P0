# NON TERMINALES
ASSIGN          = "ASSIGN"
LPARENT         = "LPARENT"
RPARENT         = "RPARENT"
LBRACKED        = "LBRACKED"
RBRACKED        = "RBRACKED"
COMMA           = "COMMA"
SEMMICOLON      = "SEMMICOLON"
ID              = "ID"
NUMBER          = "NUMBER"
DEFVAR          = "DEFVAR"
DEFPROC         = "DEFPROC"
DEFVAR          = "DEFVAR"
DEFPROC         = "DEFPROC"
JUMP            = "JUMP"
WALK            = "WALK"
LEAP            = "LEAP"
TURN            = "TURN"
TURNTO          = "TURNTO"
DROP            = "DROP"
GET             = "GET"
GRAB            = "GRAB"
LETGO           = "LETGO"
NOP             = "NOP"
FACING          = "FACING"
CAN             = "CAN"
NOT             = "NOT"
NORTH           = "NORTH"
SOUTH           = "SOUTH"
WEST            = "WEST"
EAST            = "EAST"
FRONT           = "FRONT"
BACK            = "BACK"
RIGHT           = "RIGHT"
LEFT            = "LEFT"
CHIPS           = "CHIPS"
BALLONS         = "BALLONS"
IF              = "IF"
ELSE            = "ELSE"
WHILE           = "WHILE"
REPEAT          = "REPEAT"
TIMES           = "TIMES"
BLOCK           = "BLOCK"
PARAMS          = "PARAMS"
LIST_PARAMS     = "LIST_PARAMS"
PARAM           = "PARAM"
COMMA_PARAM     = "COMMA_PARAM"
VARIABLE        = "VARIABLE"
STATEMENT       = "STATEMENT"
GROUP_STATEMENT = "GROUP_STATEMENT"
NEXT_STATEMENT  = "NEXT_STATEMENT"
PROCEDURE       = "PROCEDURE"
COMMAND         = "COMMAND"
CONTROL         = "CONTROL"
ITERATOR        = "ITERATOR"
CONDITION       = "CONDITION"
LIST_ID         = "LIST_ID"
LIST_STATEMENTS = "LIST_STATEMENTS"

# PRODUCTION RULES
# CONVENTIONS

productionRules = {
    NORTH           : "NORTH",
    SOUTH           : "SOUTH",
    WEST            : "WEST",
    EAST            : "EAST",
    FRONT           : "FRONT",
    BACK            : "BACK",
    RIGHT           : "RIGHT",
    LEFT            : "LEFT",
    CHIPS           : "CHIPS",
    BALLONS         : "BALLONS",
    SEMMICOLON      : ";",
    NUMBER          : "",
    LIST_ID         : "",
    ID              : "",
    COMMA           : "",
    LPARENT         : "",
    RPARENT         : "",
    LIST_STATEMENTS : "",
    RBRACKED        : [
                        [""],
                        [DEFPROC],
                        [LBRACKED],
                      ],
    LBRACKED        : [
                        [RBRACKED],
                        [LBRACKED],
                        [JUMP, RBRACKED],
                        [WALK, RBRACKED],
                        [LEAP, RBRACKED],
                        [TURN, RBRACKED],
                        [TURNTO, RBRACKED],
                        [DROP, RBRACKED],
                        [GET, RBRACKED],
                        [LETGO, RBRACKED],
                        [NOP, RBRACKED],
                        [CAN, RBRACKED],
                        [FACING, RBRACKED],
                        [NOT, RBRACKED],
                        [LIST_STATEMENTS, RBRACKED],
                      ],
    ELSE            : [
                        [LBRACKED],
                      ],
    IF              : [
                        [CAN, LBRACKED, ELSE],
                        [FACING, LBRACKED, ELSE],
                        [NOT, LBRACKED, ELSE],
                      ],
    WHILE           : [
                        [CAN, LBRACKED],
                        [FACING, LBRACKED],
                        [NOT, LBRACKED],
                      ],
    REPEAT          : [
                        [CAN, LBRACKED, ELSE],
                        [FACING, LBRACKED, ELSE],
                        [NOT, LBRACKED, ELSE],
                      ],
    TIMES           : [
                        [LBRACKED],
                      ],
    ASSIGN          : [
                        [NUMBER, SEMMICOLON, TIMES],
                        [ID, RBRACKED, TIMES]
                      ],
    DEFVAR          : [
                        [ID, NUMBER],
                      ],
    DEFPROC         : [
                        [ID, LPARENT, RPARENT],
                        [ID, LPARENT, ID, RPARENT],
                        [ID, LPARENT, LIST_ID, RPARENT],
                      ],
    JUMP            : [
                        [LPARENT, NUMBER, NUMBER, RPARENT], 
                        [LPARENT, ID, ID, RPARENT],
                      ],
    WALK            : [
                        [LPARENT, NUMBER, RPARENT], 
                        [LPARENT, NUMBER, NORTH, RPARENT],
                        [LPARENT, NUMBER, SOUTH, RPARENT],
                        [LPARENT, NUMBER, WEST, RPARENT],
                        [LPARENT, NUMBER, EAST, RPARENT],
                        [LPARENT, NUMBER, FRONT, RPARENT],
                        [LPARENT, NUMBER, LEFT, RPARENT],
                        [LPARENT, NUMBER, RIGHT, RPARENT],
                        [LPARENT, NUMBER, BACK, RPARENT],
                      ],
    LEAP            : [
                        [LPARENT, NUMBER, RPARENT], 
                        [LPARENT, NUMBER, NORTH, RPARENT],
                        [LPARENT, NUMBER, SOUTH, RPARENT],
                        [LPARENT, NUMBER, WEST, RPARENT],
                        [LPARENT, NUMBER, EAST, RPARENT],
                        [LPARENT, NUMBER, FRONT, RPARENT],
                        [LPARENT, NUMBER, LEFT, RPARENT],
                        [LPARENT, NUMBER, RIGHT, RPARENT],
                        [LPARENT, NUMBER, BACK, RPARENT],
                      ],
    TURN            : [
                        [LPARENT, FRONT, RPARENT],
                        [LPARENT, LEFT, RPARENT],
                        [LPARENT, RIGHT, RPARENT],
                        [LPARENT, BACK, RPARENT],
                      ],
    TURNTO          : [
                        [LPARENT, NORTH, RPARENT],
                        [LPARENT, SOUTH, RPARENT],
                        [LPARENT, WEST, RPARENT],
                        [LPARENT, EAST, RPARENT],
                      ],
    DROP            : [
                        [LPARENT, NUMBER, RPARENT]
                      ],
    GET             : [
                        [LPARENT, NUMBER, RPARENT]
                      ],
    GRAB            : [
                        [LPARENT, NUMBER, RPARENT]
                      ],
    LETGO           : [
                        [LPARENT, NUMBER, RPARENT]
                      ],
    NOP             : [
                        [LPARENT, RPARENT]
                      ],
    CAN             : [
                        [LPARENT, JUMP, RPARENT],
                        [LPARENT, WALK, RPARENT],
                        [LPARENT, LEAP, RPARENT],
                        [LPARENT, TURN, RPARENT],
                        [LPARENT, TURNTO, RPARENT],
                        [LPARENT, DROP, RPARENT],
                        [LPARENT, GET, RPARENT],
                        [LPARENT, GRAB, RPARENT],
                        [LPARENT, LETGO, RPARENT],
                        [LPARENT, NOP, RPARENT],
                      ],
    FACING          : [
                        [LPARENT, NORTH, RPARENT],
                        [LPARENT, SOUTH, RPARENT],
                        [LPARENT, WEST, RPARENT],
                        [LPARENT, EAST, RPARENT],
                      ],
    NOT             : [
                        [CAN]
                      ],
}