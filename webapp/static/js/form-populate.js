async function populate(){
    //grab id from the url
    const url = new URL(window.location);
    const searchParams = new URLSearchParams(url.search);

    //use id to construct a fetch response to the fetchById api route
    let response = await fetch('/api/fetchById?id=' + searchParams.get('id'));
    let data = await response.json();
    if (data.status == 'failure') {
        document.querySelector('.login-alert').innerHTML = "Invalid Plant ID";
        document.querySelector('.login-alert').setAttribute('style', 'display: inline-block');
    }
    else {
        plant = data.plant;
        document.querySelector('#name').value = plant.name;
        document.querySelector('#species').value = plant.species;
        document.querySelector('#description').value = plant.description;
        document.querySelector('#lastWatered').value = plant.lastWatered;
        document.querySelector('#picture').value = plant.fname;
    }
}

window.onload = populate();
