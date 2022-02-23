
// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("bar");
var bar = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["2000", "2005", "2010", "2015", "2020"],
    datasets: [{
      label: "India",
      backgroundColor: "dodgerblue",
      borderColor: "transparent",
      data: [1057, 1148, 1234, 1310, 1380],
    },
    {
      label: "China",
      backgroundColor: "purple",
      borderColor: "transparent",
      data: [1291, 1331, 1369, 1407, 1439],
    },
    {
      label: "United States",
      backgroundColor: "red",
      borderColor: "transparent",
      data: [282, 295, 309, 321, 331],
    },
    ],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'year'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: true
    }
  }
});

