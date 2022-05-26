# Created by Deltaion Lee (MCMi460) on Github

from . import *

Region = enum.Enum('Memory Region', 'main heap alias aslr')

codes = [
'0TMR00AA AAAAAAAA VVVVVVVV (VVVVVVVV)',
'1TMC00AA AAAAAAAA VVVVVVVV (VVVVVVVV)',
'2X000000',
'300R0000 VVVVVVVV',
]

fHex = lambda value : hex(struct.unpack('I', struct.pack('f', value))[0]) # Basically, just convert float to binary, then convert to an integer, which can be converted to hexadecimal
def isHex(string):
    for char in string:
        if not char.lower() in '0123456789abcdef':
            return False
    return True if string else False

def overHex(char):
    char = char[:1]
    if not char.lower() in '0123456789abcdef':
        char = '0'
    return char

class Cheat():
    def storeStatic(T:str, M:Region, R:overHex, A:str, V:str):
        return ('0%s%s%s0000 %s %s' % (T[:1], M.value - 1, R, A[:8], V[:8])
        + ((' %s' % V[8:]) if len(V) > 8 else '')
        )

    def beginCondition(T:str, M:Region, C:str, A:str, V:str):
        return ('1%s%s%s0000 %s %s' % (T[:1], M.value - 1, C, A[:8], V[:8])
        + ((' %s' % V[8:]) if len(V) > 8 else '')
        )

    def endCondition(X:bool):
        return '2%s000000' % int(X)

    def loop(R:overHex, V:str, end = False):
        return ('3%s0%s0000' % (int(end), R)
        + ((' %s' % V[:8]) if not end else '')
        )

    def loadRegisterStatic(R:overHex, V:str):
        return ('400%s0000 %s' % (R, V[:8])
        + ((' %s' % V[8:]) if len(V) > 8 else '')
        )
