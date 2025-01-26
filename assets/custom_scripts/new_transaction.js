//Init

let memberCode = document.querySelector("select#id_member");

let fullName = document.querySelector('p[data="full-name"]');
let image = document.querySelector('img[data="image"]');

memberCode.addEventListener('change', ()=>{
    if (memberCode.value != "") {
        fetch(`?id=${memberCode.value}&action=detail`).then((response)=>{
            return response.json();
        }).then((data)=>{
            
            fullName.textContent = data.full_name;
            image.src = data.image;
            image.classList.replace('hidden', 'block');
        });
    } 
    
    else {
        fullName.textContent = "Choose Member";
        image.src = '';
    }
});


let dateInput = document.querySelector("input[name='date']");
dateInput.setAttribute("type", "date");

let lastDate = document.querySelector('input#latest_date');
let lastBtn = document.querySelector('input#use-last-date')

lastBtn.addEventListener("change", function(event){
    
    if (lastBtn.checked) {
        dateInput.value = lastDate.value;
    } else {
        dateInput.value = "";
    }

});

let edit = document.querySelector('input[name="edit"]');

if (edit) {
    dateInput.value = edit.value;
}


let generalTransactionBtn = document.querySelector('button#general-transaction');
let customTransactionBtn = document.querySelector('button#custom-transaction');

let generalTransaction = document.querySelector('div#general-transaction');
let customTransaction = document.querySelector('div#custom-transaction');


let btns = [generalTransactionBtn, customTransactionBtn];
let forms = [generalTransaction, customTransaction];


btns.forEach(function(btn){
    btn.addEventListener('click', function(){

        let index = btns.indexOf(btn);

        btns.forEach(function(_btn){
            _btn.classList.replace('active-t', 'inactive-t');
        });

        forms.forEach(function(form){
            form.classList.replace('block', 'hidden');
        });

        btn.classList.replace('inactive-t', 'active-t');
        forms[index].classList.replace('hidden', 'block');
    });
});