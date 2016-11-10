$(document).ready(function() {
    $("#submit-comment").click(function() {
        $.ajax({
            method: "POST",
            //url: "/post/" + $(this).attr("post-id") + "/comment",
            url: "/post/1/comment",
            data: { 
                commentcontent: $("#comment-content").val(),
            },
            success: function(data) {
                $("#comment-content").val("");
                $("#comment-box").prepend(data);
            },
            error: function(error) {
            }
        });
    });
});
