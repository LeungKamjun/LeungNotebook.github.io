<?php
include_once "database_connect.php";
echo '这里是删除id为' . $_GET['id'] . '的界面';
$sql = 'delete from bbs_user where id='.$_GET['id'];
$obj = mysqli_query($link,$sql);
if ($obj){
    exit("<script>alert('删除成功!');location.href='".$_SERVER["HTTP_REFERER"]."';</script>");
}else{
    echo '删除失败';
    echo mysqli_error($link);
}
mysqli_close($link);

