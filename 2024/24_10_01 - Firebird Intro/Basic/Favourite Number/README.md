# Favourite Number [225 points] (18 solves)
The favourite number we want is `-2147483648`, let go through the 5 if statement one by one.
`n % 2` this will return 0, since `2147483648` is indeed a even number.
`n % 3` this will return -2 instead of 0, 1, 2.
`abs(n) != n` this will return `-2147483648` instead of the expected `2147483648`, this is because `+2147483648` cannot be represented in a 32-bit signed integer, as we know max is `+2147483647`.
 
Therefore, `-2147483648` is the only number that can pass the check.