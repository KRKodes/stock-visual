let chartInstance;

document.querySelector('#form').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    fetch('/fetch', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const indicatorKey = `Technical Analysis: ${formData.get('indicator')}`;
            const indicatorData = data[indicatorKey];
            console.log(indicatorData); // Check if correct data

            if (indicatorData) {
                const labels = Object.keys(indicatorData);
                const values = labels.map(date => indicatorData[date][formData.get('indicator')]);
                console.log(labels);
                console.log(values);

                // Translate the time unit based on the user's interval
                const interval = formData.get('interval');
                const intervalMapping = {
                    '1min': 'minute',
                    '5min': 'minute',
                    '15min': 'minute',
                    '30min': 'minute',
                    '60min': 'minute',
                    'daily': 'day',
                    'weekly': 'week',
                    'monthly': 'month'
                };
                const timeUnit = intervalMapping[interval];

                // Update the chart options with the correct time unit
                createChart('myChart', labels, values, timeUnit);

                // Increment the count after API call is successful
                fetch("/increment-count", {
                        method: "POST"
                    })
                    .then(response => response.json())
                    .then(incrementData => {
                        if (incrementData.count >= 10) {
                            alert("Only 10 submissions a day, come back tomorrow.");
                        }
                    });
            } else {
                console.error('Indicator data not found.');
            }
        })
        .catch(error => console.error('Error:', error));
});

function createChart(chartId, labels, values, timeUnit) {
    var ctx = document.getElementById(chartId).getContext('2d');

    if (chartInstance) {
        // Update existing chart
        chartInstance.data.labels = labels;
        chartInstance.data.datasets[0].data = values; // Update line dataset
        chartInstance.options.scales.x.time.unit = timeUnit; // Update time unit
        chartInstance.update();
    } else {
        // Create new chart
        chartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                //ChatGPT told me about how to do this datasets section because I had been asking about doing an overlay since chart.js doesn't explicitly say I can, but I ended up switching to just a line graph as I realized I don't get the price when fetching from alphavantage. I kept this section because I knew I could change the color of the data here
                datasets: [{
                    label: 'Line Dataset',
                    data: values,
                    borderColor: '#FFC107',
                    backgroundColor: 'transparent'
                }]
            },
            options: {
                legend: {
                    labels: {
                        fontColor: '#FFC107'
                    }
                },
                scales: {
                    x: {
                        type: 'time',
                        time: {
                            unit: timeUnit,
                        },
                        grid: {
                            color: 'black'
                        },
                        ticks: {
                            color: 'black'
                        }
                    },
                    y: {
                        beginAtZero: false,
                        grid: {
                            color: 'black'
                        },
                        ticks: {
                            color: 'black'
                        }
                    }
                }
            }
        });
    }
}
