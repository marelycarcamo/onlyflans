$(document).ready(function() {
	$('#back-to-home').click(function() {
		window.location.href = "{% url 'index' %}";
	});
});