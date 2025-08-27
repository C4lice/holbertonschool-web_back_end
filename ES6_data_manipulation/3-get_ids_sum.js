export default function getStudentIdsSum(getListStudents) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  return getListStudents.reduce(myFunction, 0);

  function myFunction(total, value, index, array) {
    return total + value['id'];
  } 
}
