<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login | Sustainability System</title>
    <link rel="stylesheet" href="style.css">

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap" rel="stylesheet">
</head>
<body>

<div class="container">
    <div class="card">
        <h2>Welcome Back </h2>
        <p class="subtitle">Login to your account</p>

        <div class="input-group">
            <input type="text" id="username" required>
            <label>Username</label>
        </div>

        <div class="input-group">
            <input type="password" id="password" required>
            <label>Password</label>
            <span class="toggle" onclick="togglePassword()"></span>
        </div>

        <button onclick="login()">Login</button>

        <p class="bottom-text">
            "Don't have an account?"
            <a href="register.html">Register</a>
        </p>
    </div>
</div>

<script src="script.js"></script>

<script>
//  Show/Hide Password
function togglePassword() {
    const pwd = document.getElementById("password");
    pwd.type = pwd.type === "password" ? "text" : "password";
}
</script>

</body>
</html>