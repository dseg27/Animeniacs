// CONVERT JSON FILES TO READABLE DATA 

// // PRINT ANIME TITLES TO CONSOLE
// var anime_data = fetch("data.json")
//         .then(response => response.json())
//         .then(anime_data => {
//             for (i =0; i < anime_data.length; i++){
//                 console.log(data[i].title);
//             }
//         })

// // PRINT LIVE ACTION TITLE NAMES TO CONSOLE
// var live_data = fetch("live_data.json")
//         .then(response => response.json())
//         .then(live_data =>{
//             for (i=0; i<live_data.length; i++){
//                 console.log(live_data[i].title);
//             }
//         })



// CREATES A LIST 
var anime_data = fetch("clean_anime.json")
            .then(response => response.json())
            .then(anime_data =>{
                for (i=0; i<anime_data.length; i++){
                    anime_data[i] = anime_data[i].title;
                }
            console.log(anime_data[0])
            })


// CREATES A LIST 
var live_data = fetch("clean_live.json")
            .then(response => response.json())
            .then(live_data =>{
                for (i=0; i<live_data.length; i++){
                    live_data[i] = live_data[i].title;
                }
            console.log(live_data[0])
            })
  


// CREATE SEARCHABLE DROP DOWN BAR 
// https://makitweb.com/make-a-dropdown-with-search-box-using-jquery/

$(document).ready(function(){
    // Initialize select2
    $(".s2").select2();

    // Read selected option
    $('#but_read').click(function(){
        // create list of anime titles from anime json
        var anime_titles = fetch("clean_anime.json")
            .then(response => response.json())
            .then(anime_data =>{
                for (i=0; i<anime_data.length; i++){
                    anime_data[i] = anime_data[i].title;
                }
        // create list recs[] to hold 5 anime recommendation titles 
        // and print the result 
            recs = []; 
            for (i=0; i<5; i++){
                recs = recs + anime_data[i] + "<br>";
            }
            
            console.log(anime_data[1])
            $('#result').html("Your top 5 recommended animes are: <br> <br>" + recs);
            })
      });
  });

