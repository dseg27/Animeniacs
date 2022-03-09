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



// // CREATES A LIST 
// var anime_data = fetch("Updated Website/clean_anime.json")
//             .then(response => response.json())
//             .then(anime_data =>{
//                 for (i=0; i<anime_data.length; i++){
//                     anime_data[i] = anime_data[i].title;
//                 }
//             console.log(anime_data[0])
//             })


// // CREATES A LIST 
// var live_data = fetch("Updated Website/clean_live.json")
//             .then(response => response.json())
//             .then(live_data =>{
//                 for (i=0; i<live_data.length; i++){
//                     live_data[i] = live_data[i].title;
//                 }
//             console.log(live_data[0])
//             })

// // CREATES A LIST 

// var final_data = fetch("Updated Website/final_live_actions_with_anime_recs.json")
//             .then(response => response.json())
//             .then(final_data=>{
//                 for (i=0; i<final_data.length; i++){
//                     final_data[i] = final_data[i].title;
//                 }
//             console.log(final_data[0])
//             })
  


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
    var final_data = fetch("Updated Website/final_live_actions_with_anime_recs.json")
          .then(response => response.json())
          .then(final_data => {
              rec_1 = []; 
              rec_2 = [];
              rec_3 = [];
              rec_4 = [];
              rec_5 = []; 
              for (i=0; i<final_data.length; i++){
                  rec_1[i] = final_data[i].rec1;   
                  rec_2[i] = final_data[i].rec2;   
                  rec_3[i] = final_data[i].rec3;   
                  rec_4[i] = final_data[i].rec4;       
                  rec_5[i] = final_data[i].rec5;  
              }

                rec_1 = rec_1[c]; 
                rec_2 = rec_2[c];
                rec_3 = rec_3[c];
                rec_4 = rec_4[c];
                rec_5 = rec_5[c]; 
              
             
              // print the result 
              $('#result').html("Your top 5 recommended animes are: <br> <br>" + "1. " + rec_1 + "<br> <br> 2. "+ rec_2 + "<br> <br> 3. " + rec_3 + "<br> <br> 4. " + rec_4 + "<br> <br> 5. " + rec_5 + "<br>" );          

            })
        });
  });