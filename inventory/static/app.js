// Inventory Dashboard Chart
// Active Checkouts By Type

const labels = window.chartLabels;
const data = window.chartData;

// Bar Chart
const barCtx = document.getElementById('myBarChart');

new Chart(barCtx, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: "Active Checkouts By Type",
            data: data,
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: { beginAtZero: true }
        }
    }
});
