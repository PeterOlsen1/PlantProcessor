//this is done so that when i update my nav element, i don't need to do it on every page
const nav = document.querySelector('nav');

nav.innerHTML = `
    <div id="navigation-image">
        <a href="/index"><img src="/views/plant-favicon.png" style='top: 5%' title="Home" class='nav-image'></a>
    </div>
    <div id="navigation-image">
        <a><img src="/views/logout.webp" title="Logout" style='top: 10%' onclick='logout()' class='nav-image'></a>
    </div>
    <div id="navigation-links">
        <a href="/aboutMe">About Me</a> <a href='/templates/plantFeed'>View Other Plants</a> <a href="/templates/myPlants">My Plants</a> <a href="/addPlant">Add a Plant</a>
    </div>
`;

function logout() {
    fetch('/api/logout');
    window.location.href="/";
}