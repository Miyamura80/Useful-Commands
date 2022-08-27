# NodeJS

### Making quick js scripts:
1. `echo "" > script.js`
2. `code script.js`
3. `node script.js`

## Having Async Scripts
```js
const fs = require('fs').promises;

(async () => {
    const txt = await fs.readFile('test.txt', 'utf-8');
    console.log(txt);
})();
```


