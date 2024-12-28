document.getElementById("repairSelect").addEventListener("change", function(event){
    var repair = document.getElementById("repairSelect").value;
    if (repair === ""){
        document.getElementById("repairFormEdit").style.display = "none";
        console.log("No repair selected");
        return;
    }
    fetch(`/agency/repair/${repair}`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        data = data[0];
        document.getElementById("repairDateEdit").value = data.REPAIR_DATE;
        document.getElementById("repairStatusEdit").value = data.STATUS;
        document.getElementById("repairDescriptionEdit").value = data.DESCRIPTION;
        document.getElementById("repairPropertyEdit").value = data.PROPERTY_ID;
        document.getElementById("repairFormEdit").style.display = "block";

    });
});  

document.getElementById("updateRepair").addEventListener("click", function(event){
    event.preventDefault();
    var repair = document.getElementById("repairSelect").value;
    var repairDate = document.getElementById("repairDateEdit").value;
    var repairStatus = document.getElementById("repairStatusEdit").value;
    var repairDescription = document.getElementById("repairDescriptionEdit").value;
    var repairProperty = document.getElementById("repairPropertyEdit").value;
    var queryParams = new URLSearchParams({
        repair_date: repairDate,
        status: repairStatus,
        description: repairDescription,
        property_id: repairProperty
    });
    fetch(`/agency/repair/${repair}?${queryParams}`, {
        method: "PUT"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message === "Repair updated"){
            alert("Zaktualizowano dane naprawy");
            location.reload();
        } else {
            alert("Nie udało się zaktualizować danych naprawy " + data.detail);
        }
    });
});

document.getElementById("addRepair").addEventListener("click", function(event){
    event.preventDefault();
    var repairDate = document.getElementById("repairDate").value;
    var repairStatus = document.getElementById("repairStatus").value;
    var repairDescription = document.getElementById("repairDescription").value;
    var repairProperty = document.getElementById("repairProperty").value;
    
    var queryParams = new URLSearchParams({
        repair_date: repairDate,
        status: repairStatus,
        description: repairDescription,
        property_id: repairProperty
    });
    fetch(`/agency/repair?${queryParams}`, {
        method: "POST"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message === "Repair inserted successfully"){
            alert("Dodano nową naprawę");
            location.reload();
        } else {
            alert("Nie udało się dodać nowej naprawy " + data.detail);
        }
    });
});

document.getElementById("deleteRepair").addEventListener("click", function(event){
    event.preventDefault();
    var repair = document.getElementById("repairSelect").value;
    if (repair === ""){
        alert("Wybierz naprawę");
        return;
    }
    fetch(`/agency/repair/${repair}`, {
        method: "DELETE"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message == "Repair deleted successfully"){
            alert("Usunięto naprawę");
            location.reload();
        } else {
            alert("Nie udało się usunąć naprawy " + data.detail);
        }
    });
});