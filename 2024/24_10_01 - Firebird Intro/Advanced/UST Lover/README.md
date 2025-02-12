# UST Lover [375 points] (5 solves)
First, use tool like [wavacity](https://wavacity.com/) to view the waveform of `.wav` file, and you can see something interesting. There are short and slightly longer bar, the intuitive idea is that it might represent the morse code, and we indeed get the message after decoding it. \
Morse code: `----- -..- .. .-.. --- ...- . ..- ... - -..- -----` \
The message is `0XILOVEUSTX0`, which is quite related to the challenge name, this might be the password of a compressed file.

Then, we put the `ust.png` into [aperisolve](www.aperisolve.com), then can see the first half of the flag is in the lower right corner, concatenate with the `0XILOVEUSTX0` ~~should be the flag(?~~