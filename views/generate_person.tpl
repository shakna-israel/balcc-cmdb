<head>
<title>CMDB - New Person</title>
<link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<style>
@media (min-width: 30em) {
    .row { width: 100%; display: table; table-layout: fixed; }
    .col { display: table-cell; }
    body { width: 100%; }
}
body {
	margin-left: auto;
	margin-right: auto;
	width: 90%;
}
</style>
<form action="/new/person" method="POST">
<div class="row">
	<div class="col">
		<p>User Name</p>
		<input name="name" type="text" required placeholder="James Milne" /></br>
	</div>
	<div class="col">
		<p>Role</p>
		<select name="role">
			<option value="students">Student</option>
			<option value="teachers">Teacher</option>
			<option value="staff">Staff Member</option>
		</select>
</div>
</div>
</br></br><input value="Submit" type="submit" />
</form>
</body>
