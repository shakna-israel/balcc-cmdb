<head>
<title>CMDB</title>
<link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<style>
.hidden {
    display:none;
}
td {
    font-size: 0.67em !important;
}
td.unknown {
    background-color: rgb(0, 0, 0);
    background-color: rgba(0, 0, 0, 0.8);
    color: rgb(255,255,255);
}
td.red {
    background-color: rgb(255, 0, 0);
    background-color: rgba(255, 0, 0, 0.8);
    color: rgb(0,0,0);
}
td.orange {
    background-color: rgb(255, 165, 0);
    background-color: rgba(255, 165, 0, 0.8);
    color: rgb(0,0,0);
}
td.yellow {
    background-color: rgb(255, 255, 0);
    background-color: rgba(255, 255, 0, 0.8);
    color: rgb(0,0,0);
}
td.blue {
    background-color: rgb(0, 0, 255);
    background-color: rgba(0, 0, 255, 0.8);
    color: rgb(255,255,255);
}
td.green {
    background-color: rgb(0, 128, 0);
    background-color: rgba(0, 128, 0, 0.8);
    color: rgb(255,255,255);
}
@media (min-width: 30em) {
    .row { width: 100%; display: table; table-layout: fixed; }
    .col { display: table-cell; }
}
</style>
<body>
<div class="row">
    <div class="col">
        <p><a href="/create">Create New Device</a></p>
    </div>
    <div class="col">
        <p><a href="/new/person">Create New User</a></p>
    </div>
    <div class="col">
        <p><a href="/del/person">Delete Existing User</a></p>
    </div>
    <div class="col">
        <p><a href="/edit/person">Edit Existing User</a></p>
    </div>
</div>
<div class="row">
    <div class="col">
    % deviceCount = len(data.keys())
    % if deviceCount == '1':
        <p>{{deviceCount}} device under management.</p>
    % else:
        <p>{{deviceCount}} devices under management.</p>
    % end
    </div>
    
    % deviceCountNew = 0
    % for device in data.values():
        % if device['Status'] == 'New':
            % deviceCountNew += 1
        % end
    % end
    % if deviceCountNew == 1:
        <div class="col">
            <p>{{deviceCountNew}} new device.</p>
        </div>
    % elif deviceCountNew > 0:
        <div class="col">
            <p>{{deviceCountNew}} new devices.</p>
        </div>
    % end
    
    
    % deviceCountOk = 0
    % for device in data.values():
        % if device['Status'] == 'Ok':
            % deviceCountOk += 1
        % end
    % end
    % if deviceCountOk == 1:
        <div class="col">
            <p>{{deviceCountOk}} ok device.</p>
        </div>
    % elif deviceCountOk > 0:
        <div class="col">
            <p>{{deviceCountOk}} ok devices.</p>
        </div>
    % end
    
    
    % deviceCountServiceable = 0
    % for device in data.values():
        % if device['Status'] == 'Serviceable':
            % deviceCountServiceable += 1
        % end
    % end
    % if deviceCountServiceable == 1:
        <div class="col">
            <p>{{deviceCountServiceable}} serviceable device.</p>
        </div>
    % elif deviceCountServiceable > 0:
        <div class="col">
            <p>{{deviceCountServiceable}} serviceable devices.</p>
        </div>
    % end
    
    
    % deviceCountServiceRequired = 0
    % for device in data.values():
        % if device['Status'] == 'Service Required':
            % deviceCountServiceRequired += 1
        % end
    % end
    % if deviceCountServiceRequired == 1:
        <div class="col">
            <p>Service Required for {{deviceCountServiceRequired}} device.</p>
        </div>
    % elif deviceCountServiceRequired > 0:
        <div class="col">
            <p>Service Required for {{deviceCountServiceRequired}} devices.</p>
        </div>
    % end


    % deviceCountReplacementRequired = 0
    % for device in data.values():
        % if device['Status'] == 'Replacement Required':
            % deviceCountReplacementRequired += 1
        % end
    % end
    % if deviceCountReplacementRequired == 1:
        <div class="col">
            <p>Replacement Required for {{deviceCountReplacementRequired}} device.</p>
        </div>
    % elif deviceCountReplacementRequired > 0:
        <div class="col">
            <p>Replacement Required for {{deviceCountReplacementRequired}} devices.</p>
        </div>
    % end


    % deviceCountUnknownStatus = 0
    % for device in data.values():
        % if device['Status'] == 'UNKNOWN':
            % deviceCountUnknownStatus += 1
        % end
    % end
    % if deviceCountUnknownStatus == 1:
        <div class="col">
            <p>{{deviceCountUnknownStatus}} device with an unknown status.</p>
        </div>
    % elif deviceCountUnknownStatus > 0:
        <div class="col">
            <p>{{deviceCountUnknownStatus}} devices with an unknown status.</p>
        </div>
    % end
    
</div>

<div class="row">
    <div class="col">
        <small>Do not use the characters '|' or '%'</small>
    </div>
</div>

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
        <td>Estimated Worth</td>
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
            <td contenteditable='true' id="{{device.replace(" ","_") + "$name"}}">{{device}}</td>
            % if data[device]['SNID'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$snid"}}">{{data[device]['SNID']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$snid"}}">{{data[device]['SNID']}}</td>
            % end
            % if data[device]['Type'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$type"}}">{{data[device]['Type']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$type"}}">{{data[device]['Type']}}</td>
            % end
            % if data[device]['Model'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$model"}}">{{data[device]['Model']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$model"}}">{{data[device]['Model']}}</td>
            % end
            % if data[device]['IP'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$IP"}}">{{data[device]['IP']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$IP"}}">{{data[device]['IP']}}</td>
            % end
            % if data[device]['MAC'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$MAC"}}">{{data[device]['MAC']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$MAC"}}">{{data[device]['MAC']}}</td>
            % end
            % if data[device]['Purchase Date'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$PurchaseDate"}}">{{data[device]['Purchase Date']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$PurchaseDate"}}">{{data[device]['Purchase Date']}}</td>
            % end
            % if data[device]['Current Worth'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Current Worth']}}</td>
            % else:
                <td>${{data[device]['Current Worth']}}</td>
            % end
            % if data[device]['Age'] == 'UNKNOWN':
                <td class="unknown">{{data[device]['Age']}}</td>
            % else:
                <td>{{data[device]['Age']}}</td>
            % end
            % if data[device]['License'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$License"}}">{{data[device]['License']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$License"}}">{{data[device]['License']}}</td>
            % end
            % if data[device]['Cost'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$Cost"}}">{{data[device]['Cost']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$Cost"}}">${{data[device]['Cost']}}</td>
            % end
            % if data[device]['Operating System'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$OS"}}">{{data[device]['Operating System']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$OS"}}">{{data[device]['Operating System']}}</td>
            % end
            % if data[device]['Physical Location'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$Location"}}">{{data[device]['Physical Location']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$Location"}}">{{data[device]['Physical Location']}}</td>
            % end
            % if data[device]['Phone Type'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$PhoneType"}}">{{data[device]['Phone Type']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$PhoneType"}}">{{data[device]['Phone Type']}}</td>
            % end
            % if data[device]['Phone Number'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$PhoneNumber"}}">{{data[device]['Phone Number']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$PhoneNumber"}}">{{data[device]['Phone Number']}}</td>
            % end
            % if data[device]['Depends On'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$DependsOn"}}">{{data[device]['Depends On']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$DependsOn"}}">{{data[device]['Depends On']}}</td>
            % end
            % if data[device]['Assigned To'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$AssignedTo"}}">{{data[device]['Assigned To']}}</td>
            % else:
                <td contenteditable='true' id="{{device.replace(" ","_") + "$AssignedTo"}}">{{data[device]['Assigned To']}}</td>
            % end

            % if data[device]['Status'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$Status"}}">{{data[device]['Status']}}</td>
            % elif data[device]['Status'] == 'New':
                <td contenteditable='true' class="green" id="{{device.replace(" ","_") + "$Status"}}">{{data[device]['Status']}}</td>
            % elif data[device]['Status'] == 'Ok':
                <td contenteditable='true' class="blue" id="{{device.replace(" ","_") + "$Status"}}">{{data[device]['Status']}}</td>
            % elif data[device]['Status'] == 'Serviceable':
                <td contenteditable='true' class="yellow" id="{{device.replace(" ","_") + "$Status"}}">{{data[device]['Status']}}</td>
            % elif data[device]['Status'] == 'Service Required':
                <td contenteditable='true' class="orange" id="{{device.replace(" ","_") + "$Status"}}">{{data[device]['Status']}}</td>
            % elif data[device]['Status'] == 'Replacement Required':
                <td contenteditable='true' class="red" id="{{device.replace(" ","_") + "$Status"}}">{{data[device]['Status']}}</td>
            % end

            % if data[device]['Expiry Date'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown" id="{{device.replace(" ","_") + "$ExpiryDate"}}">{{data[device]['Expiry Date']}}</td>
            % else:
                <td contenteditable='true'  id="{{device.replace(" ","_") + "$ExpiryDate"}}">{{data[device]['Expiry Date']}}</td>
            % end
            % if data[device]['General Comments'] == 'UNKNOWN':
                <td contenteditable='true' class="unknown"  id="{{device.replace(" ","_") + "$GeneralComments"}}">{{data[device]['General Comments']}}</td>
            % else:
                <td contenteditable='true'  id="{{device.replace(" ","_") + "$GeneralComments"}}">{{data[device]['General Comments']}}</td>
            % end
            </tr>
        % end
    </tbody>
    </table>
% else:
    <p>No Data Found</p>
% end

<form action="/edit/tableData" method="POST">
<input name="data" type="text" id="tableDataPost" class="hidden" />
<input onclick="onSubmit()" value="Submit Changes" type="submit" />
</form>

<script>
function onSubmit() {
    var tableDataPost = document.getElementById('tableDataPost')
    tableDataPost.value = ""
    % for device in data:
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$name'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$snid'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$type'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$model'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$IP'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$MAC'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$PurchaseDate'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$License'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$Cost'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$OS'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$Location'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$PhoneType'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$PhoneNumber'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$DependsOn'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$AssignedTo'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$Status'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$ExpiryDate'}}").innerHTML
        tableDataPost.value += '|'
        tableDataPost.value += document.getElementById("{{device.replace(" ","_") + '$GeneralComments'}}").innerHTML
        tableDataPost.value += '%'
    % end
    console.log(tableDataPost.value)
}
</script>

</body>
