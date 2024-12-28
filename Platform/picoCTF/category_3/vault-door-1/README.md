# vault-door-1 [Medium] (by Mark E. Haase) - picoCTF 2019
> This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: <a href='//jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java'>VaultDoor1.java</a>

```java
class Main {
    public static void main(String[] args) {
        char[] password = new char[32];
        
        password[0]  = 'd';
        password[29] = '9';
        password[4]  = 'r';
        password[2]  = '5';
        password[23] = 'r';
        password[3]  = 'c';
        password[17] = '4';
        password[1]  = '3';
        password[7]  = 'b';
        password[10] = '_';
        password[5]  = '4';
        password[9]  = '3';
        password[11] = 't';
        password[15] = 'c';
        password[8]  = 'l';
        password[12] = 'H';
        password[20] = 'c';
        password[14] = '_';
        password[6]  = 'm';
        password[24] = '5';
        password[18] = 'r';
        password[13] = '3';
        password[19] = '4';
        password[21] = 'T';
        password[16] = 'H';
        password[27] = '5';
        password[30] = '2';
        password[25] = '_';
        password[22] = '3';
        password[28] = '0';
        password[26] = '7';
        password[31] = 'e';
        
        System.out.println("picoCTF{" + new String(password) + "}");
    }
}
```

flag: `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}`