$(document).ready(function () {
    window.onload = function () {

        $('#own-tab').click();
    }


    $(" #pending-tab, #accepted-tab, #own-tab").click(function () {
        $("li").removeClass("active");
        $(this).addClass("active");
    });


    $("#pending-tab").click(function () {
        hideAllLocation();
        $("#pending-table").show();
    });

    $("#accepted-tab").click(function () {
        hideAllLocation();
        $("#accepted-table").show();
    });

    $("#own-tab").click(function () {
        hideAllLocation();
        $("#own-table").show();
    });

    function hideAllLocation() {
        $("#accepted-table").hide();
        $("#pending-table").hide();
        $("#own-table").hide();
    }


});

function confirmCompleteAppt(id) {
    var c = confirm("You are about to complete this appointment. Are you sure?");

    id_num = id;
    id_name = "delete_c";
    id_name = id_name.concat(id_num.toString());
    if (c == true) {
        var request = $.ajax({
            method: "POST",
            type: "POST",
            url: "apptComplete",
            data: '&appt_id=' + id_num
        });

        request.done(function (html) {
            alert("Request success");
            window.location.reload();
        });

        request.fail(function (jqXHR, textStatus) {
            alert("Request failed: " + textStatus);
        });
    }
    else {

    }
}

function confirmCancelMeeting(id) {
    var c = confirm("You are about to cancel this meeting. Are you sure?");

    id_num = id;
    id_name = "delete_s";
    id_name = id_name.concat(id_num.toString());

    if (c == true) {
        var request = $.ajax({
            method: "POST",
            type: "POST",
            url: "cancelmeeting",
            data: '&meeting_id=' + id_num
        });

        request.done(function (html) {
            alert("Request success");
            window.location.reload();
        });

        request.fail(function (jqXHR, textStatus) {
            alert("Request failed: " + textStatus);
        });
    }
    else {

    }
}
