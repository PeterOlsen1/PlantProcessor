// This is for card page functionality, so that we can eventually add new cards and create new pages dynamically

var cardlist = []

/* 
Plant objects should look the following way:

var _ = {
    name: "name",
    species: "species",
    description: "description string"
    }

More arguments will be added/acceptable soon
*/


// eventually make it so that we can grab these from a database instead of manually typing each one
var bird = {
    name: "Bird",
    species: "Bird of Paradise",
    description: "Big!"
}

var pearls = {
    name: "Her",
    species: "String of Pearls",
    description: "Long with little balls"
}

var philodendrin = {
    name: "New guy",
    species: "Philodendrin?",
    description: "Should be watered kinda often"
}

var small_succulent = {
    name: "Tiny guy",
    species: "Succulent",
    description: "My day 1"
}

//populate the list manually for now
cardlist.push(small_succulent);
cardlist.push(philodendrin);
cardlist.push(pearls);
cardlist.push(bird);

//create string to put inside of #plant-cards div
function card_maker(list) {
    let outString = "";
    for (let i = 0; i < list.length; i++){
        let tempString = "<div class=\"card\" onclick=\"redirectToPlantPage('" + encodeURIComponent(JSON.stringify(list[i])) + "')\"><div class=\"card-top\">";
        //put an image maybe in the card top

        //add a divider and set up for .card-bottom
        tempString += "</div><div class=\"card-divider\"></div><div class=\"card-bottom\">";

        for (let property in list[i]){
            tempString += "<b>" + property.charAt(0).toUpperCase() + property.slice(1) + "</b>: " + list[i][property] + "<br>";
        }

        //close .card-bottom and .card divs
        tempString += "</div></div>";
        outString += tempString;
    }
    return outString;
}

//function to save the selected plant in local storage and redirect to new webpage
function redirectToPlantPage(plantData) {
    localStorage.setItem('selectedPlant', plantData);
    window.location.href = 'plantPage.html';
}

window.onload = () => {
    let plant_cards = document.querySelector("#plant-cards");
    plant_cards.innerHTML = card_maker(cardlist);
}