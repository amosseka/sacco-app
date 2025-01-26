//Init

let form = document.querySelector("#pay-fines-form");

let submitBtn = document.querySelector("input[type='submit']");
let errorList = document.querySelector("ul.errorlist");

let fines = document.querySelector("span[label='total-fines']").getAttribute("data");
let finesInput = document.querySelector("input#id_fines");

submitBtn.addEventListener("click", function(event){
    event.preventDefault();
    let totalFines = Number(fines);
    let finesValue = Number(finesInput.value);

    if (totalFines - finesValue >= 0) {
        finesInput.value = -finesValue;
        form.submit();
    } else {    
        errorList.children[0].textContent = "Value exceeds fines";
    }
});


let dateInput = document.querySelector("input[name='date']");
dateInput.setAttribute("type", "date");