export default function setFromArray(value) {
  const set = new Set();
  value.forEach(element => {
    set.add(element);
  });
  return set;
}
