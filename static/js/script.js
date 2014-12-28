$(document).on('change', '.btn-file :file', function() {
  var input = $(this),
      numFiles = input.get(0).files ? input.get(0).files.length : 1,
      label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);
});

$(document).ready(function() {
    
    /* Upload Window*/
    $('#openBtn').click(function() {
        $('#myModal').modal({
            show: true,
            keyboard:true
        })
    });
    
    $('.file-upload').click(function() {
	    $('.upload-body').html("<div class='col-lg-12 col-sm-12 col-12 cursor' style='text-align:center'><form class='dragndrop' action='/upload/' method='POST' enctype='multipart/form-data'> <input type='file' accept='video/webm,image/gif' class='file-input' name='file'><p class='upload-step1'>Drag your files here or click in this area.</p></form></div>");
	    $('form input').change(function () {
            $('form p').text(this.files[0].name + " is loaded. (Put better text here)");
        
            if($("form input")[0].files.length > 0) {
                $(".file-input").css({"visibility":"hidden"});
                $(".upload-step1").hide();
                $(".dragndrop").css({"border":"none"});
                $(".dragndrop").append("<div class='upload-step2'>Description (Optional): </div><div class='form-group'> <textarea class='form-control description-ta' name='description'></textarea></div>");
                $(".modal-footer").append("<button class='btn btn-primary upload-submit'>Submit</button>");
                
                $(".upload-submit").click(function () {
                   $("form").submit();
                });
            }
        });
        
        $(".close-btn").click(function() {
           return $(".upload-body").html("<div class='col-lg-6 col-sm-6 col-12 cursor file-upload' style='text-align:center'> <i class='glyphicon glyphicon-upload upload-choices'></i> <br /> <h3>Upload Your WebM/GIF</h3> </div> <div class='col-lg-6 col-sm-6 col-12 cursor direct-upload' style='text-align:center'> <i class='glyphicon glyphicon-globe upload-choices'></i> <br /> <h3>Upload From A URL</h3> </div>"); 
           
        });
        
        return false;
    });
    
    $(".direct-upload").click(function() {
        $(".upload-body").html("<div class='col-lg-12 col-sm-12 col-12 cursor' style='text-align:center'><form action='/upload/' method='POST' enctype='multipart/form-data'> <div class='upload-step11'>URL: <input type='text' class='form-control webm-check' name='url'/></div><br /><div class='upload-step2'>Description (Optional): </div><div class='form-group'> <textarea class='form-control description-ta' name='description'></textarea><div class='webm-preview'></div></div></form></div>");
        $(".modal-footer").append("<button class='btn btn-primary upload-submit'>Submit</button>");
        $(".upload-submit").click(function () {
           $("form").submit();
        });
        
        $(".webm-check").on("change keyup paste",function() {
	        var url = $("webm-check").val();
	        var resp = {url:url};
	        var response = $.ajax({
                type: "POST",
                url: '/api/v1/verify',
                data: resp,
                success: function(data) {
                    console.log(data);
                }
            });
        });
        $(".close-btn").click(function() {
           $(".upload-body").html("<div class='col-lg-6 col-sm-6 col-12 cursor file-upload' style='text-align:center'> <i class='glyphicon glyphicon-upload upload-choices'></i> <br /> <h3>Upload Your WebM/GIF</h3> </div> <div class='col-lg-6 col-sm-6 col-12 cursor direct-upload' style='text-align:center'> <i class='glyphicon glyphicon-globe upload-choices'></i> <br /> <h3>Upload From A URL</h3> </div>"); 
           return false;
        });
        
        return false;
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
    
    /* Points function */
    
    $(".updown").on("click", function() {
	    var contentType = $(this).data("type");
	    var contentId = $(this).data("id");
	    var plusminus = $(this).data("points");
	    console.log("Type: " + contentType);
	    console.log("Id: " + contentId);
	    console.log("Points: " + plusminus);
	
	    $.get("/api/v1/user_login", function(user_login) {
	        if (user_login.username == "False") {
	            window.location = "/login/";
	        } else {
	            var points = {
	                "id": contentId,
	                "points": plusminus,
	                "type": contentType,
	                "user": user_login.username
	            };
	            console.log(points);
	            var response = $.ajax({
	                type: "POST",
	                url: '/api/v1/points',
	                data: points,
	                success: function(data) {
	                    console.log(data);
	                    var total = data.total;
	                    $("#points").html(total);
	                }
	            });
	        }
	    });
	});
	
	/* End Points */
	
	/* Begin Delete Posts Function */
	
	$(".delete_post").on("click", function() {
		var accountId = $(this).data("author");
		var contentId = $(this).data("id");
		var contentType = $(this).data("type");
		console.log("AccountID: " + accountId);
		console.log("Type: " + contentType);
	    console.log("Id: " + contentId);
        
        
        $("#reportModal").html("<div class='modal-dialog'> <div class='modal-content'> <div class='modal-header'> <button type='button' class='close' data-dismiss='modal'>×</button> <h3>Delete Post</h3> </div> <div class='modal-body'><div class='input-group'> <h3>Are you sure that you want to delete this comment??</h3> </div> <div class='modal-footer'> <button id='delete_post' class='btn btn-primary' data-dismiss='modal'>Yes</button> <button class='btn' data-dismiss='modal'>No</button> </div> </div> </div>").modal({
            show: true,
            keyboard: true
        });

		$("#delete_post").one('click', function (e) {
			var deletePost = {
                "id": contentId,
                "type": contentType,
                "accountId": accountId
        	};
            console.log(deletePost);
            var response = $.ajax({
                type: "POST",
                url: '/api/v1/delete',
                data: deletePost,
                success: function(data) {
                    console.log(data);
                    $("#" +  contentId).fadeOut(1000, function() {
                        $(this).remove();
                    });;
                }
            });
		});    
	});
	/* End Delete Posts Function */
	
	$(".edit_post").on("click", function() {
		var accountId = $(this).data("author");
		var contentId = $(this).data("id");
		var contentType = $(this).data("type");
		var postContent = $("#post_" + contentId).html();
		console.log("AccountID: " + accountId);
		console.log("Type: " + contentType);
	    console.log("Id: " + contentId);
	    
	    $("#post_" + contentId).html("");
	    $("#post_" + contentId).append(
	        "<div class='form-group'><input type='text' id='comment_box_edit' name='comment' class='comment_box' value='" + postContent + "' placeholder='Confess thy opinion.' size='255' autofocus> <input type='submit' value='Post' class='btn btn-primary' id='edit_button'> <div id='count_edit'>255</div></div>"
	    );
	    $("#comment_box_edit").keyup(function() {
	        var chars = $("#comment_box_edit").val().length;
	        var charsLeft = 255 - parseInt(chars);
	        //Debug
	        //console.log(charsLeft);
	        $('#count_edit').html(charsLeft);
	    });
	
	    /*$('#comment_box_edit').blur(function() {
	        $('#post_' + contentId).html(postContent);
	    });*/
	    var newContent = $("#comment_box_edit").val();
	    
	    $("#edit_button").on("click", function(){
		    if(postContent != newContent) {
		    	var editPost = {"id":contentId, "user":accountId, "comment":newContent}
	            var response = $.ajax({
	                type: "POST",
	                url:'/api/v1/edit_post',
	                data: editPost,
	                success: function(data) {
	                    console.log(data);
	                    $("#" +  contentId).fadeOut(1000, function() {
	                        $(this).remove();
	                    });
	                }
	            });
	    	}
	    });
	    
	});
    
    

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

/* Edit Post */
var editPost = (function(postId){
    
    console.log(postId);
    var postContent = $("#post_" + postId).html();
    $("#post_" + postId).html("");
    $("#post_" + postId).append(
        "<div class='form-group'><input type='text' id='comment_box_edit' name='comment' class='comment_box' value='" + postContent + "' placeholder='Confess thy opinion.' size='255' autofocus> <input type='submit' value='Post' class='btn btn-primary' id='edit_button'> <div id='count_edit'>255</div></div>"
    );
    $("#comment_box_edit").keyup(function() {
        var chars = $("#comment_box_edit").val().length;
        var charsLeft = 255 - parseInt(chars);
        //Debug
        //console.log(charsLeft);
        $('#count_edit').html(charsLeft);
    });

    $('#comment_box_edit').blur(function() {
        $('#post_' + postId).html(postContent);
    });
});   
/* End Edit Post */

/* Report Content */
var reportContent = (function(contentId,type) {
    console.log(contentId);
    console.log(type);
    $("#reportModal").html("<div class='modal-dialog'> <div class='modal-content'> <div class='modal-header'> <button type='button' class='close' data-dismiss='modal'>×</button> <h3>Report Content</h3> </div> <div class='modal-body'><div class='input-group'> <h3>Are you sure that this content breaks WebMub's Terms and Services?</h3> </div> <div class='modal-footer'> <button id='report' class='btn btn-primary' data-dismiss='modal'>Yes</button> <button class='btn' data-dismiss='modal'>No</button> </div> </div> </div>").modal({
                    show: true,
                    keyboard: true
                });
    $("#report").one('click', function (e) {
        $.get( "/api/v1/user_login", function(user_login)
        {
            var report = {"id":contentId, "user":user_login}
            var response = $.ajax({
                 type: "POST",
                 url:'/api/v1/reports',
                 data: report
            });
            
            console.log(response);
            
            // Whenever I get the chance I should add this back in. But gotta get to work.
            /* .done(function( data ) {
                $("#reportModal").modal('hide');
                $("#reportModal").html("");
                
                $("#reportModal").html("<div class='modal fade'> <div class='modal-dialog'> <div class='modal-content'> <div class='modal-header'> <button type='button' class='close' data-dismiss='modal'><span aria-hidden='true'>&times;</span><span class='sr-only'>Close</span></button> </div> <div class='modal-body'> <p>" + data.message + "</p> </div> <div class='modal-footer'> <button type='button' class='btn btn-default' data-dismiss='modal'>Close</button> </div> </div> </div></div>").modal({
                    show: true,
                    keyboard: true
                    }); */
        });
    });
});
