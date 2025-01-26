// Init

let formCtn = document.querySelector("div[data-label='form-container']");
let btn = document.querySelector("a[data-label='form-toggler']");
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

let dateTakenOut = document.querySelector('input[name="date_taken_out"]') ? 
    document.querySelector('input[name="date_taken_out"]') :
    null;

if (dateTakenOut) {
    dateTakenOut.setAttribute('type', 'date');
}


let dateInput = document.querySelector('input[name="date_due"]') ? 
    document.querySelector('input[name=date_due]') : 
    document.querySelector('input[name="date"]');
    
dateInput.setAttribute("type", "date");

let ignores = document.querySelectorAll('.actions-m')
let ignoreIds = Array.from(ignores).map((btn)=>{
    let _id = btn.getAttribute('id');
    return _id;
})

console.log(ignoreIds);
printBtn = document.querySelector('#print-btn');

printBtn.addEventListener('click', ()=>{
    printJS({
        printable: 'print',
        type: 'html',
        style: "font-family: sans-serif",
        css: ['/static/stylesheets/print.custom.css','/static/stylesheets/output.css'],
        ignoreElements: ignoreIds,
        scanStyles: false,
    });    
})