import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.integrate import odeint


def t6ss_model(y, t, r, s, alpha_AB, alpha_BA):
    A, B = y
    dA_dt = A * (r - s * (A + B) - alpha_AB * B)
    dB_dt = B * (r - s * (A + B) - alpha_BA * A)
    return [dA_dt, dB_dt]


r = 2.0
s = 2.0
t = np.linspace(0, 20, 500)


fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.35) 

# Initial parameter values
init_A = 0.51
init_B = 0.49
init_alpha_AB = 0.5
init_alpha_BA = 0.5

# Solve initially
y0 = [init_A, init_B]
sol = odeint(t6ss_model, y0, t, args=(r, s, init_alpha_AB, init_alpha_BA))

# Plot initial lines
line_A, = ax.plot(t, sol[:, 0], 'b-', lw=2, label='Strain A (Cooperator)')
line_B, = ax.plot(t, sol[:, 1], 'r-', lw=2, label='Strain B (Cheater)')

ax.set_title('Interactive T6SS Well-Mixed ODE Simulation', fontsize=14)
ax.set_xlabel('Time')
ax.set_ylabel('Population Density')
ax.set_ylim(0, 1.1)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='center right')

# 3. Create Sliders
axcolor = 'lightgoldenrodyellow'
ax_A = plt.axes([0.15, 0.20, 0.65, 0.03], facecolor=axcolor)
ax_B = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_alpha_AB = plt.axes([0.15, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_alpha_BA = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=axcolor)

slider_A = Slider(ax_A, 'Initial A', 0.0, 1.0, valinit=init_A)
slider_B = Slider(ax_B, 'Initial B', 0.0, 1.0, valinit=init_B)
slider_alpha_AB = Slider(ax_alpha_AB, 'A kills B Rate', 0.0, 2.0, valinit=init_alpha_AB)
slider_alpha_BA = Slider(ax_alpha_BA, 'B kills A Rate', 0.0, 2.0, valinit=init_alpha_BA)

# 4. Define the Update Function
def update(val):
    # Read values from sliders
    A0 = slider_A.val
    B0 = slider_B.val
    a_AB = slider_alpha_AB.val
    a_BA = slider_alpha_BA.val
    
    # Recalculate ODE
    new_sol = odeint(t6ss_model, [A0, B0], t, args=(r, s, a_AB, a_BA))
    
    # Update plot lines
    line_A.set_ydata(new_sol[:, 0])
    line_B.set_ydata(new_sol[:, 1])
    
    # Redraw the canvas
    fig.canvas.draw_idle()

# 5. Attach the update function to the sliders
slider_A.on_changed(update)
slider_B.on_changed(update)
slider_alpha_AB.on_changed(update)
slider_alpha_BA.on_changed(update)

# Show the interactive plot
plt.show()