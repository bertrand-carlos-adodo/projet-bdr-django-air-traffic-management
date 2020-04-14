var height = 0;

$(window).scroll(function () {
    if($(this).scrollTop() > height) {
        $('.navbar').addClass('fixed');
    }else {
        $('.navbar').removeClass('fixed');
    }
});
