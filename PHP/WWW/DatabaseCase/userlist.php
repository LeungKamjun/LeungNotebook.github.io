<?php
// 连接数据库
include_once "database_connect.php";
// 查询用户表数据
$sql = "select * from bbs_user";
$obj = mysqli_query($link, $sql); //返回结果集对象
//$res = mysqli_fetch_assoc($obj);
//print_r($res);
//HTML部分
echo '<table width="600" border="1" align="left" >';
    echo '<th>编号</th><th>用户名</th><th>地址</th><th>性别</th><th>年龄</th><th>操作</th>';
    while ($res = mysqli_fetch_assoc($obj)) {
        echo '<tr>';
        echo '<td>' . $res['id'] . '</td>';
        echo '<td>' . $res['username'] . '</td>';
        echo '<td>' . $res['address'] . '</td>';
        echo '<td>' . ($res['sex'] == 1 ? '男' : '女') . '</td>';
        echo '<td>' . $res['age'] . '</td>';
        echo '<td>' . '<a href="delete.php?id=' . $res['id'] . '">删除</a>/<a href="update.php?id=' . $res['id'] . '">修改</a>';
        echo '</tr>';
    }
echo '</table>';
echo '<a href="add.php">添加</a>';

mysqli_close($link);