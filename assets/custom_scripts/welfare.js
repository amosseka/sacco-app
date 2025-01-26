
printBtn = document.querySelector('#print-btn');

printBtn.addEventListener('click', ()=>{
    printJS({
        printable: 'print',
        type: 'html',
        style: "font-family: sans-serif",
        css: ['/static/stylesheets/print.custom.css','/static/stylesheets/output.css'],
        scanStyles: false,
    });    
})