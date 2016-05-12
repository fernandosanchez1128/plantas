
def preprocesamiento (paises):
	matriz= [];
	archivo = open("plantas2.arff", "r") 
	for linea in archivo.readlines():
		fila = [0 for c in range (len(paises)+1)]
		palabras = linea.split(',')
		fila[0] = palabras[0]
		palabras = palabras[1:-1]
		contador = 1
		for pais in paises :
			if pais in palabras:
				fila[contador]=1
			else:
				fila[contador]=0
			contador +=1    
			    
		matriz.append(fila)	
	return matriz		
			    
				
def archivo_preprocesado (matriz, paises):
	f=open("plantas.arff","w")
	f.write("@relation plantas\n")
	f.write("@attribute "+ 'nombre' +" string\n")
	for pais in paises:
		f.write("@attribute "+ pais+" {0,1}\n")
	
	f.write("@data\n")
	for fila in matriz:
		for posicion in range(len(fila)-1):
			f.write(str(fila[posicion])+", ")
		f.write(str(fila[len(fila)-1]))
		f.write("\n")
	f.close()
			
		
			


paises = ['ab','ak','ar','az','ca','co','ct','de','dc','fl','ga','hi','id','il','in','ia','ks','ky','la','me','md','ma','mi','mn','ms','mo','mt','ne','nv','nh','nj','nm','ny','nc','nd','oh','ok','or','pa','pr','ri','sc','sd','tn','tx','ut','vt','va','vi','wa','wv','wi','wy','al','bc','mb','nb','lb','nf','nt','ns','nu','on','qc']

matriz = preprocesamiento(paises)
archivo_preprocesado (matriz,paises)
