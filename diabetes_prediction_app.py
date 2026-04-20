import numpy as np
import pickle
import streamlit as st

# loading the saved model (simple path)
model_path = 'trained_model.sav'

with open(model_path, 'rb') as file:
    loaded_model = pickle.load(file)


# creating a function for Prediction
def diabetes_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person is *not diabetic* ✅'
    else:
        return 'The person is *diabetic* ⚠️'


def main():

    st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

    st.title('🩺 Diabetes Prediction Web App')
    st.markdown('Enter the patient details below and click *Predict* to check for diabetes.')
    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', 0, 20, 0)
        Glucose = st.number_input('Glucose Level', 0.0, 300.0, 100.0)
        BloodPressure = st.number_input('Blood Pressure value', 0.0, 200.0, 70.0)
        SkinThickness = st.number_input('Skin Thickness value', 0.0, 100.0, 20.0)

    with col2:
        Insulin = st.number_input('Insulin Level', 0.0, 900.0, 80.0)
        BMI = st.number_input('BMI value', 0.0, 70.0, 25.0)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', 0.0, 3.0, 0.5)
        Age = st.number_input('Age of the Person', 1, 120, 30)

    st.markdown('---')

    if st.button('🔍 Diabetes Test Result'):
        diagnosis = diabetes_prediction([
            Pregnancies, Glucose, BloodPressure, SkinThickness,
            Insulin, BMI, DiabetesPedigreeFunction, Age
        ])

        st.subheader('Result:')
        if 'not diabetic' in diagnosis:
            st.success(diagnosis)
        else:
            st.warning(diagnosis)


if _name_ == '_main_':
    main()
