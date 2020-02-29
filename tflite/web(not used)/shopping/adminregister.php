<?php include('adminserver.php') ?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="style2.css">
	<title>Admin Register</title>

</head>
<body>
	<div class="header">
    <a href="home.php" id="home">JSJ Marketing Inventory</a>
    </div>

	<div class="container">
        <div class="logintext">
        </div>
        <div class="flexcenter">
	<div class="headerr">
		<br><img src="icons/admin.png" width="80" height="70">
		<h2>Admin Register</h2>
	</div>
	
	<form method="post" action="adminregister.php">

		<?php include('errors.php'); ?>

		<div class="input-group">
			<label>Username</label>
			<input type="text" name="username" value="<?php echo $username; ?>">
		</div>
	
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="password_1">
		</div>
		<div class="input-group">
			<label>Confirm password</label>
			<input type="password" name="password_2">
		</div><br>
		<div class="input-group">
			<button type="submit" class="btn" name="reg_user">Register</button>
		</div>
		<p>
			<br>Already a member? <a href="adminlogin.php">Sign in</a>
		</p>
	</form>
</body>
<style> 
	.flexcenter{
        display: flex;
        justify-content: space-around;
    }
    .logintext{
        display: flex;
        background: yellowgreen;
        justify-content: center;
        font-family: Roboto;
    }

    .container {
        flex-direction: column;
        border: 3px solid yellowgreen;
        width: 30%;
        margin: 0 auto;
        height: 45%;
    }
    .header {
        display: flex;
        flex-direction: column;
        font-size: 30;
        background: yellowgreen;
        width: 50%;
		height: 50px;
        margin: 0 auto;
        align-items: center;
        margin-bottom: 50px;
        font-family: Roboto;
		text-align: center;
		color:red;
    }
    #signup {
        font-family: Roboto;
        font-size: 20;
        color: teal;
    }
    #signup:hover {
        font-family: Roboto;
        font-size: 20;
        color: blue;
	}
	#home {
		color: black;
	}
    .btn {
		border-radius: 12px;
		padding: 5px;
		background-color: #04e300;
		color: black;
	}

</style>
</html>