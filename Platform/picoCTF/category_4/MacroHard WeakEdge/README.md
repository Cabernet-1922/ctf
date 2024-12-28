# MacroHard WeakEdge [Medium] (by madStacks) - picoCTF 2021
> I've hidden a flag in this file. Can you find it? <a href='//mercury.picoctf.net/static/2e739f9e0dc9f4c1556ea6b033c3ec8e/Forensics is fun.pptm'>Forensics is fun.pptm</a>

unzip the `.pptm` file and in the folder `\ppt\slideMasters`, the file `hidden` caught our attention, simply b64 decode the content inside to get the flag.
`Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q` -> `flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}`

flag: `picoCTF{D1d_u_kn0w_ppts_r_z1p5}`