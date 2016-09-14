<?php
if($_SERVER["REQUEST_METHOD"] == 'POST'){
	#echo 'hi';
	if($_POST['user'] == 'IwannaWatch' && $_POST['pass'] == 'SumMovies')
		echo 'GCTF{3ncryp7_y0ur_c0nn3c710n}';
		#echo 'watch sum movie with me m8!';
}

?>

<html>

<form method="post">
Login:<input type='text' name='user'>
Password: <input type='text' name='pass'>
<input type='submit'>
</form>


</html>
