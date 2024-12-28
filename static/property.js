document.getElementById('propertySelect').addEventListener('change', function() {
    var propertyId = this.value;
    if (propertyId) {
        // Fetch property details using AJAX or similar method
        fetch(`/agency/property/${propertyId}`)
            .then(response => response.json())
            .then(data => {
                data = data[0];
                document.getElementById('address').value = data.ADDRESS;
                document.getElementById('city').value = data.CITY;
                document.getElementById('state').value = data.STATE;
                document.getElementById('postal_code').value = data.POSTAL_CODE;
                document.getElementById('size').value = data.SIZE;
                document.getElementById('bedrooms').value = data.BEDROOMS;
                document.getElementById('bathrooms').value = data.BATHROOMS;
                document.getElementById('price').value = data.PRICE;
                document.getElementById('type').value = data.TYPE;
                document.getElementById('description').value = data.DESCRIPTION;
                document.getElementById('propertyFormEdit').style.display = 'block';
            });
    } else {
        document.getElementById('propertyFormEdit').style.display = 'none';
        console.log('No property selected');
    }
});
    //update property after changing values in form 
document.getElementById('editPropertyForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var propertyId = document.getElementById('propertySelect').value;
    var address = document.getElementById('address').value;
    var city = document.getElementById('city').value;
    var state = document.getElementById('state').value;
    var postalCode = document.getElementById('postal_code').value;
    var size = document.getElementById('size').value;
    var bedrooms = document.getElementById('bedrooms').value;
    var bathrooms = document.getElementById('bathrooms').value;
    var price = document.getElementById('price').value;
    var type = document.getElementById('type').value; // Convert to integer
    var description = document.getElementById('description').value;

    let queryParams = new URLSearchParams({
        property_id: propertyId,
        address: address,
        city: city,
        state: state,
        postal_code: postalCode,
        size: size,
        bedrooms: bedrooms,
        bathrooms: bathrooms,
        price: price,
        type1: type,
        description: description
    }).toString();
    console.log(queryParams);

    fetch(`/agency/property/${propertyId}?${queryParams}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.status == 'Property updated') {
            alert('Property updated successfully');
        } else {
            alert('Failed to update property'+ data.detail);
        }
        console.log(data);
    });
});
    // Deleting property after clicking delete button
document.getElementById('deleteProperty').addEventListener('click', function() {
    var answer = confirm('Are you sure you want to delete this property?');
    if (answer) {
        var propertyId = document.getElementById('propertySelect').value;
        fetch(`/agency/property/${propertyId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if(data.message == 'Property deleted successfully') {
                alert('Property deleted successfully');
                document.getElementById('propertyFormEdit').style.display = 'none';
                document.getElementById('propertySelect').value = '';
            } else {
                alert('Failed to delete property'+ data.detail);

            }
            console.log(data);
        });
    
    }
});
    // Adding new property after clicking submit button
document.getElementById('addPropertyForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var address = document.getElementById('add_address').value;
    var city = document.getElementById('add_city').value;
    var state = document.getElementById('add_state').value;
    var postalCode = document.getElementById('add_postal_code').value;
    var size = document.getElementById('add_size').value;
    var bedrooms = document.getElementById('add_bedrooms').value;
    var bathrooms = document.getElementById('add_bathrooms').value;
    var price = document.getElementById('add_price').value;
    var type = document.getElementById('add_type').value; // Convert to integer
    var description = document.getElementById('add_description').value;

    let queryParams = new URLSearchParams({
        address: address,
        city: city,
        state: state,
        postal_code: postalCode,
        size: size,
        bedrooms: bedrooms,
        bathrooms: bathrooms,
        price: price,
        type1: type,
        description: description
    }).toString();
    console.log(queryParams);

    fetch(`/agency/property?${queryParams}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if(data.message == 'Property inserted successfully') {
            alert('Property added successfully');
            document.getElementById('add_address').value = '';
            document.getElementById('add_city').value = '';
            document.getElementById('add_state').value = '';
            document.getElementById('add_postal_code').value = '';
            document.getElementById('add_size').value = '';
            document.getElementById('add_bedrooms').value = '';
            document.getElementById('add_bathrooms').value = '';
            document.getElementById('add_price').value = '';
            document.getElementById('add_type').value = '';
            document.getElementById('add_description').value = '';
        } else {
            alert('Failed to add property'+ data.detail);
        }
        console.log(data);
    });
});