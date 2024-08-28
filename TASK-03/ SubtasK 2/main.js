const fs = require('fs');


const inputFilePath = 'input.txt';
const outputFilePath = 'output.txt';

fs.readFile(inputFilePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }

  
    fs.writeFile(outputFilePath, data, (err) => {
        if (err) {
            console.error('Error writing file:', err);
            return;
        }

        console.log('Content successfully copied from ' + inputFilePath + ' to ' + outputFilePath);
    });
});
