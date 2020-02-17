<html>
<head>
    <title>
        JSJ Marketing Login Page
    </title>
</head>
<body>

    <div class="header">
    <p>JSJ Marketing Inventory</p>
    </div>

    <div class="container">
        <div class="logintext">
            <p>LOGIN AS</p>
        </div>
        <div class="flexcenter">
            <div>
                <br><img src="icons/admin.png" width="100" height="90">
                <div><a href="adminlogin.php">Admin</a></div>
            </div>
            <div>
                <br><img src="icons/cashier.png" width="100" height="90">
                <div><a href="cashierlogin.php">Cashier</a></div>
            </div>
        </div>
    </div>
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
        height: 40%;
    }
    .header {
        display: flex;
        flex-direction: column;
        font-size: 30;
        background: yellowgreen;
        width: 50%;
        margin: 0 auto;
        align-items: center;
        margin-bottom: 40px;
        font-family: Roboto;
    }
    a {
        font-family: Roboto;
        font-size: 20;
        color: teal;
    }
    a:hover {
        font-family: Roboto;
        font-size: 20;
        color: blue;
        
    }

</style>
</html>