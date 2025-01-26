//Init

//Global Variables

let _OPTIONS = {};
let memberCode = document.querySelector('input[name=member-code]');

let totalShares = document.querySelector('[data=total-shares]');
let totalWelfare = document.querySelector('[data=total-welfare]');
let totalSavings = document.querySelector('[data=total-savings]');
let totalWithdraw = document.querySelector('[data=total-withdraw]');
let totalFines = document.querySelector('[data=total-fines]');
let totalOther = document.querySelector('[data=total-other]');

function fetchChartData(options) {

    let url = '/api/member-report?code=' + memberCode.value;

    if (options) {

        if (options['year']) {
            url = url + `&year=${options.year}`;
        }

        if (options['month']) {
            url = url + `&month=${options.month}`;
        }

    }

    console.log(url);

    fetch(url).then((response)=>{
        return response.json();
    }).then((data)=>{

        let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        let chartType;

        console.log(data);

        //Performing some clearing, both the months container 
        //And the charts
        //Plus the days container
        
        Array.from(charts).forEach((chart)=>{
            chart.innerHTML = "";
        });
        monthsContainer.innerHTML = "";
        // daysContainer.innerHTML = "";

        let search_months = data['search_months'];

        for (let search_month in search_months) {

            let monthBtn = monthBtnTemplate.cloneNode();
            monthBtn.classList.remove('report-btn-active');
            monthBtn.setAttribute('value', search_month);
            monthBtn.textContent = search_months[search_month];

            if (options && options.month == search_month) {                
                monthBtn.classList.add('report-btn-active');
            }

            monthBtn.addEventListener('click', fetchChartMonths);
            monthsContainer.appendChild(monthBtn);

            monthBtnTemplate = monthBtn;
        }

        //The totals
        totalShares.textContent = `${data['total']['shares']} = ${commaSeparator(data['total']['shares'] * 5000)}`;
        totalWelfare.textContent = commaSeparator(data['total']['welfare']);
        totalSavings.textContent = commaSeparator(data['total']['savings']);
        totalWithdraw.textContent = commaSeparator(data['total']['withdraw']);
        totalFines.textContent = commaSeparator(data['total']['fines']);
        totalOther.textContent = commaSeparator(data['total']['other']);
        
        //The response data

        let category = [];

        let totals = [];
        let shares = [];
        let welfare = [];
        let savings = [];
        let withdraw = [];
        let fines = [];
        let other = [];

        if (data['chart_type'] == 'year') {

            category = months;

            for (let month of months ) {
                shares.push(data['totals'][month]['shares']);
                welfare.push(data['totals'][month]['welfare']);
                savings.push(data['totals'][month]['savings']);
                withdraw.push(data['totals'][month]['withdraw']);
                fines.push(data['totals'][month]['fines']);
                other.push(data['totals'][month]['other']);
                totals.push(data['totals'][month]['total_transactions']);
            }
        }
        else if (data['chart_type'] == 'month') {

            for (let day in data['totals']) {

                category.push(day);

                shares.push(data['totals'][day]['shares']);
                welfare.push(data['totals'][day]['welfare']);
                savings.push(data['totals'][day]['savings']);
                withdraw.push(data['totals'][day]['withdraw']);
                fines.push(data['totals'][day]['fines']);
                other.push(data['totals'][day]['other']);
                totals.push(data['totals'][day]['total_transactions']);

            }
        }
        
        _OPTIONS['year'] = data['year'];

        Array.from(document.querySelectorAll('[data=year]')).forEach(btn => btn.classList.remove('report-btn-active'));
        document.querySelector(`[value="${data['year']}"]`).classList.add('report-btn-active');

        //Charts

        let totalsOption = {
            chart: {
                height: 450,
                width: '100%',
                type: 'area',
                background: '#f4f4f4',
                foreColor: '#333'
            },
            series: [{
                name: 'Total',
                data: totals
            }],
            xaxis: {
                categories: category,
            },
            
        }

        let totalsChart = new ApexCharts(document.querySelector("#chart-totals"), totalsOption);
        totalsChart.render();


        let sharesOptions = {
            chart: {
                height: 450,
                width: '100%',
                type: chartType || 'bar',
                background: '#f4f4f4',
                foreColor: '#333',
            },
            series: [{
                name: 'shares',
                data: shares,
            }],
            xaxis: {
                categories: category,
            },
        };
        
        let sharesChart = new ApexCharts(document.querySelector("#chart-shares"), sharesOptions);
        sharesChart.render();


        let welfareOptions = {
            chart: {
                height: 450,
                width: '100%',
                type: 'bar',
                background: '#f4f4f4',
                foreColor: '#333',
            },
            series: [{
                name: 'welfare',
                data: welfare,
            }],   
            xaxis: {
                categories: category,
            },
            dataLabels: {
                enabled: true,
                formatter: val => commaSeparator(val)
            }
        };

        let welfareChart = new ApexCharts(document.querySelector("#chart-welfare"), welfareOptions);
        welfareChart.render();


        let savingsOptions = {
            chart: {
                height: 450,
                width: '100%',
                type: 'bar',
                background: '#f4f4f4',
                foreColor: '#333',
            },
            series: [{
                name: 'savings',
                data: savings,
            }],
            xaxis: {
                categories: category,
            },
            dataLabels: {
                enabled: true,
                formatter: val => commaSeparator(val)
            }
        };
        
        let savingsChart = new ApexCharts(document.querySelector("#chart-savings"), savingsOptions);
        savingsChart.render();

        let withdrawOptions = {
            chart: {
                height: 450,
                width: '100%',
                type: 'bar',
                background: '#f4f4f4',
                foreColor: '#333',
            },
            series: [{
                name: 'withdraw',
                data: withdraw,
            }],
            xaxis: {
                categories: category,
            },
            dataLabels: {
                enabled: true,
                formatter: val => commaSeparator(val)
            }
        };
        
        let withdrawChart = new ApexCharts(document.querySelector("#chart-withdraw"), withdrawOptions);
        withdrawChart.render();


        let finesOptions = {
            chart: {
                height: 450,
                width: '100%',
                type: 'bar',
                background: '#f4f4f4',
                foreColor: '#333',
            },
            series: [{
                name: 'fines',
                data: fines,
            }],
            xaxis: {
                categories: category,
            },
            dataLabels: {
                enabled: true,
                formatter: val => commaSeparator(val)
            }
        };
        
        let finesChart = new ApexCharts(document.querySelector("#chart-fines"), finesOptions);
        finesChart.render();


        let otherOptions = {
            chart: {
                height: 450,
                width: '100%',
                type: 'bar',
                background: '#f4f4f4',
                foreColor: '#333',
            },
            series: [{
                name: 'other',
                data: other,
            }],
            xaxis: {
                categories: category,
            },
            dataLabels: {
                enabled: true,
                formatter: val => commaSeparator(val)
            }
        };
        
        let otherChart = new ApexCharts(document.querySelector("#chart-other"), otherOptions);
        otherChart.render();

    });



    function commaSeparator(val) {
            
        if (val == null) {
            return val;
        } 
        
        else {
            let num = String(val).split('').reverse().join('');
        
            let regex = /\w{3}/g;
            let match = num.match(regex);
            
            if (match) {
                let mapped = match.map((val)=>{return val + ","});
                let tail = num.slice(match.length * 3);
                
                let result = mapped;
                result.push(tail);
                result.join('');
                result = result.join('');

                if (tail == '') {
                    result = result.slice(0, result.length - 1);
                }

                return result.split('').reverse().join('');

            } else {
                return val;
            }
            
        }
    }
}


//Fetch Data
fetchChartData()

let yearBtns = document.querySelectorAll('button[data=year]');
let charts = document.querySelectorAll('.chart');

let monthsContainer = document.querySelector('.months-container');
let monthBtnTemplate = monthsContainer.firstElementChild;

console.log(monthBtnTemplate);

Array.from(yearBtns).forEach((yearBtn)=>{
    
    yearBtn.addEventListener('click', (event)=>{
        let year = event.target.getAttribute('value');
        _OPTIONS['year'] = year;
        _OPTIONS['month'] = null;
        fetchChartData(_OPTIONS);
    })
});


function fetchChartMonths() {
    let month = this.getAttribute('value');
    _OPTIONS['month'] = month;
    fetchChartData(_OPTIONS);
}

