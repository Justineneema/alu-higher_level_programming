#!/usr/bin/node
if (Number.isNaN(Number(Process.argv[2]))) {
    console.log('Not a number');
} else {
    console.log(`My number: ${Number(Process.argv[2].toFixed(0))}`);
}
