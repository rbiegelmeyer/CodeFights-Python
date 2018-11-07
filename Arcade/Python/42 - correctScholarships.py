def correctScholarships(bestStudents, scholarships, allStudents):
    return all(x in scholarships for x in bestStudents) and all(x in allStudents for x in scholarships) and not all(x in scholarships for x in allStudents)

#solução melhor
# def correctScholarships(bestStudents, scholarships, allStudents):
#     return set(bestStudents) <= set(scholarships) < set(allStudents)


bestStudents = [3, 5]
scholarships = [3, 5, 7]
allStudents = [1, 2, 3, 4, 5, 6, 7]
print (correctScholarships(bestStudents,scholarships,allStudents))
#true

bestStudents = [3, 5]
scholarships = [3, 5]
allStudents = [3, 5]
print (correctScholarships(bestStudents,scholarships,allStudents))
#false

bestStudents = [3]
scholarships = [1, 3, 5]
allStudents = [1, 2, 3]
print (correctScholarships(bestStudents,scholarships,allStudents))
#false

bestStudents = [1, 2, 3]
scholarships = [1, 2, 3, 4, 5, 6, 7]
allStudents = [1, 2, 3, 4, 5, 6, 7]
print (correctScholarships(bestStudents,scholarships,allStudents))
#false