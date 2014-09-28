$(document).ready(function () {



    $(window).scroll(function () {
        // get scroll position
        var s = $(window).scrollTop();
        // scroll value and opacity
        opacityVal = (s / 280.0);
        // opacity value 0% ~ 100%
        $('.blurred-img').css('opacity', opacityVal);
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


    //scroll action -navbar

    $(window).on('scroll', function() {
        var detailHeight = $('.Detail_Container').attr("height");

        var srlTop = $(this).scrollTop();
        var winHeight = $(window).height();
        if (srlTop > winHeight - 53) {
            $('.Humans_Navbar').attr('style', 'background: #ffffff; border:solid 1px;');
        } else {
            $('.Humans_Navbar').attr('style', 'background: transparent;');
        }
    });

    //scroll action -glyphen
    $(window).bind('scroll', function () {
        var srlTop = $(this).scrollTop();
        var winHeight = $(window).height();
        if (srlTop > winHeight) {

            $('.Prev_detail').css({position: 'fixed', top: '350px', left: '50px'});
            $('.Next_detail').css({position: 'fixed', top: '350px', right: '50px'});
        }
        else {
            $('.Prev_detail').css({position: 'relative', left:'50px'});
            $('.Next_detail').css({position: 'relative', right:'50px'});
        }
    });



    // postJSON
    $.postJSON = function (url, data, success) {
        return $.ajax({
            type: 'POST',
            url: url,
            data: data,
            success: success,
            dataType: 'json',
            contentType: "application/json; charset=UTF-8"
        });
    };

    // Humans Like
    $('.js-humansLike').on('click', function() {
        var humans_id = $(this).data('humans-id');

        var jsonData = new Object();
        jsonData.humans_id = humans_id;
        jsonData = JSON.stringify(jsonData);

        $.postJSON('/humans/like', jsonData, function(result) {
            alert(result.APIMessage);
            if(result.APICode == 200) {
                $('.Humans_counts').text(result.APIPayload);
            }
        })
    });
});