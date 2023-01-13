$(document).ready(function () {   
   $('#shareProfileModal').modal('show')
})

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
