// Wait for the document to fully load before executing jQuery code
$(document).ready(function() {
  // Make a GET request to the SWAPI API endpoint
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Extract the character name from the API response data
    var characterName = data.name;
    
    // Set the character name as the content of the <div id="character"> element
    $('#character').text(characterName);
  });
});

