//this is done so that when i update my nav element, i don't need to do it on every page
const nav = document.querySelector('nav');

nav.innerHTML = `
    <div id="navigation-image">
        <a href="/index"><img src="/views/plant-favicon.png" width="40" height="40" title="Home"></a>
    </div>
    <div id="navigation-image">
        <a><img src="/views/logout.webp" width="40" height="40" title="Logout" style='left: 5px; top: 10px' onclick='logout()'></a>
    </div>
    <div id="navigation-links">
        <a href="/aboutMe">About Me</a> <a href="/templates/myPlants">My Plants</a> <a href="/addPlant">Add a Plant</a>
    </div>
`;

function logout() {
    fetch('/api/logout');
    window.location.href="/"
}