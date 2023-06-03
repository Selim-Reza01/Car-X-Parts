const fs = require("fs");

let dataArr = [];

fs.readFile("./names.txt", (err, data) => {
  if (err) throw err;
  let dataFromFile = data.toString();
  dataArr = dataFromFile.split("\n");
  // console.log(dataArr);
  dataArr.map((val) => {
    let value = val.trim();
    let categoryArr = val.split("_");
    let placeholder = categoryArr[0]
      .concat("_")
      .concat(categoryArr[1])
      .concat(".jpg");
    if (val !== "") {
      fs.copyFile(
        `./placeholder/${placeholder}`,
        `./placeholder/copied-images/${value}`,
        (err) => {
          if (err) throw err;
        }
      );
    }
  });
});
