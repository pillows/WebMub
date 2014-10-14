$(document).ready(function() {
    
    /* Upload Window*/
    $('#openBtn').click(function() {
        $('#myModal').modal({
            show: true,
            keyboard:true
        })
    });
    /* End Upload Window */
    
    /* WebM Stats */
    $("[data-toggle=tooltip]").tooltip();
    /* End WebM Stats */
    
    /* Comment box character count */

    $("#comment_box").keyup(function() {
        var chars = $("#comment_box").val().length;
        var charsLeft = 255 - parseInt(chars);
        //Debug
        //console.log(charsLeft);
        $('#count').html(charsLeft);

    });
    /* End Comment box character count */
    
    /* Report AJAX */
    $('#reportBtn').click(function(contentId) {
        $.get( "/api/v1/user_login", function( data ) {
            if(data.username == "False") {
                window.location="/login/";
            }
            else {
                $('#reportModal').modal({
                    show: true,
                    keyboard: true
                })
                var report = {"id":contentId}
                $.ajax( {
                    type: "POST",
                     url:'/api/v1/reports',
                     data: report
                 });         
            }
        });
    });
    /* End Report AJAX */
    
    /* Edit Post */
    
    /* End Edit Post */


    /* Navbar */
    $(window).scroll(function() {
        if ($(window).scrollTop() > 80) {
            $('.navbar').removeClass('navbar-transparent');
        } else {
            $('.navbar').addClass('navbar-transparent');
        }
    });

    /* Filtering Image */
    var $wrapper = $('.wrapper-portfolio');
    $wrapper.isotope({
        filter: '*',
        animationOptions: {
            duration: 750,
            easing: 'easeOutBounce',
            queue: false
        }
    });

    $('.portfolio-sort > li').on('click', function() {
        $('.portfolio-sort > li.active').removeClass('active');
        $(this).addClass('active');

        var selector = $(this).attr('data-filter');
        $wrapper.isotope({
            filter: selector,
            animationOptions: {
                duration: 750,
                easing: 'easeOutBounce',
                queue: false
            }
        });
        setProjects();

        return false;
    });

    /* Set Column Portfolio */
    function splitColumns() {
        var winWidth = $(window).width(),
            columnNumb = 1;
        if (winWidth > 1200) {
            columnNumb = 4;
        } else if (winWidth > 992 && winWidth < 1200) {
            columnNumb = 4;
        } else if (winWidth > 768 && winWidth < 992) {
            columnNumb = 2;
        } else if (winWidth > 480 && winWidth < 768) {
            columnNumb = 2;
        } else if (winWidth < 480) {
            columnNumb = 1;
        }
        return columnNumb;
    }

    function setColumns() {
        var winWidth = $(window).width(),
            columnNumb = splitColumns(),
            postWidth = Math.floor(winWidth / columnNumb);
        $wrapper.find('.wrapper-portfolio li').each(function() {
            $(this).css({
                width: postWidth + 'px'
            });
        });
    }

    function setProjects() {
        setColumns();
        $wrapper.isotope('reLayout');
    }

    $wrapper.imagesLoaded(function() {
        setColumns();
    });

    $(window).bind('resize', function() {
        setProjects();
    });

    /* Masonry Blog Layout */
    var $container = $('.container-post');
    $container.imagesLoaded(function() {
        $container.masonry();
    });

    //$('#map').gmap3('get').setCenter(new google.maps.LatLng(-7.866315,110.389574));

    /* Toggle Map */
    var mapContainer = $('.mapcontainer');
    $('#openmap').on('click', function() {
        $(this).toggleClass('closemap');
        $('#map').toggleClass('showMap');
        mapContainer.toggleClass('hidecontainer');
        $('#map').gmap3('get').setCenter(new google.maps.LatLng(-7.866315, 110.389574));
    });

    $(function() {
        $('.button-checkbox').each(function() {
            var $widget = $(this),
                $button = $widget.find('button'),
                $checkbox = $widget.find('input:checkbox'),
                color = $button.data('color'),
                settings = {
                    on: {
                        icon: 'glyphicon glyphicon-check'
                    },
                    off: {
                        icon: 'glyphicon glyphicon-unchecked'
                    }
                };

            $button.on('click', function() {
                $checkbox.prop('checked', !$checkbox.is(':checked'));
                $checkbox.triggerHandler('change');
                updateDisplay();
            });

            $checkbox.on('change', function() {
                updateDisplay();
            });

            function updateDisplay() {
                var isChecked = $checkbox.is(':checked');
                // Set the button's state
                $button.data('state', (isChecked) ? "on" : "off");

                // Set the button's icon
                $button.find('.state-icon')
                    .removeClass()
                    .addClass('state-icon ' + settings[$button.data('state')].icon);

                // Update the button's color
                if (isChecked) {
                    $button
                        .removeClass('btn-default')
                        .addClass('btn-' + color + ' active');
                } else {
                    $button
                        .removeClass('btn-' + color + ' active')
                        .addClass('btn-default');
                }
            }

            function init() {
                updateDisplay();
                // Inject the icon if applicable
                if ($button.find('.state-icon').length == 0) {
                    $button.prepend('<i class="state-icon ' + settings[$button.data('state')].icon + '"></i> ');
                }
            }
            init();
        });
    });
});

var editPost = (function(postId) {
        console.log(postId);
    });