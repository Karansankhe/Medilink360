import streamlit as st
import pandas as pd
from datetime import datetime, timedelta


doctors_data = {
    'Doctor ID': [1, 2, 3],
    'Doctor Name': ['Dr. Patel', 'Dr. Sharma', 'Dr. Gupta'],
    'Specialization': ['Cardiologist', 'Dermatologist', 'Orthopedic'],
    'Degree': ['MBBS', 'MBBS', 'MBBS'],
}


doctors_df = pd.DataFrame(doctors_data)


def generate_time_slots(day, start_time, end_time, slot_duration):
    current_time = datetime.strptime(start_time, '%H:%M')
    end_time = datetime.strptime(end_time, '%H:%M')
    time_slots = []

    while current_time < end_time:
        time_slots.append(current_time.strftime('%H:%M'))
        current_time += timedelta(minutes=slot_duration)

    return {'day': day, 'time_slots': time_slots}


availability_data = [
    generate_time_slots('Monday', '09:00', '17:00', 30),
    generate_time_slots('Tuesday', '09:30', '16:30', 30),
    generate_time_slots('Wednesday', '10:00', '18:00', 30),
]

availability_df = pd.DataFrame(availability_data)


st.title('Rural Doctor Availability Platform')


st.subheader('Available Doctors:')
st.table(doctors_df)


selected_doctor = st.selectbox('Select a doctor:', doctors_df['Doctor Name'])
selected_day = st.selectbox('Select a day:', availability_df['day'])

st.subheader('Available Time Slots:')
selected_doctor_id = doctors_df.loc[doctors_df['Doctor Name'] == selected_doctor, 'Doctor ID'].values[0]
selected_availability = availability_df.loc[availability_df['day'] == selected_day]

st.write(f"Available time slots for {selected_day}:")
st.table(selected_availability[['day', 'time_slots']])


chosen_time_slot = st.selectbox('Select a time slot:', selected_availability['time_slots'])
user_name = st.text_input('Enter your name:')
user_phone = st.text_input('Enter your phone number:')

if st.button('Schedule Appointment'):
   
    st.success(f"Appointment scheduled successfully!\n"
               f"Doctor: {selected_doctor}\n"
               f"Day: {selected_day}\n"
               f"Time: {chosen_time_slot}\n"
               f"Patient: {user_name}\n"
               f"Phone: {user_phone}")


st.subheader('Additional Rural-Friendly Features:')
st.write("- Offline functionality")
st.write("- Mobile-friendly design")
st.write("- SMS or phone call appointment scheduling")
st.write("- Community outreach and assistance")
