window.onload = function() {
  showStep1();
};

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


function step1(){
    //alert("confirm");
    /*var name = document.getElementsByName('name')[0].value;
    var email = document.getElementsByName('email')[0].value;
    var phone = document.getElementsByName('phone')[0].value;
    var date = document.getElementsByName('date')[0].value;
    var sTime = document.getElementsByName('startTime')[0].value;
    var service = document.getElementById('service');
    var location = document.getElementsByName('location')[0].value;*/
    var e = document.getElementById("employee");
    var strvalue = e.options[e.selectedIndex].value;
    var strname = e.options[e.selectedIndex].text;
    var values = $('#employee').val();
    var list = document.getElementById("listnames").querySelectorAll(".select");
    //alert(list.length);
    if(list.length == 0)
    {
        alert("Please Select at least one Employee!");
        return false;
    }

    var employees = {
        selected: []
    };

    list.forEach(function(el) {
      //alert(el.children[0].innerHTML);
      employees.selected.push({
          "employee_id" : el.children[0].innerHTML
      });
    })

  var data_emp = JSON.stringify(employees);
  //alert(data_emp);
  var request = $.ajax({
    method: "POST",
    type: "POST",
    url: "scheduletime",
    data: data_emp,
    contentType: "application/json"
  });

  request.done(function(html) {
       //alert("Request success");

   });

 request.fail(function(jqXHR, textStatus) {
       alert( "Request failed: " + textStatus );
   });
//   document.getElementById("step1").style.display = 'none';
//   document.getByElementId("step2").style.display = "block";
     showStep2();
}

function hideAllSteps()
{
  document.getElementById("step1").style.display = 'none';
  document.getElementById("step2").style.display = 'none';
  document.getElementById("step3").style.display = 'none';
}

function showStep1()
{
  hideAllSteps();
  document.getElementById("step1").style.display = 'block';
}

function showStep2()
{
  hideAllSteps();
  document.getElementById("step2").style.display = 'block';
}

function showStep3()
{
  hideAllSteps();
  document.getElementById("step3").style.display = 'block';

}
function getEndTime()
{
  var e = document.getElementById("meet_length");
  var length = e.options[e.selectedIndex].value;

  start_time = document.getElementById("starttime").value;
  start_time = moment(start_time, 'hh:mm A');
  //alert(start_time);
  //alert(length);
  end_time = start_time.clone();
  added = end_time.add(length,'minutes').format('hh:mm A');
  start_time = start_time.format('hh:mm A');
  end_time = end_time.format('hh:mm A');
  return end_time;
}

function step2()
{
  //alert("step2");

  year = document.getElementById("date").value;
  start_time = document.getElementById("starttime").value;
  if(year.length ==0 || start_time.length==0 )
  {
    alert("Please select date and time!");
    return false;
  }
  end_time = getEndTime();
  var list = document.getElementById("listnames").querySelectorAll(".select");
  //alert(list.length);

  var data_json = {
      selected: [],
      start: start_time,
      end: end_time,
      date: year
  };

  list.forEach(function(el) {
    //alert(el.children[0].innerHTML);
    data_json.selected.push({
        "employee_id" : el.children[0].innerHTML
    });
  })

  var data = JSON.stringify(data_json);
  //alert(data);

  var request = $.ajax({
    method: "POST",
    type: "POST",
    url: "scheduleroom",
    data: data,
    contentType: "application/json"
  });

  request.done(function(html) {
      // alert("Request success");
       document.getElementById('step3a').innerHTML = html;
   });

 request.fail(function(jqXHR, textStatus) {
       alert( "Request failed: " + textStatus );
   });

  showStep3();
}

function selectSlot(year,month, day, start, end)
{
  //alert("hooo");
  document.getElementById("date").value = day+"."+month+"."+year;
  document.getElementById("starttime").value = start;
  //alert(document.getElementById("date").value);
  //alert(document.getElementById("starttime").value);


  step2();
}

function step3(room_id)
{
  //alert("step3");
  year = document.getElementById("date").value;
  start_time = document.getElementById("starttime").value;
  if(year.length ==0 || start_time.length==0 )
  {
    alert("Please select date and time!");
    return false;
  }
  end_time = getEndTime();

  var list = document.getElementById("listnames").querySelectorAll(".select");
  //alert(list.length);

  var data_json = {
      selected: [],
      start: start_time,
      end: end_time,
      date: year,
      room: room_id
  };

  list.forEach(function(el) {
   // alert(el.children[0].innerHTML);
    data_json.selected.push({
        "employee_id" : el.children[0].innerHTML
    });
  })

  var data = JSON.stringify(data_json);
  //alert(data);
  // construct an HTTP request
  var request = $.ajax({
    method: "POST",
    type: "POST",
    url: "submitmeeting",
    data: data,
    contentType: "application/json"
  });

  request.done(function(html) {
       //alert("Request success");
       document.getElementById("main-calendar").innerHTML = html;
   });

 request.fail(function(jqXHR, textStatus) {
       alert( "Request failed: " + textStatus );
   });
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
        //window.location = 'test.html';
    }
    else if(from=='3')
    {
      showStep2();
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
  var e = document.getElementById("employee");
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
  div.classList.add("select");
  div.nodeValue = strvalue;
  var id_div = document.createElement("div");
  id_div.type = "text";
  id_div.innerHTML = strvalue;
  id_div.style.display = 'none';
  div.appendChild(id_div);
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

function addMinutes(date, minutes) {
    return new Date(date.getTime() + minutes*60000);
}
