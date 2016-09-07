<html>
	<head>
		<title>RIP Harambe</title>
		<script>
			function validateform(event) {
				event.preventDefault();
				alert('FORM\'S DISABLED! STOP TRYING');
				return false;
			}
		</script>
		<style>
			.full-comment{
				border: 1px solid black;
				width: 100%;
				margin: 10px 0;
			}
			.name, .comment{
				margin: 3px;
			}
		</style>
	</head>
	<body>
		<div style="width: 50%; margin:auto;">
			<img src="Harambe.jpg" alt="Harambe" style="display: block; margin:auto"/>
			<h1 style="text-align:center">Harambe did nothing wrong.</h1>
			<div class="guestform">
			<h3>Leave your petition here</h3>
			<?php

			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				echo 'Well done, here is your flag: GCTF{n0_53cur17y_by_0b5cur17y}';
			}

			?>
			<h4>Someone keeps posting stupid comments, so the form is disabled for now.</h4>
<!-- 			<form method="POST" onsubmit="validateform(event);">
				<div style="margin-bottom:5px">
					Name: <input type="text" name="name"/>
				</div>
				<div style="margin-bottom:5px">
					Comment:<br/>
					<textarea rows="4" cols="50" name="comment"></textarea>
				</div>
				<button type="submit">Submit</button>
			</form> -->
			<div>
				<div class="full-comment">
					<div class="name">
						<strong>Name</strong>: Lucy
					</div>
					<div class="comment">
						<strong>Comment</strong>:<br/>
						<div>
							He died doing what he loved. Kidnapping children.
						</div>
					</div>
				</div>
				<div class="full-comment">
					<div class="name">
						<strong>Name</strong>: Qiurong
					</div>
					<div class="comment">
						<strong>Comment</strong>:<br/>
						<div>
							This is stupid. You are stupid. This website is stupid.
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>