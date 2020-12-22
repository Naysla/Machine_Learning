#EDA visual

#El EDA num�rico que hizo en el ejercicio anterior le proporcion� informaci�n muy importante, como los nombres y los tipos de datos de las columnas y las dimensiones del Marco de datos. Seguir esto con algo de EDA visual le dar� una mejor comprensi�n de los datos. En el video, Hugo us� la scatter_matrix()funci�n en los datos de Iris para este prop�sito. Sin embargo, es posible que haya notado en el ejercicio anterior que todas las caracter�sticas de este conjunto de datos son binarias; es decir, son 0 o 1. Por lo tanto, un tipo diferente de gr�fico ser�a m�s �til aqu�, como el de Seaborncountplot .
#
#Dada a la derecha es una countplotde la 'education'factura, generada a partir del siguiente c�digo:
#
#plt.figure()
#sns.countplot(x='education', hue='party', data=df, palette='RdBu')
#plt.xticks([0,1], ['No', 'Yes'])
#plt.show()
#En sns.countplot(), especificamos los datos del eje x para ser 'education'y el matiz para ser 'party'. Recordemos que 'party'tambi�n es nuestra variable objetivo. Entonces, la gr�fica resultante muestra la diferencia en el comportamiento de votaci�n entre las dos partes del 'education'proyecto de ley, con cada parte coloreada de manera diferente. Especificamos manualmente el color 'RdBu', ya que el partido republicano se ha asociado tradicionalmente con el rojo y el partido dem�crata con el azul.
#
#Parece que los dem�cratas votaron rotundamente en contra de este proyecto de ley, en comparaci�n con los republicanos. Este es el tipo de informaci�n que nuestro modelo de aprendizaje autom�tico buscar� aprender cuando intentemos predecir la afiliaci�n a un partido �nicamente en funci�n del comportamiento de votaci�n. Un experto en pol�tica de los EE. UU. Puede predecir esto sin el aprendizaje autom�tico, pero probablemente no de manera instant�nea, �y ciertamente no si estamos tratando con cientos de muestras!
#
#En IPython Shell, explore m�s el comportamiento de la votaci�n generando diagramas de conteo para los proyectos de ley 'satellite'y 'missile', y responda la siguiente pregunta: �De estos dos proyectos de ley, por cu�les votan los dem�cratas a favor de los republicanos? Aseg�rese de comenzar sus declaraciones de trazado para cada figura con el plt.figure()fin de configurar una nueva figura. De lo contrario, sus parcelas se superpondr�n en la misma figura.

plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()


plt.figure()
sns.countplot(x='satellite', hue='missile', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()