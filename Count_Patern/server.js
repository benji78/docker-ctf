const express = require("express");
const path = require("path");
const { exec } = require("child_process");

const app = express();

app.use((req, res, next) => {
    if (req.url.endsWith(".js")) {
        res.status(403).send("403 Access denied");
    } else {
        next();
    }
});

app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

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
    console.log(`Server running on ${url}`);
});
