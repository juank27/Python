def is_palindromo(string:str)->bool:
   #borrando espacios y pasandollo a minusculas
   string = string.replace(" ", "").lower()
   return string == string[::-1]


def is_primo(number: int) -> bool:
   return all([False if number % num == 0 else True for num in range(2, number)])

def run():
   print(is_palindromo("ana"))
   print(is_primo(6))

if __name__ == '__main__':
   run()
