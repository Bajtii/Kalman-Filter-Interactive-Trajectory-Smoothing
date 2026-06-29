import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# =========================
# 1. RYSOWANIE TRAJEKTORII
# =========================
drawing = []
is_drawing = False

fig, ax = plt.subplots()
ax.set_title("Draw trajectory (LPM)")
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

line_draw, = ax.plot([], [], 'k-')

def on_press(event):
    global is_drawing
    is_drawing = True
    drawing.clear()

def on_move(event):
    if is_drawing and event.xdata and event.ydata:
        drawing.append([event.xdata, event.ydata])
        d = np.array(drawing)
        line_draw.set_data(d[:,0], d[:,1])
        fig.canvas.draw()

def on_release(event):
    global is_drawing
    is_drawing = False
    plt.close()

fig.canvas.mpl_connect("button_press_event", on_press)
fig.canvas.mpl_connect("motion_notify_event", on_move)
fig.canvas.mpl_connect("button_release_event", on_release)

plt.show()

drawing = np.array(drawing)

# =========================
# 2. INTERPOLACJA
# =========================
N = 300
t = np.linspace(0, len(drawing)-1, N)

true = np.zeros((N,2))
true[:,0] = np.interp(t, np.arange(len(drawing)), drawing[:,0])
true[:,1] = np.interp(t, np.arange(len(drawing)), drawing[:,1])

# =========================
# 3. OKNO + SUWAKI
# =========================
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

ax.set_title("Kalman Filter - LIVE")
ax.set_xlim(np.min(true[:,0])-2, np.max(true[:,0])+2)
ax.set_ylim(np.min(true[:,1])-2, np.max(true[:,1])+2)

lt, = ax.plot([], [], 'g-', label="True")
lm, = ax.plot([], [], 'rx', alpha=0.4, label="Meas")
le, = ax.plot([], [], 'b-', label="Kalman")
ax.legend()

# =========================
# SUWAKI
# =========================
ax_noise = plt.axes([0.2, 0.25, 0.65, 0.03])
ax_q     = plt.axes([0.2, 0.20, 0.65, 0.03])
ax_r     = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_speed = plt.axes([0.2, 0.10, 0.65, 0.03])

s_noise = Slider(ax_noise, "Noise", 0.1, 2.0, valinit=0.6)
s_q     = Slider(ax_q, "Q (model)", 0.001, 0.2, valinit=0.02)
s_r     = Slider(ax_r, "R (meas)", 0.1, 5.0, valinit=0.6)
s_speed = Slider(ax_speed, "Speed", 0.5, 5.0, valinit=1.0)

# =========================
# MODEL
# =========================
dt = 1.0

F = np.array([[1,0,dt,0],
              [0,1,0,dt],
              [0,0,1,0],
              [0,0,0,1]])

H = np.array([[1,0,0,0],
              [0,1,0,0]])

def run():
    noise = s_noise.val
    Q = np.eye(4) * s_q.val
    R = np.eye(2) * s_r.val**2

    true_states = []
    meas = []

    x = np.array([true[0,0], true[0,1], 0, 0])

    for i in range(1, N):

        target = true[i]
        accel = (target - x[:2]) * 0.05

        x[2:] += accel
        x[:2] += x[2:] * dt * s_speed.val

        true_states.append(x.copy())
        meas.append(x[:2] + np.random.randn(2)*noise)

    true_states = np.array(true_states)
    meas = np.array(meas)

    # Kalman
    xk = np.zeros(4)
    P = np.eye(4)

    est = []

    for z in meas:

        xk = F @ xk
        P = F @ P @ F.T + Q

        y = z - H @ xk
        S = H @ P @ H.T + R
        K = P @ H.T @ np.linalg.inv(S)

        xk = xk + K @ y
        P = (np.eye(4) - K @ H) @ P

        est.append(xk.copy())

    return true_states, meas, np.array(est)

true_states, meas, est = run()

# =========================
# ANIMACJA
# =========================
def update(i):
    lt.set_data(true_states[:i,0], true_states[:i,1])
    lm.set_data(meas[:i,0], meas[:i,1])
    le.set_data(est[:i,0], est[:i,1])
    return lt, lm, le

ani = FuncAnimation(fig, update, frames=N, interval=30)

# =========================
# LIVE UPDATE SUWAKÓW
# =========================
def refresh(val):
    global true_states, meas, est
    true_states, meas, est = run()

s_noise.on_changed(refresh)
s_q.on_changed(refresh)
s_r.on_changed(refresh)
s_speed.on_changed(refresh)

plt.show()
