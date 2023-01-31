vvod=input()
mn=set(vvod)
numbers={'0','1','2','3','4','5','6','7','8','9'}
alfa={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
bukv = mn.intersection(alfa)
cifr = mn.intersection(numbers)
sim = mn.difference(bukv.union(cifr))
print(*bukv)
print(*cifr)
print(*sim)