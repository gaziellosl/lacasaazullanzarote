function hamburgerMenu() {
  var x = document.getElementById("hamburguer_links");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

// Slides

function showSlides(n, plus=) {
  var i;
  var n = plus;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length-1) {slideIndex = 0}
  if (n < 0) {slideIndex = slides.length-1}
  for (i = 0; i < slides.length; i++) {
      if (slides[i].style.display == "block"){
        slides[i].style.display = "none";
        slideIndex = slideIndex + i;
        break;
      }
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex].style.display = "block";
  dots[slideIndex].className += " active";
}

// Next/previous controls
function plusSlides(n) {
  showSlides(n);
}

// Thumbnail image controls
function currentSlide(n) {
  var slideIndex = getSlidesIndex();
  showSlides(slideIndex = n);
}

showSlides(0);

// setTimeout(plusSlides(+1), 1000)
