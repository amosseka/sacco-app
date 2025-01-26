//Init

let selection = document.querySelector("select[name='comparison']");
let form = document.querySelector("form#comparison-form");

selection.addEventListener("change", function(){
    
    if (selection.value == "between") {
        let dateInput = document.createElement("input");
        dateInput.setAttribute("type", "date");
        dateInput.setAttribute("name", "date_2");
        form.insertBefore(dateInput, form.children[form.children.length-2]);
    } 
    else {
        form.querySelector('[name="date_2"]') ? form.querySelector('[name="date_2"]').remove() : null; 
    }
});


let modalContainer = document.querySelector('#modal-container');
let transactionDelBtns = document.querySelectorAll('.transaction-del-btn');

let cancelModal = document.querySelector("a#cancel-modal");
let confirmModal = document.querySelector("a#confirm-modal");


transactionDelBtns.forEach((btn)=>{
    btn.addEventListener('click', ()=>{
        modalContainer.style.display = "block";
        let transactionId = btn.getAttribute('data');
        let memberCode = btn.getAttribute('member')
        let url = "/transaction/" + transactionId + `/?action=delete&referer=member-transactions&member-code=${memberCode}`;
        confirmModal.href = url;
    })
});

cancelModal.addEventListener("click", ()=>{
    modalContainer.style.display = "none";
    confirmModal.href = "#";
});



printBtn = document.querySelector('#print-btn');

let pagNavigation = document.querySelector('#pagination-navigation').getAttribute('id');

let actions = document.querySelectorAll('.actions');

let actionsIds = Array.from(actions).map((action)=>{
    let _id = action.getAttribute('id');
    return _id;
});

let actionsTh = document.querySelector('#actions-th').getAttribute('id');

let editProfile = document.querySelector('#edit-profile').getAttribute('id');


printBtn.addEventListener('click', ()=>{
    printJS({
        printable: 'main-body',
        type: 'html',
        style: "font-family: sans-serif",
        css: ['/static/stylesheets/print.custom.css','/static/stylesheets/output.css'],
        ignoreElements: actionsIds.concat(actionsTh).concat(pagNavigation).concat(editProfile),
        scanStyles: false,
    });    
});