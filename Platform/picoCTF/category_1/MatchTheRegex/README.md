# MatchTheRegex [Medium] (by Sunday Jacob Nwanyim) - picoCTF 2023
> <p>How about trying to match a regular expression</p>

Source code:
```javascript
function send_request() {
    let val = document.getElementById("name").value;
    // ^p.....F!?
    fetch(`/flag?input=${val}`)
        .then(res => res.text())
        .then(res => {
            const res_json = JSON.parse(res);
            alert(res_json.flag)
            return false;
        })
    return false;
}
```
where val is your input. There is a comment inside the code, it means we can use regex to match the flag format.
Payload: `picoCTF{.*}`

flag: `picoCTF{succ3ssfully_matchtheregex_08c310c6}`