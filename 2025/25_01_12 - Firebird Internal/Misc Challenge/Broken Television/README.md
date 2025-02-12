# Broken Television [611 points] (9 solves)
Extract all the frame to a folder, and easy to notice that the first frame scroll up one row of pixel to second frame. Also, a small square area in the frame changed when switch from first frame to second frame. Assume there is `f` row in each frame, then `frame_1[1:]` and `frame[:f-1]` will have all same pixels except that square area. Xor the two frame to get a QR-code.
```python
import cv2

video = cv2.VideoCapture('tv.mp4')
frames = []

for _ in range(2):
    ret, frame = video.read()
    frames.append(frame)
video.release()
f = frames[0].shape[0] # 216
cv2.imwrite("out.jpg",cv2.bitwise_xor(frames[0][1:], frames[1][:f-1]))
```