#funciones anonimas Lambda
palindrome = lambda string: string == string[::-1]
print(palindrome("ana"))

#realizada por funcion
def palindromee(string):
   return string == string[::-1]
#print de funcion
print(palindromee("ana"))