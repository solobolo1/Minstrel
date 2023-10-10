document.addEventListener('DOMContentLoaded', function () {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "../static/main1/desc.json", true);

    xhr.send();

    xhr.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {

            var jsonData = JSON.parse(this.responseText);

            var p = document.getElementById('desc')

            p.innerHTML = `<p class="format" id="desc"><strong>${jsonData}</strong></p>`;
            console.log('desc done');
        }
    };
});