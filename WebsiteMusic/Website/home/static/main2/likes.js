const count = document.getElementById("counter");
const count1 = document.getElementById("counter1");
const count2 = document.getElementById("counter2");

var c = 0;
var c1 = 0;
var c2 = 0;

count.innerHTML = c;
count1.innerHTML = c1;
count2.innerHTML = c2;

function increment() {
    c++;
    count.innerHTML = c;
    $this.addClass('cc');
}

function increment1() {
    c1++;
     count1.innerHTML = c1;
     $this.addClass('cc');
}

function increment2() {
    c2++;
    count2.innerHTML = c2;
    $this.addClass('cc');
}