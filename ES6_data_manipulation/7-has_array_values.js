export default function hasValuesFromArray(set, array) {
  for (var i = 0 ; i < array.length ; i++){
    if (!set.has(array[i])) {
      return false;
    }
  }
  return true;
}
