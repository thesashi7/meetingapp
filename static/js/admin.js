$(document).ready(function() {
window.onload = function(){
$('#own-tab').click();
}

$(" #pending-tab, #accepted-tab, #own-tab").click(function(){
	$("li").removeClass("active");
	$(this).addClass("active");
});


$("#pending-tab").click(function(){
	hideAllLocation();
	$("#pending-table").show();
});

$("#accepted-tab").click(function(){
	hideAllLocation();
	$("#accepted-table").show();
});

$("#own-tab").click(function(){
	hideAllLocation();
	$("#own-table").show();
});

function hideAllLocation(){
  $("#accepted-table").hide();
	$("#pending-table").hide();
	$("#own-table").hide();
}


});



function acceptMeeting(meeting_attendee_id)
{
    //alert("accepting");
    var c = confirm("You are about to accept this Meeting. Are you sure?");

		if(c==true){
			var request = $.ajax({
			 method: "POST",
			 type: "POST",
			 url: "acceptmeeting",
			 data:'&meeting_attendee_id='+meeting_attendee_id
		 });

		request.done(function(html) {
				 alert("Request success");
				 window.location.reload();
		 });

		request.fail(function(jqXHR, textStatus) {
				 alert( "Request failed: " + textStatus );
		 });
		}
		else{

		}
}


function declineMeeting(meeting_attendee_id)
{
    //alert("decline");
		var c = confirm("You are about to decline this meeting. Are you sure?");

		if(c==true){
			var request = $.ajax({
			 method: "POST",
			 type: "POST",
			 url: "declinemeeting",
			 data:'&meeting_attendee_id='+meeting_attendee_id
		 });

		request.done(function(html) {
				 alert("Request success");
				 window.location.reload();
		 });

	 request.fail(function(jqXHR, textStatus) {
				 alert( "Request failed: " + textStatus );
		 });
		}
		else{

		}
}


function confirmCancelMeeting(id)
{
   var c = confirm("You are about to cancel this meeting. Are you sure?");


   if(c==true){
     var request = $.ajax({
      method: "POST",
      type: "POST",
      url: "cancelmeeting",
      data:'&meeting_id='+id_num
    });

   request.done(function(html) {
        alert("Request success");
        window.location.reload();
    });

  request.fail(function(jqXHR, textStatus) {
        alert( "Request failed: " + textStatus );
    });
   }
   else{

   }
}
