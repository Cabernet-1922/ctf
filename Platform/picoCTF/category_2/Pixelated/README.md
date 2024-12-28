# Pixelated [Medium] (by Sara) - picoCTF 2021
> I have these 2 images, can you make a flag out of them? <a href='//mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled1.png'>scrambled1.png</a> <a href='//mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled2.png'>scrambled2.png</a>

```python
import cv2
import numpy as np

image1 = cv2.imread("scrambled1.png", cv2.IMREAD_UNCHANGED)
image2 = cv2.imread("scrambled2.png", cv2.IMREAD_UNCHANGED)
combined_image = (image1.astype(float) + image2.astype(float)) / 2
combined_image = combined_image.astype(np.uint8)

b, g, r = cv2.split(combined_image)
xor_image = cv2.bitwise_xor(b, cv2.bitwise_xor(g, r))
_, processed = cv2.threshold(xor_image, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("revealed_flag.png", processed)
```

flag: `picoCTF{0542dc1d}`