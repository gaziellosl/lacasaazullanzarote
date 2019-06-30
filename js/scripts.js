function hamburgerMenu() {
  var x = document.getElementById("hamburguer_links");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

// Slides

function showSlides(n, id, to=null) {
  var i;
  if (to!=null){slideIndex[n]=to;}
  console.log(slideIndex[n]);
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
   var div = document.getElementById("slideshow-container_"+id);
   console.log("HELLO")
   div.mouseIsOver = false;
   div.onmouseover = function()   {
      this.mouseIsOver = true;
   };
   div.onmouseout = function()   {
      this.mouseIsOver = false;
   }
   // div.onclick = function()   {
   //    if (this.mouseIsOver)   {
   //       ....
   //    }
   // }
}
