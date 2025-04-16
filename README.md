# ANSF_S950_RangoC_LR-DV
Genera la sopraelevazione ferroviaria minima dalla normativa ANSFISA per S=950 Rango C.

Input: File .txt nominato con la velocità massima contenente su ogni riga i dati tabulati della lunghezza della transizione e il raggio della curva.

Output: All'avvio dell'exe vengono aggiunti altre due colonne che rapprensentano la sopraelevazione minima e la velocità massima ammissibile.

Esempio 50.txt:
```
33.350    100.000
22.000    110.000
```
Risultato:
```
33.350    100.000    100    50
22.000    110.000    45    45
```
