from typing import Tuple, Dict, List 

def suma(a:int, b:int)->int:
   return a+b;

def tipado():
   #listas
   positives: List[int] = [1,2,3,4,5]
   #Diccionarios
   users : Dict[str,int]={
      'argentina' : 1,
      'mexico' : 34,
      'colombia' : 45
   }
   #Lista de diccionarios
   countries: List[dict[str,str]] = [
      {
         'name':'Argentina',
         'people': '45000'
      },
      {
         'name': 'Mexico',
         'people': '66000'
      },
      {
         'name': 'Colomabia',
         'people': '99999'
      },
   ]
   #tuplas
   numbers : Tuple[int, float, int] = (1, 0.5, 1)
   CoordinatesType = List[Dict[str, Tuple[int, int]]]
   coordinates: CoordinatesType = [
      {
         "coord1": (1, 2),
         "coord2": (3, 5)
      },
      {
         "coord1": (0, 1),
         "coord2": (2, 5)
      }
   ]

print(suma(5,6))
