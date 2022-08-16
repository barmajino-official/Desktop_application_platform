document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
});

document.onkeydown = function (e) {

    if (event.keyCode == 123) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'S'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'H'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'F'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'N'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'J'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'A'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'E'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'T'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'O'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'S'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'D'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'G'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'K'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'L'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'N'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'W'.charCodeAt(0)) {
        return false;
    }


}
document.firstElementChild.style.zoom = "reset";
window.addEventListener('onunload', function (e) {
    e.preventDefault();
    location.replace('/closed');
});
