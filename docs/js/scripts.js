

// function dropDownClick(id) {
//   var x = document.getElementById(id);
//   if (x.className.indexOf("w3-show") == -1) {
//     x.className += " w3-show";
//   } else {
//     x.className = x.className.replace(" w3-show", "");
//   }
// }


function toggleSwitchButton(state, id){
  const slidesShow = document.getElementById(`slideshow-container_${id}`);
  const virtualTour = document.getElementById(`virtual-tour-${id}`);
  if (state) {
    slidesShow.style.display = "none";
    virtualTour.style.display = "block";
  } else {
    slidesShow.style.display = "block";
    virtualTour.style.display = "none";
  }
}

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

  body += "%0D%0A" + "Note: there was an error with the website.".replace(' ',"%20") + "%0D%0A";

  var text = "mailto:gaziellosl@gmail.com?subject=" + subject + "&body=" + body;
  window.open(text);
}

function formDisappear(){
  var reservation_form = document.getElementById("reserve_form");
  var reservation_form_text = document.getElementById("reservation_form_text");
  reservation_form.style.display = "none";
  reservation_form_text.style.display = "none";

  var loading_spinner = document.getElementById("loading_spinner");
  loading_spinner.style.display = "block"
}

function updateForm(success) {

  var loading_spinner = document.getElementById("loading_spinner");
  loading_spinner.style.display = "none"

  var reservation_form_success = document.getElementById("reservation_form_success");
  var reservation_form_failure= document.getElementById("reservation_form_failure");

  if (success){
    reservation_form_success.style.display = "block";
    reservation_form_failure.style.display = "none";
  } else {
    reservation_form_success.style.display = "none";
    reservation_form_failure.style.display = "block";
  }
}


function sendRequest() {

  var obj = document.getElementsByClassName("w3-input")

  results = {}

  results['name'] = obj.item(0).value
  results['email'] = obj.item(1).value
  results['qty_people'] = obj.item(2).value
  results['qty_nights'] = obj.item(4).value
  results['date'] = document.getElementById("dateForm").value;
  results['apartment'] = document.getElementById("dropdown_reserve_button").innerHTML;
  results['special'] = obj.item(6).value

  const xhr = new XMLHttpRequest();
  const url = 'https://tjdh4namwe.execute-api.us-east-1.amazonaws.com/default/server-lacasaazul';
  xhr.open("POST", url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = (e) => {
    updateForm(parseInt(xhr.response))
  }

  xhr.send(JSON.stringify(results));
  formDisappear()

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

function languageChanged(language) {
  setLanguage(language);
  window.location = "/" + language;
}

function setLanguage(language) {
  document.cookie = "language=" + language + "; expires=Thu, 8 Dec 2033 12:00:00 UTC";
}
