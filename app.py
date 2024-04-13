import streamlit as st
st.title('Title-> Hello Geeks, welcome to GFG!!')             #title
#------------------------------------------------------------

st.header('header-> Hello Geeks, welcome to GFG!!')           #header
#------------------------------------------------------------

st.subheader('Subheader-> Hello Geeks, welcome to GFG!!')     #Subheader
#------------------------------------------------------------

st.text('Text-> Hello Geeks, welcome to GFG!!')                #text
#------------------------------------------------------------

st.markdown('# Hi!!')
st.markdown('## Hi!!')
st.markdown('### Hi!!')
st.markdown('#### Hi!!')
st.markdown('##### Hi!!')                                      #markdown
#------------------------------------------------------------

st.success('success!')                                         #success
#------------------------------------------------------------

st.info('information')                                         #info
#------------------------------------------------------------

st.warning('Warning')                                          #warning
#------------------------------------------------------------

st.error('Error!!!!')                                          #error
#------------------------------------------------------------

# Example 1

st.markdown('#### Exception example 1.')                       #exception

exp=ZeroDivisionError('Division not possible with 0')
st.exception(exp)

st.markdown('#### Exception example 2.')


#Example 2

st.exception(ZeroDivisionError('Division not possible with 0'))
#-----------------------------------------------------------------

st.subheader('help(): used for documentation reading purpose.')

st.help(ZeroDivisionError)                                        #help
#-----------------------------------------------------------------

st.subheader('write')
st.write('range(1,10)')                                           #write

st.write(range(1,10))

st.write('1+2+3')

st.write(1+2+3)
                                                  
#-----------------------------------------------------------------
st.subheader('Code')                                              #Code
st.code('x=10 \n'
         'for i in range(x):\n'
         '\tprint(i)')

#-----------------------------------------------------------------
st.subheader('checkbox')                                          #checkbox

st.checkbox('Male')       #only checkbox.
st.checkbox('Female')

if(st.checkbox('CS/IT')):  #checkbox with validation. [multi select]
    st.write('eligible!')
#-----------------------------------------------------------------

st.subheader('Radio Button')                                       #radio Button

#radio button. [single-select]

radioButton=st.radio('select:', ('Male','Female','Other'))

if(radioButton == 'Male'):
    st.write("You're a Male")
elif(radioButton == 'Female'):
    st.write("You're a Female")
elif(radioButton == 'Other'):
    st.write("You're an Other Gender")

#-----------------------------------------------------------------

st.subheader('Select Box')                                          #select Box

selectBox=st.selectbox('Data Science:' , ['Data Analysis','Web Scraping',
                                'Machine Learning',
                                'Deep Learning',
                                'Natural Language Processing',
                                'Computer Vision',
                                'Image Processing'])

st.write('you have selected : ',selectBox)

#-----------------------------------------------------------------
 
st.subheader('MultiSelect Box')                                     #multiselect Box

multiSelectBox=st.multiselect('Data Science:' ,
                               ['Data Analysis',
                                'Web Scraping',
                                'Machine Learning',
                                'Deep Learning',
                                'Natural Language Processing',
                                'Computer Vision',
                                'Image Processing'])


st.write('you have selected: ',len(multiSelectBox),'courses.')

#-----------------------------------------------------------------

st.subheader('Button')                                              #Button

if(st.button('click me')):
    st.write('thanks for clicking.')

#-----------------------------------------------------------------

st.subheader('Slider')                                              #Slider
 
volume=st.slider('select the volume',1,100,step=1)
st.write('volume is: ',volume)

#-----------------------------------------------------------------

st.subheader('Example 1.')                                      #textInput

st.subheader('Text input')

name=st.text_input('enter name: ')
if(name):
    st.write('Hi, ',name)

st.subheader('Example 2.')

st.subheader('Text input')
username=st.text_input('enter Username: ')
password=st.text_input('enter Password: ',type='password')
if(username):
    st.write('Hi, ',username)

#-----------------------------------------------------------------

st.subheader('Text Area')                                           #text_area

textArea=st.text_area('write about yourself')

#-----------------------------------------------------------------

st.subheader("Input Number")                           # Input-Number

st.number_input('Select your age',18,110)              # from 18 till 110 only
                                          
#-----------------------------------------------------------------

st.subheader("Input Date")                              # Input-Date
st.date_input('Date')

#-----------------------------------------------------------------

st.subheader("Input Time")                              # Input-Time
st.time_input('Time')



















































