
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
    {
      label: "US",
      backgroundColor: "green",
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

// TIME SERIES CHART!!

let filename = 'chart_data/mock_timeseries.csv'
d3.csv(filename).then(function(loadedData){
  let livedata = [];
  let animedata = [];
  let labels = [];

  for (let i=0; i<loadedData.length; i++){
    let year = loadedData[i].release_year;
    labels.push(year)

    let liveCount = loadedData[i].count_live_actions;
    livedata.push(liveCount)

    let animeCount = loadedData[i].count_animes;
    animedata.push(animeCount)
  }
  console.log(animedata)

  const ctx = document.getElementById('line');
  const line = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: "Live Action",
          data: livedata,
          fill: true,
        },
        {
          label: "Anime",
          data: animedata,
          fill: true,
        }]

      }
    })


});

// MOVIE VS SHOWS CHART!!

let filename2 = 'chart_data/movie_vs_show_count.csv'
d3.csv(filename2).then(function(loadedData){
  let netflix = [];
  let hulu = [];
  let amazon = [];
  let disney = [];
  let anime = [];

  for (let i=0; i<loadedData.length; i++){
  
    
    if (loadedData[i].source == "netflix"){
      let netflixdataM = loadedData[i].count_movie;
      let netflixdataS = loadedData[i].count_show;
      netflix.push(netflixdataM, netflixdataS);
    }
    else if (loadedData[i].source == "hulu") {
      let huludataM = loadedData[i].count_movie;
      let huludataS = loadedData[i].count_show;
      hulu.push(huludataM, huludataS);
    }
    else if (loadedData[i].source == "amazon") {
      let amazondataM = loadedData[i].count_movie; 
      let amazondataS = loadedData[i].count_show;
      amazon.push(amazondataM, amazondataS);
    }
    else if (loadedData[i].source == "disney") {
      let disneydataM = loadedData[i].count_movie; 
      let disneydataS = loadedData[i].count_show;
      disney.push(disneydataM, disneydataS);
    }
    else if (loadedData[i].source == "anime"){
      let animedataM = loadedData[i].count_movie; 
      let animedataS = loadedData[i].count_show;
      anime.push(animedataM,animedataS );
      
      // console.log(animefiltered);
    }
    else{
      console.log("error")
    }

  
   console.log(anime)
  
  }
  const ctx = document.getElementById('bar2');
  const line = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ["Movies", "Shows"],
        datasets: [{
          label: "Netflix",
          backgroundColor: "dodgerblue",
          borderColor: "transparent",
          data: netflix,
        },
        {
          label: "Hulu",
          backgroundColor: "purple",
          borderColor: "transparent",
          data: hulu,
        },
        {
          label: "Amazon",
          backgroundColor: "red",
          borderColor: "transparent",
          data: amazon,
        },
        {
          label: "Disney",
          backgroundColor: "green",
          borderColor: "transparent",
          data: disney,
        },
        {
          label: "Animes",
          backgroundColor: "pink",
          borderColor: "transparent",
          data: anime,
        },
        ],
      },
    })

});




// STACKED GENRE BAR CHART!!

let filename3 = 'chart_data/top5genres_stack.csv'
d3.csv(filename3).then(function(loadedData){
  let netflixgenres = [];
  let hulugenres = [];
  let amazongenres = [];
  let disneygenres = [];
  let animegenres = [];
  let labels = [];

  for (let i=0; i<loadedData.length; i++){
    let source = loadedData[i].source;
    labels.push(source);

    let ngenrecount = loadedData[i].netflix;
    netflixgenres.push(ngenrecount);

    let hgenrecount = loadedData[i].hulu;
    hulugenres.push(hgenrecount);

    let agenrecount = loadedData[i].amazon;
    amazongenres.push(agenrecount);

    let dgenrecount = loadedData[i].disney;
    disneygenres.push(dgenrecount);

    let animgenrecount = loadedData[i].anime;
    animegenres.push(animgenrecount);
  }
  console.log(animegenres)

  const ctx = document.getElementById('bar3');
  const line = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: "Netflix",
          data: netflixgenres,
          backgroundColor: "dodgerblue",
          borderColor: "transparent",
          fill: true,
        },
        {
          label: "Hulu",
          backgroundColor: "purple",
          borderColor: "transparent",
          data: hulugenres,
          fill: true,
        },
        {
          label: "Amazon",
          backgroundColor: "red",
          borderColor: "transparent",
          data: amazongenres,
          fill: true,
        },
        {
          label: "Disney",
          backgroundColor: "green",
          borderColor: "transparent",
          data: disneygenres,
          fill: true,
        },
        {
          label: "Anime",
          backgroundColor: "pink",
          borderColor: "transparent",
          data: animegenres,
          fill: true,
        }],
        },
        options: {
          scales: {
            xAxes: [{ stacked: true }],
            yAxes: [{ stacked: true }]
          }
        }

      
    });

});
