export default function getStudentsByLocation(getListStudents, city) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  return getListStudents.filter(myFunction);

  function myFunction(value, index, array) {
    return value["location"] === city;
  }
}
