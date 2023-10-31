document.addEventListener('DOMContentLoaded', function () {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "../static/main2/ids.json", true);

    xhr.send();

    xhr.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {

            var jsonData = JSON.parse(this.responseText);

            var id1 = jsonData.id1;
            var id2 = jsonData.id2;
            var id3 = jsonData.id3;

            function updateIframes() {
                var iframe1 = document.getElementById('song1');
                iframe1.innerHTML = `<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/${id1}" width="675px" height="152" frameborder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>`;

                var iframe2 = document.getElementById('song2');
                iframe2.innerHTML = `<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/${id2}" width="675px" height="152" frameborder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>`;

                var iframe3 = document.getElementById('song3');
                iframe3.innerHTML = `<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/${id3}" width="675px" height="152" frameborder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>`;
            }

            updateIframes();
            console.log('iframes');
        }
    };
});