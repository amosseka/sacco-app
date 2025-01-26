function fetchChartData() {

    let url = '/api/reports';

    console.log(url);

    fetch(url).then((response)=>{
        return response.json();
    }).then((data)=>{

        let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        console.log(data);

        //The response data

        let category = [];

        let totals = [];


        if (data['chart_type'] == 'year') {

            category = months;

            for (let month of months ) {
                totals.push(data['totals'][month]['total_transactions']);
            }
        }

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
    });
}

fetchChartData();