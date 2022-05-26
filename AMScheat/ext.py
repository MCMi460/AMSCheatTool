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
    if not char.lower() in '0123456789abcdef':
        char = '0'
    return char

class Cheat():
    def storeStatic(T:str, M:Region, R:overHex, A:str, V:str):
        return ('0%s%s%s00%s %s %s' % (T[:1], M.value - 1, R, A[:2], A[2:], V[:8])
        + ((' %s' % V[8:]) if len(V) > 8 else '')
        )
