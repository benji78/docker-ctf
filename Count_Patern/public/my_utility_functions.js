/**
 * Implémentation de MD5 en JavaScript
 * Fait par l'ia, je n'arrivais pas a faire fonctionnée les hashage importé
 */
function md5(string) {
    function cmn(q, a, b, x, s, t) {
        a = add32(add32(a, q), add32(x, t));
        return add32((a << s) | (a >>> (32 - s)), b);
    }
    function ff(a, b, c, d, x, s, t) {
        return cmn((b & c) | (~b & d), a, b, x, s, t);
    }
    function gg(a, b, c, d, x, s, t) {
        return cmn((b & d) | (c & ~d), a, b, x, s, t);
    }
    function hh(a, b, c, d, x, s, t) {
        return cmn(b ^ c ^ d, a, b, x, s, t);
    }
    function ii(a, b, c, d, x, s, t) {
        return cmn(c ^ (b | ~d), a, b, x, s, t);
    }
    function md5cycle(state, block) {
        var a = state[0],
            b = state[1],
            c = state[2],
            d = state[3];

        a = ff(a, b, c, d, block[0], 7, -680876936);
        d = ff(d, a, b, c, block[1], 12, -389564586);
        c = ff(c, d, a, b, block[2], 17, 606105819);
        b = ff(b, c, d, a, block[3], 22, -1044525330);
        a = ff(a, b, c, d, block[4], 7, -176418897);
        d = ff(d, a, b, c, block[5], 12, 1200080426);
        c = ff(c, d, a, b, block[6], 17, -1473231341);
        b = ff(b, c, d, a, block[7], 22, -45705983);
        a = ff(a, b, c, d, block[8], 7, 1770035416);
        d = ff(d, a, b, c, block[9], 12, -1958414417);
        c = ff(c, d, a, b, block[10], 17, -42063);
        b = ff(b, c, d, a, block[11], 22, -1990404162);
        a = ff(a, b, c, d, block[12], 7, 1804603682);
        d = ff(d, a, b, c, block[13], 12, -40341101);
        c = ff(c, d, a, b, block[14], 17, -1502002290);
        b = ff(b, c, d, a, block[15], 22, 1236535329);

        a = gg(a, b, c, d, block[1], 5, -165796510);
        d = gg(d, a, b, c, block[6], 9, -1069501632);
        c = gg(c, d, a, b, block[11], 14, 643717713);
        b = gg(b, c, d, a, block[0], 20, -373897302);
        a = gg(a, b, c, d, block[5], 5, -701558691);
        d = gg(d, a, b, c, block[10], 9, 38016083);
        c = gg(c, d, a, b, block[15], 14, -660478335);
        b = gg(b, c, d, a, block[4], 20, -405537848);
        a = gg(a, b, c, d, block[9], 5, 568446438);
        d = gg(d, a, b, c, block[14], 9, -1019803690);
        c = gg(c, d, a, b, block[3], 14, -187363961);
        b = gg(b, c, d, a, block[8], 20, 1163531501);
        a = gg(a, b, c, d, block[13], 5, -1444681467);
        d = gg(d, a, b, c, block[2], 9, -51403784);
        c = gg(c, d, a, b, block[7], 14, 1735328473);
        b = gg(b, c, d, a, block[12], 20, -1926607734);

        a = hh(a, b, c, d, block[5], 4, -378558);
        d = hh(d, a, b, c, block[8], 11, -2022574463);
        c = hh(c, d, a, b, block[11], 16, 1839030562);
        b = hh(b, c, d, a, block[14], 23, -35309556);
        a = hh(a, b, c, d, block[1], 4, -1530992060);
        d = hh(d, a, b, c, block[4], 11, 1272893353);
        c = hh(c, d, a, b, block[7], 16, -155497632);
        b = hh(b, c, d, a, block[10], 23, -1094730640);
        a = hh(a, b, c, d, block[13], 4, 681279174);
        d = hh(d, a, b, c, block[0], 11, -358537222);
        c = hh(c, d, a, b, block[3], 16, -722521979);
        b = hh(b, c, d, a, block[6], 23, 76029189);
        a = hh(a, b, c, d, block[9], 4, -640364487);
        d = hh(d, a, b, c, block[12], 11, -421815835);
        c = hh(c, d, a, b, block[15], 16, 530742520);
        b = hh(b, c, d, a, block[2], 23, -995338651);

        a = ii(a, b, c, d, block[0], 6, -198630844);
        d = ii(d, a, b, c, block[7], 10, 1126891415);
        c = ii(c, d, a, b, block[14], 15, -1416354905);
        b = ii(b, c, d, a, block[5], 21, -57434055);
        a = ii(a, b, c, d, block[12], 6, 1700485571);
        d = ii(d, a, b, c, block[3], 10, -1894986606);
        c = ii(c, d, a, b, block[10], 15, -1051523);
        b = ii(b, c, d, a, block[1], 21, -2054922799);
        a = ii(a, b, c, d, block[8], 6, 1873313359);
        d = ii(d, a, b, c, block[15], 10, -30611744);
        c = ii(c, d, a, b, block[6], 15, -1560198380);
        b = ii(b, c, d, a, block[13], 21, 1309151649);
        a = ii(a, b, c, d, block[4], 6, -145523070);
        d = ii(d, a, b, c, block[11], 10, -1120210379);
        c = ii(c, d, a, b, block[2], 15, 718787259);
        b = ii(b, c, d, a, block[9], 21, -343485551);

        state[0] = add32(state[0], a);
        state[1] = add32(state[1], b);
        state[2] = add32(state[2], c);
        state[3] = add32(state[3], d);
    }

    function md5blk(s) {
        var md5blks = [];
        for (var i = 0; i < 64; i += 4) {
            md5blks[i >> 2] = s.charCodeAt(i) +
                (s.charCodeAt(i + 1) << 8) +
                (s.charCodeAt(i + 2) << 16) +
                (s.charCodeAt(i + 3) << 24);
        }
        return md5blks;
    }

    function md51(s) {
        var n = s.length,
            state = [1732584193, -271733879, -1732584194, 271733878],
            i;
        for (i = 64; i <= n; i += 64) {
            md5cycle(state, md5blk(s.substring(i - 64, i)));
        }
        s = s.substring(i - 64);
        var tail = Array(16).fill(0);
        for (i = 0; i < s.length; i++) {
            tail[i >> 2] |= s.charCodeAt(i) << ((i % 4) * 8);
        }
        tail[i >> 2] |= 0x80 << ((i % 4) * 8);
        if (i > 55) {
            md5cycle(state, tail);
            tail = Array(16).fill(0);
        }
        tail[14] = n * 8;
        md5cycle(state, tail);
        return state;
    }

    function rhex(n) {
        var s = '',
            j;
        for (j = 0; j < 4; j++) {
            s += ('0' + ((n >> (j * 8)) & 0xFF).toString(16)).slice(-2);
        }
        return s;
    }

    function hex(x) {
        for (var i = 0; i < x.length; i++) {
            x[i] = rhex(x[i]);
        }
        return x.join('');
    }

    function add32(a, b) {
        return (a + b) & 0xFFFFFFFF;
    }

    return hex(md51(string));
}

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

function logout() {
    sessionStorage.removeItem("role");
    window.location.href = "login.html";
}


async function login(event) {
    event.preventDefault();
    const msg = document.getElementById("message");
    const user = document.getElementById("username").value;
    const password = md5(document.getElementById("password").value);
    const data = await fetchCSV();
    const found = data.find(item => item.username === user);
    const wrongPassword = "Password or username is incorrect. Please try again. Password can only contain numbers and have max 6 characters."
    if (!found) {
        msg.textContent = wrongPassword;
        return;
    }
    if (password === found.password) {
        if (found.username === "admin") {
            sessionStorage.setItem("role", "admin");
            window.location.href = "admin.html";
        } else {
            sessionStorage.setItem("role", "user");
            window.location.href = "user.html";
        }
    } else {
        msg.textContent = wrongPassword;
    }
}
