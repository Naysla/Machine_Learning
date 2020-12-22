#How many defaults might we expect?
#Let's say a bank made 100 mortgage loans. It is possible that anywhere between 0 and 100 of the loans will be defaulted upon. You would like to know the probability of getting a given number of defaults, given that the probability of a default is p = 0.05. To investigate this, you will do a simulation. You will perform 100 Bernoulli trials using the perform_bernoulli_trials() function you wrote in the previous exercise and record how many defaults we get. Here, a success is a default. (Remember that the word "success" just means that the Bernoulli trial evaluates to True, i.e., did the loan recipient default?) You will do this for another 100 Bernoulli trials. And again and again until we have tried it 1000 times. Then, you will plot a histogram describing the probability of the number of defaults.

#�Cu�ntos valores predeterminados podemos esperar?
#Digamos que un banco hizo 100 pr�stamos hipotecarios. Es posible que entre 0 y 100 de los pr�stamos sean incumplidos. Le gustar�a saber la probabilidad de obtener un n�mero determinado de valores predeterminados, dado que la probabilidad de un incumplimiento es p = 0.05. Para investigar esto, har�s una simulaci�n. Realizar� 100 pruebas de Bernoulli utilizando la perform_bernoulli_trials()funci�n que escribi� en el ejercicio anterior y registrar� cu�ntos valores predeterminados tenemos. Aqu�, un �xito es un defecto. (Recuerde que la palabra "�xito" solo significa que el ensayo de Bernoulli se eval�a True, es decir, �el incumplimiento del destinatario del pr�stamo?) Har� esto para otros 100 ensayos de Bernoulli. Y una y otra vez hasta que lo hayamos probado 1000 veces. Luego, trazar� un histograma que describe la probabilidad del n�mero de valores predeterminados.

# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults=np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)


# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot
plt.show()