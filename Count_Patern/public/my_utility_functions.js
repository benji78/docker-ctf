function compter(e) {
    e.preventDefault();
    const text = document.getElementById("texte").value;
    const pattern = document.getElementById("pattern").value;
    const crash_limit = 10000

    if (text.length === 0 || pattern.length === 0) {
        alert("Both the text and pattern fields must be filled out.");
        return;
    }

    if (text.length > crash_limit || pattern.length > crash_limit) {
        document.getElementById("result").textContent = "this_is_too_heavy__i_cannot_count_that";
        return;
    }

    let count = 0, index = 0;
    while (true) {
        const i = text.indexOf(pattern, index);
        if (i === -1) break;
        count++;
        index = i + pattern.length;
    }
    document.getElementById("result").textContent = "Occurrences: " + count;
}

async function fetchCSV() {
    const response = await fetch("./db.csv");
    const text = await response.text();
    const rows = text.trim().split("\n");
    const data = [];
    for (let i = 1; i < rows.length; i++) {
        const [username, password] = rows[i].split(",");
        data.push({ username: username.trim(), password: password.trim() });
    }
    return data;
}

async function login(event) {
    event.preventDefault();
    const msg = document.getElementById("message");
    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;
    const data = await fetchCSV();
    const found = data.find(item => item.username === user);
    if (!found) {
        msg.textContent = "Incorrect credentials.";
        return;
    }
    if (pass === found.password) {
        if (found.username === "admin") {
            sessionStorage.setItem("role", "admin");
            window.location.href = "admin.html";
        } else {
            sessionStorage.setItem("role", "user");
            window.location.href = "user.html";
        }
    } else {
        msg.textContent = "Incorrect credentials.";
    }
}

function logout() {
    sessionStorage.removeItem("role");
    window.location.href = "login.html";
}
