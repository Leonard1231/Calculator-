
from Stacks import Stack
# class Rechner:
#     def __init__(self):
#         self.Rechnung= input("Rechnung eingeben")
#     def Auswertung(self):
#         x= "" 
#         y=""
#         op=""
#         i=0
#         #erste Zahl lesen
#         while self.Rechnung[i].isdigit():
#             x+=self.Rechnung[i]
#             i+=1
#         op = self.Rechnung[i]
#         i +=1
#         #zweite Zahl lesen
#         while i <len(self.Rechnung):
#             y+=self.Rechnung[i]
#             i+=1
#         x = int(x)
#         y = int(y)
#         if op== "+":
#             return x+y
#         elif op =="-":
#             return x-y
#         elif op == "*":
#             return x*y
#         elif op == "/":
#             return x/y
        

# class Rechner2:
#     def __init__(self):
#         self.OpStack=Stack()
#         self.ZStack=Stack()
#         self.Zwischenspeicher=[]
#         self.Rechnung = input("Rechnung hier eingeben:")
#     def SaveChain(self,i,):
#         while i < len(self.Rechnung) and self.Rechnung[i].isdigit(): #Zahlenreihe zwischenspeichern
#             self.Zwischenspeicher.append(self.Rechnung[i])
#             i+=1 
        
#         if self.Zwischenspeicher:    #Zahlenreihe pushen
#             self.ZStack.push(int("".join(self.Zwischenspeicher)))
#             self.Zwischenspeicher.clear() 
#         return i
        
#     def calc(self): #Rechnen
#         Z2=self.ZStack.pop()
#         Z1=self.ZStack.pop()
#         Op=self.OpStack.pop()
#         if Op == "+":
#             return Z1+Z2
#         elif Op =="-":
#             return Z1-Z2
#         elif Op in ["/",":"]:
#             return Z1/Z2
#         elif Op == "*":
#             return Z1*Z2
#         else: return 0
#     def Split(self,i=0):
        
#         i=self.SaveChain(i)

#         if (
#             i + 1 < len(self.Rechnung) #check minus und op
#             and self.Rechnung[i] in "+-/*()"
#             and self.Rechnung[i + 1] == "-"
#         ):
#             self.OpStack.push(self.Rechnung[i])
#             self.Zwischenspeicher.append(self.Rechnung[i+1])

#             i+=2
#             i=self.SaveChain(i) 
            
#             if self.ZStack.top is not None and self.ZStack.top.next is not None and self.OpStack.top is not None:
#                 result = self.calc()
#                 self.ZStack.push(result)
#             self.Split(i)
#         elif ( #push op
#             i + 1 < len(self.Rechnung)
#             and self.Rechnung[i] in "+-/*()"
            
#         ):
#             self.OpStack.push(self.Rechnung[i])

#             i+=1
            
#             i=self.SaveChain(i)
#             #hier nochmal einfügen +rechnung
#             #Rechnung
#             if self.ZStack.top is not None and self.ZStack.top.next is not None and self.OpStack.top is not None:
#                 result = self.calc()
#                 self.ZStack.push(result)
#             self.Split(i)

#         elif i==len(self.Rechnung):
#             print("Done")

class Rechner3:
    #Struktur:
    #1. digits pushen mit while check
    #klammern pushen check
    #op prüfen, priority >= neue priority? -->rechnen sonst push
    #ende klammer? solange rechnen bis ende klammer
    #ops in opstack? weiter rechnen
    #pop finalen wert
    def __init__(self):
        self.OpStack=Stack()
        self.ZStack=Stack()
        self.Rechnung=input("Rechnung hier eingeben:")
        self.Zwischenspeicher=[]
        self.i=0
    def Split(self,i):
        while i < len.self.Rechnung:
            while self.Rechnung[i].isDigit():
                self.ZStack.push(self.Rechnung[i])
                i+=1
            if self.Rechnung[i]== "(":
                self.OpStack.push(self.Rechnung[i])
                i+=1
        
        
        

    def Gewichtung(op):
        if op in "+-":
            return 1
        if op in "/:*":
            return 2
        if op == "/":
            return 3
        else:
            return 0
    def Calc(): # hier rechnen?
        
#TESTS
# s = Rechner2()
# s.Split()
# print("Zahlenstack:", s.ZStack)
# print("OpStack:", s.OpStack)

            
    
