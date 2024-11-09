/**
 * find the Minimun excluded (Mex) non negative number that is not in the array.
 * Solution:
 *  Sort the array, find the gap in the array and return it
 * @param {*} arr
 * @returns the mex
 */
function findTheMex(arr) {
  const sortedArray = arr.sort((a, b) => a - b);
  if (sortedArray.length === 0 || sortedArray[0] != 0) {
    return 0;
  }
  const gap = sortedArray.find((value, idx, arr) => {
    if (value < 0) {
      return false;
    }
    return arr[idx + 1] - value > 1;
  });
  if (!gap) {
    return 0;
  }
  return gap + 1;
}

const mex = findTheMex([0, 1, 2, 3, -100, -200]);
console.log("mex", mex);
