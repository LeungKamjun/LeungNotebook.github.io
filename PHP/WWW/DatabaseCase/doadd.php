<?php
//获取add.php的传值
$username = $_GET['username'];
$password = $_GET['password'];
$address = $_GET['address'];
$sex = $_GET['sex'];
$age = $_GET['age'];
// 连接数据库
include_once 'database_connect.php';
$sql = "insert into bbs_user(username,password,address,sex,age)values('$username','$password','$address'," . ($sex === '男' ? 1 : 0) . ",'$age')";
$obj = mysqli_query($link, $sql);
$result = mysqli_insert_id($link);
$id = $result;
if ($id) {
//    exit("<script>alert('修改成功!');</script>");
    echo "<form action='userlist.php'><input type='submit' value='返回用户列表'></form>";
} else {
    echo '修改失败';
    echo mysqli_error($link);
}
