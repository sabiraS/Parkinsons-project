import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# loading the models
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Parkinsons Disease Prediction System',
                           ['Parkinsons Prediction',
                            'Information'],
                           icons=['person', 'activity'],
                           default_index=0)

# Ensure input is numeric and has correct shape
input_features = [[0 for _ in range(22)]]  # Placeholder for features to avoid shape errors

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        # Ensure no input fields are empty
        if '' in [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                  APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]:
            parkinsons_diagnosis = "Please fill in all the fields."
        else:
            try:
                # Convert all input fields to float
                input_features = [
                    [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP),
                     float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5),
                     float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1),
                     float(spread2), float(D2), float(PPE)]]

                # Prediction
                parkinsons_prediction = parkinsons_model.predict(input_features)

                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"

            except Exception as e:
                parkinsons_diagnosis = f"Error: {e}"

    st.success(parkinsons_diagnosis)

if selected == 'Information':
    st.title('About Parkinsons Disease')

    st.subheader('Select Information Category:')
    info_category = st.radio(
        'Choose information category:',
        ['Overview', 'Symptoms', 'Causes and Risk Factors', 'Diagnosis and Treatment', 'Living with Parkinson\'s',
         'Seek Professional Advice', 'External Medications', 'Side Effects']
    )

    if info_category == 'Overview':
        st.write("""
        Parkinson's disease is a neurodegenerative disorder that affects movement control. 
        It develops gradually, sometimes starting with a barely noticeable tremor in just one hand. 
        While tremors are common, the disorder also commonly causes stiffness or slowing of movement.
        """)
    elif info_category == 'Symptoms':
        st.write("""
        - Tremors: Involuntary shaking, usually in the hands, fingers, or limbs.
        - Bradykinesia: Slowness of movement, making simple tasks difficult and time-consuming.
        - Muscle Rigidity: Stiffness of the muscles, which can be uncomfortable and limit range of motion.
        - Postural Instability: Impaired balance and coordination, leading to difficulties in maintaining an upright posture.
        - Others: Changes in handwriting, speech, and facial expression.
        """)
    elif info_category == 'Causes and Risk Factors':
        st.write("""
        The exact cause of Parkinson's disease is unknown, but it is thought to involve a combination of genetic and environmental factors. 
        Some risk factors include age, family history, and exposure to certain toxins.
        """)
    elif info_category == 'Diagnosis and Treatment':
        st.write("""
        Diagnosis is based on medical history, symptoms, and sometimes imaging tests. 
        There is no cure for Parkinson's disease, but treatment options include medications, surgery, and physical therapy to manage symptoms.
        """)
    elif info_category == 'Living with Parkinson\'s':
        st.write("""
        Living with Parkinson's requires a multidisciplinary approach. 
        Patients often benefit from support groups, exercise, and a healthcare team that may include neurologists, physical therapists, and occupational therapists.
        """)
    elif info_category == 'Seek Professional Advice':
        st.write("""
        It's crucial for individuals experiencing symptoms or those diagnosed with Parkinson's to consult with healthcare professionals for personalized advice and treatment.
        """)
    elif info_category == 'External Medications':
        st.write("""
        In addition to internal medications, some external medications and therapies can help manage Parkinson's symptoms:
        - Physical therapy for improving mobility and balance
        - Occupational therapy for activities of daily living
        - Speech therapy for speech and swallowing difficulties
        - Assistive devices to aid in movement and daily tasks
        """)
        st.write("""
        Consult with your healthcare team to determine the most suitable external interventions for your specific needs.
        """)
    elif info_category == 'Side Effects':
        st.write("""
        Some common side effects of Parkinson's medications may include:
        - Nausea
        - Dizziness
        - Constipation
        - Hallucinations
        - Sleep disturbances
        - Dyskinesia (involuntary movements)
        - Mood changes
        """)
        st.write("""
        If you experience severe or persistent side effects, it's important to contact your healthcare provider.
        """)
