exam_results = [
{"student_name": "Анна", "score": 91},
{"student_name": "Богдан", "score": 58},
{"student_name": "Вікторія", "score": 75},
{"student_name": "Григорій", "score": 45}
]
passing_score = 60 # Прохідний бал


for result in exam_results:

    if result["score"] >= passing_score:
        result["passed"] = True
    else:
        result["passed"] = False

print(exam_results)