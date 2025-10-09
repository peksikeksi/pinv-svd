import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

path = "data\dog.jpeg"
img = Image.open(path).convert("L")
X = np.array(img, dtype=float)

U, S, Vt = np.linalg.svd(X, full_matrices=False)
print(f"Dimenzije: U={U.shape}, S={S.shape}, Vt={Vt.shape}")


def reconstruct_image(U, S, Vt, r):
    """Rekonstruiše sliku korišćenjem prvih r sing. vrednosti."""
    return U[:, :r] @ np.diag(S[:r]) @ Vt[:r, :]


r_vals = [10, 30, 150]

# Reconstructed images
#############################################################
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Original
axes[0, 0].imshow(X, cmap="gray")
axes[0, 0].set_title("Оригинална слика")
axes[0, 0].axis("off")

# Komprimovane slike
for ax, r in zip(axes.flat[1:], r_vals):
    Xr = reconstruct_image(U, S, Vt, r)
    ax.imshow(Xr, cmap="gray")
    ax.set_title(f"r = {r}")
    ax.axis("off")

plt.tight_layout()
plt.savefig("results/image_recons.png", dpi=200)
plt.close(fig)
plt.show()

# Singular vals vs rank
###############################################################
plt.figure(figsize=(7, 5))
plt.semilogy(S, linewidth=1.5, label="Singularne vrednosti")
plt.semilogy(r_vals, [S[r - 1] for r in r_vals], "o", label="r = 10, 30, 150")
plt.title("Сингуларне вредности у зависности од ранга r")
plt.xlabel("Ранг (r)")
plt.ylabel("Сингуларна вредност (логаритамска скала)")
plt.legend()
plt.grid(True)
plt.savefig("results/sigma_v_r.png", dpi=200)
plt.close(fig)
plt.show()

# Cumulative sum
##############################################################
cum_sum = np.cumsum(S) / np.sum(S)
plt.plot(np.arange(1, len(S) + 1), cum_sum * 100, label="Кумулативна енергија")

for r in [10, 30, 150]:
    plt.plot(r, cum_sum[r - 1] * 100, "o", label=f"r = {r}")

plt.xlabel("Ранг (r)")
plt.ylabel("Кумулативна сума (%)")
plt.title("Однос кумулативне суме и ранга r")
plt.legend()
plt.grid(True)
plt.savefig("results/cum_sum.png", dpi=200)
plt.close(fig)
plt.show()
