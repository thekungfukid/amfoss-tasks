function isPrime(n) {
    if (n <= 1) {
        return false;
    }
    for (let i = 2; i * i <= n; i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

function primeNumbers(n) {
    for (let i = 2; i <= n; i++) {
        if (isPrime(i)) {
            process.stdout.write(i + " ");
        }
    }
    console.log();
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter the No upto which to print Prime Number:", (input) => {
    const n = parseInt(input);
    primeNumbers(n);
    rl.close();
});

