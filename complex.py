import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import keyboard

MIN_VALUE = -1
MAX_VALUE = 1
STEP = 100

# Sets colors based on the order of the visible electromagnetic spectrum, then violet to black
colors = ListedColormap(['#ff0000','#ff1100','#ff2200','#ff3300','#ff4400','#ff5500','#ff6600','#ff7700','#ff8800','#ff9900','#ffaa00','#ffbb00','#ffcc00','#ffdd00','#ffee00','#ffff00','#eeff00','#ddff00','#ccff00','#bbff00','#aaff00','#99ff00','#88ff00','#77ff00','#66ff00','#55ff00','#44ff00','#33ff00','#22ff00','#11ff00','#00ff00','#00ff11','#00ff22','#00ff33','#00ff44','#00ff55','#00ff66','#00ff77','#00ff88','#00ff99','#00ffaa','#00ffbb','#00ffcc','#00ffdd','#00ffcc','#00ffdd','#00ffee','#00ffff','#00eeff','#00ddff','#00ccff','#00bbff','#00aaff','#0099ff','#0088ff','#0077ff','#0066ff','#0055ff','#0044ff','#0033ff','#0022ff','#0011ff','#0000ff','#1100ff','#2200ff','#3300ff','#4400ff','#5500ff','#6600ff','#7700ff','#8800ff','#9900ff','#aa00ff','#bb00ff','#cc00ff','#dd00ff','#ee00ff','#ff00ff','#ee00ee','#dd00dd','#cc00cc','#bb00bb','#aa00aa','#990099','#880088','#770077','#660066','#550055','#440044','#330033','#220022','#110011','#000000'])

# Put whatever function f(z) here. For a graphics without animation, remove the 'i' from the equation.
def polynomial(z, i):
    return z**3 + i

# Click space to pause the animation   
paused = False 
def pause(event):
    global paused
    paused = not paused
keyboard.on_press_key(' ', pause)

# Axes and point grid
x = np.linspace(-1.5, 1.5, 1000)
y = np.linspace(-1.5j, 1.5j, 1000)
X, Y = np.meshgrid(x, y)

# Applying the function at each point
frames = np.linspace(MIN_VALUE, MAX_VALUE, STEP)
c, r = [], []
for i in frames:
    c.append(polynomial(X + Y, i))
    r.append(polynomial(x, i))

# Create screen
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))
ax1.axhline(y=0, color='white', linewidth=1)
ax2.set_ylim(MIN_VALUE, MAX_VALUE)
ax2.set_xlim(MIN_VALUE, MAX_VALUE)
ax2.axhline(y=0, color='black', linewidth=1)
ax3.set_ylim(MIN_VALUE, MAX_VALUE)
ax3.set_xlim(MIN_VALUE, MAX_VALUE)
ax3.axhline(y=0, color='black', linewidth=1)

# Initialize graphics
complex_graph = ax1.imshow(np.abs(c[0]), cmap=colors, extent=[MIN_VALUE, MAX_VALUE, MIN_VALUE, MAX_VALUE], vmin=0, vmax=1, interpolation='nearest', aspect='equal', origin='lower', alpha=0.8)
curve1_graph, = ax2.plot(x, r[0], color='#ff0000')
curve2_graph, = ax3.plot(x, abs(r[0]), color='#ff0000')

# Animation function
def animate(i):  
    global paused 
    if not paused:
        # Update data
        complex_graph.set_data(np.abs(c[i]))
        curve1_graph.set_data(x, r[i])
        curve2_graph.set_data(x, abs(r[i]))
    
# Animation
anim = FuncAnimation(fig, animate, STEP, interval=50)

# Plot
plt.show()