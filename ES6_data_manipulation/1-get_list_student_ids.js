export default function getListStudentIds(listObject) {
  if (!Array.isArray(listObject)) {
    return [];
  }
  return listObject.map(myFunction);

  function myFunction(value) {
    return value["id"];
  }
}
