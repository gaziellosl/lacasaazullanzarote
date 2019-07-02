

// function dropDownClick(id) {
//   var x = document.getElementById(id);
//   if (x.className.indexOf("w3-show") == -1) {
//     x.className += " w3-show";
//   } else {
//     x.className = x.className.replace(" w3-show", "");
//   }
// }

function dropDownClick(id, callback) {

  var x = document.getElementById(id);
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }

  if (typeof callback === 'function' && callback()){
    callback();
  }
}

// Slides

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

document.onclick = function(event) {
    // Compensate for IE<9's non-standard event model
    //
    // if (event===undefined) event= window.event;
    // var target= 'target' in event? event.target : event.srcElement;
    // alert('clicked on '+target.tagName);
    for (dropdownName of dropdownNames) {
      dropdown = document.getElementById(dropdownName)
      button = document.getElementById(dropdownName + '_button')
      if (dropdown.style.display != "none" && (!dropdown.mouseIsOver && !button.mouseIsOver)){
        dropdown.style.display = "none";
      }
    }
};

function setLanguage(language) {
  //document.cookie = "language=" + language + "; expires=Thu, 8 Dec 2033 12:00:00 UTC";
}
