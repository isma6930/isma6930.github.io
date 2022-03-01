function calculer()
{
alert('ok')
	var ab= document.getElementById('ab').value;
	alert(ab)
	var bc= document.getElementById('bc').value;
	var ac= document.getElementById('ac').value;
	
		


if (ab**2+ac**2===bc**2)
{document.getElementById('resultat').innerHTML="le triangle est rectangle en A ";
}
else if  (bc**2+ab**2===ac**2)
{document.getElementById('resultat').innerHTML="le triangle est rectangle en B ";
}

else if (bc**2+ac**2===ab**2)
{document.getElementById('resultat').innerHTML="le triangle est rectangle en C ";
}
else 
{document.getElementById('resultat').innerHTML="le triangle n'est rectangle";
}	
}
