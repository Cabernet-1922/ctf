# Wordlands [483 points] (48 solves)
```bash
$ zsteg wordlands.png

b1,r,lsb,xy         .. text: "`$aedJIMe\"am"
b1,g,lsb,xy         .. text: "b*\"J Bkc"
b1,b,lsb,xy         .. file: PGP symmetric key encrypted data - Plaintext or unencrypted data
b1,b,msb,xy         .. text: ["Z" repeated 17 times]
b1,rgb,lsb,xy       .. file: Adobe Photoshop Image, 400 x 267, RGB, 3x 8-bit channels
b1,rgb,msb,xy       .. text: "(xxxxxxxxxxxxxxxxxx"
b1,bgr,lsb,xy       .. /var/lib/gems/3.2.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s': stack level too deep (SystemStackError)
        from /var/lib/gems/3.2.0/gems/iostruct-0.2.0/lib/iostruct.rb:167:in `inspect'
        from /var/lib/gems/3.2.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.2.0/gems/iostruct-0.2.0/lib/iostruct.rb:167:in `inspect'
        from /var/lib/gems/3.2.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.2.0/gems/iostruct-0.2.0/lib/iostruct.rb:167:in `inspect'
        from /var/lib/gems/3.2.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.2.0/gems/iostruct-0.2.0/lib/iostruct.rb:167:in `inspect'
        from /var/lib/gems/3.2.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
         ... 10066 levels...
        from /var/lib/gems/3.2.0/gems/zsteg-0.2.13/lib/zsteg.rb:26:in `run'
        from /var/lib/gems/3.2.0/gems/zsteg-0.2.13/bin/zsteg:8:in `<top (required)>'
        from /usr/local/bin/zsteg:25:in `load'
        from /usr/local/bin/zsteg:25:in `<main>'
```
It is easy to notice the line: `b1,rgb,lsb,xy       .. file: Adobe Photoshop Image, 400 x 267, RGB, 3x 8-bit channels`, then, try to extract the `.psd` file from the image:
```bash
zsteg -E b1,rgb,lsb,xy wordlands.png > extracted.psd
```
Use photoshop or photopea to open the file, and you can see the edit history of the lines (50 layers).

flag: `bronco{i_love_admiring_beautiful_winter_landscape}`