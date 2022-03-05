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

// // PRINT FINAL.JSON RESULTS TO CONSOLE 
// var final_data = fetch("final.json")
//         .then(response => response.json())
//         .then(final_data => {
//             for (i=0; i<5; i++){
//                 console.log(final_data[i].recommended_animes)
//             };
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

// CREATES A LIST 

var final_data = fetch("final_live_actions_with_anime_recs.json")
            .then(response => response.json())
            .then(final_data=>{
                for (i=0; i<final_data.length; i++){
                    final_data[i] = final_data[i].title;
                }
            console.log(final_data[0])
            })
  


// CREATE SEARCHABLE DROP DOWN BAR 
// https://makitweb.com/make-a-dropdown-with-search-box-using-jquery/

$(document).ready(function(){
    // Initialize select2
    $(".s2").select2();

     // Read selected option
  $('#but_read').click(function(){
    // assign value to selection 
    var c = $('#selUser').val();
      
    // create list of recommendations
    var final_data = fetch("final_live_actions_with_anime_recs.json")
          .then(response => response.json())
          .then(final_data => {
              //final_anime_recommendations = []; 
              //or (i=0; i<final_data.length; i++){
              //    final_anime_recommendations[i] = [final_data[i].rec1, final_data[i].rec2];                  
              //}
              //recs = final_anime_recommendations[c];
             
              // print the result 
              $('#result').html("Your top 5 recommended animes are: <br> <br>" + final_data[c].rec1+ 
              "<br>"+final_data[c].rec2+ 
              "<br>"+final_data[c].rec3+ 
              "<br>"+final_data[c].rec4+ 
              "<br>"+final_data[c].rec5);          

            })
        });
  });