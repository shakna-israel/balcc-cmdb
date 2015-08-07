<style>
.hidden {
	display:none;
}
</style>
<form action="/create/software" method="POST">
<input class="hidden" name="snid" type="text" value="{{SNID}}" />
<p>License:</p>
<input name="license" type="text" placeholder="10291-10281-102928-1029" /></br>
<p>Expiry Date:</p>
<input name="expiry_date" type="text" placeholder="DD/MM/YYYY"/></br>
</br></br><input value="Submit" type="submit" />
</form>