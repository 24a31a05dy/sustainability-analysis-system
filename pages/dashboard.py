<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h1>Sustainability Dashboard 🌱</h1>
<div class="card fade-in">

<input type="number" id="energy" placeholder="Energy">
<input type="number" id="water" placeholder="Water">
<input type="number" id="waste" placeholder="Waste">

<button onclick="predict()">Predict</button>

<h2 id="result"></h2>

<script src="script.js"></script>
</body>
</html>