exam_score = float(input("nota examen: "))
clases_totales = 50
class_attendance = float(input("clases a las que se ha atendido: "))
if  exam_score >=70 and class_attendance >=(80/100*clases_totales): 
 print(" Has aprobado, sal de casa.")
else : print("No aprobaste, vete de la carrera, no sirves para esto.")