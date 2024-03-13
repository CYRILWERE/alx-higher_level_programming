#!/usr/bin/node

const fs = require('fs');

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destinationPath = process.argv[4];

const fileAContent = fs.readFileSync(fileAPath, 'utf8');
const fileBContent = fs.readFileSync(fileBPath, 'utf8');

const concatenatedContent = `${fileAContent}${fileBContent}`;

fs.writeFileSync(destinationPath, concatenatedContent);

