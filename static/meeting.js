document.getElementById("meetingSelect").addEventListener("change", function(event){
    var meeting = document.getElementById("meetingSelect").value;
    if (meeting === ""){
        document.getElementById("meetingFormEdit").style.display = "none";
        console.log("No meeting selected");
        return;
    }
    fetch(`/agency/meeting/${meeting}`, {
        method: "GET"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        data = data[0];
        document.getElementById("edit_date").value = data.DATE_MEETING;
        document.getElementById("edit_time").value = data.TIME_MEETING;
        document.getElementById("clientSelectEdit").value = data.CLIENT_ID;
        document.getElementById("propertySelectEdit").value = data.PROPERTY_ID;
        document.getElementById("agentSelectEdit").value = data.AGENT_ID;
        document.getElementById("statusSelectEdit").value = data.STATUS;
        document.getElementById("meetingFormEdit").style.display = "block";
    });
});

document.getElementById("editMeeting").addEventListener("click", function(event){
    event.preventDefault();
    var meeting = document.getElementById("meetingSelect").value;
    var meetingDate = document.getElementById("edit_date").value;
    var meetingTime = document.getElementById("edit_time").value;
    var client = document.getElementById("clientSelectEdit").value;
    var property = document.getElementById("propertySelectEdit").value;
    var agent = document.getElementById("agentSelectEdit").value;
    var status = document.getElementById("statusSelectEdit").value;
    
    var queryParams = new URLSearchParams({
        date_meeting: meetingDate,
        time_meeting: meetingTime,
        client_id: client,
        property_id: property,
        agent_id: agent,
        status: status
    });
    fetch(`/agency/meeting/${meeting}?${queryParams}`, {
        method: "PUT"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message === "Meeting updated"){
            alert("Zaktualizowano dane spotkania");
            location.reload();
        } else {
            alert("Nie udało się zaktualizować danych spotkania " + data.detail);
        }
    });
});

document.getElementById("addMeeting").addEventListener("click", function(event){
    event.preventDefault();
    var meetingDate = document.getElementById("add_date").value;
    var meetingTime = document.getElementById("add_time").value;
    var client = document.getElementById("clientSelect").value;
    var property = document.getElementById("propertySelect").value;
    var agent = document.getElementById("agentSelect").value;
    var status = document.getElementById("statusSelect").value;
    
    var queryParams = new URLSearchParams({
        date_meeting: meetingDate,
        time_meeting: meetingTime,
        client_id: client,
        property_id: property,
        agent_id: agent,
        status: status
    });
    fetch(`/agency/meeting?${queryParams}`, {
        method: "POST"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message === "Meeting inserted successfully"){
            alert("Dodano nowe spotkanie");
            location.reload();
        } else {
            alert("Nie udało się dodać nowego spotkania " + data.detail);
        }
    });
});

document.getElementById("deleteMetting").addEventListener("click", function(event){
    event.preventDefault();
    var meeting = document.getElementById("meetingSelect").value;
    if (meeting === ""){
        alert("Wybierz spotkanie");
        return;
    }
    fetch(`/agency/meeting/${meeting}`, {
        method: "DELETE"
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.message == "Meeting deleted successfully"){
            alert("Usunięto spotkanie");
            location.reload();
        } else {
            alert("Nie udało się usunąć spotkania " + data.detail);
        }
    });
});