#NMF aprende temas de documentos
#En el video, aprendi� cuando NMF se aplica a los documentos, los componentes corresponden a temas de documentos y las caracter�sticas de NMF reconstruyen los documentos a partir de los temas. Verifique esto usted mismo para el modelo NMF que cre� anteriormente utilizando los art�culos de Wikipedia. Anteriormente, viste que el valor de la tercera caracter�stica del NMF era alto para los art�culos sobre los actores Anne Hathaway y Denzel Washington. En este ejercicio, identifique el tema del componente NMF correspondiente.

#El modelo NMF que cre� anteriormente est� disponible como model, mientras que wordses una lista de las palabras que etiquetan las columnas de la matriz de frecuencia de palabras.

#Una vez que hayas terminado, �t�mate un momento para reconocer el tema que tienen en com�n los art�culos sobre Anne Hathaway y Denzel Washington!

# Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df =pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())



#Answer

(6, 13125)
film       0.627877
award      0.253131
starred    0.245284
role       0.211451
actress    0.186398
Name: 3, dtype: float64

#Great work! Take a moment to recognise the topics that the articles about Anne Hathaway and Denzel Washington have in common!
