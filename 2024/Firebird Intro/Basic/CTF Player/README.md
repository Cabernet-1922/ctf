# CTF Player [250 points] (7 solves)
This challenge is about gc collector, we can notice this by the imported gc library.
Flag is written in the paper, then the paper is stored in the short term memory.
The paper and brain is subsequently deleted, however the object still exists in memory due to `gc.set_threshold(0)`, since it simply prevents python from automatically cleaning up unused objects.
So it is still exist in memory and can be found in gc collector.

```python
print([x.written for x in gc.get_objects() if isinstance(x, Paper)][0])
```
`gc.get_objects()` return all objects in memory, since the list is very long, we need `isinstance(x, Paper)` to filter out all the unneeded object and find the Paper object to get our flag.
`x.written` help us get the text store in the Paper object. Without it, we can only get the object but not the text we want.
[0] can be ignored, but it simply means get the one and only one we found in the list.