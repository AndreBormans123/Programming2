class Money: #Classe
   def __init__(self, money, currency_type):
     self.money = money
     self.currency_type = currency_type

   @property
   def amount(self):
     return self.money

   @property
   def currency(self):
        return self.currency_type
    
   def __add__(self, other): #+
      if self.currency_type == other.currency_type:
         return Money (
            self.money + other.money,
            self.currency_type
         )
      else: #raise error
         raise RuntimeError("Mismatched currencies!")
      
   def __sub__ (self, other): # - 
      if self.currency_type == other.currency_type:
         return Money (
            self.money - other.money,
            self.currency_type #dont forget the second argument
         )
      else:
         raise RuntimeError("Mismatched currencies!")
      
   def __mul__(self, other): # *
      return Money(
         self.money * other,
         self.currency_type
      )
   
   def __str__(self):
     return f"{self.amount} {self.currency}" #string to print te results
     
money = Money(10, "EUR")
