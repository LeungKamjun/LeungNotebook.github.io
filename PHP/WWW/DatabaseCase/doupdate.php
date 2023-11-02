<?php
//获取update.php的传值
$id = $_GET['id'];
$username = $_GET['username'];
$address = $_GET['address'];
$sex = $_GET['sex'];
$age = $_GET['age'];
//echo $sex;
//连接数据库
include_once 'database_connect.php';
//编写sql语句
 $sql = "update bbs_user set username ='$username' , address = '$address' , sex=".($sex==='男'?1:0) .", age=$age where id=$id";
$obj = mysqli_query($link, $sql);
//echo $sql;
if ($obj) {
//    exit("<script>alert('修改成功!');</script>");
    echo "<form action='userlist.php'><input type='submit' value='返回用户列表'></form>";
} else {
    echo '修改失败';
    echo mysqli_error($link);
}