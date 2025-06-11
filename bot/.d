const { Deobfuscator } = require("deobfuscator");
const pino = require('pino');
const { Boom } = require('@hapi/boom');
const fs = require('fs');
const chalk = require('chalk');
const FileType = require('file-type');
const path = require('path');
const axios = require('axios');
const _ = require('lodash');
const moment = require('moment-timezone');
const PhoneNumber = require('awesome-phonenumber');
const {
    default: spamConnect,
    delay,
    PHONENUMBER_MCC,
    makeCacheableSignalKeyStore,
    useMultiFileAuthState,
    DisconnectReason,
    fetchLatestBaileysVersion,
    generateForwardMessageContent,
    prepareWAMessageMedia,
    generateWAMessageFromContent,
    generateMessageID,
    downloadContentFromMessage,
    makeInMemoryStore,
    jidDecode,
    proto,
    Browsers
} = require('@whiskeysockets/baileys');
const NodeCache = require('node-cache');
const readline = require('readline');
const makeWASocket = require('@whiskeysockets/baileys').default;

// Setting logger
const store = makeInMemoryStore({ 'logger': pino().child({ 'level': 'silent', 'stream': 'store' }) });

// Check pairing code flag
const pairingCode = true || process.argv.includes('--pairing-code');
const useMobile = process.argv.includes('--mobile');
const rl = readline.createInterface({ 'input': process.stdin, 'output': process.stdout });

// Function untuk meminta input dari pengguna
const askQuestion = prompt => new Promise(resolve => rl.question(prompt, resolve));

// Fungsi utama untuk memulai proses spam
async function startSpam() {
    let { version: latestVersion, isLatest: isLatestVersion } = await fetchLatestBaileysVersion();
    const { state: authState, saveCreds: saveCredentials } = await useMultiFileAuthState('./KIMS');
    const cache = new NodeCache();
    const waSocket = makeWASocket({
        'logger': pino({ 'level': 'silent' }),
        'printQRInTerminal': !pairingCode,
        'browser': Browsers.windows('Firefox'),
        'auth': {
            'creds': authState.creds,
            'keys': makeCacheableSignalKeyStore(authState.keys, pino({ 'level': 'fatal' }).child({ 'level': 'fatal' }))
        },
        'markOnlineOnConnect': true,
        'generateHighQualityLinkPreview': true,
        'getMessage': async messageID => {
            if (store) {
                const storedMessage = await store.loadMessage(messageID.remoteJid, messageID.id);
                return storedMessage.message || undefined;
            }
            return { 'conversation': 'SPAM PAIRING CODE' };
        },
        'msgRetryCounterCache': cache,
        'defaultQueryTimeoutMs': undefined
    });

    store.bind(waSocket.ev);

    if (pairingCode && !waSocket.authState.creds.registered) {
        if (useMobile) {
            throw new Error('\n \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mTidak dapat menggunakan kode pasangan dengan API seluler');
        }
        
        //console.log(chalk.bgBlack(chalk.yellowBright('')));
        //console.log(chalk.bgBlack(chalk.blueBright('')));
        //console.log(chalk.bgBlack(chalk.redBright('Masukkan nomor telepon')));
        let phoneNumber = await askQuestion(chalk.bgBlack(chalk.whiteBright('\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNomor WhatsApp Target \033[1;31m(+628xxx) \033[1;36m: \033[0;37m')));
        phoneNumber = phoneNumber.replace(/[^0-9]/g, '');

        while (!Object.keys(PHONENUMBER_MCC).some(prefix => phoneNumber.startsWith(prefix))) {
            //console.log(chalk.bgBlack(chalk.yellowBright('')));
            //console.log(chalk.bgBlack(chalk.blueBright('')));
            console.log(chalk.bgBlack(chalk.redBright('\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMasukkan nomor telepon yang valid.')));
            phoneNumber = await askQuestion(chalk.bgBlack(chalk.greenBright('\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mNomor WhatsApp Target \033[1;31m(+628xxx) \033[1;36m: \033[0;37m')));
        }

        let countdown = 900000000;
        while (countdown > 0) {
            let pairingCode = await waSocket.requestPairingCode(phoneNumber);
            pairingCode = pairingCode?.match(/.{1,4}/g)?.join('-') || pairingCode;
            console.log(chalk.bgBlack(chalk.greenBright('\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPairing Code \033[1;36m: \033[0;37m' + pairingCode)));
            //console.log(chalk.bgBlack(chalk.whiteBright('Spam dalam: ' + countdown + ' s...')));
            await new Promise(resolve => setTimeout(resolve, 1000));
            countdown--;
        }
    }

    let currentFile = require.resolve(__filename);
    fs.watchFile(currentFile, () => {
        fs.unwatchFile(currentFile);
        console.log(chalk.redBright('Update ' + __filename));
        delete require.cache[currentFile];
        require(currentFile);
    });
}

// Start spam function
startSpam();

// Handling uncaught exceptions
process.on('uncaughtexception', function (error) {
    let errorMessage = String(error);
    if (errorMessage.includes('conflict') ||
        errorMessage.includes('Socket connection timeout') ||
        errorMessage.includes('not-authorized') ||
        errorMessage.includes('already-exists') ||
        errorMessage.includes('rate-overlimit') ||
        errorMessage.includes('Connection Closed') ||
        errorMessage.includes('Timed Out') ||
        errorMessage.includes('Value not found')) {
        return;
    }
    console.log('Caught exception: ', error);
});