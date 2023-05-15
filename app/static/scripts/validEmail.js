var emailButton = document.getElementById("emailButton");
var emailField = document.getElementById("emailAddress");
var emailLabel = document.getElementById("emailLabel");

function validEmail () {
	return (/^[A-Za-z0-9][A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/.test(emailField.value));
}

function showvalid () {
	if (validEmail()) {
		//emailLabel.style.color = "black";
		emailButton.disabled=false;
	} else {
		//emailLabel.style.color = "red";
		emailButton.disabled=true;
	}
}