$(document).ready(() => {
  $("DIV#toggle_header")
    .css({ cursor: "pointer" })
    .click(() => {
      $("header").toggleClass("red");
      $("header").toggleClass("green");
    });
});
