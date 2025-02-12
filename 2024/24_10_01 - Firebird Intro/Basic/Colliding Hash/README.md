# Colliding Hash [275 points] (10 solves)
```php
<?php

include("config.php");

register_shutdown_function('finish');

function finish(){
    echo('<p><a href="index.php?-s">Show Source</a></p>');
}

if(isset($_GET['-s'])){
    highlight_file(__FILE__);
    die();
}

if(isset($_GET['hash'])){
  if($_GET['hash'][0]!=$_GET['hash'][1] && md5($_GET['hash'][0])==md5($_GET['hash'][1])){    
    echo("The flag is " . $config["flag"]);
  }
}

?>
```
The source code perform a main function that if two hash value is not the same but has equal MD5 hash, the page will show the flag variable.
`/index.php?hash[]=240610708&hash[]=QNKCDZO` will successfully show the flag in the page.



reference:
https://stackoverflow.com/questions/22140204/why-md5240610708-is-equal-to-md5qnkcdzo
https://www.mscs.dal.ca/~selinger/md5collision/