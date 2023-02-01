$(document).ready(function () {   
   $('#followersModal').modal('show')
})
$(function () {

   if ($('.popular-posts-carousel').length > 0) {
      $('.popular-posts-carousel').owlCarousel({
         center: false,
         items: 1,
         loop: false,
         stagePadding: 0,
         margin: 20,
         smartSpeed: 1000,
         autoplay: true,
         nav: true,
         dots: true,
         pauseOnHover: true,
         responsive: {
            600: {
               margin: 20,
               nav: true,
               items: 1
            },
            1000: {
               margin: 20,
               stagePadding: 0,
               nav: true,
               items: 1
            }
         }
      });
   }

})

var AuthorPosts = function () {
   $(".author-posts").owlCarousel({
      loop: false,
      autoplay: false,
      margin: 20,
      autoplayTimeout: 3000,
      animateOut: "fadeOut",
      animateIn: "fadeIn",
      nav: true,
      dots: true,
      autoplayHoverPause: true,
      items: 1,
      navText: [         
         "<i class='fa-solid fa-caret-left text-xl'></i>",
         "<i class='fa-solid fa-caret-right text-xl'></i>",
      ],
      responsive: {
         0: {
            items: 1,
         },
         600: {
            items: 2,
         },
         1000: {
            items: 3,
         },
      },
   });
};
AuthorPosts();
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
$("#inputTags").selectize({
   plugins: ["restore_on_backspace", "remove_button"],
   delimiter: ",",
   persist: false,
   maxItems: 6,
   create: function (input) {
      return {
         value: input,
         text: input,
      };
   },
});
$(function () {
   $(".custom-dropdown").on("show.bs.dropdown", function () {
      var that = $(this);
      setTimeout(function () {
         that.find(".dropdown-menu").addClass("active");
      }, 100);
   });
   $(".custom-dropdown").on("hide.bs.dropdown", function () {
      $(this).find(".dropdown-menu").removeClass("active");
   });
});
let TODAY = new Date(Date.now());
let EIGHTEEN_YEARS_BACK = new Date(
   new Date(TODAY).getDate() +
   "/" +
   new Date(TODAY).getMonth() +
   "/" +
   (new Date(TODAY).getFullYear() - 16)
);
const myInput = document.querySelector(".profileDate");
const fp = flatpickr(myInput, {
   altInput: true,
   altFormat: "F j, Y",
   dateFormat: "Y-m-d",
   // maxDate: EIGHTEEN_YEARS_BACK,
});
