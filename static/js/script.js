document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const flashes = document.querySelectorAll(".flash");
        flashes.forEach(flash => flash.remove());
    }, 4000);
});

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("demo");
  let captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}

const sections = document.querySelectorAll('section');

window.addEventListener('scroll', () => {
  const triggerBottom = window.innerHeight / 5 * 4;

  sections.forEach(section => {
    const sectionTop = section.getBoundingClientRect().top;

    if(sectionTop < triggerBottom) {
      section.classList.add('show');
    } else {
      section.classList.remove('show');
    }
  });
});
  const spot = document.getElementById('spotlight');

  window.addEventListener('mousemove', e => {
    spot.style.left = e.clientX + 'px';
    spot.style.top  = e.clientY + 'px';
  }, {passive: true});

  window.addEventListener('touchmove', e => {
    const t = e.touches[0];
    if (!t) return;
    spot.style.left = t.clientX + 'px';
    spot.style.top  = t.clientY + 'px';
  }, {passive: true});

  document.addEventListener('mousedown', () => {
    spot.style.width = '420px';
    spot.style.height = '420px';
  });
  document.addEventListener('mouseup', () => {
    spot.style.width = '';
    spot.style.height = '';
  });