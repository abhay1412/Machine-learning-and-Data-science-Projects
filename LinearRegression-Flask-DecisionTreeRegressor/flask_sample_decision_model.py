from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/")
def welcome():
    #returns 'Welcome to Flask'
    return render_template('index.html')

def ls_prediction(gdp):
    tree_reg = joblib.load("gdp_decision_model.sav")
    prediction = tree_reg.predict([[gdp]])
    return prediction

@app.route('/linear',
           methods=['POST', 'GET'])

def linear():
    if (request.method == 'POST'):
        values = request.form
        print(values)
        country_name = values['Country_Name']
        gdp = values['GDP']
        gdp = int(gdp)
        life_satisfaction = ls_prediction(gdp)

        data = {
            'name':country_name,
            'gdp': gdp,
            'life_satisfaction':life_satisfaction[0][0]

        }
        return  render_template('DecisionTree_reg.html',
                                data = data)

        #return str(life_satisfaction)
        #return render_template('DecisionTree_reg.html')

if __name__ == "__main__":
    app.run()