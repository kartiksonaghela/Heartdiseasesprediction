import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle


def cal(x, y):
    if (y == 1):
        x = 'slope_of_peak_exercise_st_segment_' + x
        dict1 = {'slope_of_peak_exercise_st_segment_1': 0, 'slope_of_peak_exercise_st_segment_2': 0,
                 'slope_of_peak_exercise_st_segment_3': 0}
        if x in dict1:
            dict1[x] = 1
    elif (y == 2):
        x= 'thal_' + x
        dict1 = {'thal_fixed_defect': 0, 'thal_normal': 0, 'thal_reversible_defect': 0}
        if x in dict1:
            dict1[x] = 1
    elif (y == 3):
        x = 'chest_pain_type_' + x
        dict1 = {'chest_pain_type_1': 0, 'chest_pain_type_2': 0,'chest_pain_type_3':0,'chest_pain_type_4':0}
        if x in dict1:
            dict1[x] = 1
    elif (y == 4):
        x = 'exercise_induced_angina_' + x
        dict1 = {'exercise_induced_angina_0': 0,
                 'exercise_induced_angina_1': 0}
        if x in dict1:
            dict1[x] = 1
    elif (y == 5):
        x = 'num_major_vessels_' + x
        dict1 = {'num_major_vessels_0': 0,
                 'num_major_vessels_1': 0, 'num_major_vessels_2': 0,
                 'num_major_vessels_3': 0}
        if x in dict1:
            dict1[x] = 1
    elif (y == 6):
        x='fasting_blood_sugar_gt_120_mg_per_dl_'+x
        dict1 = {'fasting_blood_sugar_gt_120_mg_per_dl_0': 0, 'fasting_blood_sugar_gt_120_mg_per_dl_1': 0}
        if x in dict1:
            dict1[x] = 1
    elif (y == 7):
        x='resting_ekg_results_'+x
        dict1 = {'resting_ekg_results_0': 0, 'resting_ekg_results_1': 0,'resting_ekg_results_2':0}
        if x in dict1:
            dict1[x] = 1
    elif(y==8):
        if(x=='male'):
            dict1={'sex_0':0,'sex_1':1}
        else:
            dict1 = {'sex_0': 1, 'sex_1': 0}
    elif(y==9):
        x=int(x)
        dict1={'age_(28.952, 38.6]':0,'age_(38.6, 48.2]':0,'age_(48.2, 57.8]':0,'age_(57.8, 67.4]':0,
               'age_(67.4, 77.0]':0}
        if 28.952 < x <= 38.6:
            dict1['age_(28.952, 38.6]']=1
        if  38.6<x<= 48.2:
            dict1['age_(38.6, 48.2]']=1
        if 48.2<x<= 57.8:
            dict1['age_(48.2, 57.8]']=1
        if 57.8 <x<=67.4:
            dict1['age_(57.8, 67.4]']=1
        if 67.4<x<= 77.0:
            dict1['age_(67.4, 77.0]']=1
    elif(y==10):
        x = int(x)
        dict1={'resting_blood_pressure_(93.914, 108.333]':0,'resting_blood_pressure_(108.333, 122.667]':0,
               'resting_blood_pressure_(122.667, 137.0]':0,'resting_blood_pressure_(137.0, 151.333]':0,
               'resting_blood_pressure_(151.333, 165.667]':0,'resting_blood_pressure_(165.667, 180.0]':0}
        if 93.914<x<= 108.333:
            dict1['resting_blood_pressure_(93.914, 108.333]']=1
        if 108.333<x<= 122.667:
            dict1['resting_blood_pressure_(108.333, 122.667]']=1
        if 122.667<x<= 137.0:
            dict1['resting_blood_pressure_(122.667, 137.0]']=1
        if 137.0<x<= 151.333:
            dict1['resting_blood_pressure_(137.0, 151.333]']=1
        if 151.333<x<= 165.667:
            dict1['resting_blood_pressure_(151.333, 165.667]']=1
        if 165.667<x<= 180.0:
            dict1['resting_blood_pressure_(165.667, 180.0]']=1
    elif(y==11):
        x = int(x)
        dict1 = {'serum_cholesterol_mg_per_dl_(125.562, 213.6]': 0,
                 'serum_cholesterol_mg_per_dl_(213.6, 301.2]': 0,
                 'serum_cholesterol_mg_per_dl_(301.2, 388.8]': 0,
                 'serum_cholesterol_mg_per_dl_(388.8, 476.4]': 0,
                 'serum_cholesterol_mg_per_dl_(476.4, 564.0]': 0}
        if 125.562<x<= 213.6:
            dict1['serum_cholesterol_mg_per_dl_(125.562, 213.6]']=1
        if 213.6<x<= 301.2:
            dict1['serum_cholesterol_mg_per_dl_(213.6, 301.2]']=1
        if 301.2<x<= 388.8:
            dict1['serum_cholesterol_mg_per_dl_(301.2, 388.8]']=1
        if 388.8<x<= 476.4:
            dict1['serum_cholesterol_mg_per_dl_(388.8, 476.4]']=1
        if 476.4<x<= 564.0:
            dict1['serum_cholesterol_mg_per_dl_(476.4, 564.0]']=1
    elif(y==12):
        x=int(x)
        dict1={'max_heart_rate_achieved_(95.894, 117.2]':0,'max_heart_rate_achieved_(117.2, 138.4]':0,
               'max_heart_rate_achieved_(138.4, 159.6]':0,'max_heart_rate_achieved_(159.6, 180.8]':0,
               'max_heart_rate_achieved_(180.8, 202.0]':0}
        if 95.894<x<= 117.2:
            dict1['max_heart_rate_achieved_(95.894, 117.2]']=1
        if 117.2<x<= 138.4:
            dict1['max_heart_rate_achieved_(117.2, 138.4]']=1
        if 138.4<x<= 159.6:
            dict1['max_heart_rate_achieved_(138.4, 159.6]']=1
        if 159.6<x<= 180.8:
            dict1['max_heart_rate_achieved_(159.6, 180.8]']=1
        if 180.8>x<= 202.0:
            dict1['max_heart_rate_achieved_(180.8, 202.0]']=1


    else:
        x = int(x)
        dict1 = {'oldpeak_eq_st_depression_(-0.0062, 0.689]':0,'oldpeak_eq_st_depression_(0.689, 1.378]':0,
                 'oldpeak_eq_st_depression_(1.378, 2.067]':0,'oldpeak_eq_st_depression_(2.067, 2.756]':0,
                 'oldpeak_eq_st_depression_(2.756, 3.444]':0,'oldpeak_eq_st_depression_(3.444, 4.133]':0,
                 'oldpeak_eq_st_depression_(4.133, 4.822]':0,'oldpeak_eq_st_depression_(4.822, 5.511]':0,
                 'oldpeak_eq_st_depression_(5.511, 6.2]':0}
        if -0.0062<x<= 0.689:
            dict1['oldpeak_eq_st_depression_(-0.0062, 0.689]']=1
        if 0.689<x<= 1.378:
            dict1['oldpeak_eq_st_depression_(0.689, 1.378]']=1
        if 1.378<x<= 2.067:
            dict1['oldpeak_eq_st_depression_(1.378, 2.067]']=1
        if 2.067<x<= 2.756:
            dict1['oldpeak_eq_st_depression_(2.067, 2.756]']=1
        if 2.756<x<= 3.444:
            dict1['oldpeak_eq_st_depression_(2.756, 3.444]']=1
        if 3.444<x<= 4.133:
            dict1['oldpeak_eq_st_depression_(3.444, 4.133]']=1
        if 4.133<x<= 4.822:
            dict1['oldpeak_eq_st_depression_(4.133, 4.822]']=1
        if 4.822<x<= 5.511:
            dict1['oldpeak_eq_st_depression_(4.133, 4.822]']=1
        if 5.511<x<= 6.2:
            dict1['oldpeak_eq_st_depression_(5.511, 6.2]']=1
    return dict1


app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    slope_of_peak_exercise_st_segment = request.form['slope_of_peak_exercise_st_segment']
    slope = cal(slope_of_peak_exercise_st_segment, 1)
    thal = request.form['thal']
    th = cal(thal, 2)
    chest= request.form['chest_pain_type']
    ch = cal(chest, 3)
    exercise = request.form['exercise_induced_angina']
    exer= cal(exercise, 4)
    num_major_vessels= request.form['num_major_vessels']
    num = cal(num_major_vessels, 5)
    fasting_blood_sugar_gt_120_mg_per_dl = request.form['fasting_blood_sugar_gt_120_mg_per_dl']
    fast = cal(fasting_blood_sugar_gt_120_mg_per_dl, 6)
    resting_ekg_results = request.form['resting_ekg_results']
    result = cal(resting_ekg_results, 7)
    sex = request.form['sex']
    sex = cal(sex, 8)
    age = request.form['age']
    age = cal(age, 9)
    resting_blood_pressure = request.form['resting_blood_pressure']
    resting = cal(resting_blood_pressure, 10)
    serum_cholesterol_mg_per_dl = request.form['serum_cholesterol_mg_per_dl']
    serum = cal(serum_cholesterol_mg_per_dl, 11)
    max_heart_rate_achieved = request.form['max_heart_rate_achieved']
    max = cal(max_heart_rate_achieved, 12)
    oldpeak_eq_st_depression = request.form['oldpeak_eq_st_depression']
    oldpeak = cal(oldpeak_eq_st_depression, 13)

    input_data = [{**slope, **th, **ch, **exer, **num, **fast, **result, **sex, **age,**resting,**serum ,**max,**oldpeak}]
    final = []

    data = pd.DataFrame(input_data)
    prediction = model.predict(data)[0]
    prediction = round(prediction)
    print(prediction)
    if (prediction == 1.0):
        output = 'effected'
    else:
        output = 'not effected'
    return render_template('index.html', prediction_text="The person is {}".format(output))


if __name__ == '__main__':
    app.run()