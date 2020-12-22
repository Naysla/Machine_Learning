#Examinando el SparkContext
#En este ejercicio te familiarizar�s con el SparkContext.
#
#Probablemente notar� que el c�digo tarda m�s en ejecutarse de lo que podr�a esperar. Esto se debe a que Spark es un software serio. Se tarda m�s tiempo en iniciarse de lo que podr�a estar acostumbrado. Tambi�n puede encontrar que ejecutar c�lculos m�s simples puede llevar m�s tiempo de lo esperado. Esto se debe a que todas las optimizaciones que Spark tiene bajo su cap� est�n dise�adas para operaciones complicadas con grandes conjuntos de datos. �Eso significa que para problemas simples o peque�os, Spark puede funcionar peor que otras soluciones!

Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.3.1
      /_/

Using Python version 3.5.2 (default, Nov 23 2017 16:37:01)
SparkSession available as 'spark'.

# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)

#<SparkContext master=local[*] appName=pyspark-shell>
#2.3.1

#Awesome! You're up and running with Spark.