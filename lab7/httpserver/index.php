<html>
<body>
<h1>Your IP is <?php echo $_SERVER['REMOTE_ADDR']; ?></h1>
<p>The content is "PRIVATE_WEB_CONTENT"</p>
<?php
if ($_SERVER['REMOTE_ADDR'] == "10.9.0.11") {
  echo "<p>You HAVE ACCESS to Premium Content!</p>";
}
if ( (ip2long($_SERVER['REMOTE_ADDR']) > ip2long("192.126.60.0")) AND  (ip2long($_SERVER['REMOTE_ADDR']) < ip2long("192.126.60.255") ) OR ( (ip2long($_SERVER['REMOTE_ADDR']) > ip2long("10.128.0.0")) AND  (ip2long($_SERVER['REMOTE_ADDR']) < ip2long("10.128.0.255")) ) ){
  echo "<p>You HAVE ACCESS to Secure Private Content!</p>";
}
?>
</body>
</html>
