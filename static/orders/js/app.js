document.addEventListener('DOMContentLoaded', () => {
    const dropdown = $('#myDropdown');
    const dropButton = $('.dropbtn');
    const closeButton = $('closeNotification');
    const notification = $('#notificationsLog')

    // By default, dropdown menu is closed
    dropdown.hide();

    // When the profile button is clicked, open the menu
    dropButton.click(() => {
        dropdown.fadeToggle();
    });

    // When it is focused out, close the menu.
    dropButton.focusout(() => {
        dropdown.fadeOut();
    });

    closeButton.click(() => {
        console.log('clicked')
        notification.fadeOut();
    });

    var itemsMainDiv = ('.MultiCarousel');
    var itemsDiv = ('.MultiCarousel-inner');
    var itemWidth = "";

    $('.leftLst, .rightLst').click(function () {
        var condition = $(this).hasClass("leftLst");
        if (condition)
            click(0, this);
        else
            click(1, this)
    });

    ResCarouselSize();


    $(window).resize(function () {
        ResCarouselSize();
    });

    //this function define the size of the items
    function ResCarouselSize() {
        var incno = 0;
        var dataItems = ("data-items");
        var itemClass = ('.item');
        var id = 0;
        var btnParentSb = '';
        var itemsSplit = '';
        var sampwidth = $(itemsMainDiv).width();
        var bodyWidth = $('body').width();
        $(itemsDiv).each(function () {
            id = id + 1;
            var itemNumbers = $(this).find(itemClass).length;
            btnParentSb = $(this).parent().attr(dataItems);
            itemsSplit = btnParentSb.split(',');
            $(this).parent().attr("id", "MultiCarousel" + id);


            if (bodyWidth >= 1200) {
                incno = itemsSplit[3];
                itemWidth = sampwidth / incno;
            } else if (bodyWidth >= 992) {
                incno = itemsSplit[2];
                itemWidth = sampwidth / incno;
            } else if (bodyWidth >= 768) {
                incno = itemsSplit[1];
                itemWidth = sampwidth / incno;
            } else {
                incno = itemsSplit[0];
                itemWidth = sampwidth / incno;
            }
            $(this).css({'transform': 'translateX(0px)', 'width': itemWidth * itemNumbers});
            $(this).find(itemClass).each(function () {
                $(this).outerWidth(itemWidth);
            });

            $(".leftLst").addClass("over");
            $(".rightLst").removeClass("over");

        });
    }


    //this function used to move the items
    function ResCarousel(e, el, s) {
        var leftBtn = ('.leftLst');
        var rightBtn = ('.rightLst');
        var translateXval = '';
        var divStyle = $(el + ' ' + itemsDiv).css('transform');
        var values = divStyle.match(/-?[\d\.]+/g);
        var xds = Math.abs(values[4]);
        if (e == 0) {
            translateXval = parseInt(xds) - parseInt(itemWidth * s);
            $(el + ' ' + rightBtn).removeClass("over");

            if (translateXval <= itemWidth / 2) {
                translateXval = 0;
                $(el + ' ' + leftBtn).addClass("over");
            }
        } else if (e == 1) {
            var itemsCondition = $(el).find(itemsDiv).width() - $(el).width();
            translateXval = parseInt(xds) + parseInt(itemWidth * s);
            $(el + ' ' + leftBtn).removeClass("over");

            if (translateXval >= itemsCondition - itemWidth / 2) {
                translateXval = itemsCondition;
                $(el + ' ' + rightBtn).addClass("over");
            }
        }
        $(el + ' ' + itemsDiv).css('transform', 'translateX(' + -translateXval + 'px)');
    }

    //It is used to get some elements from btn
    function click(ell, ee) {
        var Parent = "#" + $(ee).parent().attr("id");
        var slide = $(Parent).attr("data-slide");
        ResCarousel(ell, Parent, slide);
    }


    // Sizing Options:
    // 1 = Small
    // 2 = Large
    // If type is 0, then it means that the product is either PASTA or SALAD
    $('.orderButton').click((event) => {

        var product_id = event.target.dataset.id;
        var count = false
        var sizing_small = $(`#${product_id.split("-")[0]}-small-${product_id.split("-")[1]}`).is(":checked");
        var sizing_large = $(`#${product_id.split("-")[0]}-large-${product_id.split("-")[1]}`).is(":checked");


        // // Special cases for pasta and salad:

        if (product_id.split("-")[0] != 'pasta' && product_id.split("-")[0] !='salad') {
            if (sizing_small) {
                count = 'small';
            } else if (sizing_large) {
                count = 'large';
            } else {
                alert('Nothing selected');
                return;
            }
        }

        const request = new XMLHttpRequest();


        request.open('GET', `/showcart?product=${product_id}&type=${count}`);

        // request.onload = function () {
        //     const data = JSON.parse(request.responseText)
        //     var product = data.product_id;
        //     var size = data.size;
        //     var place = $('#menuItems')
        //
        //     //   SIZE: 1=SMALL / 2=LARGE / 0=PASTA OR SALAD
        //
        //    place.text(`${product} is product and ${size} is size`)
        // }

        request.send()


    });


});


// bugs in SICILIAN and DINNER PLATTERS