<?php

    
    ob_start();
    session_start();

     if(isset($_SESSION['id']) && isset($_SESSION['comp_name']))
    {
    }
    else
    {
        header('Location: login.php');
    }

    include('head.php');
    include('functions.php');

    $users = getUsers($_SESSION['comp_name']);

?>

<html>
    <head>

    </head>
    <body>
        <h1 style="font: Bold 32px Montserrat; color: #1C2759">Welcome to UserManager!</h1>
        <h2 class="ms-bold-22">Users of <?php echo $_SESSION['comp_name']?></h2>
        <table>
            <thead>
                <th>Name</th>
                <th>Surname</th>
                <th>Email</th>
            </thead>
            <tbody>
            <?php foreach ((array)$users as $user): ?>
                <tr id="row_user_<?php echo($user['id']) ?>">
                    <td><?php echo($user['name'])?></td>
                    <td><?php echo($user['surname'])?></td>
                    <td><?php echo($user['email'])?></td>
                </tr>
            <?php endforeach; ?>
            </tbody>
        </table>
    </body>
</html>