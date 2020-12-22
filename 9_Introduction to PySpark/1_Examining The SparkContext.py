#Examinando el SparkContext
#En este ejercicio te familiarizarás con el SparkContext.
#
#Probablemente notará que el código tarda más en ejecutarse de lo que podría esperar. Esto se debe a que Spark es un software serio. Se tarda más tiempo en iniciarse de lo que podría estar acostumbrado. También puede encontrar que ejecutar cálculos más simples puede llevar más tiempo de lo esperado. Esto se debe a que todas las optimizaciones que Spark tiene bajo su capó están diseñadas para operaciones complicadas con grandes conjuntos de datos. ¡Eso significa que para problemas simples o pequeños, Spark puede funcionar peor que otras soluciones!

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