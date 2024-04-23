#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);

  const charactersUrls = movie.characters;
  const charactersNames = [];

  const fetchCharacter = (url) => {
    request.get(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      charactersNames.push(character.name);

      if (charactersUrls.length === charactersNames.length) {
        charactersNames.forEach((name) => console.log(name));
      }
    });
  };

  charactersUrls.forEach((url) => fetchCharacter(url));
});

