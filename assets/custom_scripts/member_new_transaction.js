//Init 

let dateInput = document.querySelector("input[name='date']");
dateInput.setAttribute("type", "date");


let form1 = document.querySelector("div[data-label='control-1']");
let form2 = document.querySelector("div[data-label='control-2']");

let generalBtn = document.querySelector("button#general-transaction");
let otherBtn = document.querySelector("button#other-transaction");

generalBtn.addEventListener("click", function(){
    generalBtn.classList.replace("inactive-t", "active-t");
    otherBtn.classList.replace("active-t", "inactive-t");
    form1.classList.replace("hidden", "block");
    form2.classList.replace("block", "hidden");
    document.querySelector('div[data-label="welfare"]').style.cssText = "display: block;";
});

otherBtn.addEventListener("click", function(){
    generalBtn.classList.replace("active-t", "inactive-t");
    otherBtn.classList.replace("inactive-t", "active-t");
    form1.classList.replace("block", "hidden");
    form2.classList.replace("hidden", "block");
    document.querySelector('div[data-label="welfare"]').style.cssText = "display: none;";
});


let dateInpt = document.querySelector("input[name='date']");
dateInput.setAttribute("type", "date");


let lastDate = document.querySelector('input#latest_date');
let lastBtn = document.querySelector('input#use-last-date')

lastBtn.addEventListener("change", function(event){
    
    if (lastBtn.checked) {
        dateInpt.value = lastDate.value;
    } else {
        dateInpt.value = "";
    }

});