/**
 * Created by loctrinh on 1/6/16.
 */
$(document).ready(function(){
    $(".select_video").click(function(){
        $("#player").show();
        $("#add_form").show();

        var videoId = $(this).attr("data-videoId");
        var title = $(this).attr("data-title");
        $("#add_to_queue").attr( "data-videoId", videoId );
        $("#add_to_queue").attr( "data-title", title );

        $.get("/player/", {"videoId": videoId}, function(data){
            $("#player").html(data);
        });
        $.get("/related_videos/", {"videoId": videoId}, function(data){
            $("#related").html(data);
        });
    });

    $("#related").on("click",'.select_related_video', function(){
        $("#player").show();
        $("#add_form").show();

        var videoId = $(this).attr("data-videoId");
        var title = $(this).attr("data-title");
        $("#add_to_queue").attr( "data-videoId", videoId );
        $("#add_to_queue").attr( "data-title", title );

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

    $("#add_to_queue").on("submit", function(e){
        e.preventDefault();
        $("#add_form").hide();
        var videoId = $(this).attr("data-videoId");
        var title = $(this).attr("data-title");
        var playlist = $("#playlist_select").val();
        $.get("/add_to_queue/", {"videoId": videoId, "playlist": playlist, "title": title}, function(data){
            $("#download_queue").html(data);
        });
    });

});