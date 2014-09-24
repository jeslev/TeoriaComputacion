#Valores por defecto para reconocedor de secuencia

tamano_alfabeto= 2 #alfabeto usado en input
z  = [ 0, 1] #alfabeto usado
salida = []
seq_estados = []
#estados etiquetados de 0 a cantidad_estados -1  / inclusivo
tabla_transiciones_f = [[ 0, 1] ,
						[ 0, 2],
						[ 0, 2] ]  #cada fila es un estado
tabla_salidas_g = [ [0, 0],
					[0, 0],
					[0, 1] ]


#busca la posicion en el alfabeto del simbolo actual para luego buscar en las tablas
def posicionAlfabeto(busco):
	pos = 0
	for letra in z:
		if letra==busco:
			break
		else:
			pos += 1
	return pos

#simula la maquina de estado finito
def mef(entrada, s0 = 0):
	global salida, seq_estados
	
	#se recorre la entrada 
	seq_estados.append(s0)
	for i in range(len(entrada)):
		
		#se busca en el alfabeto
		actual = int(entrada[i])
		pos = posicionAlfabeto(actual)
		output = tabla_salidas_g[s0][pos] #salida del estado actual
		s0 = tabla_transiciones_f[s0][pos] #siguiente estado
		salida.append(output)
		seq_estados.append(s0)
		

def main():
	print "** Maquina de Estado Finito con Salida **"
	print "Reconocedor de secuencia 111"
	seq = raw_input("Ingrese la secuencia:\n")
	mef(seq)

	print "Secuencia de Estados:"
	for x in seq_estados:
		print "s"+str(x)+" ",
	print ''
	
	print "Salida:"
	for x in salida:
		print x,
	print ''
	
	print "Fin del programa."

if __name__ == "__main__":
	main()
	
