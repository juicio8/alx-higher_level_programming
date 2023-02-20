$(document).ready(() => {
  $("DIV#red_header")
    .css({ cursor: "pointer" })
    .click(() => {
      $("header").css({ color: "#FF0000" });
    });
});
