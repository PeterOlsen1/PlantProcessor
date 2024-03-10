//Function to take care of building a new webpage when cards are clicked

var plant_image_captions = ["Aww, look at it, so cute!", 
                            "That's your child, you must be so proud!", 
                            "Looking big and healthy!",
                            "Growing stronger every day!",
                            "<em>Nature's little masterpiece!</em>",
                            "Nature's beauty in a pot!",
                            "Bringing a touch of green to your day!"]

function start() {
    //grab item from local storage to ensure it was transported properly
    let plantData = localStorage.getItem('selectedPlant');
    if (plantData) {
        //get the uri that was sent
        let plant = JSON.parse(decodeURIComponent(plantData));

        //chnage items in the document to match that of the plant
        document.querySelector("#p-title").innerHTML = plant.name + " Information";
        document.querySelector("#p-header").innerHTML = "All about " + plant.name;

        // Picture and caption area
        document.querySelector("#plant-picture").setAttribute("src", plant.src);
        document.querySelector("#plant-picture").setAttribute("alt", "Picture of " + plant.name);
        document.querySelector("#caption").innerHTML = plant_image_captions[Math.floor(Math.random() * plant_image_captions.length)]

    } else {
        alert("There was a problem loading this webpage");
    }
}

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

window.onload = start;