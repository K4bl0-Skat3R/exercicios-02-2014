#coding:utf-8 (desmarquie porque meu teclado ta US aqui no linux)
# algoritimo dada idade do nadador verifique sua categoria
# professor Habib
#aluno Genilson M. Souza
#exercicio 07
n1= input("para saber a categoria de um nadador, digite aqui a sua idade: ")
if (n1>=5) and (n1<=7):
	print "nadador infantial A"
elif (n1>=8) and (n1<=10):
	print "nadador infantil B"
elif (n1 >=11) and (n1<=13):
	print "nadador juvenil A"
elif (n1>=14) and (n1<=17):
	print "nadador juvenil B"
elif n1>=18:
	print "nadador adulto"
else:
	print "entrada nao permitida"
