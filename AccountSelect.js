window.addEventListener("load",InitControls);
window.addEventListener("load",addListener);

function addListener()
{
	document.getElementById("btnsubmit").addEventListener("click",CheckInfo);
}

function CheckInfo()
{
	document.getElementById("btnAdmin").value = 1;
	document.getElementById("btnUser").value = 2;
}
