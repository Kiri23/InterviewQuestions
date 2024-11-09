function findTheMex(arr) {
  const sortedArray = arr.sort((a, b) => a - b);
  console.log("arr sorted", sortedArray);
  if (sortedArray.length === 0 || sortedArray[0] != 0) {
    return 0;
  }
  const gap = sortedArray.find((value, idx, arr) => {
    if (value < 0) {
      return;
    }
    console.log("value", value);
    console.log(arr[idx + 1]);
    return arr[idx + 1] - value > 1;
  });
  if (!gap) {
    return 0;
  }
  return gap + 1;
}

// sort , find the minimun - encuentra el gap despues del sort
// pero tienes que skipear los negativos
const mex = findTheMex([0, 1, 2, 3, -100, -200]);
console.log("mex", mex);
