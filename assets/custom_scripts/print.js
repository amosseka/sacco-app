//Init

window.onload = function() {
    window.print();
}

var previousUrl;
previousUrl = document.querySelector("input[name='previous-page']").value;

window.onafterprint = function() {
    console.log("Finished printing");
    window.location.search = null;
    window.location.pathname = `/${previousUrl}/`;
}
