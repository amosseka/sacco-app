//Init

let form = document.querySelector("#pay-using-shares-form");

let submitBtn = document.querySelector("input[type='submit']");
let errorList = document.querySelector("ul.errorlist");

let totalShares = document.querySelector("span[label='total-shares']").getAttribute("data");
let sharesInput = document.querySelector("input[name='shares']");

totalShares = Number(totalShares);

submitBtn.addEventListener("click", function(event){
    event.preventDefault();
    
    let inputValue = Number(sharesInput.value);

    if (totalShares - inputValue >= 0) {
        sharesInput.value = -inputValue;
        form.submit();
    } else {    
        errorList.children[0].textContent = "Value exceeds available shares";
    }
});

let dateInput = document.querySelector("input[name='date']");
dateInput.setAttribute("type", "date");