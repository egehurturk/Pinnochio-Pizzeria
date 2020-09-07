document.addEventListener('DOMContentLoaded', () => {
    const dropdown = $('#myDropdown');
    const dropButton = $('.dropbtn');
    const closeButton = $('closeNotification');
    const notification = $('#notificationsLog')
    var model = $("#succesmodal")

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


    $('.orderButton').click((event) => {

        var product = event.target.dataset.id;
        var category_name = `${product.split("-")[0]}` // name of category
        var product_id = `${product.split("-")[1]}` // product id
        var sm = $(`#${category_name}-small-${product_id}`).is(":checked");
        var lg = $(`#${category_name}-large-${product_id}`).is(":checked");
        var product_type; // "small", "large", "only"

        if (sm) {
            product_type = "small"
        } else if (lg) {
            product_type = "large"
        } else {
            product_type = "only"
        }

        if (category_name !== "pasta") {
            if (category_name !== "salad") {
                if (sm === false) {
                    if (lg === false) {
                        alert("Nothing is selected")
                        return;
                    }
                }
            }
        }



        $.ajax("/showcart", {
            type: "GET",
            data: {
                product: product,
                type: product_type
            },
            success: function(response) {
                model.fadeToggle();
                var succesbtn = $("#succesbtn")
                succesbtn.click(()=> {
                    model.fadeOut();
                })
                var product_id = response["product_id"] // id
                var product_name = response["product_name"] // name gotten from menu
                var query_category = response["query_category"] // category
                var crust = response["query_crust"] // crust for pizza
                var large_price = response["query_large_price"] // large_price (null if there isn't)
                var max_toppings = response["query_max_toppings"] // max_toppings for pizza
                var name = response["query_name"] // name
                var price = response["query_price"] // price (null if there isn't)
                var small_price = response["query_small_price"] // small_price (null if there isn't)
                var query = response["queryset"] // query
                var size = response["size"] // null if it is salad or pasta
                console.log(`${product_id} \n  ${product_name} \n
                 ${query_category}\n ${crust}\n ${large_price}\n ${max_toppings}\n ${name}\n ${price} \n${small_price}\n
                    ${query}\n ${size}`)

                $("#menuItems").append() // implement this.


            },
            error: function(resp) {
                console.log("Something went wrong.")
            }

        })



    });


});

