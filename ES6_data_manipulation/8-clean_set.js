export default function cleanSet(set, startString) {
  if (!startString || startString.length === 0) {
    return '';
  }

  let start = true;
  let text = [];
  
  for (const value of set) {
    if (typeof value === 'string') {
      if (value.indexOf(startString) === 0) {
        if (start) {
          text += value.substring(startString.length);
          start = false;
        } else {
          text += `-${value.substring(startString.length)}`;
        }
      }
    }
  }
  return text;
}
