$(document).ready(function(){
    $('.scrollspy').scrollSpy();
  });

$(document).ready(function(){
  $('.ir-arriba').click(function(){
    $('body, html').animate({
      scrollTop: '0px'
    });
  });

  $(window).scroll(function(){
    if($(this).scrollTop() > 0){
        $('.ir-arriba').slideDown(300);
    }else{
      $('.ir-arriba').slideUp(300);
    }
  });

});

$(".button-collapse").sideNav();

  $('.button-collapse').sideNav({
      menuWidth: 300, // Default is 300
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens
    }
  );

$('.slider').slider({
  height: 500,
  transition: 1000,
});