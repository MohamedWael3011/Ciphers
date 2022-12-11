
def Encrypt(Text,Key):
    Operation = list(Text)
    for i in range(len(Operation)):
        if Operation[i].isupper():
            Operation[i] = chr((ord(Operation[i])-ord('A')+Key)%26 + ord('A'))
        else:
            Operation[i] = chr((ord(Operation[i])-ord('a')+Key)%26 + ord('a'))
    return Operation
    
def Decrypt(Text,Key):
    Operation = list(Text)
    for i in range(len(Operation)):
        if Operation[i].isupper():
            Operation[i] = chr((ord(Operation[i])-ord('A')-Key+26)%26 + ord('A'))
        else:
            Operation[i] = chr((ord(Operation[i])-ord('a')-Key+26)%26 + ord('a'))
    return Operation
        
class CaesarCipher:
    Cipher = ""
    def __init__(self, Text, Key):
        self.Text = Text
        self.Key = Key
        self.Cipher = self.Text
        self.Cipher = "".join(Encrypt(self.Text,self.Key))

        
        

    
    def ShowCipher(self):
        print("Cipher Text is : " + self.Cipher)
    def ShowPlain(self):
        print("Plain Text is : " + self.Text)
    @staticmethod
    def ToCipher(Text,Key):
        return "".join(Encrypt(Text,Key))
    @staticmethod
    def ToPlain(Text,Key):
        return "".join(Decrypt(Text,Key))
        
        
            
print(CaesarCipher.ToPlain("Ynulpkcnwldu",22))


    