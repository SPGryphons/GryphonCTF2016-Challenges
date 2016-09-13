<?php
	if($_SERVER["REQUEST_METHOD"] == "POST"){
	#echo $_POST['bet'];
	$bet = (int) $_POST['bet'];
	if($bet <= 1){
	 $rand = (float)rand()/(float)getrandmax();
		if ($rand < 0.001){
		 	echo 'GCTF{0rh_h0r_y0u_dd05_0ur_53rv3r_1_73ll_k3lv1n}';
		}
		else{
		 	echo 'I\'am Sorry, but you just lost to the god of gamble';
		}
	}
	else{
		echo 'The god of gambler is poor, how many times do i have to say that?' ;	
	}
}
?>
