<style>
.hidden {
	display:none;
}
</style>
<form action="/create/phone" method="POST">
<input class="hidden" name="snid" type="text" value="{{SNID}}" />
<p>Phone Number:</p>
<input name="phone_number" type="tel" placeholder="03 5337 5900" /></br>
</br></br><input value="Submit" type="submit" />
</form>