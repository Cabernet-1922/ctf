# plumbing [Medium] (by Alex Fulton/Danny Tunitis) - picoCTF 2019
> Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to <code>jupiter.challenges.picoctf.org 7480</code>.


`nc jupiter.challenges.picoctf.org <port> | grep -oP "picoCTF{.*}"` directly prints out the flag.

flag: `picoCTF{digital_plumb3r_06e9d954}`