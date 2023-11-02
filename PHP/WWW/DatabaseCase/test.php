<?php
include_once 'database_connect.php';
for ($i = 0; $i <= 100; $i++) {
    $sql = "insert into bbs_user(id,username,password,address,sex,age)values('$i','$i','$i','$i','$i','$i')";
    $obj = mysqli_query($link, $sql);
}

