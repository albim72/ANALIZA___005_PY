import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#przygotowanie danych dla funkcji harmomnicznej tłumionej
x = np.linspace(-2*np.pi,2*np.pi,100)
y = np.sinc(x)

#dwa wykresy na jednej figurze
fig,ax = plt.subplots(ncols=2,figsize=(12,8))
ax[0].plot(x,y)
ax[0].set_title('pojedyncza krzywa')
ax[1].plot(x,y)
ax[1].plot(x*2.0,y)
ax[1].set_title('dwie krzywe')
plt.show()

#dwa wykresy -> lewa strona: wykresy przesunięte względem siebie i zawężone do zadanego x
#prawa strona: wykresy przesunięte względem siebie i autoskalowane

fig2,ax2 = plt.subplots(ncols=2,figsize=(12,8))
ax2[0].plot(x,y)
ax2[0].set_xlim(left=-1,right=1)
ax2[0].plot(x+np.pi*0.5,y)
ax2[0].set_title('set_xlim(left=-1,right=1)\n')


ax2[1].plot(x,y)
ax2[1].set_xlim(left=-1,right=1)
ax2[1].plot(x+np.pi*0.5,y)
ax2[1].autoscale()
ax2[1].set_title('set_xlim(left=-1,right=1)\nautoscale()\n')

plt.show()


print(mpl.__version__)
#wykres tej samej funkcji w formie wyświetlenia punktów (punkty - gwiazdki)
fig3,ax3 = plt.subplots()

collection = mpl.collections.StarPolygonCollection(
    5,7,[150,],
    offsets = np.column_stack([x,y]),
    transOffset = ax3.transData
)
ax3.add_collection(collection)
ax3.autoscale_view()
plt.show()
