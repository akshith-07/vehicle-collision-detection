from camera import startapplication
import streamlit as st 
import os
from mail import send_sms

st.title('VEHICLE COLLISION DETECTION')

st.markdown(
    """
    Accidents happen unexpectedly, and every second counts in providing timely assistance. 
    Our Vehicle Collision Detection System utilizes advanced technology to detect and classify 
    different levels of accidents in real-time. Upload a video file to initiate the detection process 
    and receive prompt alerts based on the severity of the detected collision.
    """
)

up_vdo = st.file_uploader('Upload Video', type=['mp4'])

if up_vdo is not None:
    with open(os.path.join(os.getcwd(), up_vdo.name), 'wb') as f:
        f.write(up_vdo.getvalue())
            
if st.button('Detect'):
    if up_vdo is not None:
        probs = startapplication(up_vdo.name)
        if (probs > 69).any():
            st.write('Accident Detected at  12th Main Road, Vijaya Nagar,Velacheri, Chennai - 600 042')
            st.write('Level of the Accident is Severe')
            st.write('Major Accident: Probability: {}'.format(probs))
            try:
                msg = 'Major accident detected at the intersection of 12th Main Road and Vijaya Nagar in Velacheri, Chennai (Zip Code: 600042). Urgent attention is required, with immediate medical support imperative.'
                send_sms(msg)
            except:
                print("SMS NOT SENT")
        elif (probs > 40).any():
            st.write('Accident Detected at  12th Main Road, Vijaya Nagar,Velacheri, Chennai - 600 042')
            st.write('Level of the Accident is Moderate')
            st.write('Moderate Accident: Probability: {}'.format(probs))

            try:
                msg = 'Moderate accident detected at the intersection of 12th Main Road and Vijaya Nagar in Velacheri, Chennai (Zip Code: 600042). Immediate medical support and clearance action are required'

                send_sms(msg)
            except:
                print("SMS NOT SENT")
        else:
            st.write('Accident Detected at  12th Main Road, Vijaya Nagar,Velacheri, Chennai - 600 042')
            st.write('Level of the Accident is not severe')
            try:
                msg = 'Minor accident detected at 12th Main Road, Vijaya Nagar,Velacheri, Chennai - 600 042 '
                send_sms(msg)
            except:
                print("SMS NOT SENT")
    else:
        st.write('Please upload a video file.')