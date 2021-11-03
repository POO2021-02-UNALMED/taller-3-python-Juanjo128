class TV :
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1
        
    def getCanal(self):
        return self.canal    
            
    def setCanal(self,canal):
        if ((self.estado==True) and (canal>=1 and canal<=120)):
            self._canal=canal
                
    def getMarca(self):
        return self.marca
            
    def setMarca(self,marca):
        self.marca = marca
            
    def getControl(self):
        return self.control
            
    def setControl(self, control):
        self.control = control
            
    def getPrecio(self):
        return self.precio
            
    def setPrecio(self, precio):
        self.precio = precio    

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        if ((self.estado==True) and (volumen>=0 and volumen<=7)):
            self._volumen= volumen

    @classmethod    
    def getNumTV(cls):
        return TV.numTV
    @classmethod    
    def setNumTV(cls,num):
        TV.NumTV= num

    def turnOn(self):
        if(self.estado == False):
            self.estado == True    
                
    def turnOff(self):
        if(self.estado == True):
            self.estado == False       

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if (self.estado==True):
            if self.canal!=120:
                self.canal+=1
    
    def canalDown(self):
        if (self.estado==True):
            if self.canal!=1:
                self.canal-=1

    def volumenUp(self):
        if (self.estado==True):
            if self.volumen!=7:
                self.volumen+=1
    
    def volumenDown(self):
        if (self.estado==True):
            if self.volumen!=0:
                self.volumen-=1