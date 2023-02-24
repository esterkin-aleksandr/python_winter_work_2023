import re
def abre(text):
     lst = re.findall(r'\b[а-яА-Я]', text)
     abre = (''.join(lst)).upper()
     return(abre)
text = 'Самое большое простое число'
print(abre(text))