<head>
<title>CMDB</title>
<link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
% if data:
        <table class="pure-table">
        <thead>
        <tr>
        <td>Name</td>
        <td>SNID</td>
        <td>Type</td>
        <td>Model</td>
        <td>IP</td>
        <td>MAC</td>
        <td>Purchase Date</td>
        <td>Age</td>
        <td>License</td>
        <td>Cost</td>
        <td>Operating System</td>
        <td>Physical Location</td>
        <td>Phone Type</td>
        <td>Phone Number</td>
        <td>Depends On</td>
        <td>Assigned To</td>
        <td>Status</td>
        <td>Expiry Date</td>
        <td>General Comments</td>
        </tr>
        </thead>
        <tbody>
        % for device in data:
            <tr>
            <td>{{device}}</td>
            <td>{{data[device]['SNID']}}</td>
            <td>{{data[device]['Type']}}</td>
            <td>{{data[device]['Model']}}</td>
            <td>{{data[device]['IP']}}</td>
            <td>{{data[device]['MAC']}}</td>
            <td>{{data[device]['Purchase Date']}}</td>
            <td>{{data[device]['Age']}}</td>
            <td>{{data[device]['License']}}</td>
            <td>{{data[device]['Cost']}}</td>
            <td>{{data[device]['Operating System']}}</td>
            <td>{{data[device]['Physical Location']}}</td>
            <td>{{data[device]['Phone Type']}}</td>
            <td>{{data[device]['Phone Number']}}</td>
            <td>{{data[device]['Depends On']}}</td>
            <td>{{data[device]['Assigned To']}}</td>
            <td>{{data[device]['Status']}}</td>
            <td>{{data[device]['Expiry Date']}}</td>
            <td>{{data[device]['General Comments']}}</td>
            </tr>
        % end
        </tbody>
        </table>
% else:
    <p>No Data Found</p>
% end
</body>
