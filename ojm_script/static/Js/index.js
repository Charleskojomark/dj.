// List of translations for "Get electricians in minutes"
const texts = [
  "Chọta ndị ọkụ eletrik ozugbo", // Igbo
  "Find electricians quick quick",
  "Nemo ƴan wutan lantarki nan da nan", // Hausa
  "Wa awọn onimọ ina lẹsẹkẹsẹ", // Yoruba
  "Get electricians in minutes",
];

// Get the h1 element
const h1Element = document.getElementById('changing-text');

let index = 0;

// Function to change the text
function changeText() {
  if (h1Element) {
    h1Element.style.opacity = 0; // Fade out
    setTimeout(() => {
      h1Element.textContent = texts[index];
      h1Element.style.opacity = 1; // Fade in
      index = (index + 1) % texts.length; // Loop back to the first text after the last one
    }, 1000); // Change text after 1 second when the opacity is 0
  }
}

// Change text every 8 seconds (8000 milliseconds)
if (h1Element) {
  setInterval(changeText, 8000);
}

function removeDiv(id) {
  const element = document.getElementById(id);
  if (element) {
    element.style.display = 'none';
  }
}

// Function to auto-hide divs after 8 seconds
function autoHideDiv(id) {
  setTimeout(() => {
    removeDiv(id);
  }, 8000);
}

const errorContainer = document.getElementById('error-container');

if (errorContainer) {
  // autoHideDiv('error-container');
}

// ads display
function swiperOne() {
  const swiperContainer = document.querySelector(".swiper-container");
  if (swiperContainer) {
    const swiper = new Swiper(".swiper-container", {
      loop: true, // Add this option to enable continuous sliding
      autoplay: {
        delay: 6000,
        disableOnInteraction: false,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: "fraction",
      },
    });
  }
}

swiperOne();

// services section
function swiperTwo() {
  const servicesSection = document.querySelector(".services_section");
  if (servicesSection) {
    let swiperServices = new Swiper(".services_section", {
      loop: true,
      grabCursor: true,
      spaceBetween: 48,
      autoplay: {
        delay: 8000,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: "fraction",
        dynamicBullets: true,
      },
      breakpoints: {
        568: {
          slidesPerview: 2,
        }
      }
    });
  }
}

swiperTwo();

// expert section
function swiperThree() {
  const expertSection = document.querySelector(".expert_section");
  if (expertSection) {
    let swiperServices = new Swiper(".expert_section", {
      loop: true,
      grabCursor: true,
      spaceBetween: 48,
      autoplay: {
        delay: 7000,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: "fraction",
        dynamicBullets: true,
      },
      breakpoints: {
        568: {
          slidesPerview: 2,
        }
      }
    });
  }
}

swiperThree();

// trending services
function swiperFour() {
  const trendingServices = document.querySelector(".trending_services");
  if (trendingServices) {
    let swiperServices = new Swiper(".trending_services", {
      slidesPerView: 1,
      autoplay: {
        delay: 7000,
      },
    });
  }
}

swiperFour();

const testimonialContainer = document.querySelector(".testimonial_container");
if (testimonialContainer) {
  let swiperTestimonial = new Swiper(".testimonial_container", {
    grabCursor: true,
    autoplay: {
      delay: 5000,
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      480: {
        slidesPerView: 1,
        spaceBetween: 30
      },
      676: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      796: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      900: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      1200: {
        slidesPerView: 3,
        spaceBetween: 40
      },
    }
  });
}
