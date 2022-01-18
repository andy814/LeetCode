#from bitstring import Bits
import sys
'''
a=0xFFFFFFFF
print(a)
print(~0xFFFFFFFF)
print(~~0xFFFFFFFF)
print(~(a^0xFFFFFFFF))
print(bin(~(0xF)))
print(0xF)
'''
'''
print(bin(-4))
print(bin(2))
print(bin(-4^2))
print(int(bin(-4^4),0))
print(int("-0b110",2))
'''

# 1.输入为十进制负数，求补码
# 2. 输入为负数的补码，求值
def twos(val, bytes):
    import sys
    #val = int(val_str, 2)
    b = val.to_bytes(bytes, byteorder=sys.byteorder, signed=False)       
    return int.from_bytes(b, byteorder=sys.byteorder, signed=True)


def encode(val,byte): # int->comp
    return val.to_bytes(byte,byteorder=sys.byteorder,signed=True)
    
def decode(val_str,byte): # comp->int
    val=int(val_str,2)
    b=val.to_bytes(byte,byteorder=sys.byteorder,signed=True)
    #print(b)
    ret=int.from_bytes(b,byteorder=sys.byteorder,signed=True)
    return ret

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val       


print(twos(254,1))
#print(decode("1001",1))
#print(encode(10,1))
#val_str="1001"
#val=-9
#valbyte=val.to_bytes(1,byteorder=sys.byteorder, signed=True)
#print(valbyte)
#val_str="10000001"
#print(twos(val_str,1))