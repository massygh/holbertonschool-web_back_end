import taskBlock from './1-block-scoped.js';

console.log(taskBlock(true));  // Expected output: [ false, true ]
console.log(taskBlock(false)); // Expected output: [ false, true ]