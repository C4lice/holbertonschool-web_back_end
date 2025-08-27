export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  return getListStudents.filter(getByLoc).map(myFunction);

  function getByLoc(value, index, array) {
    return value["location"] === city;
  }

  function myFunction(value) {
    var grade = 'N/A';
    newGrades.forEach(idGrade => {
      if(idGrade['studentId'] === value['id']) {
        grade = idGrade['grade'];
      }
    });
    return {
      ...value,
      grade,
    };
  }
}
