import streamlit as st
from PIL import Image

img = 'delphes.jpg'








st.markdown("""
    # Project DELPHES
    Project DELPHES is an application that predicts the European group corresponding to a given ideology based on the twitter account of 472 deputies.
""")


image = Image.open(img)
st.image(image, use_column_width=True)

target = ('country', 'deputies name', 'gender', 'political group')
output = st.sidebar.selectbox("You have to chose the target!", target)
st.sidebar.write(f'You chosed the {output} for the prediction.')


input_type = ("sentence", 'twitter account', 'article')
inp = st.sidebar.selectbox("You do have to chose a input type!", input_type)
st.sidebar.write(f'You chosed the {inp} to make the prediction.')


def get_result(output):
    if output == "deputies name":
        return "deputy name", "url of deputies"
    elif output == "political group":
        return "political group", "accuracy", "Url political group"
    elif output == "gender":
        return "gender" , "accuracy"
    else:
        return "country_name"


st.markdown("""
    ## **Results**
""")

text = st.text_input( 'Enter a sentence')



import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

f'and the results is ...{get_result(output)}'

    
