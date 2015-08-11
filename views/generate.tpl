<head>
<title>CMDB - New Item</title>
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
<form action="/create" method="POST">
<div class="row">
	<div class="col">
		<p>Type: (Required)</p>
		<select name="type">
		<option value="UNKNOWN">Unknown</option>
		% for item in dataFields:
		    <option value={{item}}>{{item}}</option>
		% end
		</select></br>
	</div>
	<div class="col">
		<p>SNID: (Required)</p>
		<input name="snid" type="text" required placeholder="0128D0921KS" /></br>
	</div>
	<div class="col">
		<p>Model: (Required)</p>
		<input name="model" type="text" required placeholder="Veratitude 2000" /></br>
	</div>
</div>
<div class="row">
	<div class="col">
		<p>Purchase Date:</p>
		<input name="purchase-date" type="date" placeholder="DD/MM/YYYY" /></br>
	</div>
	<div class="col">
		<p>Cost: (Without the '$')</p>
		<input name="cost" type="text" placeholder="200.56" /></br>
	</div>
	<div class="col">
		<p>Depends On:</p>
		<select name="depends-on">
		<option value="UNKNOWN">Unknown</option>
		% for item in devices:
		    <option value="{{item}}">{{item}}</option>
		% end
		</select>
	</div>
</div>

<div class="row">

	<div class="col">
		<p>Assigned To:</p>
		<select name="assigned-to">
		<option value="UNKNOWN">Unknown</option>
		% for item in staff:
		    <option value="{{item}}">Staff: {{item}}</option>
		% end
		% for item in teachers:
		    <option value="{{item}}">Teacher: {{item}}</option>
		% end
		% for item in students:
		    <option value="{{item}}">Student: {{item}}</option>
		% end
		</select>
	</div>

	<div class="col">
		<p>Physical Location:</p>
		<select name="physical-location">
		<option value="UNKNOWN">Unknown</option>
		% for room in locations:
		    <option value="{{room}}">{{room}}</option>
		% end
		</select>
	</div>

	<div class="col">
		<p>Status:</p>
		<select name="status">
			<option value="UNKNOWN">Unknown</option>
			<option value="New">New</option>
			<option value="Ok">Ok</option>
			<option value="Serviceable">Serviceable</option>
			<option value="Service Required">Service Required</option>
			<option value="Replacement Required">Replacement Required</option>
		</select></br>
	</div>

</div>
</br></br><input value="Submit" type="submit" />
</form>
</body>