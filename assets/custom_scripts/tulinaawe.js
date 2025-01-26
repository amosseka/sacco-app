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
    
dateInput.setAttribute("type", "date");


// if (document.querySelector('#tulinaawe-contributor-form')) {
//     let form = document.querySelector('#tulinaawe-contributor-form');
//     let contributor = document.querySelector('select[name=member]')

//     contributor.addEventListener('change', (event)=>{
//         console.log(event.target.value);
//     })
// }

let delBtns = document.querySelectorAll('.del-btn');
let contacts = document.querySelectorAll('.contact');

let ignoreDelIds = Array.from(delBtns).map((btn)=>{
    let _id = btn.getAttribute('id');
    return _id;
});

let ignoreContactIds = Array.from(contacts).map((contact)=>{
    let _id = contact.getAttribute('id');
    return _id;
});


printBtn = document.querySelector('#print-btn');

printBtn.addEventListener('click', ()=>{
    printJS({
        printable: 'print',
        type: 'html',
        style: "font-family: sans-serif",
        css: ['/static/stylesheets/print.custom.css','/static/stylesheets/output.css'],
        ignoreElements: ignoreDelIds.concat(ignoreContactIds),
        scanStyles: false,
    });    
});

if (document.querySelector('[name=member]')) {
    let memberInput = document.querySelector('[name=member]');
    let choice = document.querySelector('#choose-member');

    memberInput.addEventListener('focus', ()=>{
        choice.classList.replace('hidden', 'block');
    });

    memberInput.addEventListener('focusout', ()=>{
        setTimeout(()=>choice.classList.replace('block', 'hidden'),200)
    })

    fetch(`/tulinaawe/?action=lookup&member_name=`)
        .then((response)=>{return response.json()})
        .then((data)=>{
            members = JSON.parse(data);
            for (item of members) {
                let para = `<p class="border-b p-2 text-sm text-slate-700" value=${item.code}>${item.code} - ${item.full_names}</p>`;
                choice.innerHTML += para;
            }
        })

    memberInput.addEventListener('input', ()=>{
        let val = memberInput.value;
        choice.innerHTML = '';
        fetch(`/tulinaawe/?action=lookup&member_name=${val}`)
        .then((response)=>{return response.json()})
        .then((data)=>{
            members = JSON.parse(data);
            for (item of members) {
                let para = `<p class="border-b p-2 text-sm text-slate-700" value=${item.code}>${item.code} - ${item.full_names}</p>`;
                choice.innerHTML += para;
            }
        })
    });

    choice.addEventListener('click', (event)=>{
        document.querySelector('[for=member]').innerText = "Member: " + event.target.innerText;
        memberInput.value = event.target.getAttribute('value');
    })
}