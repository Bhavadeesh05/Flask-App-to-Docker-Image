import numpy as np
import pickle
from flask import Flask, request, render_template

model = pickle.load(open('model.pkl', 'rb')) 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('data_form.html')

@app.route('/predict', methods =['POST'])
def predict():
    
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    prediction = model.predict(array_features)
    
    output = prediction
    
    if output == 1:
        return render_template('result1.html')
    else:
        return render_template('result2.html')

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=8000)
    
    