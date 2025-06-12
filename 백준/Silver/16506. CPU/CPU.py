op = {
    'ADD':'0000', 'SUB':'0001', 'MOV':'0010', 'AND':'0011','OR':'0100',
    'NOT':'0101','MULT':'0110', 'LSFTL':'0111', 'LSFTR':'1000',
    'ASFTR':'1001','RL':'1010','RR':'1011'
    }

n = int(input())

for _ in range(n):
    opcode, x, y, z = input().split()
    result = ''
    
    if opcode[-1]=='C':
        result += op.get(opcode[:-1])
        result += '1'
        
    else:
        result += op.get(opcode)
        result += '0'
        
    result += '0'

    result += str(bin(int(x)))[2:].zfill(3)
    result += str(bin(int(y)))[2:].zfill(3)

    if result[4]=='0':
        result+=str(bin(int(z)))[2:].zfill(3)
        result+='0'
        
    else:
        result+=str(bin(int(z)))[2:].zfill(4)
    
    print(result)