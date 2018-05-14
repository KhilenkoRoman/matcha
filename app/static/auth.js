function register(view_url)
{
	event.preventDefault();

	const email = document.getElementById("r_email_inp").value;
	const login = document.getElementById("r_login_inp").value;
	const pwd = document.getElementById("r_pwd_inp").value;

	$.ajax({
		url: view_url,
		data: {'email': email, 'login': login, 'pwd': pwd},
		type: 'POST',
		success: function(response)
		{
			console.log(response);
		},
		error: function(error)
		{
			console.log(error);
		}
	});
}

function ready(data)
{
	alert(data);
}