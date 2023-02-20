$(document).ready(() => {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    type: "GET",
    dataType: "json",
    success: function (res) {
      console.log(res);
      $("#character").text(res.name);
    },
  });
});
