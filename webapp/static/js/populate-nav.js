//this is done so that when i update my nav element, i don't need to do it on every page
const nav = document.querySelector('nav');

nav.innerHTML = `
    <div id="navigation-image">
        <a href="/index"><img src="/views/plant-favicon.png" width="40" height="40" title="Home"></a>
    </div>
    <div id="navigation-links">
        <a href="/aboutMe">About Me</a> <a href="/static/html/myPlants.html">My Plants</a> <a href="/addPlant">Add a Plant</a>
    </div>
`;

