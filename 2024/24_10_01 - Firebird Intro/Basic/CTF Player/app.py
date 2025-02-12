import time
import os
import gc
gc.set_threshold(0)

def dialog(text):
   print(text)
   time.sleep(1)

class Brain:
   def __init__(self):
      self.short_term_memory = None
      self.long_term_memory = self
   def look(self, paper):
      self.short_term_memory = paper
   def remember(self):
      return self.long_term_memory

class Paper:
   def __init__(self, text):
      self.written = text

Your_brain = Brain()

print("God: I will tell you the flag, please destroy it as soon as you remember it.")
dialog("You: Ok, thanks god. I've been doing this challenge for 2 days straight.")

with open("flag.txt", "r") as f:
    Oracle = Paper(f.read()) # God is giving you the paper with flag, he made sure nothing else can read it.
os.setuid(1000)

Your_brain.look(Oracle)

dialog("*You threw away the paper*")
del Oracle

dialog("Your brain: Why am I still playing CTF... What am I doing with my life...")
dialog("Your brain: Ooo, this cat in the cat video is cute OwO")

time.sleep(3)
del Your_brain
dialog("You: Oh no, I forget the flag!! :O")
print("What will you do??")

try:
   while True:
      eval(input())
except Exception as err: 
   print("Try harder.")
