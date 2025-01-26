//Init

let formCtn = document.querySelector("div[data-label='form-container']");
let btn = document.querySelector("button[data-label='form-toggler']");
let disp = false;

btn.addEventListener("click", function(){
    
    if (!disp) {
        formCtn.classList.replace("hidden", "block");
        formCtn.classList.replace("h-0", "h-max");
        disp = true;
    } 
    else {
        formCtn.classList.replace("block", "hidden");
        formCtn.classList.replace("h-max", "h-0");
        disp = false;
    }

});


let dateInput = document.querySelector('input[name="date_due"]') ? 
    document.querySelector('input[name=date_due]') : 
    document.querySelector('input[name="date"]');
    
if (dateInput) {
    dateInput.setAttribute("type", "date");
}

let expenseItemForm = document.querySelector('form#expense-item-form') ?
    document.querySelector('form#expense-item-form') :
    null;

if (expenseItemForm) {

    let quantity = document.querySelector('input[name="quantity"]');
    let costPrice = document.querySelector('input[name="cost_price"]');
    let totalValue = document.querySelector('input[name="total_value"]');
    
    costPrice.addEventListener('input', ()=>{
        let qt = Number(quantity.value);
        let ct = Number(costPrice.value);

        let totalVal = qt * ct;
        totalValue.value = totalVal;
    });

}

if (document.querySelector('#print-btn')) {
    printBtn = document.querySelector('#print-btn');

    printBtn.addEventListener('click', ()=>{
        printJS({
            printable: 'print',
            type: 'html',
            style: "font-family: sans-serif",
            css: ['/static/stylesheets/print.custom.css','/static/stylesheets/output.css'],
            // ignoreElements: ignoreDelIds.concat(ignoreContactIds),
            scanStyles: false,
        });    
    });
}