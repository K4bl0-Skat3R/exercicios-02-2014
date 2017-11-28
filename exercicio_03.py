 
# algoritimo que le hora minuto e segundo
# calcula quantos segundos se passaram desde as 00:00:00(zero horas) 
# professor Habib
#aluno Genilson M. Souza
#exercicio 03
h1= 00
m1= 00
s1= 00
Hr= input("digite a hora: ")
Mn= input("digite os minutos: ")
Sg= input("digite os segundos: ")
segundos = ((Hr * 60 + Mn) * 60 + Sg) - ((h1 * 60 + m1) * 60 + s1)
print "se passaram", segundos, "segundos, desde as 00:00:00 Hrs"
