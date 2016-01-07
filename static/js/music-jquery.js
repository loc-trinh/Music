/**
 * Created by loctrinh on 1/6/16.
 */
$(document).ready(function(){
    $(".select_video").click(function(){
        $("#player").show();
        var videoId = $(this).attr("data-videoId");
        $.get("/player/", {"videoId": videoId}, function(data){
            $("#player").html(data);
        });
        $.get("/related_videos/", {"videoId": videoId}, function(data){
            $("#related").html(data);
        });
    });

    $("#related").on("click",'.select_related_video', function(){
        $("#player").show();
        var videoId = $(this).attr("data-videoId");
        $.get("/player/", {"videoId": videoId}, function(data){
            $("#player").html(data);
        });
        $.get("/related_videos/", {"videoId": videoId}, function(data){
            $("#related").html(data);
        });
    });

    $("#basic-addon2").click(function(){
        document.forms["form"].submit();
    }).hover(function(){
        $(this).css("font-weight", "bold");
    }, function(){
        $(this).css("font-weight", "normal");
    });


});