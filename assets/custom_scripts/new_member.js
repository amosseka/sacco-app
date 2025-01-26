//Init

// dateJoined = document.querySelector('input[name="date_joined"]');
// dateJoined.setAttribute("type", "date");

// dateOfBirth = document.querySelector('input[name="date_of_birth"]');
// dateOfBirth.setAttribute("type", "date");

let next = document.querySelector('button[action="next"]');

let navButtons = Array.from(document.querySelectorAll('div#form-nav button'));
let sections = Array.from(document.querySelectorAll('div.section'));


navButtons.forEach(function(navBtn){
    navBtn.addEventListener("click", function(){
        let index = navButtons.indexOf(navBtn);

        navButtons.forEach(function(btn){
            btn.classList.remove("active");
        });

        sections.forEach(function(section){
            section.classList.replace("block", "hidden");
        })

        navBtn.classList.add("active");
        next.setAttribute("current", index);
        sections[index].classList.replace("hidden", "block");

        if (index == sections.length - 1) {
            next.classList.replace('block', 'hidden');
        } else {
            next.classList.replace('hidden', 'block');
        }

    });
});


next.addEventListener("click", function(){
    let current = Number(next.getAttribute("current"));
    let nextSection = current + 1;
    navButtons[nextSection].click();
});

let dates = JSON.parse(document.querySelector("#date-fields").textContent);

for (field of dates) {
    document.querySelector(`input[name=${field}]`).setAttribute('type', 'date');
}

let benefitsTemplate = document.querySelector('div[template=benefits-template]');
let gfeTemplate = document.querySelector('div[template=gfe-template]');

benefitsTemplate.classList.replace('hidden', 'grid');
gfeTemplate.classList.replace('hidden', 'grid');

let benefitsAddBtn = document.querySelector("button[action=deposits]");
let gfeAddBtn = document.querySelector("button[action=gfe]");

let nomineesForBenefitsCounter=document.querySelector('input[name=nominees_for_benefits_counter]')
let nomineesForGfeCounter = document.querySelector('input[name=nominees_for_gfe_counter]');

benefitsCounter = 2;
gfeCounter = 2;

benefitsAddBtn.addEventListener("click", function(event){
    event.preventDefault();
    
    let cloned = benefitsTemplate.cloneNode(true);
    let inputs = cloned.querySelectorAll('input');
    Array.from(inputs).forEach((input)=>{
        let inputName = input.getAttribute("name");
        let slicedName = inputName.slice(0, inputName.length - 1)
        slicedName += benefitsCounter;
        input.setAttribute('name', slicedName);
        input.value = "";
    })

    benefitsTemplate.insertAdjacentElement("afterend", cloned);
    benefitsTemplate = cloned;
    nomineesForBenefitsCounter.value = benefitsCounter;
    benefitsCounter += 1;
});

gfeAddBtn.addEventListener("click", function(event){
    event.preventDefault();

    let cloned = gfeTemplate.cloneNode(true);
    let inputs = cloned.querySelectorAll('input')
    Array.from(inputs).forEach((input)=>{
        let inputName = input.getAttribute("name");
        let slicedName = inputName.slice(0, inputName.length - 1)
        slicedName += gfeCounter;
        input.setAttribute('name', slicedName);
        input.value = "";
    })

    gfeTemplate.insertAdjacentElement("afterend", cloned);
    gfeTemplate = cloned;
    nomineesForGfeCounter = gfeCounter;
    gfeCounter += 1;
});
