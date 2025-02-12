# Escape Again (PPC) [200 points] (30 solves)
There are 10 rooms in this challenge. Each room will have 1+x**5 doors but only one is real. 
You need to click the right door in each of the rooms, total time limit is 30 seconds.
If we view the source code of the page, we can find that the real door has id `exit`, and each room only has one door carrying this tag.

Put below javascript into a bookmark, and click it by interval(not too fast).
```javascript
javascript:document.querySelector("#exit").click()
```