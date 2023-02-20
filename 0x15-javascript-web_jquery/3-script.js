$(document).ready(() => {
  $("DIV#red_header")
    .css({ cursor: "pointer" })
    .click(() => {
      $("header").addClass("red");
    });
});
