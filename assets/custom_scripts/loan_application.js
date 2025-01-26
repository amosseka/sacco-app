//Init


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
})

next.addEventListener("click", function(){
    let current = Number(next.getAttribute("current"));
    let nextSection = current + 1;
    navButtons[nextSection].click();
});

let dates = JSON.parse(document.querySelector("#date-fields").textContent);

console.log(dates);

for (field of dates) {
    document.querySelector(`input[name=${field}]`).setAttribute('type', 'date');
}

let memberInput = document.querySelector('select[name=member]');
let memberName = document.querySelector('input[name=member_name]');
let memberImage = document.querySelector('img[data=image]');
let memberShares = document.querySelector('input[name=value_of_shares]')
let memberSavings = document.querySelector('input[name=value_of_savings]');

console.log(memberShares.value);
memberInput.addEventListener('change', (event)=>{

    let url = '/member/?action=detail&id=' + event.target.value;
    fetch(url).then((response)=>{
        return response.json();
    }).then((data)=>{
        memberName.value = data.name;
        memberShares.value = data.shares;
        memberSavings.value = data.net_savings;

        memberImage.src = data.image;
        memberImage.classList.replace('hidden', 'block');
    })
})
