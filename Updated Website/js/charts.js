// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
// Bar Chart Example
// var ctx = document.getElementById("bar");
// var bar = new Chart(ctx, {
//   type: 'bar',
//   data: {
//     labels: ["2000", "2005", "2010", "2015", "2020"],
//     datasets: [{
//       label: "India",
//       backgroundColor: "dodgerblue",
//       borderColor: "transparent",
//       data: [1057, 1148, 1234, 1310, 1380],
//     },
//     {
//       label: "China",
//       backgroundColor: "purple",
//       borderColor: "transparent",
//       data: [1291, 1331, 1369, 1407, 1439],
//     },
//     {
//       label: "United States",
//       backgroundColor: "red",
//       borderColor: "transparent",
//       data: [282, 295, 309, 321, 331],
//     },
//     {
//       label: "US",
//       backgroundColor: "green",
//       borderColor: "transparent",
//       data: [282, 295, 309, 321, 331],
//     },
//     ],
//   },
//   options: {
//     scales: {
//       xAxes: [{
//         time: {
//           unit: 'year'
//         },
//         gridLines: {
//           display: false
//         },
//         ticks: {
//           maxTicksLimit: 6
//         }
//       }],
//       yAxes: [{
//         ticks: {
//           min: 0,
//         },
//         gridLines: {
//           display: true
//         }
//       }],
//     },
//     legend: {
//       display: true
//     }
//   }
// });

// ANIME SCORE VS EPISODES SCATTER PLOT!!

let filename1 = 'Updated Website/chart_data/chart_anime.csv'
d3.csv(filename1).then(function(loadedData){
  let ep = [];
  let sc = [];
  let titles = [];

  // x= anime_test_df['episodes'] 
  // y= anime_test_df['score']

  for (let i=0; i<loadedData.length; i++){
    let episodes = loadedData[i].episodes;
    ep.push(episodes)

    let score = loadedData[i].score;
    sc.push(score)
    
    let title = loadedData[i].title;
    titles.push(title)


  }
  let coords = ep.map( (v,i) => ({ x: v, y: sc[i], title: titles[i] }) )

  //console.log(coords)

  
  
  const ctx = document.getElementById('scatter');
  const scatter = new Chart(ctx, {
      type: 'scatter',
      data: {
        labels: "scatter dataset",
        datasets: [
          {
            label: "Scatter ",
            backgroundColor: "rgba(250,192,231,0.4)",
            borderColor: "rgb(250,192,231)",
            data: coords,
            labels: titles,
          }
        ]},
        
        options: {
          responsive: true,
          maintainAspectRatio: false,

          legend: {
            display: false,
          },
          tooltips: {
            displayColors: false,
            callbacks: {
              title: function(tooltipItem, all) {
                return [
                  all.datasets[tooltipItem[0].datasetIndex].data[tooltipItem[0].index].title,
                ]
              },
              label: function(tooltipItem, all) {
                return [
                  'Number of episodes: ' + tooltipItem.xLabel.toLocaleString() ,
                  'Score: ' +tooltipItem.yLabel.toLocaleString() 
                ]
              }
            },

          //tooltip: {
            
              //callbacks: {
               // label: function(scatter) {
                  //let label = scatter.dataset.labels || '';
                //  let label = titles

                  
                //  return label;
                //}

                //label: function(tooltipItem, scatter){
                  // let t_label = (scatter.config.data.datasets[tooltipItem.index].data[tooltipItem.index].title);
                  // t_label += " (" + scatter.parsed.x + ", " + scatter.parsed.y + ")";
                  // return t_label;
                //},
                // afterLabel: (tooltipItem, data) => [`${x}: ${tooltipItem.xLabel}`, `${y}: ${tooltipItem.yLabel}`]

                //title: (tooltipItem, data) => "New title"
                    
                    // let tit = titles[coords.dataIndex];
                    // titles += " (" + ctx.parsed.x + ", " + ctx.parsed.y + ")";
                    // return labels[coords.dataIndex];
                    //label = datasets.labels[titles.datasetIndex];
                    //return label;
                      
                      
                  
                    //}
                
            },
          borderWidth: 0,

          responsive: true,
          maintainAspectRatio: false,
          title: {
            display: true,
            text: 'Top 50 Animes Ranked: Length of Shows vs Scores',
          },  
          showLines: false,
          scales: {
            bounds: 'ticks',
            xAxes: [ {
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Length of Show (Number of Episodes)'
              },
            } ],
            yAxes: [ {
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'scores'
              }
            } ]
          },
          
     
        }
  })
  //console.log(coords[dataIndex].title)
  console.log(scatter.config.data.datasets[0].data[0].title)
  //console.log(scatter.config.data.datasets[0].data[0].titles)
 // console.log(titles[coords.datasetIndex]);
  //console.log(everything);
});
  

// TIME SERIES CHART!!

let filename = 'Updated Website/chart_data/mock_timeseries.csv'
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
  // console.log(animedata)

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
          backgroundColor: "rgba(250,192,231,0.6)",
          borderColor: "rgb(250,192,231)",
          data: animedata,
          fill: true,
        }]

      },
      options: {
        tooltips: {
          displayColors: false,
          callbacks: {
            title:function(item, everything){
              return;
            },
            label: function(tooltipItem, all) {
              // console.log(tooltipItem);
              // console.log(all);

              let year = tooltipItem.xLabel;
              let titleCount = tooltipItem.yLabel;
              let label = all.datasets[tooltipItem.datasetIndex].label;

              return[
                titleCount + ' '+ label +' titles released in ' + year 
              ]
            },
        

          }
        },
        title: {
          display: true,
          text: ['Anime Growth Over time: New Titles released each year']
        }, 
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'year released'
            },
          } ],
          yAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'number of shows released'
            }
          } ]
        }
      }
    })


});

// MOVIE VS SHOWS CHART!!

let filename2 = 'Updated Website/chart_data/movie_vs_show_count.csv'
d3.csv(filename2).then(function(loadedData){
  let netflix = [];
  let hulu = [];
  let amazon = [];
  let disney = [];
  let anime = [];

  for (let i=0; i<loadedData.length; i++){
  
    
    if (loadedData[i].source == "Netflix"){
      let netflixdataM = loadedData[i].count_movie;
      let netflixdataS = loadedData[i].count_show;
      netflix.push(netflixdataM, netflixdataS);
    }
    else if (loadedData[i].source == "Hulu") {
      let huludataM = loadedData[i].count_movie;
      let huludataS = loadedData[i].count_show;
      hulu.push(huludataM, huludataS);
    }
    else if (loadedData[i].source == "Amazon") {
      let amazondataM = loadedData[i].count_movie; 
      let amazondataS = loadedData[i].count_show;
      amazon.push(amazondataM, amazondataS);
    }
    else if (loadedData[i].source == "Disney") {
      let disneydataM = loadedData[i].count_movie; 
      let disneydataS = loadedData[i].count_show;
      disney.push(disneydataM, disneydataS);
    }
    else if (loadedData[i].source == "Anime"){
      let animedataM = loadedData[i].count_movie; 
      let animedataS = loadedData[i].count_show;
      anime.push(animedataM,animedataS );
      
      // console.log(animefiltered);
    }
    else{
      console.log("error")
    }

  
   // console.log(anime)
  
  }
  const ctx = document.getElementById('bar2');
  const bar2 = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ["Movies", "Shows"],
        datasets: [{
          label: "Netflix",
          backgroundColor: "red",
          borderColor: "transparent",
          data: netflix,
        },
        {
          label: "Hulu",
          backgroundColor: "green",
          borderColor: "transparent",
          data: hulu,
        },
        {
          label: "Amazon",
          backgroundColor: "dodgerblue",
          borderColor: "transparent",
          data: amazon,
        },
        {
          label: "Disney",
          backgroundColor: "purple",
          borderColor: "transparent",
          data: disney,
        },
        {
          label: "Animes",
          backgroundColor: "rgb(250,192,231)",
          borderColor: "transparent",
          data: anime,
        },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [ {
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Number Titles'
            }
          } ]
        },
        title: {
          display: true,
          text: ['Count of Movies vs Shows by Platform']
        }, 
      }
    })

});




// STACKED GENRE BAR CHART!!

let filename3 = 'Updated Website/chart_data/top5genres_stack.csv'
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
  // console.log(animegenres)

  const ctx = document.getElementById('bar3');
  const bar3 = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: "Netflix",
          data: netflixgenres,
          backgroundColor: "red",
          borderColor: "transparent",
          fill: true,
        },
        {
          label: "Hulu",
          backgroundColor: "green",
          borderColor: "transparent",
          data: hulugenres,
          fill: true,
        },
        {
          label: "Amazon",
          backgroundColor: "dodgerblue",
          borderColor: "transparent",
          data: amazongenres,
          fill: true,
        },
        {
          label: "Disney",
          backgroundColor: "purple",
          borderColor: "black",
          data: disneygenres,
          fill: true,
        },
        {
          label: "Anime",
          backgroundColor: "rgb(250,192,231)",
          borderColor: "transparent",
          data: animegenres,
          fill: true,
        }],
        },
        options: {
          scales: {
            xAxes: [{ stacked: true,
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Top 5 Anime Genres'
              }
            }],

            yAxes: [{ stacked: true,
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Number of Titles'
              }
            }]
          },
          responsive: true,
          maintainAspectRatio: false,
          title: {
            display: true,
            text: ['Number of Titles in Top 5 Anime Genres by Platform']
          }, 
        }

      
    });

});