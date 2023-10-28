// navbar section starts here

let a = document.body.getElementsByTagName('a')

let CurrentPage = window.location.pathname.split('/').pop()

if (CurrentPage == "why-is-saving-power-important"){
    a[1].style.textDecoration = 'underline'
}
else if (CurrentPage == "home"){
    a[0].style.textDecoration = 'underline'
}

else if (CurrentPage == "analyzer"){
    let b = document.querySelector('.saving')
    b.innerText = 'Analyzer'
}

else{
    a[0].style.textDecoration = 'underline'
}

// navbar section ends here

// table starts here


srno = 1

const tables = document.querySelector('table')

function CreateTables(){

    const NewRow = tables.insertRow(-1)

    let cell1 = NewRow.insertCell(0)
    cell1.innerHTML = (srno += 1)

    let cell2 = NewRow.insertCell(1)
    cell2.innerHTML = "<input class='textbox' type='text' name='nameofapp'>";


    let cell3 = NewRow.insertCell(2)
    cell3.innerHTML = "<input class='textbox' type = 'number' name='watts'>";

    let cell4 = NewRow.insertCell(3)
    cell4.innerHTML = "<input class='textbox' type = 'number' name='no'>";

    let cell5 = NewRow.insertCell(4)
    cell5.innerHTML = "<input class='textbox' type = 'number' name='hours'>";
}

// table ends here

// setting event listener for adding a new row in table on every click

let add = document.querySelector('.Addbutton')
add.addEventListener('click', function(){
    CreateTables()
})


// let btn = document.querySelector('.downloadlink')

// btn.addEventListener('click', function(){

//     var blob = new Blob([fileData], {type: "text/plain"});
//     var url = URL.createObjectURL(blob);
//     var link = document.createElement("a");
//     link.href = url;
//     link.download = "file.txt";
//     link.style.display = "none";
//     document.body.appendChild(link);
//     link.click();

// })

