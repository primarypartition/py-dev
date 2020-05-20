var x = $('h1');

x.css("color",'red');
x.css("background","blue");

var newCSS = {
  "color":"white",
  "background":"blue",
  "border":"red"
}

x.css(newCSS);

// Grabbing Text:
$('h1').text()

// Changing Text:
$('h1').text("Brand New Text!")

// Grabbing HTML
$('h1').html()

// Changing HTML
$('h1').html("<em>Now in Italics</em>")

// Changing an attribute
$("input").eq(1).attr('type','checkbox');

// Changing values
$("input").eq(0).attr('value',"BRAND NEW VALUE");

// Can do this more directly:
$("input").eq(0).val("cleared up");

// Add a Class
$('h2').addClass("turnRed")

// Remove a Class
$("h2").removeClass("turnRed");

// Toggle the Class on and Off
$("h3").addClass("turnBlue");

$("h3").toggleClass("turnBlue");

// Using This with jQuery
$('h3').click(function() {
  $(this).text("I was changed!");
})

// on() basically works like addEventListener()
$('h1').on("dblclick",function() {
  $('h1').addClass('turnBlue');
})

$('input').eq(1).on("click",function(){
  $(".container").slideUp(1000) ;
})
