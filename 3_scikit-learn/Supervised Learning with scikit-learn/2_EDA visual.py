#EDA visual

#El EDA numérico que hizo en el ejercicio anterior le proporcionó información muy importante, como los nombres y los tipos de datos de las columnas y las dimensiones del Marco de datos. Seguir esto con algo de EDA visual le dará una mejor comprensión de los datos. En el video, Hugo usó la scatter_matrix()función en los datos de Iris para este propósito. Sin embargo, es posible que haya notado en el ejercicio anterior que todas las características de este conjunto de datos son binarias; es decir, son 0 o 1. Por lo tanto, un tipo diferente de gráfico sería más útil aquí, como el de Seaborncountplot .
#
#Dada a la derecha es una countplotde la 'education'factura, generada a partir del siguiente código:
#
#plt.figure()
#sns.countplot(x='education', hue='party', data=df, palette='RdBu')
#plt.xticks([0,1], ['No', 'Yes'])
#plt.show()
#En sns.countplot(), especificamos los datos del eje x para ser 'education'y el matiz para ser 'party'. Recordemos que 'party'también es nuestra variable objetivo. Entonces, la gráfica resultante muestra la diferencia en el comportamiento de votación entre las dos partes del 'education'proyecto de ley, con cada parte coloreada de manera diferente. Especificamos manualmente el color 'RdBu', ya que el partido republicano se ha asociado tradicionalmente con el rojo y el partido demócrata con el azul.
#
#Parece que los demócratas votaron rotundamente en contra de este proyecto de ley, en comparación con los republicanos. Este es el tipo de información que nuestro modelo de aprendizaje automático buscará aprender cuando intentemos predecir la afiliación a un partido únicamente en función del comportamiento de votación. Un experto en política de los EE. UU. Puede predecir esto sin el aprendizaje automático, pero probablemente no de manera instantánea, ¡y ciertamente no si estamos tratando con cientos de muestras!
#
#En IPython Shell, explore más el comportamiento de la votación generando diagramas de conteo para los proyectos de ley 'satellite'y 'missile', y responda la siguiente pregunta: ¿De estos dos proyectos de ley, por cuáles votan los demócratas a favor de los republicanos? Asegúrese de comenzar sus declaraciones de trazado para cada figura con el plt.figure()fin de configurar una nueva figura. De lo contrario, sus parcelas se superpondrán en la misma figura.

plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()


plt.figure()
sns.countplot(x='satellite', hue='missile', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()