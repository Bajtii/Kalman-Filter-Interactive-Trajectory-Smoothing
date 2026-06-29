# ✏️ Kalman Filter – Interactive 2D Trajectory Smoothing

An interactive Python project demonstrating how a **Kalman Filter** works in real time on a user-drawn trajectory.

Draw any path with your mouse and watch noisy measurements being transformed into a smooth estimated trajectory.

---

# 🎯 Features

- ✍️ Draw your own trajectory with the mouse
- 📉 Simulate realistic measurement noise
- 🧠 Apply Kalman filtering in real time
- 🎛️ Adjust filter parameters using sliders
- 🎬 Watch the estimation process as an animation

---

# 🖼️ Demo

## Drawing Input Trajectory

<img width="950" height="812" alt="image" src="https://github.com/user-attachments/assets/47ba1003-b462-4608-b071-1f100d3cdd23" />


## Kalman Filter Result

<img width="942" height="815" alt="image" src="https://github.com/user-attachments/assets/b287be02-db55-48af-9eaf-fe2ca382de2c" />


## Animation


https://github.com/user-attachments/assets/a5a1c4bb-06c9-4fd1-af0d-aa5c77d5a304


# 🧠 Why Kalman Filter?

The **Kalman Filter** is one of the most widely used algorithms for state estimation.

It is designed to:

- ✅ Remove measurement noise
- ✅ Estimate the true system state
- ✅ Predict future motion

### Real-world applications

- 🤖 Robotics and localization
- 🚗 Autonomous vehicles
- 🛰️ GPS tracking
- 🎮 Motion tracking systems
- ✈️ Navigation systems
- 📡 Sensor fusion

---

# ⚙️ How It Works

## State Representation

```text
x = [pos_x, pos_y, vel_x, vel_y]
```

## Motion Model

```text
F = |1 0 dt 0 |
    |0 1 0 dt |
    |0 0 1  0 |
    |0 0 0  1 |
```

## Measurement Model

```text
H = |1 0 0 0|
    |0 1 0 0|
```

---

# 🔄 Kalman Filter Algorithm

## Prediction

```text
x = F · x
P = F · P · Fᵀ + Q
```

## Update

```text
y = z − Hx
S = HPHᵀ + R
K = PHᵀS⁻¹
x = x + Ky
P = (I − KH)P
```

---

# 🎛️ Parameters

| Parameter | Description |
|-----------|-------------|
| **Noise** | Measurement noise level |
| **Q** | Process (model) uncertainty |
| **R** | Measurement uncertainty |
| **Speed** | Animation speed |

---

# 📊 Visualization

| Color | Meaning |
|-------|---------|
| 🟢 Green | True trajectory |
| 🔴 Red | Noisy measurements |
| 🔵 Blue | Kalman filter estimation |

---

# 🚀 Installation

```bash
pip install numpy matplotlib
```

---

# ▶️ Usage

Run the program:

```bash
python main.py
```

## Steps

1. Draw any trajectory using your mouse.
2. Release the mouse button.
3. Observe the noisy measurements.
4. Watch the Kalman filter estimate the smooth trajectory in real time.

---

# 🧩 Notes

- Increasing **R** means the filter trusts the measurements less.
- Increasing **Q** makes the model respond more aggressively to changes.
- The Kalman filter automatically balances prediction and measurement.

---

# 🔧 Possible Improvements

- 🚀 Add an acceleration model
- 📡 Simulate realistic GPS errors
- 📈 Plot estimation error over time
- 🤖 Apply the filter to robot localization
- 🎯 Support multiple motion models

---

# 📂 Project Structure

```text
.
├── main.py
├── images
│   ├── drawing.png
│   ├── result.png
│   └── demo.gif
├── README.md
└── requirements.txt
```

---

# 👨‍💻 Author

Educational project created to learn:

- Kalman Filtering
- State Estimation
- Dynamic Systems
- Sensor Fusion
- Scientific Computing with Python


A short GIF significantly improves the presentation of the repository.
