document.getElementById("attachClientForm").addEventListener("submit", function(event){
    event.preventDefault();
    var user = document.getElementById("userSelect").value;
    var preffered_location = document.getElementById("attach_preffered_location").value;
    var budget = document.getElementById("attach_budget").value;
    if (user === "" || preffered_location === "" || budget === ""){
        alert("Wypełnij wszystkie pola");
        return;
    }
    var queryParams = new URLSearchParams({
        user_id: user,
        preffered_location: preffered_location,
        budget: budget
    })
    fetch(`/agency/client?${queryParams}`, {
        method: "POST"
    }).then(response => response.json())
    .then(data => {
        //console.log(data);
        if(data.message === "Client inserted successfully"){
            alert("Dodano nowego klienta");
            location.reload();
        } else {
            alert("Nie udało się dodać nowego klienta "+ data.detail);
        }
    });
});

document.getElementById("addClient").addEventListener("click", function(event){
    event.preventDefault();
    var name = document.getElementById("add_name").value;
    var surname = document.getElementById("add_surname").value;
    var email = document.getElementById("add_email").value;
    var password = document.getElementById("add_password").value;
    var address = document.getElementById("add_address").value;
    var budget = document.getElementById("add_budget").value;
    var preffered_location = document.getElementById("add_preffered_location").value;
    
    var queryParams = new URLSearchParams({
        name: name,
        surname: surname,
        email: email,
        password: password,
        address: address,
        budget: budget,
        preffered_location: preffered_location
    })
    fetch(`/agency/procedure/client?${queryParams}`, {
        method: "POST"
    }).then(response => response.json())
    .then(data => {
        //console.log(data);
        if(data.message === "New client inserted successfully"){
            alert("Dodano nowego klienta");
            location.reload();
        } else {
            alert("Nie udało się dodać nowego klienta "+ data.detail);
        }
    });
});

document.getElementById("clientSelect").addEventListener("change", function(event){
    var user = document.getElementById("clientSelect").value;
    if (user === ""){
        document.getElementById("clientFormEdit").style.display = "none";
        console.log("User not selected");
        return;
    }
    fetchClientData(user);
    fetchClientSales(user);
    fetchClientMeetings(user);
    fetchClientRents(user);
    fetchClientPhoneNumbers(user);

    document.getElementById("clientPhoneNumbers").style.display = "block";
    document.getElementById("additionalClientInfo").style.display = "block";
});

function fetchClientData(user) {
    fetch(`/agency/client/${user}`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        data = data[0];
        document.getElementById("edit_name").value = data.NAME;
        document.getElementById("edit_surname").value = data.SURNAME;
        document.getElementById("edit_email").value = data.EMAIL;
        document.getElementById("edit_password").value = data.PASSWORD;
        document.getElementById("edit_address").value = data.ADDRESS;
        document.getElementById("edit_budget").value = data.BUDGET;
        document.getElementById("edit_preffered_location").value = data.PREFFERED_LOCATION;
        document.getElementById("clientFormEdit").style.display = "block";
    });
}

function fetchClientSales(user) {
    fetch(`/agency/client/${user}/sales`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        var salesList = document.getElementById("clientSales").getElementsByTagName("ul")[0];
        salesList.innerHTML = "";
        if(data.detail === "No sales found"){
            var saleItem = document.createElement("li");
            saleItem.innerHTML = "Brak sprzedaży";
            salesList.appendChild(saleItem);
            return;
        }
        data.forEach(sale => {
            var saleItem = document.createElement("li");
            saleItem.innerHTML = `<span>Data: ${sale.SALE_DATE}</span>
                                    <span>Cena: ${sale.PRICE}</span>
                                    <span>Status: ${sale.STATUS}</span>
                                    <span>Agent: ${sale.AGENT_NAME} ${sale.AGENT_SURNAME}</span>
                                    <span>Nieruchomość: ${sale.STATE + " " + sale.CITY + " " + sale.ADDRESS}</span>`;
            salesList.appendChild(saleItem);
        });
    });
}

function fetchClientMeetings(user) {
    fetch(`/agency/client/${user}/meetings`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        var meetingsList = document.getElementById("clientMettings").getElementsByTagName("ul")[0];
        meetingsList.innerHTML = "";
        if(data.detail === "No meetings found"){
            var meetingItem = document.createElement("li");
            meetingItem.innerHTML = "Brak spotkań";
            meetingsList.appendChild(meetingItem);
            return;
        }
        data.forEach(meeting => {
            var meetingItem = document.createElement("li");
            meetingItem.innerHTML = `<span>Data: ${meeting.DATE_MEETING} ${meeting.TIME_MEETING}</span>
                                    <span>Status: ${meeting.STATUS}</span>
                                    <span>Agent: ${meeting.AGENT_NAME} ${meeting.AGENT_SURNAME}</span>
                                    <span>Nieruchomość: ${meeting.STATE + " " + meeting.CITY + " " + meeting.ADDRESS}</span>`;
            meetingsList.appendChild(meetingItem);
        });
    });
}

function fetchClientRents(user) {
    fetch(`/agency/client/${user}/rents`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        var rentsList = document.getElementById("clientRents").getElementsByTagName("ul")[0];
        rentsList.innerHTML = "";
        if(data.detail === "No rents found"){
            var rentItem = document.createElement("li");
            rentItem.innerHTML = "Brak wynajmów";
            rentsList.appendChild(rentItem);
            return;
        }
        data.forEach(rent => {
            var rentItem = document.createElement("li");
            rentItem.innerHTML = `<span>Data: ${rent.START_DATE + " - " + rent.END_DATE}</span>
                                    <span>Depozyt: ${rent.DEPOSIT}</span>
                                    <span>Status: ${rent.STATUS}</span>
                                    <span>Nieruchomość: ${rent.STATE + " " + rent.CITY + " " + rent.ADDRESS}</span>`;
            rentsList.appendChild(rentItem);
        });
    });
}

function fetchClientPhoneNumbers(user) {
    fetch(`/agency/tel_number/${user}`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        var phoneNumbersList = document.getElementById("clientPhoneNumbers").getElementsByTagName("ul")[0];
        phoneNumbersList.innerHTML = "";
        if(data.detail === "No phone numbers found"){
            var phoneItem = document.createElement("li");
            phoneItem.innerHTML = "Brak numerów telefonu";
            phoneNumbersList.appendChild(phoneItem);
            return;
        }
        data.forEach(phone => {
            var phoneItem = document.createElement("li");
            phoneItem.innerHTML =`<span class="phone-item">${phone.TEL_NUMBER}<button id="Delete${phone.TEL_NUMBER}" class="smalldeletebutton">Usuń numer</button></span>`;
            phoneNumbersList.appendChild(phoneItem);
        });
    });
}

document.getElementById("updateClient").addEventListener("click",function(event){
    event.preventDefault();
    var user = document.getElementById("clientSelect").value;
    var name = document.getElementById("edit_name").value;
    var surname = document.getElementById("edit_surname").value;
    var email = document.getElementById("edit_email").value;
    var password = document.getElementById("edit_password").value;
    var address = document.getElementById("edit_address").value;
    var budget = document.getElementById("edit_budget").value;
    var preffered_location = document.getElementById("edit_preffered_location").value;
    var queryParams = new URLSearchParams({
        name: name,
        surname: surname,
        email: email,
        password: password,
        address: address,
        budget: budget,
        preffered_location: preffered_location
    })
    fetch(`/agency/procedure/client/${user}?${queryParams}`, {
        method: "PUT"
    }).then(response => response.json())
    .then(data => {
        //console.log(data);
        if(data.message === "Client updated"){
            alert("Zaktualizowano dane klienta");
            location.reload();
        } else {
            alert("Nie udało się zaktualizować danych klienta "+ data.detail);
        }
    });
});

document.getElementById("disconnectClient").addEventListener("click", function(event){
    event.preventDefault();
    var user = document.getElementById("clientSelect").value;
    if (user === ""){
        alert("Wybierz klienta");
        return;
    }
    fetch(`/agency/client/${user}`, {
        method: "DELETE"
    }).then(response => response.json())
    .then(data => {
        //console.log(data);
        if(data.message == "Client deleted successfully"){
            alert("Odłączono klienta");
            location.reload();
        } else {
            alert("Nie udało się odłączyć klienta "+ data.detail);
        }
    });
});

document.getElementById("addPhoneNumber").addEventListener("click", function(event){
    event.preventDefault();
    var user = document.getElementById("clientSelect").value;
    var tel_number = document.getElementById("add_tel_number").value;
    if (user === "" || tel_number === ""){
        alert("Wypełnij wszystkie pola");
        return;
    }
    var queryParams = new URLSearchParams({
        user_id: user,

        tel_number: tel_number
    })
    fetch(`/agency/tel_number?${queryParams}`, {
        method: "POST"
    }).then(response => response.json())
    .then(data => {
        //console.log(data);
        if(data.message === "Telephone number inserted successfully"){
            alert("Dodano numer telefonu");
            location.reload();
        } else {
            alert("Nie udało się dodać numeru telefonu "+ data.detail);
        }
    });
});

document.getElementById("clientPhoneNumbers").addEventListener("click", function(event){
    if(event.target.className === "smalldeletebutton"){
        var user = document.getElementById("clientSelect").value;
        var tel_number = event.target.id.slice(6);
        var queryParams = new URLSearchParams({
            user_id: user,
            tel_number: tel_number
        })

        fetch(`/agency/tel_number?${queryParams}`, {
            method: "DELETE"
        }).then(response => response.json())
        .then(data => {
            //console.log(data);
            if(data.message == "Telephone number deleted successfully"){
                alert("Usunięto numer telefonu");
                location.reload();
            } else {
                alert("Nie udało się usunąć numeru telefonu "+ data.detail);
            }
        });
    }
});