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