import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle


df = pd.read_csv("diabetes.csv")

x = df.drop('Outcome', axis = 1)
y = df[['Outcome']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)



lr = LogisticRegression()
model = lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
print(accuracy_score(y_pred, y_test)*100)



# save the model to disk
filename = 'diabetic_lr.model'
pickle.dump(model, open(filename, 'wb'))