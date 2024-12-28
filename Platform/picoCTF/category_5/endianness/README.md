# endianness [Easy] (by Nana Ama Atombo-Sackey) - picoCTF 2024
> <p>Know of little and big endian?</p>
<p><a href='https://artifacts.picoctf.net/c_titan/116/flag.c' download>Source</a></p>

After you get the `word` that remote server send you, \
little endian: `echo <word> | rev | xxd -p`
big endian: `echo <word> | xxd -p`

flag: `picoCTF{3ndi4n_sw4p_su33ess_91bc76a4}`