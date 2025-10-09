# Python script for geometric visualization of SVD transformations
import numpy as np
import matplotlib.pyplot as plt

theta_V_deg = 45
theta_U_deg = -30
sigma1, sigma2 = 2.0, 0.8

# Convert angles from degrees to radians
theta_V = np.deg2rad(theta_V_deg)
theta_U = np.deg2rad(theta_U_deg)

V = np.array([[np.cos(theta_V), -np.sin(theta_V)], [np.sin(theta_V), np.cos(theta_V)]])
U = np.array([[np.cos(theta_U), -np.sin(theta_U)], [np.sin(theta_U), np.cos(theta_U)]])
Vt = V.T
Sigma = np.diag([sigma1, sigma2])

# Create circle
t = np.linspace(0, 2 * np.pi, 400)
circle = np.vstack((np.cos(t), np.sin(t)))

# Apply transformations
points_step1 = Vt @ circle
points_step2 = Sigma @ points_step1
points_step3 = U @ points_step2

steps = [
    (circle, "Јединични круг", np.eye(2)),
    (
        points_step1,
        f"Корак 1: после Vᵀ - почетна ротација {theta_V_deg}°",
        Vt @ np.eye(2),
    ),
    (
        points_step2,
        f"Корак 2: после Σ - скалирање (σ₁={sigma1}, σ₂={sigma2})",
        Sigma @ Vt @ np.eye(2),
    ),
    (
        points_step3,
        f"Корак 3: после U - коначна ротација {theta_U_deg}°)",
        U @ Sigma @ Vt @ np.eye(2),
    ),
]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

for ax, (pts, title, basis) in zip(axes, steps):
    ax.plot(pts[0], pts[1], linewidth=2)
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    for vec in basis.T:
        ax.arrow(
            0,
            0,
            vec[0],
            vec[1],
            head_width=0.05,
            length_includes_head=True,
            color="red",
        )
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(title)
    ax.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("results/svd_geometry.png", dpi=200)
plt.close(fig)
plt.show()
