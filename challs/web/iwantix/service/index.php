<?php
	#Set Cookie
	setcookie('currentTime',time(),time()+3600);;
	
	#Get cookie
	$time = $_COOKIE['currentTime'];
	
	#echo $time;

	# If time is more than Nov 7th. time to give sum flags yo
	if($time >= 1478476800){

?>

<html>
<p> <img src='eason.jpg'> </p>
<p> Wow!! Amazing!! You can get your tickets now!!! </p>
<?php echo 'GCTF{cl13n751d3_'; ?>
<p> Hmm... It's just half of the flag.. Where's the other half? </p>

<form method='post' id='niceform' action='flag.php'></form>

<button type='submit' disabled='true' form='niceform'>Buy ticket</button>


</html>

<?php
}
else{
?>

<html>
<p>Sorry,concert ticket not for sales yet</p>
<p>BUTTT YOU CAN LISTEN TO SOME OF HIS MUSIC!</p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/UdWlBBqiC7I" frameborder="0" allowfullscreen></iframe>
</html>

<?php
}
?>


