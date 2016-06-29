$('#page-button').click(function() {
  var page = $('#user-page').val();
  var body = $('#iframe').contents().find('body');
  body.html('');
  body.append(page);
  $('#colTwo').show();
  $('#colOne').hide();
});

$('#edit-button').click(function() {
  $('#colTwo').hide();
  $('#colOne').show();
});

$(document).on('ready',function() {
  var greeting = "Hello, world";
  console.log("hi there");

  function greetMe() {
    console.log(greeting);
  }

  $(document).on('keydown',function(e) {
    if (e.which == 78) {
      greeting = greeting + '!';
      greetMe();
    }
  });
});
