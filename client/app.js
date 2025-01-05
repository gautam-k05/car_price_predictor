document.addEventListener("DOMContentLoaded", () => {
    fetchBrands();
    enableForm();
});

// Function to fetch car brands from Flask API
function fetchBrands() {
    const brandSelect = document.getElementById("brand");

    fetch("https://car-price-prediction-10fw.onrender.com/get_brands")
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to fetch brands");
            }
            return response.json();
        })
        .then(data => {
            if (data.brands && data.brands.length > 0) {
                data.brands.forEach(brand => {
                    const option = document.createElement("option");
                    option.value = brand;
                    option.textContent = brand;
                    brandSelect.appendChild(option);
                });
            } else {
                console.error("No brands found");
            }
        })
        .catch(error => {
            console.error("Error fetching brands:", error);
            alert("Failed to load brands. Please try again later.");
        });
}

// Function to enable the form once brands are loaded
function enableForm() {
    fetch("https://car-price-prediction-10fw.onrender.com/get_brands")
        .then(response => response.json())
        .then(() => {
            document.querySelector("button[type='submit']").disabled = false;
        })
        .catch(error => {
            console.error("Error enabling form:", error);
        });
}

// Function to handle price prediction
function onEstimatePrice(event) {
    event.preventDefault();  // Prevent form submission

    const brand = document.getElementById("brand").value;
    const year = document.getElementById("year").value;
    const kmDriven = document.getElementById("km_driven").value;
    const mileage = document.getElementById("mileage").value;
    const fuel = document.querySelector("input[name='fuel']:checked").value;
    const transmission = document.querySelector("input[name='transmission']:checked").value;

    if (!brand) {
        alert("Please select a car brand");
        return;
    }

    // Make POST request to predict price
    fetch("https://car-price-prediction-10fw.onrender.com/predict_price", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
            brand,
            year,
            km_driven: kmDriven,
            milage: mileage,
            fuel,
            transmission
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Prediction failed");
        }
        return response.json();
    })
    .then(data => {
        const resultBox = document.getElementById("predictedPrice");
        resultBox.textContent = `Estimated Price: ₹${data.predicted_price} Lakhs`;
        setTimeout(() => {
            document.getElementById("result").scrollIntoView({ behavior: 'smooth' });
        }, 300);  // 300ms delay
    })
    .catch(error => {
        console.error("Error predicting price:", error);
        document.getElementById("predictedPrice").textContent = "Prediction failed. Please try again.";
    });
}
