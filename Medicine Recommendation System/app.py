import pickle
import streamlit as st
import numpy as np
import pandas as pd

sym_des = pd.read_csv("data/symtoms_df.csv")
precautions = pd.read_csv("data/precautions_df.csv")
workout = pd.read_csv("data/workout_df.csv")
description = pd.read_csv("data/description.csv")
medications = pd.read_csv('data/medications.csv')
diets = pd.read_csv("data/diets.csv")

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def process_text(Symptoms):
    Symptoms = [s.strip() for s in Symptoms.split(',')]
    Symptoms = [symptom.strip("[]' ") for symptom in Symptoms]
    
    sym_array = np.zeros(132)
    
    columns = ['itching',
 'skin_rash',
 'nodal_skin_eruptions',
 'continuous_sneezing',
 'shivering',
 'chills',
 'joint_pain',
 'stomach_pain',
 'acidity',
 'ulcers_on_tongue',
 'muscle_wasting',
 'vomiting',
 'burning_micturition',
 'spotting_ urination',
 'fatigue',
 'weight_gain',
 'anxiety',
 'cold_hands_and_feets',
 'mood_swings',
 'weight_loss',
 'restlessness',
 'lethargy',
 'patches_in_throat',
 'irregular_sugar_level',
 'cough',
 'high_fever',
 'sunken_eyes',
 'breathlessness',
 'sweating',
 'dehydration',
 'indigestion',
 'headache',
 'yellowish_skin',
 'dark_urine',
 'nausea',
 'loss_of_appetite',
 'pain_behind_the_eyes',
 'back_pain',
 'constipation',
 'abdominal_pain',
 'diarrhoea',
 'mild_fever',
 'yellow_urine',
 'yellowing_of_eyes',
 'acute_liver_failure',
 'fluid_overload',
 'swelling_of_stomach',
 'swelled_lymph_nodes',
 'malaise',
 'blurred_and_distorted_vision',
 'phlegm',
 'throat_irritation',
 'redness_of_eyes',
 'sinus_pressure',
 'runny_nose',
 'congestion',
 'chest_pain',
 'weakness_in_limbs',
 'fast_heart_rate',
 'pain_during_bowel_movements',
 'pain_in_anal_region',
 'bloody_stool',
 'irritation_in_anus',
 'neck_pain',
 'dizziness',
 'cramps',
 'bruising',
 'obesity',
 'swollen_legs',
 'swollen_blood_vessels',
 'puffy_face_and_eyes',
 'enlarged_thyroid',
 'brittle_nails',
 'swollen_extremeties',
 'excessive_hunger',
 'extra_marital_contacts',
 'drying_and_tingling_lips',
 'slurred_speech',
 'knee_pain',
 'hip_joint_pain',
 'muscle_weakness',
 'stiff_neck',
 'swelling_joints',
 'movement_stiffness',
 'spinning_movements',
 'loss_of_balance',
 'unsteadiness',
 'weakness_of_one_body_side',
 'loss_of_smell',
 'bladder_discomfort',
 'foul_smell_of urine',
 'continuous_feel_of_urine',
 'passage_of_gases',
 'internal_itching',
 'toxic_look_(typhos)',
 'depression',
 'irritability',
 'muscle_pain',
 'altered_sensorium',
 'red_spots_over_body',
 'belly_pain',
 'abnormal_menstruation',
 'dischromic _patches',
 'watering_from_eyes',
 'increased_appetite',
 'polyuria',
 'family_history',
 'mucoid_sputum',
 'rusty_sputum',
 'lack_of_concentration',
 'visual_disturbances',
 'receiving_blood_transfusion',
 'receiving_unsterile_injections',
 'coma',
 'stomach_bleeding',
 'distention_of_abdomen',
 'history_of_alcohol_consumption',
 'fluid_overload.1',
 'blood_in_sputum',
 'prominent_veins_on_calf',
 'palpitations',
 'painful_walking',
 'pus_filled_pimples',
 'blackheads',
 'scurring',
 'skin_peeling',
 'silver_like_dusting',
 'small_dents_in_nails',
 'inflammatory_nails',
 'blister',
 'red_sore_around_nose',
 'yellow_crust_ooze',
 'prognosis']

    
    for s in Symptoms:
        if s in columns:
            index = columns.index(s)
            sym_array[index] = 1
    return sym_array

lab_map = {0: '(vertigo) Paroymsal  Positional Vertigo',
 1: 'AIDS',
 2: 'Acne',
 3: 'Alcoholic hepatitis',
 4: 'Allergy',
 5: 'Arthritis',
 6: 'Bronchial Asthma',
 7: 'Cervical spondylosis',
 8: 'Chicken pox',
 9: 'Chronic cholestasis',
 10: 'Common Cold',
 11: 'Dengue',
 12: 'Diabetes ',
 13: 'Dimorphic hemmorhoids(piles)',
 14: 'Drug Reaction',
 15: 'Fungal infection',
 16: 'GERD',
 17: 'Gastroenteritis',
 18: 'Heart attack',
 19: 'Hepatitis B',
 20: 'Hepatitis C',
 21: 'Hepatitis D',
 22: 'Hepatitis E',
 23: 'Hypertension ',
 24: 'Hyperthyroidism',
 25: 'Hypoglycemia',
 26: 'Hypothyroidism',
 27: 'Impetigo',
 28: 'Jaundice',
 29: 'Malaria',
 30: 'Migraine',
 31: 'Osteoarthristis',
 32: 'Paralysis (brain hemorrhage)',
 33: 'Peptic ulcer diseae',
 34: 'Pneumonia',
 35: 'Psoriasis',
 36: 'Tuberculosis',
 37: 'Typhoid',
 38: 'Urinary tract infection',
 39: 'Varicose veins',
 40: 'hepatitis A'}

def help(disease):

    #Description

    if disease in description['Disease'].tolist():
        st.write('--------------------------------------------------------')
        st.write('### Disease Name : ' +  disease + ' ####')
        st.write('--------------------------------------------------------')
        x = description[description['Disease']==disease].reset_index(inplace=False)
        for i in range(len(x)):
            st.write(x['Description'][i])
            st.write('---------------------------------------------------------')

    #Precaustions

    if disease in precautions['Disease'].tolist():
        st.write('### Precautions ####')
        x = precautions[precautions['Disease']==disease].reset_index(inplace=False)
        for i in range(len(x)):
            st.write('--------------------------------------------------------')
            st.write('1. '+x.loc[0,'Precaution_1'])
            st.write('2. '+x.loc[0,'Precaution_2'])
            if x.loc[0,'Precaution_3']!= "":
                st.write('3. '+str(x.loc[0,'Precaution_3']))
            if x.loc[0,'Precaution_4']!= "":
                st.write('4. '+x.loc[0,'Precaution_4'])
            st.write('--------------------------------------------------------')

    # Med 
    
    if disease in medications['Disease'].tolist():
        st.write('### Medicine ####')
        x = medications[medications['Disease']==disease].reset_index(inplace=False)
        for i in range(len(x)):
            st.write('--------------------------------------------------------')
            text = x['Medication'][i].strip("[]").replace("'", "")
            list = text.split(',')
            i = 0
            for l in list:
                st.write(str(i+1)+ ". "+l.strip()) 
                i += 1 
            st.write('---------------------------------------------------------')

    #Diets

    if disease in diets['Disease'].tolist():
        st.write('### Diet ####')
        x = diets[diets['Disease']==disease].reset_index(inplace=False)
        for i in range(len(x)):
            st.write('--------------------------------------------------------')
            text = x['Diet'][i].strip("[]").replace("'", "")
            list = text.split(',')
            i = 0
            for l in list:
                st.write(str(i+1)+ ". "+l.strip()) 
                i += 1 
            st.write('---------------------------------------------------------')

    # Workout

    if disease in workout['disease'].tolist():
        st.write('### Workout ####')
        x = workout[workout['disease']==disease].reset_index(inplace=False)
        st.write('--------------------------------------------------------')
        for i in range(len(x)):
            st.write(str(i+1)+ ". "+x['workout'][i])
        st.write('---------------------------------------------------------')

def main():
    st.title("MEDICINE RECOMMENDATION SYSTEM")
    Symptoms = st.text_input('Enter the Symtoms : ').lower()
    if Symptoms != "" :
        array = process_text(Symptoms)
        disease	 = lab_map[model.predict(array.reshape(1,-1))[0]]
        help(disease)

if __name__ == "__main__":
    main()