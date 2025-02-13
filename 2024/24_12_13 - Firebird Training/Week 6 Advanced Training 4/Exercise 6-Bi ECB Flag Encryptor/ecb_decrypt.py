import cv2
from hashlib import sha256
import numpy as np

colors = [b"\x00" * 16, b"\xff" * 16]
color_index = 0

ciphers = {
    # Storing the previously seen and the next ciphertexts and corresponding colors
}

image = cv2.imread("encrypted.png", cv2.IMREAD_GRAYSCALE)
shape = image.shape
image = image.flatten()
image = bytes(image)
decrypted = b""

for i in range(0, len(image), 16):
    block = image[i : i + 16]
    if block not in ciphers:
        decrypted += colors[color_index]
        ciphers[block] = colors[color_index]
        color_index += 1
    else:
        decrypted += ciphers[block]
    ciphers[sha256(block).digest()[:16]] = ciphers[block]

decrypted = np.array(list(decrypted))
decrypted = decrypted.reshape(shape)
cv2.imwrite("decrypted.png", decrypted)

# 00000000 -> abcdef -> 123456 -> abdfgh -> ...