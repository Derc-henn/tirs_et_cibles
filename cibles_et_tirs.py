
from random import randint

nb_tirs = 50
nb_cibles = 21
proba_toucher_une_cible = 0.4

tableau_comptage_par_cible = [0 for _ in range(nb_cibles)]
numeros_cibles = [u for u in range(nb_cibles)]

for i in range(nb_tirs):    
    x = randint(0, 1000)
    if(x<=proba_toucher_une_cible*1000):      
        tableau_comptage_par_cible[randint(0,nb_cibles-1)] += 1
    
    
for i in range(nb_cibles):
    print(i, tableau_comptage_par_cible[i])
    
    
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = numeros_cibles
counts = tableau_comptage_par_cible
bar_labels =  numeros_cibles

ax.bar(fruits, counts, label=bar_labels)

ax.set_ylabel('nombre')
ax.set_title('N et P')
#ax.legend(title='numero de la cible')

plt.savefig("distribution_graphique.png")
    
    


