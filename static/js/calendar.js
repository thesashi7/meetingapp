window.onload = function() {
  hideEventForm();
};


function hideEventForm()
{
  //alert("hide");
  document.getElementById('contact-main').style.display = "none";
}

function hideEventEdit()
{
  //alert("hide");
  document.getElementById('edit-event').style.display = "none";
}

function addEvent(year,month,day)
{
  document.getElementById('contact-main').style.display = "block";
  //alert(username);
  document.getElementsByName('date')[0].value = month+"-"+day+"-"+year;
  document.getElementsByName('std_date')[0].value = day+"."+month+"."+year;

}

function submitEvent()
{


}

function calendar(year,month,day)
{

  date = day+"."+month+"."+year;
  //alert(date);
  var data_json = {
      date: date
  };


  var data = JSON.stringify(data_json);
  //alert(data);

  var request = $.ajax({
    method: "POST",
    type: "POST",
    url: "calendar",
    data: data,
    contentType: "application/json"
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
       alert("Request success");
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

function saveEvent(info, date, start, end)
{
  var request = $.ajax({
   method: "POST",
   type: "POST",
   url: "addevent",
   data:'&info='+info+"&date="+date+"&start="+start+"&end="+end
 });

request.done(function(html) {
     alert(html);
     if(html == "Saved")
     {
       hideEventEdit();
       window.location.reload();
     }
 });

request.fail(function(jqXHR, textStatus) {
     alert( "Request failed: " + textStatus );
 });

}

function updateEvent(info, date, start, end, id)
{
//alert("id="+id);
  var request = $.ajax({
   method: "POST",
   type: "POST",
   url: "updateevent",
   data:'&info='+info+"&date="+date+"&start="+start+"&end="+end+"&id="+id
 });

request.done(function(html) {
     alert(html);
     if(html == "Saved")
     {
       hideEventEdit();
       window.location.reload();
     }
 });

request.fail(function(jqXHR, textStatus) {
     alert( "Request failed: " + textStatus );
 });

}


function deleteEvent(event_id, info, meeting_id, start, end)
{
   //alert(info);
   if(info == "Meeting")
   {
    alert("Please refer to Meeting Menu");
    return false;
   }
  var c = confirm("You are about to delete this Room. Are you sure?");

  if(c==true){
    var request = $.ajax({
     method: "POST",
     type: "POST",
     url: "deleteevent",
     data:'&id='+event_id
   });

  request.done(function(html) {
    alert(html);
    if(html == "Deleted")
    {
      hideEventEdit();
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


function addTime(time,length)
{
  start_time = moment(time, 'hh:mm A');
  //alert(start_time);
  //alert(length);
  end_time = start_time.clone();
  added = end_time.add(length,'minutes').format('hh:mm A');
  start_time = start_time.format('hh:mm A');
  end_time = end_time.format('hh:mm A');
  return end_time;
}

function submitEvent()
{
  var info = document.getElementsByName('info')[0].value;
  var start = document.getElementById("start");
  start = start.options[start.selectedIndex].value;
  var length = document.getElementById("length");
  length = length.options[length.selectedIndex].value;
  var date = document.getElementsByName('std_date')[0].value;
  if(info.length <= 0 || start.length <= 0 || length.length <= 0)
  {
    alert("Please don't leave the fields empty!");
    return false;
  }
  //  alert(date);
   // alert(start);
  //alert(room_id+" "+name+" "+capacity);
  var end = addTime(start, length);
  //alert(start+" - "+end);

  if(moment(start, "hh:mm A") >= end)
  {
    alert("Time must be apart!");
    return false;
  }
  //alert(date+" "+start+" - "+end);
  //alert("Passed");
  saveEvent(info, date, start, end);
}

function editEvent(event_id, info, meeting_id, start, end, month, day, year)
{
    //alert(info);
    if(info == "Meeting")
    {
        alert("Please refer to Meeting Menu");
        return false;
    }

    //alert("edit event");
      document.getElementById('edit-event').style.display = "block";
  //alert(username);
  document.getElementsByName('id2')[0].value = event_id
  document.getElementsByName('date_2')[0].value = month+"-"+day+"-"+year;
  document.getElementsByName('std_date_2')[0].value = day+"."+month+"."+year;
  document.getElementsByName('info_2')[0].value = info;
  document.getElementById("start_2").value = start
  document.getElementById("end_2").value = end
}

function submitEditEvent()
{
    //alert("submission");
  var info = document.getElementsByName('info_2')[0].value;
  var start = document.getElementById("start_2");
  start = start.options[start.selectedIndex].value;
  var length = document.getElementById("length_2");
  length = length.options[length.selectedIndex].value;
  var date = document.getElementsByName('std_date_2')[0].value;
  var id = document.getElementsByName('id2')[0].value
  if(info.length <= 0 || start.length <= 0 || length.length <= 0)
  {
    alert("Please don't leave the fields empty!");
    return false;
  }
   // alert(date);
 //   alert(start);
  //alert(room_id+" "+name+" "+capacity);
  var end = addTime(start, length);
  //alert(start+" - "+end);

  if(moment(start, "hh:mm A") >= end)
  {
    alert("Time must be apart!");
    return false;
  }
  //alert(date+" "+start+" - "+end);
  //alert("Passed");
  updateEvent(info, date, start, end, id);
}