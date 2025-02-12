# Closure [275 points] (12 solves)

```javascript
eval(function(p, a, c, k, e, d) {
    e = function(c) {
        return c.toString(36)
    };
    if (!''.replace(/^/, String)) {
        while (c--) {
            d[c.toString(a)] = k[c] || c.toString(a)
        }
        k = [function(e) {
            return d[e]
        }];
        e = function() {
            return '\\w+'
        };
        c = 1
    };
    while (c--) {
        if (k[c]) {
            p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c])
        }
    }
    return p
}('v 9=["\\b\\e\\j\\b\\i","\\w\\c\\7\\d\\8\\l\\7\\u\\d\\l\\k\\e\\h\\g","\\k\\e\\h\\g\\s\\p\\o\\7\\7\\a\\c\\f\\b\\e\\j\\b\\i\\f\\h\\e\\d\\8\\7\\f\\n\\a\\8\\8\\d\\b\\7\\f\\m\\8\\a\\c\\g\\x","\\n\\a\\8\\8\\d\\b\\7","\\m\\8\\a\\c\\g","\\a\\c","\\p\\o\\7\\7\\a\\c"];$(9[6])[9[5]](9[0],r(){t(q(9[1])==9[2]?9[3]:9[4])})', 34, 34, '|||||||x74|x72|_0x7177|x6F|x63|x6E|x65|x6C|x5F|x67|x61|x6B|x69|x66|x20|x57|x43|x75|x62|prompt|function|x7B|alert|x68|var|x45|x7D'.split('|'), 0, {}))
```
Try to find out the mapping of these alphabets:
```text
\\b\\e\\j\\b\\i
\\w\\c\\7\\d\\8\\l\\7\\u\\d\\l\\k\\e\\h\\g
"\\k\\e\\h\\g\\s\\p\\o\\7\\7\\a\\c\\f\\b\\e\\j\\b\\i\\f\\h\\e\\d\\8\\7\\f\\n\\a\\8\\8\\d\\b\\7\\f\\m\\8\\a\\c\\g\\x"
\\n\\a\\8\\8\\d\\b\\7
\\m\\8\\a\\c\\g
\\a\\c
\\p\\o\\7\\7\\a\\c
```
```text
\\b\\e\\j\\b\\i -> "click"
b -> c
e -> l
j -> i
b -> c
i -> k

\\w\\c\\7\\d\\8\\l\\7\\u\\d\\l\\k\\e\\h\\g -> "Enter the flag"
w -> E
c -> n
7 -> t
d -> e
8 -> r
l -> (space)
7 -> t
u -> h
d -> e
l -> (space)
k -> f
e -> l
h -> a
g -> g

\\n\\a\\8\\8\\d\\b\\7 -> "Correct"
n -> C
a -> o
8 -> r
8 -> r
d -> e
b -> c
7 -> t

\\m\\8\\a\\c\\g -> "Wrong"
m -> W
8 -> r
a -> o
c -> n
g -> g

\\a\\c -> "on"
a -> o
c -> n

\\p\\o\\7\\7\\a\\c -> "button"
p -> b
o -> u
7 -> t
7 -> t
a -> o
c -> n
```
With the mapping is enough to map the flag:
```text
\\k\\e\\h\\g\\s\\p\\o\\7\\7\\a\\c\\f\\b\\e\\j\\b\\i\\f\\h\\e\\d\\8\\7\\f\\n\\a\\8\\8\\d\\b\\7\\f\\m\\8\\a\\c\\g\\x
flag{button_click_alert_Correct_Wrong}
```

