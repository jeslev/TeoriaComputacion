#Valores por defecto para reconocedor de secuencia

tamano_alfabeto= 2 #alfabeto usado en input
tabla_str = [ '00', '01', '10', '11'] #alfabeto usado
salida = ''
seq_estados = []
#estados etiquetados de 0 a cantidad_estados -1  / inclusivo
tabla_transiciones_f = [[ 0, 0, 0, 1] ,
						[ 0, 1, 1, 1] ]  #cada fila es un estado
tabla_salidas_g = [ [0, 1, 1, 0],
					[1, 0, 0, 1] ]


#busca la posicion en el alfabeto del simbolo actual para luego buscar en las tablas
def posicionAlfabeto(busco):
	pos = 0
	for letra in tabla_str:
		if letra==busco:
			break
		else:
			pos += 1
	return pos

#simula la maquina de estado finito
def mef(s1, s2, s0 = 0):
	global salida, seq_estados
	
	#se recorre la entrada 
	seq_estados.append(s0)
	for i in range(len(s1)-1, -1, -1):
		
		#se busca en el alfabeto
		actual = s1[i]+s2[i]
		pos = posicionAlfabeto(actual)
		output = tabla_salidas_g[s0][pos] #salida del estado actual
		s0 = tabla_transiciones_f[s0][pos] #siguiente estado
		salida = salida + str(output)
		seq_estados.append(s0)
	if s0 == 1:
		salida = salida + '1'
	seq_estados.append(2)


def main():
	print "\n** Maquina de Estado Finito con Salida **"
	print "Sumador de cadenas\n"
	seq1 = raw_input("Ingrese secuencia 1:\n")
	seq2 = raw_input("\nIngrese secuencia 2:\n")

	#Inicio: Igualar longitud de las secuencias
	mini_len = min(len(seq1), len(seq2))
	if len(seq1) == mini_len:
		st = ''
		for x in range(len(seq2)-mini_len):
			st = st+'0'
		seq1 = st + seq1
	else:
		st = ''
		for x in range(len(seq1)-mini_len):
			st = st+'0'
		seq2 = st + seq2
	#Termina: Igualar longgitud de las secuencias

	mef(seq1, seq2)
	
	#print seq1
	#print seq2, mini_len
	print "\nSecuencia de Estados:"
	salida_rev = salida[::-1]
	for x in seq_estados:
		print "s"+str(x)+" ",
	print ''
	
	print "\nSalida:"
	print salida_rev
	
	print "\nFin del programa."

if __name__ == "__main__":
	main()
	
