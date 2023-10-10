document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".music-notes-container");

    var imageArray = new Array();
    imageArray[0] = "qnote.png";
    imageArray[1] = "8thnote.png";
    imageArray[2] = "8thdouble.png";
    imageArray[3] = "16thnote.png";
    imageArray[4] = "triplet.png";
    imageArray[5] = "halfnote.png";
    imageArray[6] = "wholenote.png";

    function createNote() {
        const note = document.createElement("img");
        var index = Math.floor(Math.random()*6);
        note.src = "../static/home/" + imageArray[index];
        note.classList.add("music-note");
        note.style.left = `${Math.random() * (window.innerWidth - 20)}px`;
        container.appendChild(note);

        note.addEventListener("animationend", () => {
            note.remove();
        });
    }

    function startFallingNotes() {
        setInterval(createNote, 500);
    }

    startFallingNotes();

    const button = document.querySelector(".btn-custom");
    button.addEventListener("click", (event) => {
        event.stopPropagation();
    });
});