
<?php


$mysqli = new mysqli('localhost', 'root', "", 'shopping') or die (mysqli_error($mysqli));
$id = 0;
$update = false;
$item = '';
$quantity = '';
$price = '';
$weight = '';




if(isset($_POST['save'])){
    $item = $_POST['item'];
    $quantity = $_POST['quantity'];
    $price = $_POST['price'];
    $weight = $_POST['weight'];
    
    $mysqli->query("INSERT INTO products(item, quantity, price, weight) VALUES('$item', '$quantity', '$price', '$weight')") or die ($mysqli->error);

    header("location: cashier.php");
   
    
}


if (isset($_GET['edit'])) {
    $id = $_GET['edit'];
    $update = true;
    $result = $mysqli->query("SELECT * FROM products WHERE id =$id") or die($mysqli->error());
   
    if (array($result) !==null) {
        $row = $result->fetch_array();
        $item = $row['item'];
        $quantity = $row['quantity'];
        $price = $row['price'];
        $weight = $row['weight'];
    }
}

if (isset($_POST['update'])){
     $id = $_POST['id'];
     $item = $_POST['item'];
     $quantity = $_POST['quantity'];
     $price = $_POST['price'];
     $weight = $_POST['weight'];

     $mysqli->query(" UPDATE products SET item='$item', quantity='$quantity', price='$price', weight='$weight' WHERE id =$id") or die ($mysqli->error) ;

     header("location: cashier.php");
     ob_end_flush();
}

?>

