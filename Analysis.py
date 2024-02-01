import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data
data = {
    'PatientID': [1, 2, 3, 4, 5],
    'Age': [35, 42, 28, 50, 65],
    'BloodPressure': [120, 130, 110, 140, 135],
    'HeartRate': [75, 80, 70, 90, 85],
    'Diagnosis': ['Hypertension', 'Diabetes', 'Normal', 'Hypertension', 'Hyperlipidemia'],
}

patient_data = pd.DataFrame(data)

# Streamlit App
st.title('Single Patient Data Analysis App')

# Allow the user to select a patient
selected_patient = st.selectbox('Select a patient:', patient_data['PatientID'])

# Filter the data for the selected patient
selected_patient_data = patient_data[patient_data['PatientID'] == selected_patient]

# Display selected patient information
st.subheader('Selected Patient Information:')
st.dataframe(selected_patient_data)

# Visualization 1: Blood Pressure vs. Heart Rate for the selected patient
st.subheader('Blood Pressure vs. Heart Rate:')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='BloodPressure', y='HeartRate', hue='Diagnosis', data=selected_patient_data, palette='viridis', ax=ax)
st.pyplot(fig)

# Visualization 2: Distribution of Diagnoses
st.subheader('Distribution of Diagnoses:')
diagnosis_counts = selected_patient_data['Diagnosis'].value_counts()
fig, ax = plt.subplots()
diagnosis_counts.plot(kind='bar', ax=ax, color='skyblue')
ax.set_xlabel('Diagnosis')
ax.set_ylabel('Count')
st.pyplot(fig)

# Visualization 3: Age Distribution for the selected patient
st.subheader('Age Distribution:')
fig, ax = plt.subplots()
sns.histplot(selected_patient_data['Age'], bins=20, kde=True, color='salmon')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Visualization 4: Pair Plot for numerical features
st.subheader('Pair Plot for Numerical Features:')
numerical_features = ['Age', 'BloodPressure', 'HeartRate']
fig = sns.pairplot(selected_patient_data[numerical_features])
st.pyplot(fig)
