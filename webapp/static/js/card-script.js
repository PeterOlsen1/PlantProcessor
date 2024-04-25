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
    description: "Big!",
    water: "02282024",
    src: "../views/bird.jpeg"
}

var pearls = {
    name: "Her",
    species: "String of Pearls",
    description: "Long with little balls",
    water: "03112024",
    src:"../views/pearls.jpeg"
}

var pothos = {
    name: "New guy",
    species: "Pothos",
    description: "Should be watered kinda often",
    water:"03112024",
    src: "../views/pothos.jpeg"
}

var small_succulent = {
    name: "Tiny guy",
    species: "Succulent",
    description: "My day 1",
    water:"03062024",
    src: "../views/tinyguy.jpeg"
}

//populate the list manually for now
cardlist.push(small_succulent);
cardlist.push(pothos);
cardlist.push(pearls);
cardlist.push(bird);

//create string to put inside of #plant-cards div
function card_maker(list) {
    let outString = "";
    for (let i = 0; i < list.length; i++){
        let lastWatered = getDateDifference(list[i].water).toFixed(1);
        let tempString;
        if (lastWatered < 7) {
            tempString = "<div class=\"card\" onclick=\"redirectToPlantPage('" + encodeURIComponent(JSON.stringify(list[i])) + "')\"><div class=\"card-top\">";
        }
        else if (lastWatered < 14 ) {
            tempString = "<div class=\"card\" onclick=\"redirectToPlantPage('" + encodeURIComponent(JSON.stringify(list[i])) + "')\" style='border: 1px solid yellow'><div class=\"card-top\">";
        }
        else {
            tempString = "<div class=\"card\" onclick=\"redirectToPlantPage('" + encodeURIComponent(JSON.stringify(list[i])) + "')\" style='border: 1px solid red'><div class=\"card-top\">";
        }
        //put an image maybe in the card top
        tempString += "<img src='" + list[i].src + "' width=120px height=170px>"
        //add a divider and set up for .card-bottom
        tempString += "</div><div class=\"card-divider\"></div><div class=\"card-bottom\">";

        //get rid of this so that our loop doesn't go over it
        delete list[i].src;

        for (let property in list[i]){
            if (property == 'water') {
                if (lastWatered < 7) {
                    tempString += "<b>Last Watered</b>: " + lastWatered + " days ago<br>";
                }
                else if (lastWatered < 14) {
                    tempString += "<b>Last Watered</b>: <span style='color: yellow'>" + lastWatered + " days ago</span><br>";
                }
                else {
                    tempString += "<b>Last Watered</b>: <span style='color: red'>" + lastWatered + " days ago</span><br>";
                }
            }
            else {
                tempString += "<b>" + property.charAt(0).toUpperCase() + property.slice(1) + "</b>: " + list[i][property] + "<br>";
            }
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


//although this function is in individual-plant.js, i couldn't get the import statements to work
function getDateDifference(str) {
    //initialize both date objects
    let currentDate = new Date();
    let month = str.slice(0, 2);
    let day = str.slice(2, 4);
    let year = str.slice(4);
    let otherDate = new Date(year, month-1, day);

    //do the math to find the difference between the two
    let msDifference = currentDate - otherDate;
    let dayDifference = msDifference / 1000 / 60 / 60/ 24;
    return dayDifference;
}

//execute everything
let plant_cards = document.querySelector("#plant-cards");
plant_cards.innerHTML = card_maker(cardlist);