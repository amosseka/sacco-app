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
        let url = "/transaction/" + transactionId + "/?action=delete";
        confirmModal.href = url;
    })
});

cancelModal.addEventListener("click", ()=>{
    modalContainer.style.display = "none";
    confirmModal.href = "#";
});