# login [Medium] (by BrownieInMotion) - picoMini by redpwn
> <p>My dog-sitter's brother made this website but I can't get in; can you help?</p>
<p><a href="https://login.mars.picoctf.net">login.mars.picoctf.net</a></p>

From the `index.js`:
```javascript
(async () => {
    await new Promise((e => window.addEventListener("load", e))),
    document.querySelector("form").addEventListener("submit", (e => {
        e.preventDefault();
        const r = {
            u: "input[name=username]",
            p: "input[name=password]"
        }
          , t = {};
        for (const e in r)
            t[e] = btoa(document.querySelector(r[e]).value).replace(/=/g, "");
        return "YWRtaW4" !== t.u ? alert("Incorrect Username") : "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" !== t.p ? alert("Incorrect Password") : void alert(`Correct Password! Your flag is ${atob(t.p)}.`)
    }
    ))
}
)();
```
We see the username `YWRtaW4` and password `cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ`, b64 decode the password will see the flag.

flag: `picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}`