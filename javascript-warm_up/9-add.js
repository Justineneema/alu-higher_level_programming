#!/usr/bin/node
function add (a, b) {
    console.log(a + b);
}
add(parsetInt(ProcessingInstruction.argv[2]), parseInt(ProcessingInstruction.argv[3]));
