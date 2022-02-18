const tableData = data; 

var tbody = d3.select("tbody"); 

function buildTable(data){
    // Clear data
    tbody.html("");  

    // For each data row, append a row to table
    data.forEach((dataRow)=> {
        let row = tbody.append("tr");

        // New function to add data (td) to table rows
        Object.values(dataRow).forEach((val)=>{
            let cell = row.append("td");
            cell.text(val);
        });
    });  
}

function handleClick(){
    let title = d3.select("#title").property("value");
    let filteredData = tableData;
    if(title){
        filteredData = filteredData.filter(row => row.title === title);
    };
    buildTable(filteredData);
}

d3.selectAll("#filter-btn").on("click", handleClick);

buildTable(tableData);