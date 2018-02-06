$(document).ready(function() {
window.onload = function(){

        $('#accepted-tab').click();
}

var idleTime = 0;
$(document).ready(function () {
    //Increment the idle time counter every minute.
    var idleInterval = setInterval(timerIncrement, 1000); // 1 minute

    //Zero the idle timer on mouse movement.
    $(this).mousemove(function (e) {
        idleTime = 0;
    });
    $(this).keypress(function (e) {
        idleTime = 0;
    });
});

function timerIncrement() {
    idleTime = idleTime + 1;
    if (idleTime > 10) { // 20 minutes
        //window.location.reload();
    }
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

function confirmCompleteAppt(id)
{
   var c = confirm("You are about to complete this appointment. Are you sure?");

   id_num = id;
   id_name = "delete_c";
   id_name = id_name.concat(id_num.toString());
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

function confirmDeleteStylist(id)
{
   var c = confirm("You are about to delete this record. Are you sure?");

   id_num = id;
   id_name = "delete_s";
   id_name = id_name.concat(id_num.toString());

   if(c==true){
      document.getElementById(id_name).click();
   }
   else{

   }
}
