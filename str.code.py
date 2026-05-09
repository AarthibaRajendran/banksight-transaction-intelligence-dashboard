import streamlit as st

#--------------------title------------------------------------#

st.title("This is my streamlit app")

#---------------------header,subheader,text-------------------#

st.header("This is Header")
st.subheader("This is subheader")
st.text("This is text.. we can use it for text and write a paragrap")

#---------------------Markdown-------------------------------#
st.markdown("""
        **BOLD TEXT**  *ITALIC TEXT*   ***BOLD AND ITALIC***     

        - Bullet Poit 1 
        - Bullet Point 2
            
        1. Numbered List
        2. Second items
            
        [link text]()
            
        'inline code'

""")
#-----------------------write--------------------------------#

st.write("text,dataframe,object,etc..")
st.write("Multiple","arguments",123)
st.write({"key" : "values"})

#---------------------code----------------------------------- #

st.code("""
def hello_world():
        print("Hello,Streamlit!"
        return true
        """,language="python")

#----------------------Formula---------------------------------#

st.latex(r"\int_a^b f(x)dx = F(b) - F(a)")

#----------------------lighter text----------------------------#

st.caption("This is caption - smaller - lighter text ")

#-----------------------divide line----------------------------#

st.divider()

#-----------------------HTML-----------------------------------#

st.html(""" 
<div style="backgrond: linear-gradient(to right, #ff6b6b, #4ecdc4);
            padding: 20px; border-radius: 10px;">
    <h2>Custom HTML Content</h2>
</div>
""")
#---------------------------------------------------------------#

import pandas as pd 

# Data Display

#DataFreame (Interactive)

df = pd.DataFrame({
    'Name' : ['Alice','Bob','Charlie'],
    'Age': [25,30,35],
    'City': ['NYC','London','Parise']
})
st.dataframe(df)  


df = pd.DataFrame({
    'Name' : ['Alice','Bob','Charlie'],
    'Age': [25,30,35],
    'City': ['NYC','London','Parise']
})
st.dataframe(df,use_container_width=True) 

st.dataframe(
    df.style.highlight_max(axis=0, subset=['Age']),
    use_container_width=True   
)
st.dataframe(df)  
#---------------------conver dataframe into table format--------------------#

st.table(st)

#------------ celsius,degree, Temprature(symple:alt+0176)-------------------#

st.metric(
    label="Temperature",
    value="70 °F",
    delta="1.2 °F",
    delta_color="normal"     # "normal" "inverse" "off"
)

# another method to using

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Metric 1", "100", "+10%")

    with col2:
        st.metric("Metric 2", "200", "-5%")

    with col3:
        st.metric("Metric 3", "300", "+15%")

#------------------------json format(hide and show)---------------------------#

sample_json = {
    "name": "Streamlit",
    "version": "1.0",
    "features": ["interactive", "fast"]
}

st.json(sample_json)

#---dataframe etited(fixed-we can't edited and dynamic- wecan edited the dataframe)---#

df = pd.DataFrame({
    'Name' : ['Alice','Bob','Charlie'],
    'Age': [25,30,35],
    'City': ['NYC','London','Parise']
})

edited_df = st.data_editor(
    df,
    num_rows="dynamic", #"fixed" or "dynamic"
    use_container_width=True,
    hide_index=False
)

#-------------------charts and visualitation--------------------------------#
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A','B','C']
)

#--------------------line chart---------------------------------------------#

st.line_chart(chart_data)

#--------------------area chart---------------------------------------------#

st.area_chart(chart_data)

#--------------------bar chart---------------------------------------------#

st.bar_chart(chart_data)

#---------------------------scatter_chart----------------------------------#

scatter_data = pd.DataFrame({
    'x' : np.random.randn(100),
    'y': np.random.randn(100),
    'size': np.random.randint(10, 100, 100),
    'color': np.random.choice(['A', 'B', 'C'], 100)
})

st.scatter_chart(
    scatter_data,
    x='x',
    y='y',
    size='size',
    color='color'
)

#------------------------- map ---------------------------------------#

st.map(map_data, size='size')

#------------------------ Histogram ----------------------------------#
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(np.random.randn(1000), bins=30)
ax.set_title("Histogram")

st.pyplot(fig)

#--------------------------- Interactive Chart -------------------------#

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

#-------------------- input widges --- (Button) ---------------------#

if st.button("click Me!", type='primary'):   # type: "primary" or "secondary" or "tertiary"
    st.write("Button clicked!")

if st.button("click Me!", type='secondary'):   
    st.write("Button clicked!")

if st.button("click Me!", type='tertiary'):   
    st.write("Button clicked!")

#-----------------Download Button------------------------------------#

csv_data = "Name,Age\nAlice,25\nBob,30"

st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="data.csv",
    mime="text/csv"
)

#-----------------link button------------------------------------#

st.link_button("Go to streamlit", "https:// streamlit.io")

#----------------- checkbox ------------------------------------#

agree = st.checkbox("I agreeti the terms")

if agree:
    st.write("Thank you")

#-----------------Radio Button( Vertically ) ------------------------------------#

genre = st.radio(
    "choose your favorite genre:",
    ["comedy", "Drama", "Documentary"],
    # Display horizontally
)
st.write(f" You selected: {genre}")

# Radio Button( Horizontally ) 

genre = st.radio(
    "choose your favorite genre:",
    ["comedy", "Drama", "Documentary"],
    horizontal=True       # Display horizontally
)

st.write(f" You selected: {genre}")

#-----------------select box (one select) ------------------------------------#

# select box (multiple select)

option = st.selectbox(
    "choose a color:",
    ["Red", "Green", "Blue", "Yellow"],
    index=0
)

# select box (multiple select) 

opetions = st.multiselect(
    "choose your favorite fruits:",
    ["Apple", "Banana", "Cherry", "Date"],
    default=["Apple"]             # pre- selected opetions
)

#----------------- simple slider ------------------------------------#

age = st.slider("select your age:", 0, 100, 25)

# Range slider

values = st.slider(
    "select a range:",
    0.0, 100.0, (25.0, 75.0)
)

# step slider

temp = st.slider("Temperature", -10, 40, 25, step=2)

########################

size = st.select_slider(
    "select size:",
    options=["XS", "S", "M", "L", "XL", "XXL"],
    value="M"
)

#-------------------text_input(box)-----------------------------#

name = st.text_input("Enter your name:")

name = st.text_input(
    "Enter your name:",
    value="",              #default value
    max_chars=50,          #character Limit
    placeholder="John Doe",
    type="password"   # "dafault" or "password"
)

#--------500 words eluthramathiri text box for paragraph---------#

message = st.text_area(
    "Enter your message:",
    height=100,   # opetional
    max_chars=500,  # we define (opetional)
    placeholder="type here..."
)

#------------------------ number input ---------------------------#

number = st.number_input(
    "Enter a number:",
    min_value=0,
    max_value=100,
    value=50,
    step=1
)

#------------------------ selected date  --------------------------#

selected_date = st.date_input(
    "Selected a date:",
    value=date.today(),
    min_value=date(2020, 1, 1),      # opetional
    max_value=date(2025, 12, 31)     # opetional
)

#------------------------ selected Time --------------------------#

from datetime import time

selected_time = st.time_input(
    "Selected time:",
    value=time(8, 45)
)

st.write("You selected:", selected_time)

#------------------------ File_uploader --------------------------#

# upload single file:

uploaded_file = st.file_uploader(
    "choose a file:",
    type=['csv', 'txt', 'pdf'],
    accept_multiple_files=False
)
 #upload multiple files:

uploaded_file = st.file_uploader(
    "choose a file:",
    type=['csv', 'txt', 'pdf'],
        accept_multiple_files=True
)

#------------------------ camera_input --------------------------#

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

#------------------------ color_picker --------------------------#

color = st.color_picker("pick a color:", "#00f980")
st.write(f"Selecetd color: {color}")

#------------------------ color_picker --------------------------#

st.image(
    r"C:\Users\aarth\OneDrive\Desktop\Natctue.jpeg",
    caption="Image caption",
    width=300,
    use_column_width=False
)

 # From local file
st.image(r"C:\Users\aarth\OneDrive\Desktop\Natctue.jpeg")

# Multiple images
st.image["img1.jpg", "img2.jpg", "img3.jpg"]

#------------------------ from audio file --------------------------#

audio_file = open("audio.mp3", "rb")
st.audio(audio_file.read())

#------------------------ from audio file --------------------------#

video_file = open("video.mp3", "rb")
st.video(video_file.read())

#------------------------ side bar ---------------------------------#

# add widgets to sidebar

st.sidebar.title("Sidebar Title")
st.sidebar.write("Sidebar content")

opetion = st.sidebar.selectbox(
    "choose opetion:",
    ["Opetion 1", "Opetion 2"]
)

# Equal width columns

col1, col2, col3 = st.columns(3)

with col1:
    st.write("column 1")

with col2:
    st.write("column 2")

with col3:
    st.write("column 3")

#------------------width of the columns----------------------------#

col1, col2 = st.columns[2, 1]  #2:1 ratio

with col1:
    st.write("wide column")

with col2:
    st.write("Narrow column")

#-------------------multipl tabs-----------------------------------#

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Content for Tab 1")

with tab2:
    st.write("Content for Tab 2")

with tab3:
    st.write("Content for Tab 3")

#------------------- Expander ------------------------------------#

with st.expander("Click to expand"):
    st.write("Hidden content inside expander")
 #   st.image("image.jpg")                         # petion

#---------------------container----------------------------------#

container = st.container(border=True)

with container:
    st.write("content inside container")
    st.button("Button is container")

#------------------ placeholder ----------------------------------#

placeholder = st.empty()

# Update placeholder Later
placeholder.text("Initial text")

# Update again
placeholder.success("Updated content!")

#------------------ popover --------------------------------------#

with st.popover("Open popover"):
    st.write("content inside popover")
    st.button("Button in popover")

#------------------ Dialog ---------------------------------------#

@st.dialog("Dialog Title")
def show_diaglog():
    st.write("This is a dialog/modal!")
    st.text_input("Input in dialog")

    if st.button("close"):
        st.rerun()

if st.button("open Dialog"):
    show_diaglog()

#------------------ success message -----------------------------------#

st.success("This is a success message!")

#------------------ info message -----------------------------------#

st.info("This is a info message!")

#------------------ warning message -----------------------------------#

st.warning("This is a warning message!")

#------------------ error message -------------------------------------#

st.error("This is a error message!")

#------------------ progress ------------------------------------------#

import time

progress_text = "Operation in progress..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

my_bar.empty()

#------------------ Spinner(Loading) -----------------------------------#

with st.spinner("Loadin..."):
    time.sleep(2)
st.success("Done!")

#------------------ toast ---------------------------------------------#

st.toast("Success!", icon="🎉")

if st.button("Click"):
    st.toast("Button clicked!", icon="✅")

#------------------ balloons ---------------------------------------------#

st.balloons()

#------------------ balloons ---------------------------------------------#

st.snow()


