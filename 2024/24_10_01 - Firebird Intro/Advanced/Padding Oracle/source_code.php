<?php

include("config.php");

register_shutdown_function('finish');

function finish(){
    echo('<p><a href="index.php">Get a new token</a></p>');
    echo('<p><a href="index.php?-s">Show Source</a></p>');
}

if(isset($_GET['-s'])){
    highlight_file(__FILE__);
    die();
}

$key = $config["key"];
$enc_algorithm = MCRYPT_RIJNDAEL_128;
$enc_mode = MCRYPT_MODE_CBC;
$block_size = mcrypt_get_block_size($enc_algorithm, $enc_mode);    //16

//Padding with PKCS#7
function appendPad($msg, $block_size){
    $pad = $block_size - (strlen($msg) % $block_size);
    return $msg . str_repeat(chr($pad), $pad);

}

//Convert string to hex array
function str2hex($x){
    $y = '';
    for($i=0; $i<strlen($x); $i++){
        $y .= substr('0'.dechex(ord(substr($x, $i, 1))), -2);
    }
    return $y;
}

//Convert hex array to string
function hex2str($x){
    $y = '';
    for($i=0; $i<strlen($x); $i+=2){
        $y .= chr(hexdec(substr($x, $i, 2)));
    }
    return $y;
}

if(!isset($_GET['token'])){
    $iv = mcrypt_create_iv($block_size, MCRYPT_RAND);
    $plaintext = appendPad("Guest", $block_size);
    $ciphertext = mcrypt_encrypt($enc_algorithm, $key, $plaintext, $enc_mode, $iv);
    $token = str2hex($iv) . str2hex($ciphertext);
    header("Location: index.php?token=".$token);
    die();
}else{
    $t = $_GET['token'];
    if(strlen($t) % 32 != 0 || strlen($t) < 32 || preg_match('/^[0-9a-f]+$/', $t) == 0){
        die("Error!");
    }

    $iv = hex2str(substr($t, 0, 32));
    $ciphertext = hex2str(substr($t, 32));
    $plaintext = mcrypt_decrypt($enc_algorithm, $key, $ciphertext, $enc_mode, $iv);

    //Check padding error
    $pad_error = false;
    $last_pad = ord(substr($plaintext, -1));
    if($last_pad >= 1 && $last_pad <= $block_size){
        for($i=1; $i<=$last_pad; $i++){
            if(ord(substr($plaintext, -$i, 1)) != $last_pad){
                $pad_error = true;
                break;
            }
        }
    }else{
        $pad_error = true;
    }

    if($pad_error){
        die("Error!");
    }else{
        $msg = substr($plaintext, 0, strlen($plaintext) - $last_pad);
        echo("Welcome, " . $msg . "<br />");
        if($msg == "Admin"){
            echo("The flag is " . $config["flag"]);
        }
    }

}

?>