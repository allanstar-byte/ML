# from django.shortcuts import render

# Create your views here.
import joblib
from django.shortcuts import render

# Load the model

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'pkl', 'model.pkl')  # Adjust the path as necessary
model = joblib.load(model_path)

#model = joblib.load(r"C:\Users\Allan\Desktop\Jack\model.pkl")

def predict(request):
    if request.method == 'POST':
        # Get input data from the request
        input_data = [
            request.POST['designation'],
            float(request.POST['resource_allocation']),
            float(request.POST['mental_fatigue_score']),
            float(request.POST['tenure']),
            int(request.POST['gender_encoded']),
            int(request.POST['company_type_encoded']),
            int(request.POST['wfh_setup_available_encoded'])
        ]
        prediction = model.predict([input_data])
        return render(request, 'modelapp/result.html', {'prediction': prediction[0]})
    return render(request, 'modelapp/index.html')
