<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<!-- START OF GENERIC HEAD IMPORT -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="js/jquery-1.12.3.min.js"></script>
<link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>URL Shortener</title>
</head>
<body>
	<nav class="navbar navbar-default">
	  <div class="container">
	    <!-- Brand and toggle get grouped for better mobile display -->
	    <div class="navbar-header">
	      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
	        <span class="sr-only">Toggle navigation</span>
	        <span class="icon-bar"></span>
	        <span class="icon-bar"></span>
	        <span class="icon-bar"></span>
	      </button>
	      <a class="navbar-brand" href=".">URL Shortener</a>
	    </div>
	  </div><!-- /.container-fluid -->
	</nav>
	<div class="container">
		<%	if (session.getAttribute("error") != null) {%>
			<div class="alert alert-danger" role="alert">
				<strong>Error!</strong> <%= session.getAttribute("error") %>
			</div>
		<%	session.removeAttribute("error");} %>
		<%	if (session.getAttribute("success") != null) {%>
			<div class="alert alert-success" role="alert">
				<strong>Success!</strong> <%= session.getAttribute("success") %>
			</div>
		<%	} session.removeAttribute("success"); %>
		<h1>
			Shorten all your URLs here!
		</h1>
		<hr>
		<form action="Shorten" method="POST">
	  		<div class="form-group">
	    		<label for="inputURL">URL to Shorten (Maximum 255 Characters)</label>
	    		<div class="input-group">
	    			<input type="text" class="form-control" id="inputURL" placeholder="URL to shorten" name="url">
	    			<span class="input-group-btn">
	        			<button class="btn btn-primary" type="submit">Shorten!</button>
	      			</span>
	    		</div>
	  		</div>
	  	</form>
	</div>
</body>
</html>