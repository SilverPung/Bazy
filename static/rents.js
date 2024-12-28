document.getElementById("rentsSelect").addEventListener("change", function(event){
    var rent = document.getElementById("rentsSelect").value;
    if (rent === ""){
        document.getElementById("rentsFormEdit").style.display = "none";
        console.log("No rent selected");
        return;
    }
    fetch(`/agency/rent/${rent}`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        data = data[0];
        document.getElementById("edit_start_date").value = data.START_DATE;
        document.getElementById("edit_end_date").value = data.END_DATE;
        document.getElementById("edit_deposit").value = data.DEPOSIT;
        document.getElementById("clientSelectEdit").value = data.CLIENT_ID;
        document.getElementById("propertySelectEdit").value = data.PROPERTY_ID;
        document.getElementById("statusSelectEdit").value = data.STATUS;
        document.getElementById("edit_price").value = data.PRICE;
        document.getElementById("rentsFormEdit").style.display = "block";
    });
    fetch(`/agency/rents/${rent}/payments`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        var paymentsList = document.getElementById("rentPayments").getElementsByTagName("ul")[0];
        paymentsList.innerHTML = "";
        if(data.detail == "No payments found"){
            var paymentItem = document.createElement("li");
            paymentItem.innerHTML = "Brak płatności";
            paymentsList.appendChild(paymentItem);
            return;
        }
        data.forEach(payment => {
            var paymentItem = document.createElement("li");
            paymentItem.innerHTML = `<span>Data: ${payment.PAYMENT_DATE}</span>
                                    <span>Kwota: ${payment.AMOUNT}</span>
                                    <span>Status: ${payment.STATUS}</span>
                                    <span>Metoda: ${payment.METHOD}</span>`;
            paymentsList.appendChild(paymentItem);
        });


    });
    document.getElementById("addictionalRentsInfo").style.display = "block";
    
});

document.getElementById("editRents").addEventListener("click", function(event){
    event.preventDefault();
    var rent = document.getElementById("rentsSelect").value;
    var startDate = document.getElementById("edit_start_date").value;
    var endDate = document.getElementById("edit_end_date").value;
    var deposit = document.getElementById("edit_deposit").value;
    var client = document.getElementById("clientSelectEdit").value;
    var property = document.getElementById("propertySelectEdit").value;
    var status = document.getElementById("statusSelectEdit").value;
    var price = document.getElementById("edit_price").value;
    
    var queryParams = new URLSearchParams({
        start_date: startDate,
        end_date: endDate,
        deposit: deposit,
        client_id: client,
        property_id: property,
        status: status,
        price: price
    });
    fetch(`/agency/rent/${rent}?${queryParams}`, {
        method: "PUT"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message === "Rent updated"){
            alert("Zaktualizowano dane wynajmu");
            location.reload();
        } else {
            alert("Nie udało się zaktualizować danych wynajmu " + data.detail);
        }
    });
});

document.getElementById("addRents").addEventListener("click", function(event){
    event.preventDefault();
    var startDate = document.getElementById("add_start_date").value;
    var endDate = document.getElementById("add_end_date").value;
    var deposit = document.getElementById("add_deposit").value;
    var client = document.getElementById("clientSelect").value;
    var property = document.getElementById("propertySelect").value;
    var status = document.getElementById("statusSelect").value;
    var price = document.getElementById("add_price").value;
    
    var queryParams = new URLSearchParams({
        start_date: startDate,
        end_date: endDate,
        price: price,
        deposit: deposit,
        client_id: client,
        property_id: property,
        status: status
        
    });
    fetch(`/agency/rent?${queryParams}`, {
        method: "POST"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message === "Rent inserted successfully"){
            alert("Dodano nowy wynajem");
            location.reload();
        } else {
            alert("Nie udało się dodać nowego wynajmu " + data.detail);
        }
    });
});

document.getElementById("deleteRents").addEventListener("click", function(event){
    event.preventDefault();
    var rent = document.getElementById("rentsSelect").value;
    if (rent === ""){
        alert("Wybierz wynajem");
        return;
    }
    fetch(`/agency/rent/${rent}`, {
        method: "DELETE"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message == "Rent deleted successfully"){
            alert("Usunięto wynajem");
            location.reload();
        } else {
            alert("Nie udało się usunąć wynajmu " + data.detail);
        }
    });
});