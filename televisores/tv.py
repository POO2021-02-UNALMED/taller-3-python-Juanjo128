class TV :
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = self.marca
        self.volumen = 1
        self.control
        self.marca = marca
        self.estado = estado
        TV.numTV += 1
        
        def getCanal(self):
            return self.canal    
            
        def setCanal(self, canal):
            if(canal >= 1 and canal<= 120 and self.estado == True):
                self.canal = canal 
                
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

        def setVolumen(self,volumen):
            if(volumen>= 0 and volumen<= 7 and estado == True):
                self.volumen = volumen

        @classmethod    
        def getNumTV(self):
            return TV.numTV
        @classmethod    
        def setNumTV(self,num):
            TV.NumTV= num

        def turnOn(self):
            if(self.estado == False):
                estado == True    
                
        def turnOff(self):
            if(self.estado == True):
                estado == False       

        def getEstado(self):
            return self.estado

        def canalUp(self):
            if(self.estado == True and self.canal<120 and self.canal >= 1) :
                self.canal += 1

        def canalDown(self):
            if(self.estado == True and self.canal<= 120 and self.canal > 1):
                self.canal -= 1

        def volumenlUp(self):
            if(self.estado == True and self.volumen< 7 and self.canal >= 0) :
                self.volumen += 1

        def volumenDown(self):
            if(self.estado == True and self.volumen<= 7 and self.canal > 0):
                self.volumen -= 1  