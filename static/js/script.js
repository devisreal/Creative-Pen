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
let TODAY = new Date(Date.now());
let EIGHTEEN_YEARS_BACK = new Date(new Date(TODAY).getDate() + "/" + new Date(TODAY).getMonth() + "/" + (new Date(TODAY).getFullYear() - 16));
const myInput = document.querySelector(".profileDate");
const fp = flatpickr(myInput, {
   altInput: true,
   altFormat: "F j, Y",
   dateFormat: "Y-m-d",
   // maxDate: EIGHTEEN_YEARS_BACK,
});