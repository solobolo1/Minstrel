document.addEventListener('DOMContentLoaded', function () {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "../static/main1/name.json", true);

    xhr.send();

    xhr.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {

            var jsonData = JSON.parse(this.responseText);

            var p = document.getElementById('title')

            p.innerHTML = `<h1 class="format" ><strong>${jsonData}</strong></h1>`;
            console.log('name done');
        }
    };
});