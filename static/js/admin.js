$(document).ready(function() {
window.onload = function(){
$('#own-tab').click();
requestDesktopNotificationPermission();
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

function requestDesktopNotificationPermission(){
  alert("ask permission");
 if(Notification.permission !== "granted") {
   Notification.requestPermission(function (permission) {
      if(!('permission' in Notification)) {
        Notification.permission = permission;
      }
   });
 }
}

});



function acceptMeeting(meeting_attendee_id)
{
    alert("accepting");
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

    if ('Notification' in window) {
   alert("Congrats you are using a modern browser and it supports Notification");
  }
  if (Notification.permission === "granted") {
    alert("Permission grantsted!");
    var text = "your Notification Body goes here";
    sendDesktopNotification(text);
  }
}

function sendDesktopNotification(text) {
    let notification = new Notification('Your Page Title', {
      body: text,
      tag: 'soManyNotification',
    });
    notification.onclick = function(event) {
      event.preventDefault(); // prevent the browser from focusing the Notification's tab
      window.open('https://www.google.com/', '_blank');
    }
    //’tag’ handles muti tab scenario i.e when multiple tabs are
    // open then only one notification is sent
//3. handle notification events and set timeout
/**notification.onclick = function() {
      parent.focus();
      window.focus(); //just in case, older browsers
      this.close();
    };**/
    //setTimeout(notification.close.bind(notification), 5000);
  }

function declineMeeting(meeting_attendee_id)
{
    alert("decline");
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

function confirmCompleteAppt(id)
{
   var c = confirm("You are about to complete this appointment. Are you sure?");

   if(c==true){
     var request = $.ajax({
      method: "POST",
      type: "POST",
      url: "apptComplete",
      data:'&appt_id='+id_num
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

   id_num = id;
   id_name = "delete_s";
   id_name = id_name.concat(id_num.toString());

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
