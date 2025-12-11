'''Problema

Encuesta a 250 alumnos sobre el deporte que practican:
Futbol: 120
Tenis: 22
Handball: 38
Voleibol: 56
Otros: 14
a) Probabilidad de que un alumno practique tenis.
b) Probabilidad de que un alumno no practique tenis.
Resolución

Total alumnos = 120 + 22 + 38 + 56 + 14 = 250
a) P(Tenis) = 22 / 250 = 0.088 = 8.8%
b) P(No tenis) = 1 − 0.088 = 0.912 = 91.2%'''

deportes = {'Futbol':120, 'Tenis':22, 'Handball':38, 'Voleibol':56, 'Otros':14}
total = sum(deportes.values())

p_tenis = deportes['Tenis'] / total
p_no_tenis = 1 - p_tenis

print(f"Total alumnos: {total}")
print(f"P(Tenis) = {p_tenis:.3f} ({p_tenis*100:.1f}%)")
print(f"P(No tenis) = {p_no_tenis:.3f} ({p_no_tenis*100:.1f}%)")