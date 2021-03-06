# Created by Deltaion Lee (MCMi460) on Github

from . import *

Region = enum.Enum('Memory Region', 'main heap alias aslr')

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
        return ('0%s%s%s00%s %s %s' % (T[:1], M.value - 1, R, A[:2], A[2:10], V[:8])
        + ((' %s' % V[8:]) if len(V) > 8 else '')
        )

    def beginCondition(T:str, M:Region, C:str, A:str, V:str):
        return ('1%s%s%s00%s %s %s' % (T[:1], M.value - 1, C, A[:2], A[2:10], V[:8])
        + ((' %s' % V[8:]) if len(V) > 8 else '')
        )

    def endCondition(X:bool):
        return '2%s000000' % int(X)

    def loop(R:overHex, V:str, end:bool = False):
        return ('3%s0%s0000' % (int(end), R)
        + ((' %s' % V[:8]) if not end else '')
        )

    def loadRegisterStatic(R:overHex, V:str):
        return ('400%s0000 %s' % (R, V[:8])
        + ((' %s' % V[8:]) if len(V) > 8 else '')
        )

    def loadRegisterWithMemory(T:str, M:Region, R:overHex, A:str):
        if M:
            return ('5%s%s%s00%s %s' % (T[:1], M.value - 1, R, A[:2], A[2:10]))
        return ('5%s0%s10%s %s' % (T[:1], R, A[:2], A[2:10]))

    def storeRegisterAddress(T:str, R:overHex, I:bool, o:bool, r:overHex, V:str):
        return '6%s0%s%s%s%s0 %s %s' % (T[:1], R, int(I), int(o), r, V[:8], V[8:])

    def legacyArithmetic(T:str, R:overHex, C:str, V:str):
        return '7%s0%s%s000 %s' % (T[:1], R, C, V[:8])

    def buttonActivator(k:str):
        return '8%s' % k[:7]

    def arithmetic(T:str, C:str, R:overHex, S:overHex, s:overHex, V:str):
        return ('9%s%s%s%s%s%s0' % (T[:1], C, R, S, ('0' if s else '1'), (s if s else '0'))
        + ( ((' %s %s' % (V[:8], V[8:])) if len(V) > 8 else (' %s' % V[:8])) if not s else '')
        )
