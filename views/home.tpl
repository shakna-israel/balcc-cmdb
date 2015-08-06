<head>
<title>CMDB</title>
<link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<style>
td.unknown {
    background-color: rgb(0, 0, 0);
    background-color: rgba(0, 0, 0, 0.8);
    color: rgb(255,255,255);
}
</style>
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
            % if data[device]['SNID'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['SNID']}}</td>
            % else:
                <td>data[device]['SNID']</td>
            % end
            % if data[device]['Type'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Type']}}</td>
            % else:
                <td>{{data[device]['Type']}}</td>
            % end
            % if data[device]['Model'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Model']}}</td>
            % else:
                <td>{{data[device]['Model']}}</td>
            % end
            % if data[device]['IP'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['IP']}}</td>
            % else:
                <td>{{data[device]['IP']}}</td>
            % end
            % if data[device]['MAC'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['MAC']}}</td>
            % else:
                <td>{{data[device]['MAC']}}</td>
            % end
            % if data[device]['Purchase Date'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Purchase Date']}}</td>
            % else:
                <td>{{data[device]['Purchase Date']}}</td>
            % end
            % if data[device]['Age'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Age']}}</td>
            % else:
                <td>{{data[device]['Age']}}</td>
            % end
            % if data[device]['License'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['License']}}</td>
            % else:
                <td>{{data[device]['License']}}</td>
            % end
            % if data[device]['Cost'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Cost']}}</td>
            % else:
                <td>{{data[device]['Cost']}}</td>
            % end
            % if data[device]['Operating System'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Operating System']}}</td>
            % else:
                <td>data[device]['Operating System']</td>
            % end
            % if data[device]['Physical Location'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Physical Location']}}</td>
            % else:
                <td>{{data[device]['Physical Location']}}</td>
            % end
            % if data[device]['Phone Type'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Phone Type']}}</td>
            % else:
                <td>{{data[device]['Phone Type']}}</td>
            % end
            % if data[device]['Phone Number'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Phone Number']}}</td>
            % else:
                <td>{{data[device]['Phone Number']}}</td>
            % end
            % if data[device]['Depends On'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Depends On']}}</td>
            % else:
                <td>{{data[device]['Depends On']}}</td>
            % end
            % if data[device]['Assigned To'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Assigned To']}}</td>
            % else:
                <td>{{data[device]['Assigned To']}}</td>
            % end
            % if data[device]['Status'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Status']}}</td>
            % else:
                <td>{{data[device]['Status']}}</td>
            % end
            % if data[device]['Expiry Date'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Expiry Date']}}</td>
            % else:
                <td>{{data[device]['Expiry Date']}}</td>
            % end
            % if data[device]['General Comments'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['General Comments']}}</td>
            % else:
                <td>{{data[device]['General Comments']}}</td>
            % end
            </tr>
        % end
        </tbody>
        </table>
% else:
    <p>No Data Found</p>
% end
</body>
