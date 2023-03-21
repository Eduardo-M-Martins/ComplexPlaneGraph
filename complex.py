import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import keyboard

#to do:
# - fazer ajustar limites igual o jb falou
# - deixar as coisas com parametros
# - gerar a lista de rgb não manulamente ou de alguma forma mais legal

paused = False
# Define as cores com base na ordem do espectro eletromagnético visivel (muito mais legal) e dps do violeta pro preto
my_cmap = ListedColormap(['#ff0000','#ff1100','#ff2200','#ff3300','#ff4400','#ff5500','#ff6600','#ff7700','#ff8800','#ff9900','#ffaa00','#ffbb00','#ffcc00','#ffdd00','#ffee00','#ffff00','#eeff00','#ddff00','#ccff00','#bbff00','#aaff00','#99ff00','#88ff00','#77ff00','#66ff00','#55ff00','#44ff00','#33ff00','#22ff00','#11ff00','#00ff00','#00ff11','#00ff22','#00ff33','#00ff44','#00ff55','#00ff66','#00ff77','#00ff88','#00ff99','#00ffaa','#00ffbb','#00ffcc','#00ffdd','#00ffcc','#00ffdd','#00ffee','#00ffff','#00eeff','#00ddff','#00ccff','#00bbff','#00aaff','#0099ff','#0088ff','#0077ff','#0066ff','#0055ff','#0044ff','#0033ff','#0022ff','#0011ff','#0000ff','#1100ff','#2200ff','#3300ff','#4400ff','#5500ff','#6600ff','#7700ff','#8800ff','#9900ff','#aa00ff','#bb00ff','#cc00ff','#dd00ff','#ee00ff','#ff00ff','#ee00ee','#dd00dd','#cc00cc','#bb00bb','#aa00aa','#990099','#880088','#770077','#660066','#550055','#440044','#330033','#220022','#110011','#000000'])

# Define a função 
def polynomial(z, i):
    return z**3 + i# Colocar a função f(z) que quiser aqui. Se quiser grafico sem animação é so tirar o 'i' da equação.

# Eixos e grade de pontos
x = np.linspace(-15, 15, 1000)
y = np.linspace(-15j, 15j, 1000)
X, Y = np.meshgrid(x, y)

# Cria tela
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

#ax1.axhline(y=0, color='white', linewidth=1)
#ax2.axhline(y=0, color='black', linewidth=1)
#ax3.axhline(y=0, color='black', linewidth=1)

# Faz a animação
def animate(i):
    # Aplicando a função em cada ponto
    global paused  # permite que a variável seja modificada dentro da função

    if not paused:
        W = polynomial(X + Y, i)

        # Limpa e coloca eixo real. Não usar o clear toda hora. <<<<<<<<<<<<<<<<<<<<<<<<<<--------------------------------------------
        ax1.clear()
        ax1.axhline(y=0, color='white', linewidth=1)
        ax2.clear()
        ax2.axhline(y=0, color='black', linewidth=1)
        #ax3.clear()
        #ax3.axhline(y=0, color='black', linewidth=1)
        
        # Criar variavel separada para esses parametros. pedir por argumento?nao <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<------------------------------------------------------------------------
        ax1.imshow(np.abs(W), cmap=my_cmap, extent=[-10, 10, -10, 10], vmin=0, vmax=1000, interpolation='nearest', aspect='equal', origin='lower', alpha=0.8)
        
        ax2.set_ylim(-1000, 1000)
        ax2.set_xlim(-10, 10)
        ax2.plot(x, polynomial(x, i), color='#ff0000')
        
        #ax3.set_ylim(-1000, 1000)
        #ax3.set_xlim(-10, 10)
        #ax3.plot(x, abs(polynomial(x, i)), color='#ff0000')
        
def on_space_pressed(event):
    global paused
    paused = not paused
# adiciona o callback para a tecla de espaço
keyboard.on_press_key(' ', on_space_pressed)
    
# Anima. aQUI tambem tem coisa que da pra passar por argumento pra altera velocidade de animação e distancia do passo, onde começa e onde termina <<<<<<<<<<<<<<<<<<-------------------------
anim = FuncAnimation(fig, animate, frames=np.linspace(-1000, 1000, 100), interval=50)

# Plota
plt.show()