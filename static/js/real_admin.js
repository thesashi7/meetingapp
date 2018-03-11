window.onload = function() {
  hideEdit();
};

function hideEdit()
{
  //alert("hide");
  document.getElementById('contact-main').style.display = "none";
}

function editEmployee(emp_id, username)
{
  document.getElementById('contact-main').style.display = "block";
  //alert(username);
  document.getElementsByName('username')[0].value = username;
  document.getElementsByName('emp_id')[0].value = emp_id;
}

function submitEditEmployee()
{
  var emp_id = document.getElementsByName('emp_id')[0].value;
  var username = document.getElementsByName('username')[0].value;
  var password = document.getElementsByName('password')[0].value;
  if(!validCredentials(username, password))
  {
    alert("Please don't leave the fields empty!");
    return false;
  }
  //alert(emp_id+" "+username+" "+password);

  saveEmployee(emp_id, username, password);

}

function editRoom(room_id, name, capacity)
{
  document.getElementById('contact-main').style.display = "block";
  //alert(name);
  document.getElementsByName('name')[0].value = name;
  document.getElementsByName('room_id')[0].value = room_id;
  document.getElementsByName('capacity')[0].value = capacity;
}

function submitEditRoom()
{
  var room_id = document.getElementsByName('room_id')[0].value;
  var name = document.getElementsByName('name')[0].value;
  var capacity = document.getElementsByName('capacity')[0].value;
  if(name.length <= 0 || capacity.length <= 0)
  {
    alert("Please don't leave the fields empty!");
    return false;
  }
  //alert(room_id+" "+name+" "+capacity);

  saveRoom(room_id, name, capacity);

}


function validCredentials(username, passw)
{
  if(username.length>0 && passw.length>0)
  {
    return true;
  }
  return false;
}


function saveEmployee(emp_id,username, password)
{
  var request = $.ajax({
   method: "POST",
   type: "POST",
   url: "admin_config_emp",
   data:'&employee_id='+emp_id+"&username="+username+"&password="+password
 });

request.done(function(html) {
     alert(html);
     if(html == "Saved")
     {
       hideEdit();
       window.location.reload();
     }
 });

request.fail(function(jqXHR, textStatus) {
     alert( "Request failed: " + textStatus );
 });
}


function saveRoom(room_id, name, capacity)
{
  var request = $.ajax({
   method: "POST",
   type: "POST",
   url: "admin_config_room",
   data:'&room_id='+room_id+"&name="+name+"&capacity="+capacity
 });

request.done(function(html) {
     alert(html);
     if(html == "Saved")
     {
       hideEdit();
       window.location.reload();
     }
 });

request.fail(function(jqXHR, textStatus) {
     alert( "Request failed: " + textStatus );
 });
}

function deleteRoom(room_id)
{
  var c = confirm("You are about to delete this Room. Are you sure?");

  if(c==true){
    var request = $.ajax({
     method: "POST",
     type: "POST",
     url: "delete_room",
     data:'&room_id='+room_id
   });

  request.done(function(html) {
    alert(html);
    if(html == "Deleted")
    {
      hideEdit();
      window.location.reload();
    }
   });

 request.fail(function(jqXHR, textStatus) {
       alert( "Request failed: " + textStatus );
   });
  }
  else{

  }
}

function deleteEmployee(emp_id)
{
  var c = confirm("You are about to delete this Employee. Are you sure?");

  if(c==true){
    var request = $.ajax({
     method: "POST",
     type: "POST",
     url: "delete_emp",
     data:'&employee_id='+emp_id
   });

  request.done(function(html) {
    alert(html);
    if(html == "Deleted")
    {
      hideEdit();
      window.location.reload();
    }
   });

 request.fail(function(jqXHR, textStatus) {
       alert( "Request failed: " + textStatus );
   });
  }
  else{

  }
}

function closeEdit()
{
  hideEdit();
}
