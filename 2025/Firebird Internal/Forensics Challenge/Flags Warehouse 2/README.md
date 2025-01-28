# Flags Warehouse 2 [794 points] (6 solves)
Unzip the `.docx` file, open `/word/document.xml` can reveal a bunch of flags and its own ids: `paraId`, `textId`, `rsidR`, `rsidRDefault`, `rsidP`. After browse all the ids and flags, it's easy to notice that there is only one flag, that `rsidR`, `rsidRDefault`, `rsidP` are different.

```python
import re
import numpy as np


def extract_ids(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    id_pattern = r'w14:paraId="([^"]*)" w14:textId="([^"]*)" w:rsidR="([^"]*)" w:rsidRDefault="([^"]*)" w:rsidP="([^"]*)"'
    flag_pattern = r'((?:firebird|fakebird){[^}]*})'

    id_matches = re.finditer(id_pattern, content)
    flag_matches = re.finditer(flag_pattern, content)
    id_ = np.zeros([30000,5],dtype='object')

    for index, match in enumerate(id_matches):
        id_[index] = [
            match.group(1),  # paraId
            match.group(2),  # textId
            match.group(3),  # rsidR
            match.group(4),  # rsidRDefault
            match.group(5),  # rsidP
        ]
    flag_ = np.array([match.group(1) for match in flag_matches])
    
    mask = np.all(id_ == id_[id_[:,3]!=id_[:,4]], axis=1)
    complete_rows = np.where(mask)[0]
    print(flag_[complete_rows][0])


extract_ids('document.xml')
```

