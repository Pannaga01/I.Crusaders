class User:

    def__init__(self,option,algo,text,key,path):
        
        self.option = option
        self.algo = algo
        self.text = text
        self.key = key
        self.path = path

    def encrypt_or_decrypt(self):
        
        if self.algo == "shift_cipher":
            
            if option == "encrypt":
                obj = shift_cipher(self.key,self.text,None)
                obj.encrypt()
            else:
                obj = shift_cipher(self.key,None,self.text)
                obj.decrypt()
                
        if self.algo == "hillcypher":
            
            if option == "encrypt":
                obj = hillcypher(self.key,self.text,None)
                obj.encrypt()
            else:
                obj = hillcypher(self.key,None,self.text)
                obj.decrypt()

        if self.algo == "caesarcipher":
            
            if option == "encrypt":
                obj = caesarcipher(self.key,self.text,None)
                obj.encrypt()
            else:
                obj = caesarcipher(self.key,None,self.text)
                obj.decrypt()

        obj.dsiplay()
        obj.save()

    def view_file(self):
        
        if self.option == 'view':
            view_obj = View(path)
            view_obj.getTheFile()



text = getText()
