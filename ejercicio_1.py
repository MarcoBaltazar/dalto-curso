#duracion de cursos para aprender loq ue hemos aprendido hasta ahora con dalto
min=1.5
max=7.0
pro=4.0
este=1.5

#sacamos la diferencia de porcentajes con otros cursos

dif_min=100-este/min*100

print(f"El curso de dalto es {dif_min}% mas rapido que el mas rapido")

dif_pro=100-este/pro*100

print(f"El curso de dalto es {dif_pro}% mas rapido que el promedio")

dif_max=100-este/max*100

print(f"El curso de dalto es {round(dif_max,3)}% mas rapido que el mas lento")

print("Cambio xd")