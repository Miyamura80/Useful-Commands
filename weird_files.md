# Weird Files

## JSON (Python)

- Saving:
  ```python
  import json
  with open("data_file.json", "w") as f:
      json.dump(data, f, indent=4)
  ```
  NOTE: Not to be confused with `json.dumps(data)` which converts to a string. `indent=4` pretty prints
- Loading
  ```python
  with open("data_file.json", "r") as f:
    data = json.load(f)
  ```
  Similar notes to `json.loads(json_string)` which serializes JSON

## JSON (Javascript)

- Reading:
  ```js
  const fs = require('fs');

  let rawdata = fs.readFileSync('student.json');
  let student = JSON.parse(rawdata);
  console.log(student);
  ```
- Writing:
  ```js  
  const fs = require('fs');

  let student = { 
      name: 'Mike',
      age: 23, 
      gender: 'Male',
      department: 'English',
      car: 'Honda' 
  };

  let data = JSON.stringify(student, null, 2);

  fs.writeFile('student-3.json', data, (err) => {
      if (err) throw err;
      console.log('Data written to file');
  });

  ```
