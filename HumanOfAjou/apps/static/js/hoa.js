$(document).ready(function () {

    $(window).scroll(function () {
        // get scroll position
        var s = $(window).scrollTop();
        // scroll value and opacity
        opacityVal = (s / 280.0);
        // opacity value 0% ~ 100%
        $('.blurred-img').css('opacity', opacityVal);
    });


// navbar fixed by scroll
    $(window).bind('scroll', function () {
        var srlTop = $(this).scrollTop();
        var winHeight = $(window).height();
        if (srlTop > winHeight - 53) {
            $('#Header_nav_bar').css({ position: 'fixed', top: '300px', left: '0px'});
            $('#Header_nav_bar li').css({ float: 'none'});
            $('#Header_nav_bar li').css({ width: '96px'});

            $('.Prev_detail').css({position: 'fixed', top: '330px', left: '50px'});
            $('.Next_detail').css({position: 'fixed', top: '330px', right: '50px'});
        }
        else {
            $('#Header_nav_bar').css({ position: 'relative', top: '0px', left: '0px'});
            $('#Header_nav_bar li').css({ float: 'left'});
            $('#Header_nav_bar li').css({ width: '96px'});


            $('.Prev_detail').css({position: 'relative'});
            $('.Next_detail').css({position: 'relative'});
        }
    });
    $('input[type="radio"]').radio();

    //vendor script
    $('#header')
        .css({ 'top': -50 })
        .delay(1000)
        .animate({'top': 0}, 800);

    $('#footer')
        .css({ 'bottom': -15 })
        .delay(1000)
        .animate({'bottom': 0}, 800);

    //blocksit define
    $(window).load(function () {
        $('#container').BlocksIt({
            numOfCol: 3,
            offsetX: 1,
            offsetY: 8
        });
    });

    //window resize
    var currentWidth = 1100;
    $(window).resize(function () {
        var winWidth = $(window).width();
        var conWidth;
        if (winWidth < 650) {
            conWidth = 300;
            col = 1
        }
        else if (winWidth < 1000) {
            conWidth = 600;
            col = 2
        } else if (winWidth > 1000) {
            conWidth = 1000;
            col = 3
        }

        if (conWidth != currentWidth) {
            currentWidth = conWidth;
            $('#container').width(conWidth);
            $('#container').BlocksIt({
                numOfCol: col,
                offsetX: 1,
                offsetY: 8
            });
        }
    });


    // by kimjinoh

    $(window).on('scroll', function() {
        var srlTop = $(this).scrollTop();
        var winHeight = $(window).height();
        if (srlTop > winHeight - 53) {
            $('.Humans_Navbar').attr('style', 'background: #ffffff;');
        } else {
            $('.Humans_Navbar').attr('style', 'background: transparent;');
        }
    });
});