class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        temp0b = bin(n)
        if(len(temp0b)<34):
            temp0b = '0b' + (34-len(temp0b))*'0' + temp0b[2:]
        res = '0b' + temp0b[2:][::-1]
        ans = int(res,2)
        return ans
        
        