#coding:utf-8 (desmarquie porque meu teclado ta US aqui no linux)
# algoritimo verificar se o numero e par ou impar
# aluno Genilson
# professor Habib
# exercicio 05

n1= input("digite um numero: ")
if n1 == 0:
	print "Neutro"	#usei essa opcao para testar o elif(zero e par porem nulo )
elif n1 %2 == 0:
	print "este numero e par"
else:
	print "este numero e impar" 
