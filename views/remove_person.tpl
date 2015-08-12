<head>
<title>CMDB - Remove Person</title>
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
<form action="/del/person" method="POST">
<div class="row">
	<div class="col">
		<p>User Name</p>
		<select name="name">
		    % for item in students:
				<option value="students:{{item}}">Student: {{item}}</option>
			% end
			% for item in teachers:
				<option value="teachers:{{item}}">Teacher: {{item}}</option>
			% end
			% for item in staff:
				<option value="staff:{{item}}">Staff Member: {{item}}</option>
			% end
		</select>
	</div>
</div>
</br></br><input value="Submit" type="submit" />
</form>
</body>
