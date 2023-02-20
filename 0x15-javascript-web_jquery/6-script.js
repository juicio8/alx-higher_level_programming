$(document).ready(() => {
  $("DIV#update_header")
    .css({ cursor: "pointer" })
    .click(() => {
      $("header").text("New Header!!!");
    });
});
