jQuery(document).ready(function($) {

	$('.scroll').click(function(e){		
		e.preventDefault();

		
		var defaultAnchorOffset = 0;
		var anchor = $(this).attr('data-attr-scroll');

		var anchorOffset = $('#' + anchor).attr('data-scroll-offset');
		if(!anchorOffset)
			anchorOffset = defaultAnchorOffset;

		$('html, body').animate({
			scrollTop : $('#' + anchor).offset().top - anchorOffset
		}, 500);
	});
});