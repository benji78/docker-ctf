const express = require("express");
const path = require("path");
const { exec } = require("child_process");
const fs = require("fs");
const md5 = require("md5");

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

const sessions = {};
const adminFlag = "flag{no_way_you_find_the_admin_password__take_your_flag}";

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "login.html"));
});

app.post("/login", async (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) {
        return res.status(400).send({ success: false, error: "Username and password must be provided." });
    }
    try {
        const users = await fetchCSV();
        const user = users.find((item) => item.username === username);
        if (!user || user.password !== md5(password)) {
            return res.status(401).send({ success: false });
        }
        const sessionId = Math.random().toString(36).substring(2);
        sessions[sessionId] = { username, role: username === "admin" ? "admin" : "user" };
        res.send({ success: true, role: sessions[sessionId].role, sessionId });
    } catch (error) {
        res.status(500).send({ success: false, error: "Server error" });
    }
});

app.post("/get-admin-flag", (req, res) => {
    const { sessionId } = req.body;
    if (!sessionId || !sessions[sessionId] || sessions[sessionId].role !== "admin") {
        return res.status(403).send({ success: false, error: "Forbidden" });
    }
    res.send({ success: true, flag: adminFlag });
});

app.post("/compter", (req, res) => {
    const { text, pattern } = req.body;
    if (!text || !pattern) {
        return res.status(400).send({ error: "Both text and pattern must be provided." });
    }
    const result = countOccurrences(text, pattern);
    res.send({ result });
});

app.get("/user.html", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "user.html"));
});

function countOccurrences(text, pattern) {
    const crash_limit = 10000;
    if (text.length > crash_limit || pattern.length > crash_limit) {
        return "flag{this_is_too_heavy__i_cannot_count_that}";
    }
    let count = 0, index = 0;
    while (true) {
        const i = text.indexOf(pattern, index);
        if (i === -1) break;
        count++;
        index = i + pattern.length;
    }
    return `Occurrences: ${count}`;
}

async function fetchCSV() {
    const csvPath = path.join(__dirname, "public", "db.csv");
    const data = fs.readFileSync(csvPath, "utf8").trim();
    const rows = data.split("\n");
    const result = [];
    for (let i = 1; i < rows.length; i++) {
        const [username, password] = rows[i].split(",");
        result.push({ username: username.trim(), password: password.trim() });
    }
    return result;
}

const PORT = 3000;
app.listen(PORT, () => {
    const url = `http://localhost:${PORT}`;
    switch (process.platform) {
        case "win32":
            exec(`start ${url}`);
            break;
        case "darwin":
            exec(`open ${url}`);
            break;
        default:
            exec(`xdg-open ${url}`);
            break;
    }
    console.log(`Server running at ${url}`);
});
