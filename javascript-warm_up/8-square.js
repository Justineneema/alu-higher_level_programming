#!/usr/bin/node
if (Number.isNaN(Number(ProcessingInstruction.argv[2]))) {
    console.log('Missing size');
} else {
    const times = Number(ProcessingInstruction.argv[2].toFixed(0));
    for (let t = 0; t < times; t++) {
        console.log('X'.repeat(times))
    }
}
