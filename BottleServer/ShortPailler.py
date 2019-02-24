import math
import random
class PaillerCryptoSystem(object):
    def __init__(self):
        gcdValue = 0;
        while gcdValue != 1:
            self.P = random.randint(1,500)
            while self.CheckPrime(self.P) == False:
                self.P = random.randint(1,500)
            

            print("P Value is : ",self.P)
            
            self.Q = random.randint(1,500)
            while self.CheckPrime(self.Q) == False or self.P == self.Q:
                self.Q = random.randint(1,500)
            print("Q value is : ",self.Q)
            gcdValue = math.gcd(self.P,self.Q)
        print("All Condition Satisfied")
        self.N = self.P * self.Q
        self.Lambda = (self.P-1)*(self.Q-1)
        print(" N Value : ",self.N)
        print(" Lambda Value : ",self.Lambda)
        Ans = 1
        while Ans == 1:
            self.G = random.randint(self.N,self.N**2)
            print(" Generator G : ",self.G)
            Ans = self.modInverse(self.LFunction((self.G**self.Lambda)%(self.N**2)),self.N)
        self.U = Ans
        print(" U Value : ",self.U)


    def Encryption(self,Value):
        while True:
            r = random.randint(1,self.N)
            if math.gcd(r,self.N) == 1:
                break
        print("Value R is : ",r)
        C = ((self.G**Value)*(r**self.N))%(self.N**2)
        print("Value of C is ",C)
        return C
        
    def Decryption(self,Value):
        if math.gcd(Value,self.N) == 1:
            print("Possible to Decrypt")
            self.M = (self.LFunction((Value**self.Lambda)%(self.N**2))*self.U)%self.N
            print("Decryption of C : ",self.M)
            return self.M
        else:
            print("Not possible to Decrypt")

            


    def modInverse(self,a, m) : 
        a = a % m; 
        for x in range(1, m) : 
            if ((a * x) % m == 1) : 
                return x 
        return 1

    
    def LFunction(self,No):
        Ans  = (No - 1)/self.N
        return Ans
        
    def CheckPrime(self,No):
        for i in range(2,No):
            if No % i == 0:
                return False
        return True
    def Sum(self,Value1,Value2):
        ans = (Value1*Value2) % (self.N**2)
        ans = self.Decryption(ans)
        return ans
