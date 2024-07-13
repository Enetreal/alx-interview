#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./script.js <movieId>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async (err, response, body) => {
  if (err) {
    console.error('Error fetching movie data:', err);
    return;
  }

  try {
    const movie = JSON.parse(body);
    for (const characterUrl of movie.characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, (err, response, body) => {
          if (err) {
            reject(err);
            return;
          }
          const character = JSON.parse(body);
          console.log(character.name);
          resolve();
        });
      });
    }
  } catch (error) {
    console.error('Error parsing movie data or fetching character:', error);
  }
});
