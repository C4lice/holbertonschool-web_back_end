export default function updateUniqueItems(itemmap) {
  itemmap.forEach ((value, key) => {
    if (value === 1) {
      itemmap.set(key, 100);
    }
  })
  return itemmap;
}
