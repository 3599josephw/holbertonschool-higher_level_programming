$('#toggle_header').click(function() {
    $(this).toggleClass(function(){
      return $(this).is('.red, .green') ? 'red green' : 'red';
    })
  });