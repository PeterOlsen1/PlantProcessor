//this is done so that when i update my nav element, i don't need to do it on every page
const nav = document.querySelector('nav');

nav.innerHTML = `
    <div id="navigation-image">
        <a href="index.html"><img src="../views/plant-favicon.png" width="40" height="40" title="Home"></a>
    </div>
    <div id="navigation-links">
        <a href="aboutMe.html">About Me</a> <a href="myPlants.html">My Plants</a> <a href="addPlant.html">Add a Plant</a>
    </div>
`;

