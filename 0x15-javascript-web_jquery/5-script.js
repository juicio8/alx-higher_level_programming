$(document).ready(() => {
  $("#add_item")
    .css({ cursor: "pointer" })
    .click(() => {
      $("UL.my_list").append("<li>Item</li>");
    });
});
