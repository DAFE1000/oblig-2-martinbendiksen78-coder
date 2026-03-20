import math
import numpy as np
import matplotlib.pyplot as plt

#Funksjonen
def f(x):
    return math.e**(-x/4) * math.atan(x)

#Den deriverte funksjonen, uten e^(-x/4), for jeg skal kun vise denne delen
def g(x):
    return math.atan(x) - 4/(x**2 + 1)

#Den dobbelt derivert funksjonen
def g_derivert(x):
    return 1/(x**2 + 1) + (8*x)/(x**2 + 1)**2

#Sjekker to x-verdier, hvor x = 1 er negativ og x= 2 er posetivt. Jeg vet derfor at svaret ligger mellom 1 og 2.
print(g(1))
print(g(2))

#Setter startverdi med margin
x0 = 1.5

#Løkke for å bruke Newtons metode
while True:
    #Finner x-verdi for å sammenligne med x0
    x = x0 - g(x0)/g_derivert(x0)

    #sjekker om forskjellen er mindre enn 0.0001, for vi skal bruke 4 desimaler i svaret
    if abs(x - x0) < 0.0001:
        break

    #Setter x0 til å bli x for å kunne sammenligne nye verdier
    x0 = x

#Setter en y verdi til å bli f(x) når vi har funnet riktig x-verdi, printer så ut x og y-verdiene med 4 desimaler
y = f(x)
print(round(x, 4))
print(round(y, 4))

#Setter verdier for x og y til å plotte funksjonen
x_vals = np.linspace(0, 4, 100)
y_vals = [f(x) for x in x_vals]


plt.plot(x_vals, y_vals, label="f(x)") #Plotter funksjonen
plt.scatter([x], [y], color="red", label="Toppunkt") #Setter et rødt punkt i toppunktet
plt.legend() #Ramme på siden for å se labels
plt.grid() #Legger til en grid i plottet
plt.show() #viser plottet
