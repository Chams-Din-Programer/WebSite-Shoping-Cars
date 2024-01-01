'use strict';

/**
 * navbar toggle
 */

const overlay = document.querySelector("[data-overlay]");
const navbar = document.querySelector("[data-navbar]");
const navToggleBtn = document.querySelector("[data-nav-toggle-btn]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");

const navToggleFunc = function () {
  navToggleBtn.classList.toggle("active");
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
}

navToggleBtn.addEventListener("click", navToggleFunc);
overlay.addEventListener("click", navToggleFunc);

for (let i = 0; i < navbarLinks.length; i++) {
  navbarLinks[i].addEventListener("click", navToggleFunc);
}



/**
 * header active on scroll
 */

var title = document.getElementsByTagName('title')[0].innerHTML;
var c = 0;
function writetitle(){
  document.title = title.substring(0,c)
  if(c == title.length){
    c = 0;
    setTimeout("writetitle()",1000)
  }
  else{
    c++;
    setTimeout("writetitle()",200)
  }
}
writetitle()

const prevBtn = document.querySelector('[data-prev]');
const nextBtn = document.querySelector('[data-next]');

const slider = document.querySelector('.slider-banner');
const slides = slider.querySelectorAll('.product-banner');

let currentSlideIndex = 0;

prevBtn.addEventListener('click', () => {
  currentSlideIndex--;
  moveSlide();
});

nextBtn.addEventListener('click', () => {
  currentSlideIndex++;
  moveSlide();
});

function moveSlide() {
  if (currentSlideIndex < 0) {
    currentSlideIndex = slides.length - 1;
  } else if (currentSlideIndex >= slides.length) {
    currentSlideIndex = 0;
  }

  const slideMovement = -currentSlideIndex * slides[0].clientWidth;

  slider.style.transform = `translateX(${slideMovement}px)`;
}

moveSlide();


const openBtn = document.getElementById('open-btn');
const lightbox = document.getElementById('lightbox');
const closeBtn = document.getElementById('close-btn');

openBtn.addEventListener('click', () => {
  lightbox.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
  lightbox.style.display = 'none';
});

// Show/hide the button when the user scrolls down/up
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("scroll-top-btn").style.display = "block";
  } else {
    document.getElementById("scroll-top-btn").style.display = "none";
  }
}

// Scroll to the top of the page when the button is clicked
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}