document.getElementById("predictForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const predictionResult = document.getElementById("predictionResult");
    predictionResult.innerText = "Predicting...";

    const number_of_riders = parseFloat(document.getElementById("riders").value);
    const number_of_drivers = parseFloat(document.getElementById("drivers").value);
    const vehicle_type = document.getElementById("vehicleType").value;
    const Expected_Ride_Duration = parseFloat(document.getElementById("duration").value);

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                number_of_riders,
                number_of_drivers,
                vehicle_type,
                Expected_Ride_Duration
            })
        });

        const data = await response.json();

        if (response.ok && "prediction" in data) {
            predictionResult.innerText = `Adjusted Price: ₹${data.prediction.toFixed(2)}`;
        } else {
            predictionResult.innerText = `Error: ${data.error || "Invalid server response"}`;
        }

    } catch (err) {
        predictionResult.innerText = `Error: ${err.message}`;
    }
});
