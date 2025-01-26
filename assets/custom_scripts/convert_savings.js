//Init

let form = document.querySelector("#convert-savings-form");

let submitBtn = document.querySelector("input[type='submit']");
let errorList = document.querySelector("ul.errorlist");

let totalSavings = document.querySelector("span[label='total-savings']").getAttribute('data');
let savingsInput = document.querySelector("input[name='savings']");
let sharesInput = document.querySelector("input[name='shares']");

totalSavings = Number(totalSavings);

submitBtn.addEventListener("click", function(event){
    event.preventDefault();
    let inputValue = Number(savingsInput.value)

    if (totalSavings - inputValue >= 0) {
        if (inputValue % 5000 == 0 || inputValue % 5000 == -0) {
            let shares = inputValue / 5000;

            sharesInput.value = shares;
            savingsInput.value = -inputValue;

            form.submit();
        } else {
            errorList.children[0].textContent = "Amount cannot be used to buy shares"; 
        }
    }
    else {
        errorList.children[0].textContent = "Amount is greater than savings";
    }
});

let dateInput = document.querySelector("input#id_date");
dateInput.setAttribute("type", "date");