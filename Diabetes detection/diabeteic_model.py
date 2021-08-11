import pandas as pd
from tkinter import *
import sklearn
import tkinter as tk
import pickle


# Load the dataset
def predict():
    DF = pd.DataFrame(columns=['Preg', 'Plas', 'Pres', 'skin', 'test', 'mass', 'pedi', 'age'], )
    PREG = Preg_var.get()
    DF.loc[0, 'Preg'] = PREG
    PLAS = Plas_var.get()
    DF.loc[0, 'Plas'] = PLAS
    PRES = Pres_var.get()
    DF.loc[0, 'Pres'] = PRES
    SKIN = skin_var.get()
    DF.loc[0, 'skin'] = SKIN
    TEST = test_var.get()
    DF.loc[0, 'test'] = TEST
    MASS = mass_var.get()
    DF.loc[0, 'mass'] = MASS
    PEDI = pedi_var.get()
    DF.loc[0, 'pedi'] = PEDI
    AGE = age_var.get()
    DF.loc[0, 'age'] = AGE

    output = model.predict(DF)
    if output == 1:
        result = 'Diabetic'
        predict_screen.insert(END, result)
    else:
        result = 'Non-Diabetic'
        predict_screen.insert(END, result)

    print(result)

model = pickle.load(open('Diabetic_lr.model', 'rb'))

win = tk.Tk()
win.title('Diabetes Prediction')

# Column 1
Preg = tk.Label(win, text="Preg")
Preg.grid(row=0, column=0, sticky=tk.W)
Preg_var = tk.DoubleVar()
Preg_entrybox = tk.Entry(win, width=16, textvariable=Preg_var)
Preg_entrybox.grid(row=0, column=2)
# Column 2
Plas = tk.Label(win, text="Plas")
Plas.grid(row=1, column=0, sticky=tk.W)
Plas_var = tk.DoubleVar()
Plas_entrybox = tk.Entry(win, width=16, textvariable=Plas_var)
Plas_entrybox.grid(row=1, column=2)
# Column 3
Pres = tk.Label(win, text="Pres")
Pres.grid(row=2, column=0, sticky=tk.W)
Pres_var = tk.DoubleVar()
Pres_entrybox = tk.Entry(win, width=16, textvariable=Pres_var)
Pres_entrybox.grid(row=2, column=2)
# Column 4
skin = tk.Label(win, text="skin")
skin.grid(row=3, column=0, sticky=tk.W)
skin_var = tk.DoubleVar()
skin_entrybox = tk.Entry(win, width=16, textvariable=skin_var)
skin_entrybox.grid(row=3, column=2)
# Column 5
test = tk.Label(win, text="test")
test.grid(row=4, column=0, sticky=tk.W)
test_var = tk.DoubleVar()
test_entrybox = tk.Entry(win, width=16, textvariable=test_var)
test_entrybox.grid(row=4, column=2)
# Column 6
mass = tk.Label(win, text="mass")
mass.grid(row=5, column=0, sticky=tk.W)
mass_var = tk.DoubleVar()
mass_entrybox = tk.Entry(win, width=16, textvariable=mass_var)
mass_entrybox.grid(row=5, column=2)
# Column 7
pedi = tk.Label(win, text="pedi")
pedi.grid(row=6, column=0, sticky=tk.W)
pedi_var = tk.DoubleVar()
pedi_entrybox = tk.Entry(win, width=16, textvariable=pedi_var)
pedi_entrybox.grid(row=6, column=2)
# Column 8
age = tk.Label(win, text="age")
age.grid(row=7, column=0, sticky=tk.W)
age_var = tk.DoubleVar()
age_entrybox = tk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=7, column=2)

predict_button = tk.Button(win, text="Predict", command=predict)
predict_button.grid(row=9, column=0)

predict_screen = tk.Text(win,height=10, width=20)
predict_screen.grid(row=9, column=2)

win.mainloop()