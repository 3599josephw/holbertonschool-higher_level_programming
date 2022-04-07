$(function()
{
	$.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data)
	{
        for (let i = 0; i < 7; i++) {
		  $("DIV#hello").text(data['hello']);
        }
    });
});
