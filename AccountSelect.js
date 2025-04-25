window.addEventListener("load",addListener);
window.addEventListener("load",InitControls);

function InitControls()
{
	document.getElementById("txtaccount").textContent = "";
	document.getElementById("txtaccount").focus();
}

function addListener()
{
	document.getElementById("btnenter").addEventListener("click",CheckAccount);
}

function CheckAccount()
{
	var whichaccount
	whichaccount = document.getElementById("txtaccount").value;
	if (whichaccount == "" || str(whichaccount) == "")
	{
		alert("Information is missing!");
		InitControls();
	}
}
