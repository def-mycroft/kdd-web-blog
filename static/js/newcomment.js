$(document).ready(function() {
    $("#submit-comment").click(function() {
        $.ajax({
            method: "POST",
            url: "/post/" + $("#comment-box").attr("postid") + "/comment",
            data: { 
                comment_content: $("#comment-content").val()
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
