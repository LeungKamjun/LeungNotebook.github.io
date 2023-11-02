<?php
$link = mysqli_connect('127.0.0.1', 'root', 'root');
mysqli_set_charset($link , 'utf8');
mysqli_select_db($link,'bbs');
$sql = "select * from bbs_user";
$res = mysqli_query($link,$sql);
$result = mysqli_fetch_assoc($res);
var_dump($result);
mysqli_close($link);