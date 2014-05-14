$(document).ready(function() {
	$(".entry-image-link").colorbox({
		rel : 'entry-image-link'
	});

	$('#press-release').vTicker({
		speed : 500,
		pause : 3000,
		showItems : 5,
		animation : 'fade',
		mousePause : true,
		height : 0,
		direction : 'up'
	});

});

function email_template(email) {
	email = window.atob(email);
	return '<a href="mailto:' + email + '">' + email +  '</a>';
}


jQuery( document ).ready(function( $ ) {		
  	$(".mailto").each(function(index) {	  	
  	var el = $(this); 	  	
  	var email = el.data('email');
  	var result = email_template(email); 
  	el.html(result);
  });
});
