document.addEventListener('DOMContentLoaded', function () {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "../static/main1/img.json", true);

    xhr.send();

    xhr.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {

            var jsonData = JSON.parse(this.responseText);

            var p = document.getElementById('mugshot')

            p.innerHTML = `<img src="${jsonData}" class="framed" id="mugshot">`;
            console.log('img done');
        }
    };
});