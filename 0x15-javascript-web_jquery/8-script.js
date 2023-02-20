$(document).ready(() => {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    type: "GET",
    dataType: "json",
    success: (res) => {
      const movieTitles = res.results
        .map((movie) => {
          return `<li>${movie.title}</li>`;
        })
        .join("");
      $("UL#list_movies").append(movieTitles);
    },
  });
});
