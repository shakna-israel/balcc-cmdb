<style>
.hidden {
	display:none;
}
</style>
<form action="/create/pc" method="POST">
<input class="hidden" name="snid" type="text" value="{{SNID}}" />
<p>IP Address:</p>
<input name="ip_address" type="text" placeholder="10.150.0.12" /></br>
<p>MAC Address: (Excluding ':')</p>
<input name="mac_address" type="text" placeholder="080027ed2239" /></br>
<p>Operating System:</p>
<input name="operating_system" type="text" placeholder="Syslinux 1.3" /></br>
</br></br><input value="Submit" type="submit" />
</form>