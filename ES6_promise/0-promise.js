export default function getResponseFromAPI() {
    const name = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("toto");
  }, 100);
});
    return name;
}
