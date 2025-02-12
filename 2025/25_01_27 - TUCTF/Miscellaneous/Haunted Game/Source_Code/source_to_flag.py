import cv2
import numpy as np
import os
from collections import Counter
import soundfile as sf

audio_list = [i for i in os.listdir("AudioClip") if os.path.splitext(i)[-1] == ".ogg"]
texture_list = [i for i in os.listdir("Texture2D") if
                os.path.splitext(i)[0] + ".ogg" in audio_list]


def get_most_common_color(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pixels = img_rgb.reshape(-1, 3)
    pixels_tuples = [tuple(pixel) for pixel in pixels if not (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0)]
    color_counts = Counter(pixels_tuples)
    most_common_color = color_counts.most_common(1)[0][0]
    return most_common_color


def get_average_alpha(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img.shape[-1] == 4:
        alpha_channel = img[:, :, 3]
        average_alpha = np.mean(alpha_channel)
    else:
        average_alpha = 255
    return average_alpha


def split_audio(input_file):
    data, samplerate = sf.read(input_file)
    part_length = len(data) // 3
    part1 = data[:part_length]
    part2 = data[part_length:2 * part_length]
    part3 = data[2 * part_length:]
    return part1, part2, part3, samplerate


os.chdir("Texture2D")
hash_ = dict()
for i in range(len(texture_list)):
    alpha = get_average_alpha(texture_list[i])
    hash_[texture_list[i]] = {"alpha": alpha}
hash_ = dict(sorted(hash_.items(), key=lambda x: -x[1]['alpha']))

data_ = []

for i in hash_.keys():
    colour = get_most_common_color(i)
    hash_[i]["c"] = colour
    os.chdir("../AudioClip")
    audio_ = split_audio(os.path.splitext(i)[0] + ".ogg")
    hash_[i]["c"] = sorted([[hash_[i]["c"][j], audio_[j]] for j in range(3)], key=lambda x: x[0])
    samplerate = audio_[-1]
    for k, part in enumerate(hash_[i]["c"], 1):
        data_.append(part[1])
    os.chdir("../Texture2D")

merged = np.concatenate(data_)
sf.write("../res.wav", merged, samplerate)