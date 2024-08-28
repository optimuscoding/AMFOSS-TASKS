const fs = require('fs');


function generateLine(n, i) {
    return ' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1);
}


function generateDiamond(n) {
    const upperHalf = Array.from({ length: n }, (_, i) => generateLine(n, i));
    const lowerHalf = Array.from({ length: n - 1 }, (_, i) => generateLine(n, n - 2 - i));
    return upperHalf.concat(lowerHalf).join('\n');
}


function main() {
  
    fs.readFile('input.txt', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading input file:', err);
            return;
        }

        const n = parseInt(data.trim(), 10);

        if (isNaN(n) || n <= 0) {
            console.error('Invalid number in input.txt. Please ensure it is a positive integer.');
            return;
        }

     
        const diamond = generateDiamond(n);

      
        fs.writeFile('output.txt', diamond, (err) => {
            if (err) {
                console.error('Error writing to output file:', err);
                return;
            }

            console.log('Diamond pattern written to output.txt');
        });
    });
}


main();

