window.onload = function() {
  function requestDesktopNotificationPermission(){
   if(Notification.permission !== "granted") {
     Notification.requestPermission(function (permission) {
        if(!('permission' in Notification)) {
          Notification.permission = permission;
        }
     });
   }
  }
  notify();
};

function notify()
{
  if ('Notification' in window) {
   //alert("Congrats you are using a modern browser and it supports Notification");
  }
  if (Notification.permission === "granted") {
  //  alert("Permission grantsted!");
    var text = "your Notification Body goes here";
    sendDesktopNotification(text);
  }
}

function sendDesktopNotification(text) {

  var request = $.ajax({
   method: "POST",
   type: "POST",
   url: "notify"
  });

 request.done(function(html) {
   //alert("Request success");
   var notif_data = JSON.parse(html);
   //alert(notif_data.length);
   for(var i = 0; i < notif_data.length; i++) {
      var obj = notif_data[i];
      let notification = new Notification('Meeting!', {
        body: obj.message,
        tag: 'soManyNotification'+obj.id,
        buttons: [
        { title: 'Mark' },
        { title: 'Ignore' }
      ]

      });
      notification.onclick = function(event) {
        event.preventDefault(); // prevent the browser from focusing the Notification's tab
        //alert(obj.meeting_id);
        if(obj.meeting_id)
        {
           window.open('./dashboard', '_blank');
        }
        else
        {
          var c = confirm("Don't see this again?");

          if(c==true){
           var request = $.ajax({
             method: "POST",
             type: "POST",
             url: "notify/seen",
             data:'&notification_id='+obj.id
           });
           notification.close();
          }
        }
      }
    }
});

 request.fail(function(jqXHR, textStatus) {
   //alert( "Request failed: " + textStatus );
 });

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
