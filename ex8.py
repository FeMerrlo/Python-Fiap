from ctypes.wintypes import FLOAT
from re import M

from setuptools import PEP420PackageFinder


P1= float(input ('Insira nota da P1 '))
P2= float(input ('Insira nota da P2 '))
M= (P1+P2)/2
if M >= 5:
 print ("Você foi aprovado")
else:
    print("Se fudeu")
   
