

// function dropDownClick(id) {
//   var x = document.getElementById(id);
//   if (x.className.indexOf("w3-show") == -1) {
//     x.className += " w3-show";
//   } else {
//     x.className = x.className.replace(" w3-show", "");
//   }
// }

var dropdowns =[]

function dropDownClick(id, callback) {
  if (dropdowns[id][0].style.display === "block") {
    dropdowns[id][0].style.display = "none";
  } else {
    dropdowns[id][0].style.display = "block";
  }

  if (typeof callback === 'function' && callback()){
    callback();
  }
}

document.onclick = function(event) {
    // Compensate for IE<9's non-standard event model
    //
    // if (event===undefined) event= window.event;
    // var target= 'target' in event? event.target : event.srcElement;
    // alert('clicked on '+target.tagName);
    for (dropdown of dropdowns) {
      if (dropdown[0].style.display != "none" && (!dropdown[0].mouseIsOver && !dropdown[1].mouseIsOver)){
        dropdown[0].style.display = "none";
      }
    }
};

function setDropDownButtonName(id, val){
  dropdowns[id][1].innerHTML = val;
}

// Slides

function sendEmail() {
  var obj = document.getElementsByClassName("w3-input")
  var i;
  var body = "";
  var date = document.getElementById("dateForm").value;
  var appartment = document.getElementById("dropdown_reserve_button").innerHTML;
  var subject = "Web%20Reserve:%20" + appartment + ".%20" + date;

  body += document.getElementById("appartmentFormTitle").innerHTML + "%20"
    + appartment + "%0D%0A";
  var dateTitle = document.getElementById("dateFormTitle").innerHTML;
  body += dateTitle.substring(0, dateTitle.indexOf("<")) + ":%20"
    + date + "%0D%0A";

  var text = "mailto:gaziellosl@gmail.com?subject=" + subject + "&body=" + body;
  for (i=0;i<obj.length;i++){
    var placeholder = obj.item(i).placeholder;
    var value = obj.item(i).value
    if (value != null){
      body += placeholder + ":%20" + value + "%0D%0A";
    }
  }

  var text = "mailto:gaziellosl@gmail.com?subject=" + subject + "&body=" + body;
  window.open(text);
}

function showSlides(n, id, to=null) {
  var i;
  if (to!=null){slideIndex[n]=to;}
  var slides = document.getElementsByClassName("slides_"+id);
  var dots = document.getElementsByClassName("dot_"+id);
  if (slideIndex[n] > slides.length-1) {slideIndex[n] = 0}
  if (slideIndex[n] < 0) {slideIndex[n] = slides.length-1}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex[n]].style.display = "block";
  dots[slideIndex[n]].className += " active";
}

function showSlidesPlus(n, id, plus){
   slideIndex[n]=slideIndex[n]+plus;
   showSlides(n, id);
 }

 function showSlidesPlusWithCheck(n, id, plus){
   if (!document.getElementById("slideshow-container_"+id).mouseIsOver){
     showSlidesPlus(n, id, plus)
   }
  }

var slideIndex = []

function initDivMouseOver(id)   {
   var div = document.getElementById(id);
   div.mouseIsOver = false;
   div.onmouseover = function()   {
      this.mouseIsOver = true;
   };
   div.onmouseout = function()   {
      this.mouseIsOver = false;
   }
   return div;
}


function setLanguage(language) {
  document.cookie = "language=" + language + "; expires=Thu, 8 Dec 2033 12:00:00 UTC";
}
