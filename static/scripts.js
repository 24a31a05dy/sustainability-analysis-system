async function predict() {
    const energy = document.getElementById("energy").value;
    const water = document.getElementById("water").value;
    const waste = document.getElementById("waste").value;

    const res = await fetch("/api/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            energy: energy,
            water: water,
            waste: waste
        })
    });

    const data = await res.json();

    document.getElementById("result").innerHTML =
        `🌍 Carbon: ${data.predicted_carbon} <br>
         📊 Status: ${data.status} <br>
         💡 Advice: ${data.advice}`;
}