# Homework 3-Aii Memory Hero [100 points] (6 solves)

First, use IDA to export all the nodes as text file. Initially, there should be approximately 2–3 million routes, but after eliminating the dead-ends that will jump to "fail code", there will be still 280k routes. Also, one of the three origin points may be removed since it will always lead to a dead-end. Then all the potential routes/fake flags are input into fai_check.py, and the correct flag will eventually be generated after approximately five minutes of runtime.
```python
import re
with open("fai.asm") as f:
    text = f.readlines()


node_list = ["node"+str(i)+":" for i in range(454)]
pointer = 0
for i in range(len(node_list)):
    loop_again = True
    temp = ""
    while loop_again == True:
        if node_list[i] in text[pointer]:
            while "fail_code" not in text[pointer]:
                if re.findall("node[0-9]*",text[pointer]):
                    temp += re.findall("node[0-9]*",text[pointer])[0].replace("node","")+" "
                pointer += 1
            node_list[i] = temp.rstrip(" ")
            loop_again = False
            continue
        else:
            pointer += 1
            if pointer < 7695:  
                loop_again = True
            else:
                    break
        
hash_ = dict()
for i in node_list:
    temp = i.split(" ")
    if len(temp) > 1:
        hash_[temp[0]] = temp[1:]
    else:
        hash_[temp[0]] = None

hash_['454'] = ["End"]

while None in hash_.values():
    for i in hash_:
        if hash_[i] == None:
            # print(i)
            for j in hash_:
                if hash_[j] and (i in hash_[j]):
                    hash_[j].remove(i)
                    # 
    for k in list(hash_.keys()):
        if hash_[k] == None:
            del hash_[k]
        elif hash_[k] == []:
            hash_[k] = None
# print(hash_)
print(len(hash_))


import subprocess
from fai_check import *
# Path to your executable file
exe_path = "D:\\Desktop\\fai.exe"

# Start the process
def haha(a):
    process = subprocess.Popen(
        exe_path,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=a)
    flag = stdout.split('\n')[2]
    if main(flag) == "UwU":
        print(flag)
        exit()


from collections import deque
data = hash_
start_keys = [ '60', '220']  
all_routes = []
stack = deque()
for key in start_keys:
    if key in data:
        stack.append( ([key], set([key])) )
    else:
        print(f"Start key {key} not found in data.")
while stack:
    current_route, visited = stack.pop()
    current_key = current_route[-1]
    next_keys = data.get(current_key)

    if next_keys is None:
        all_routes.append(current_route)
        continue

    if 'End' in next_keys:
        all_routes.append(current_route)  # Without 'End'
        haha('\n'.join(current_route))
        continue

    for key in next_keys:
        if key == 'End':
            all_routes.append(current_route)
            continue
        if key not in visited:
            new_route = current_route + [key]
            new_visited = visited.copy()
            new_visited.add(key)
            stack.append( (new_route, new_visited) )
        else:
            continue

# print(f"Total number of routes found: {len(all_routes)}")
```
