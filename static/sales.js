document.getElementById("salesSelect").addEventListener("change", function(event){
    var sale = document.getElementById("salesSelect").value;
    if (sale === ""){
        document.getElementById("salesFormEdit").style.display = "none";
        console.log("No sale selected");
        return;
    }
    fetch(`/agency/sale/${sale}`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        data = data[0];
        document.getElementById("edit_date").value = data.SALE_DATE;
        document.getElementById("edit_price").value = data.PRICE;
        document.getElementById("clientSelectEdit").value = data.CLIENT_ID;
        document.getElementById("propertySelectEdit").value = data.PROPERTY_ID;
        document.getElementById("agentSelectEdit").value = data.AGENT_ID;
        document.getElementById("statusSelectEdit").value = data.STATUS;
        document.getElementById("salesFormEdit").style.display = "block";
    });
});

document.getElementById("editSales").addEventListener("click", function(event){
    event.preventDefault();
    var sale = document.getElementById("salesSelect").value;
    var saleDate = document.getElementById("edit_date").value;
    var salePrice = document.getElementById("edit_price").value;
    var client = document.getElementById("clientSelectEdit").value;
    var property = document.getElementById("propertySelectEdit").value;
    var agent = document.getElementById("agentSelectEdit").value;
    var status = document.getElementById("statusSelectEdit").value;
    
    var queryParams = new URLSearchParams({
        sale_date: saleDate,
        price: salePrice,
        client_id: client,
        property_id: property,
        agent_id: agent,
        status: status
    });
    fetch(`/agency/sale/${sale}?${queryParams}`, {
        method: "PUT"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message === "Sale updated"){
            alert("Zaktualizowano dane sprzedaży");
            location.reload();
        } else {
            alert("Nie udało się zaktualizować danych sprzedaży " + data.detail);
        }
    });
});

document.getElementById("addSales").addEventListener("click", function(event){
    event.preventDefault();
    var saleDate = document.getElementById("add_date").value;
    var salePrice = document.getElementById("add_price").value;
    var client = document.getElementById("clientSelect").value;
    var property = document.getElementById("propertySelect").value;
    var agent = document.getElementById("agentSelect").value;
    var status = document.getElementById("statusSelect").value;
    
    var queryParams = new URLSearchParams({
        sale_date: saleDate,
        price: salePrice,
        client_id: client,
        property_id: property,
        agent_id: agent,
        status: status
    });
    fetch(`/agency/sale?${queryParams}`, {
        method: "POST"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message === "Sale inserted successfully"){
            alert("Dodano nową sprzedaż");
            location.reload();
        } else {
            alert("Nie udało się dodać nowej sprzedaży " + data.detail);
        }
    });
});

document.getElementById("deleteSales").addEventListener("click", function(event){
    event.preventDefault();
    var sale = document.getElementById("salesSelect").value;
    if (sale === ""){
        alert("Wybierz sprzedaż");
        return;
    }
    fetch(`/agency/sale/${sale}`, {
        method: "DELETE"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message == "Sale deleted successfully"){
            alert("Usunięto sprzedaż");
            location.reload();
        } else {
            alert("Nie udało się usunąć sprzedaży " + data.detail);
        }
    });
});