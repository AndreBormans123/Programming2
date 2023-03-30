class MusicalNote: #classe
    def __init__(self, name, pitch): #constructur
      self.__name = name #initileerd waardes
      self.__pitch = pitch

    @property #decorator
    def name(self): #getter
       return self.__name #return
    
    @property
    def pitch(self):
       return self.__pitch