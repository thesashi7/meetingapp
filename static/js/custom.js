

function selectLocation(location)
{
    //alert(location.value);
    var day = document.getElementsByName('first_day')[0];
    var month = document.getElementsByName('first_month')[0];
    var year = document.getElementsByName('first_year')[0];
    day = day.value;
    month = month.value;
    year = year.value;
    //alert(month+" "+day+" "+year);
    var request = $.ajax({
      method: "POST",
      type: "POST",
      url: "calLocation",
      data:'&location_id='+location.value+'&day='+day+'&month='+month+'&year='+year
    });

   request.done(function(html) {
        //alert("Request success");
         $('#calendar').html(html);
    });

  request.fail(function(jqXHR, textStatus) {
        //alert( "Request failed: " + textStatus );
    });
}

function calendar(day,month,year)
{
   //alert("I am an alert box!");

    var location = document.getElementById('location');
    location = location.options[location.selectedIndex].value;


   var request = $.ajax({
    method: "POST",
    type: "POST",
    url: "calendar",
    data:'func=getCalendar&day='+day+'&month='+month+'&year='+year
        +'&location='+location

  });

  request.done(function(html) {
    //alert("Request success");
    $('#calendar').html(html);
  });

  request.fail(function(jqXHR, textStatus) {
    //alert( "Request failed: " + textStatus );
  });

   return false;
}

function calendarBack(day,month,year,location)
{
   //alert(day+" "+month+" "+year+" "+location);

   var request = $.ajax({
    method: "POST",
    type: "POST",
    url: "calendar",
    data:'&func=back&day='+day+'&month='+month+'&year='+year
        +'&location='+location

  });

  request.done(function(html) {
    //alert("Request success");
    $('#main-calendar').html(html);
  });

  request.fail(function(jqXHR, textStatus) {
    //alert( "Request failed: " + textStatus );
  });

   return false;
}

function selectAppt(date,startTime,step)
{
    alert(date+" "+startTime);
    window.location.href = "selectroom.html";
    var location = document.getElementById('location');
    location = location.options[location.selectedIndex].value;

    var request = $.ajax({
      method: "POST",
      type: "POST",
      url: "appt",
      data:'&date='+date+'&startTime='+startTime+'&step='+step
      +'&location='+location
    });

   request.done(function(html) {
        //alert("Request success");
         $('#calendar-location').html("");
         $('#calendar').html("");
         $('#calendar').html(html);
    });

  request.fail(function(jqXHR, textStatus) {
        //alert( "Request failed: " + textStatus );
    });
}

function confirm(){
    //alert("confirm");
    var name = document.getElementsByName('name')[0].value;
    var email = document.getElementsByName('email')[0].value;
    var phone = document.getElementsByName('phone')[0].value;
    var date = document.getElementsByName('date')[0].value;
    var sTime = document.getElementsByName('startTime')[0].value;
    var service = document.getElementById('service');
    var location = document.getElementsByName('location')[0].value;
    service = service.options[service.selectedIndex].value;
    service = service.split(",");

    //alert(service[1]);
    $('#prompt-name').html("");
    $('#prompt-email').html("");
    $('#prompt-phone').html("");
    $('#prompt-service').html("");
    if(name.length<=1){
        $('#prompt-name').html("Please Enter Full Name");
    }
    else if(verifyEmail(email)==false){
        $('#prompt-email').html("Please Enter Email Address");
    }
    else if(verifyPhone(phone)==false){
       $('#prompt-phone').html("Please Enter Phone/Cell Number");
    }
    else if(service[0].length==0){
       $('#prompt-service').html("Please Select a Service");
    }
    else{

     document.getElementById("step2").style.display = 'block';
     document.getElementById("step1").style.display = 'none';
     $('#time-c').html(date+" "+sTime);
     $('#name-c').html(name);
     $('#email-c').html(email);
     $('#phone-c').html(phone);
     $('#service-c').html(service[1]);
     $('#location-c').html(location);
    }
}

function back(from){
    if(from=='2'){
        document.getElementById("step1").style.display = 'block';
        document.getElementById("step2").style.display = 'none';
    }
    else if(from=='1'){
        /*var date = document.getElementsByName('date')[0].value;
        var location = document.getElementsByName('location_id')[0].value;
        date = date.split("-");
        calendarBack(date[1],date[0],date[2],location);*/
        window.location = 'test.html';
    }
}

function verifyEmail(email){
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function verifyPhone(phone){
    var re = /^[(]{0,1}[0-9]{3}[)]{0,1}[-\s\.]{0,1}[0-9]{3}[-\s\.]{0,1}[0-9]{4}$/;
    return re.test(phone);
}

function addEmp(){
  var e = document.getElementById("service");
  var strvalue = e.options[e.selectedIndex].value;
  var strname = e.options[e.selectedIndex].text;
//  var a = document.getElementById("name");
  var div = document.createElement("div");
  //div.style.width = "100px";
  //div.style.height = "100px";
  div.style.background = "rgba(0,0,0,.5)";
  div.style.color = "";
  div.innerHTML = strname;
  div.id = "addedname"+strname;
  var myElem = document.getElementById(div.id);
  if (myElem !== null) return false;
  var button = document.createElement("button");
  button.innerHTML = "Remove";
  button.type = "button";
  // 3. Add event handler
  button.addEventListener ("click", function() {
    var elem = document.getElementById("addedname"+strname);
    elem.parentNode.removeChild(elem);
  });

  document.getElementById("listnames").appendChild(div);
  document.getElementById("addedname"+strname).appendChild(button);
}
