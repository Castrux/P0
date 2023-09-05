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
LIST_ID         = "LIST_ID"
LIST_STATEMENTS = "LIST_STATEMENTS"

# PRODUCTION RULES

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
    SEMMICOLON      : "",
    NUMBER          : "",
    LIST_ID         : "",
    ID              : "",
    COMMA           : "",
    LPARENT         : "",
    RPARENT         : "",
    LIST_STATEMENTS : "",
    CAN             : "",
    FACING          : "",
    NOT             : "",
    RBRACKED        : [
                        [],
                        [DEFPROC],
                        [LBRACKED],
                      ],
    LBRACKED        : [
                        [RBRACKED],
                        [JUMP, RBRACKED],
                        [WALK, RBRACKED],
                        [LEAP, RBRACKED],
                        [TURN, RBRACKED],
                        [TURNTO, RBRACKED],
                        [DROP, RBRACKED],
                        [GET, RBRACKED],
                        [LETGO, RBRACKED],
                        [NOP, RBRACKED],
                        [LIST_STATEMENTS],
                      ],
    ELSE            : [
                        [LBRACKED],
                        [JUMP],
                        [WALK],
                        [LEAP],
                        [TURN],
                        [TURNTO],
                        [DROP],
                        [GET],
                        [LETGO],
                        [NOP],
                      ],
    IF              : [
                        [CAN, LPARENT, JUMP],
                        [CAN, LPARENT, WALK],
                        [CAN, LPARENT, LEAP],
                        [CAN, LPARENT, TURN],
                        [CAN, LPARENT, TURNTO],
                        [CAN, LPARENT, DROP],
                        [CAN, LPARENT, GET],
                        [CAN, LPARENT, GRAB],
                        [CAN, LPARENT, LETGO],
                        [CAN, LPARENT, NOP],
                        [CAN, LPARENT, COMMA],
                        [FACING, LPARENT, NORTH, RPARENT, LBRACKED],
                        [FACING, LPARENT, SOUTH, RPARENT, LBRACKED],
                        [FACING, LPARENT, WEST, RPARENT, LBRACKED],
                        [FACING, LPARENT, EAST, RPARENT, LBRACKED],
                        [NOT, CAN, LPARENT, JUMP],
                        [NOT, CAN, LPARENT, WALK],
                        [NOT, CAN, LPARENT, LEAP],
                        [NOT, CAN, LPARENT, TURN],
                        [NOT, CAN, LPARENT, TURNTO],
                        [NOT, CAN, LPARENT, DROP],
                        [NOT, CAN, LPARENT, GET],
                        [NOT, CAN, LPARENT, GRAB],
                        [NOT, CAN, LPARENT, LETGO],
                        [NOT, CAN, LPARENT, NOP],
                        [NOT, CAN, LPARENT, COMMA],
                        [NOT, FACING, LPARENT, NORTH, RPARENT, LBRACKED],
                        [NOT, FACING, LPARENT, SOUTH, RPARENT, LBRACKED],
                        [NOT, FACING, LPARENT, WEST, RPARENT, LBRACKED],
                        [NOT, FACING, LPARENT, EAST, RPARENT, LBRACKED],
                      ],
    WHILE           : [
                        [CAN, LPARENT, JUMP],
                        [CAN, LPARENT, WALK],
                        [CAN, LPARENT, LEAP],
                        [CAN, LPARENT, TURN],
                        [CAN, LPARENT, TURNTO],
                        [CAN, LPARENT, DROP],
                        [CAN, LPARENT, GET],
                        [CAN, LPARENT, GRAB],
                        [CAN, LPARENT, LETGO],
                        [CAN, LPARENT, NOP],
                        [CAN, LPARENT, COMMA],
                        [FACING, LPARENT, NORTH, RPARENT, LBRACKED],
                        [FACING, LPARENT, SOUTH, RPARENT, LBRACKED],
                        [FACING, LPARENT, WEST, RPARENT, LBRACKED],
                        [FACING, LPARENT, EAST, RPARENT, LBRACKED],
                        [NOT, CAN, LPARENT, JUMP],
                        [NOT, CAN, LPARENT, WALK],
                        [NOT, CAN, LPARENT, LEAP],
                        [NOT, CAN, LPARENT, TURN],
                        [NOT, CAN, LPARENT, TURNTO],
                        [NOT, CAN, LPARENT, DROP],
                        [NOT, CAN, LPARENT, GET],
                        [NOT, CAN, LPARENT, GRAB],
                        [NOT, CAN, LPARENT, LETGO],
                        [NOT, CAN, LPARENT, NOP],
                        [NOT, CAN, LPARENT, COMMA],
                        [NOT, FACING, LPARENT, NORTH, RPARENT, LBRACKED],
                        [NOT, FACING, LPARENT, SOUTH, RPARENT, LBRACKED],
                        [NOT, FACING, LPARENT, WEST, RPARENT, LBRACKED],
                        [NOT, FACING, LPARENT, EAST, RPARENT, LBRACKED],
                      ],
    REPEAT          : [
                        [NUMBER, TIMES],
                      ],
    TIMES           : [
                        [LBRACKED],
                      ],
    ASSIGN          : [
                        [NUMBER, SEMMICOLON],
                        [NUMBER, RBRACKED],
                      ],
    DEFVAR          : [
                        [ID, NUMBER],
                      ],
    DEFPROC         : [
                        [ID, LPARENT, RPARENT, LBRACKED],
                        [ID, LPARENT, ID, RPARENT, LBRACKED],
                        [ID, LPARENT, LIST_ID, RPARENT, LBRACKED],
                      ],
    JUMP            : [
                        [LPARENT, NUMBER, COMMA, NUMBER, RPARENT, SEMMICOLON], 
                        [LPARENT, ID, COMMA, ID, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, NUMBER, RPARENT, RBRACKED], 
                        [LPARENT, ID, COMMA, ID, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, NUMBER, RPARENT, RPARENT, LBRACKED], 
                        [LPARENT, ID, COMMA, ID, RPARENT, RPARENT, LBRACKED],
                      ],
    WALK            : [
                        [LPARENT, NUMBER, RPARENT, SEMMICOLON], 
                        [LPARENT, NUMBER, COMMA, NORTH, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, SOUTH, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, WEST, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, EAST, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, FRONT, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, LEFT, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, RIGHT, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, BACK, RPARENT, SEMMICOLON],
                        [LPARENT, ID, RPARENT, SEMMICOLON], 
                        [LPARENT, ID, COMMA, NORTH, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, SOUTH, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, WEST, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, EAST, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, FRONT, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, LEFT, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, RIGHT, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, BACK, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, RPARENT, RBRACKED], 
                        [LPARENT, NUMBER, COMMA, NORTH, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, SOUTH, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, WEST, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, EAST, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, FRONT, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, LEFT, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, RIGHT, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, BACK, RPARENT, RBRACKED],
                        [LPARENT, ID, RPARENT, RBRACKED], 
                        [LPARENT, ID, COMMA, NORTH, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, SOUTH, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, WEST, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, EAST, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, FRONT, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, LEFT, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, RIGHT, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, BACK, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, RPARENT, RPARENT, LBRACKED], 
                        [LPARENT, NUMBER, COMMA, NORTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, SOUTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, WEST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, EAST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, FRONT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, LEFT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, RIGHT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, BACK, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, RPARENT, RPARENT, LBRACKED], 
                        [LPARENT, ID, COMMA, NORTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, SOUTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, WEST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, EAST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, FRONT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, LEFT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, RIGHT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, BACK, RPARENT, RPARENT, LBRACKED],
                      ],
    LEAP            : [
                        [LPARENT, NUMBER, RPARENT, SEMMICOLON], 
                        [LPARENT, NUMBER, COMMA, NORTH, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, SOUTH, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, WEST, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, EAST, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, FRONT, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, LEFT, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, RIGHT, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, COMMA, BACK, RPARENT, SEMMICOLON],
                        [LPARENT, ID, RPARENT, SEMMICOLON], 
                        [LPARENT, ID, COMMA, NORTH, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, SOUTH, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, WEST, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, EAST, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, FRONT, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, LEFT, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, RIGHT, RPARENT, SEMMICOLON],
                        [LPARENT, ID, COMMA, BACK, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, RPARENT, RBRACKED], 
                        [LPARENT, NUMBER, COMMA, NORTH, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, SOUTH, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, WEST, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, EAST, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, FRONT, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, LEFT, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, RIGHT, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, COMMA, BACK, RPARENT, RBRACKED],
                        [LPARENT, ID, RPARENT, RBRACKED], 
                        [LPARENT, ID, COMMA, NORTH, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, SOUTH, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, WEST, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, EAST, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, FRONT, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, LEFT, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, RIGHT, RPARENT, RBRACKED],
                        [LPARENT, ID, COMMA, BACK, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, RPARENT, RPARENT, LBRACKED], 
                        [LPARENT, NUMBER, COMMA, NORTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, SOUTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, WEST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, EAST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, FRONT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, LEFT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, RIGHT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, NUMBER, COMMA, BACK, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, RPARENT, RPARENT, LBRACKED], 
                        [LPARENT, ID, COMMA, NORTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, SOUTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, WEST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, EAST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, FRONT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, LEFT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, RIGHT, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, ID, COMMA, BACK, RPARENT, RPARENT, LBRACKED],
                      ],
    TURN            : [
                        [LPARENT, FRONT, RPARENT, SEMMICOLON],
                        [LPARENT, LEFT, RPARENT, SEMMICOLON],
                        [LPARENT, RIGHT, RPARENT, SEMMICOLON],
                        [LPARENT, BACK, RPARENT, SEMMICOLON],
                        [LPARENT, FRONT, RPARENT, RBRACKED],
                        [LPARENT, LEFT, RPARENT, RBRACKED],
                        [LPARENT, RIGHT, RPARENT, RBRACKED],
                        [LPARENT, BACK, RPARENT, RBRACKED],
                        [LPARENT, NORTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, SOUTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, WEST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, EAST, RPARENT, RPARENT, LBRACKED],
                      ],
    TURNTO          : [
                        [LPARENT, NORTH, RPARENT, SEMMICOLON],
                        [LPARENT, SOUTH, RPARENT, SEMMICOLON],
                        [LPARENT, WEST, RPARENT, SEMMICOLON],
                        [LPARENT, EAST, RPARENT, SEMMICOLON],
                        [LPARENT, NORTH, RPARENT, RBRACKED],
                        [LPARENT, SOUTH, RPARENT, RBRACKED],
                        [LPARENT, WEST, RPARENT, RBRACKED],
                        [LPARENT, EAST, RPARENT, RBRACKED],
                        [LPARENT, NORTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, SOUTH, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, WEST, RPARENT, RPARENT, LBRACKED],
                        [LPARENT, EAST, RPARENT, RPARENT, LBRACKED],
                      ],
    DROP            : [
                        [LPARENT, NUMBER, RPARENT, SEMMICOLON], 
                        [LPARENT, ID, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, RPARENT, RBRACKED], 
                        [LPARENT, ID, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, RPARENT, RPARENT, LBRACKED], 
                        [LPARENT, ID, RPARENT, RPARENT, LBRACKED],
                      ],
    GET             : [
                        [LPARENT, NUMBER, RPARENT, SEMMICOLON], 
                        [LPARENT, ID, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, RPARENT, RBRACKED], 
                        [LPARENT, ID, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, RPARENT, RPARENT, LBRACKED], 
                        [LPARENT, ID, RPARENT, RPARENT, LBRACKED],
                      ],
    GRAB            : [
                        [LPARENT, NUMBER, RPARENT, SEMMICOLON], 
                        [LPARENT, ID, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, RPARENT, RBRACKED], 
                        [LPARENT, ID, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, RPARENT, RPARENT, LBRACKED, LBRACKED], 
                        [LPARENT, ID, RPARENT, RPARENT, LBRACKED, LBRACKED],
                      ],
    LETGO           : [
                        [LPARENT, NUMBER, RPARENT, SEMMICOLON], 
                        [LPARENT, ID, RPARENT, SEMMICOLON],
                        [LPARENT, NUMBER, RPARENT, RBRACKED], 
                        [LPARENT, ID, RPARENT, RBRACKED],
                        [LPARENT, NUMBER, RPARENT, RPARENT, LBRACKED], 
                        [LPARENT, ID, RPARENT, RPARENT, LBRACKED],
                      ],
    NOP             : [
                        [LPARENT, RPARENT, SEMMICOLON],
                        [LPARENT, RPARENT, RBRACKED],
                        [LPARENT, RPARENT, RPARENT, LBRACKED],
                      ],
}