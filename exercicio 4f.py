#coding:utf-8 (desmarquie porque meu teclado ta US aqui no linux)
# algoritimo verificar se o numero e positivo caso for imprima seu quadrado
# senao imprima seu valor absoluto
# professor Habib
#aluno Genilson M. Souza
#exercicio 04
import math
n1= input ("digite um numero: ")
if n1 >=0:
	print "o quadrado e" ,n1*n1
else:
	print "valor absoluto de", n1, "e", math.fabs(n1)
