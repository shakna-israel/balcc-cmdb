<head>
<title>CMDB - New Location</title>
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
<form action="/del/location" method="POST">
<div class="row">
	<div class="col">
		<p>Location:</p>
		<select name="name">
                    % for location in locations:
                        <option value="{{location}}">{{location}}</option>
                    % end
                </select>
	</div>
</div>
</div>
</br></br><input value="Submit" type="submit" />
</form>
</body>
