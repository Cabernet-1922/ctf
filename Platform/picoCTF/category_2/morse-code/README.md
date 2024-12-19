# morse-code [Medium] (by Will Hong) - picoCTF 2022
> <p>Morse code is well known. Can you decrypt this?</p>
<p>Download the file <a href='https://artifacts.picoctf.net/c/79/morse_chal.wav' download>here</a>.</p>
<p>Wrap your answer with picoCTF{}, put underscores in place of pauses, and use
all lowercase.</p>


View the waveform of the audio file in audacity, we see some morse code like graph: `.-- .... ....- --... .... ....- --... .... ----. ----- -.. .-- ..--- ----- ..- ----. .... --...`. Put it into online morse code decoder to get the message inside: `WH47H47H90DW20U9H7`.
This means `WHAT HATH GOD WROUGHT`. As description states, put underscore in place of pauses and use all lowercase: `wh47_h47h_90d_w20u9h7`

flag: `picoCTF{wh47_h47h_90d_w20u9h7}`