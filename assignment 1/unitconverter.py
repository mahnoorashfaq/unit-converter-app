import streamlit as st

st.title("Unit Converter App")
st.markdown ("Convert Length, Weight and Time")
st.write ("Welcome! Pick a conversion type, enter your value, and get the result instantly.")

category = st.selectbox ("Select a category", ["Length", "Weight" ,"Time"])

def convert_unit(category , value , unit):
    if category == "Length":
        if unit ==  "Kilometers To Miles":
            return value * 0.621371 
        elif unit == "Miles To Kilometers": 
             return value / 0.621371 
    
    elif  category == "Weight":
        if unit ==  "Kilograms To Ponds":
            return value * 2.20462 
        elif unit == "Ponds To Kilograms": 
             return value / 2.20462
        
    elif  category == "Time":
        if unit ==  "Seconds To Minutes":
            return value * 60 
        elif unit == "Minutes To Seconds": 
             return value / 60
        elif unit ==  "Minutes To Hours":
            return value * 60 
        elif unit == "Hours To Minutes": 
             return value / 60
        elif unit ==  "Hours To Days":
            return value * 24
        elif unit == "Days To Hours": 
             return value / 24
        
if category == "Length":
    unit =st.selectbox ("Select Conversion", ["Kilometers To Miles", "Miles To Kilometers"])
elif category == "Weight":
    unit =st.selectbox ("Select Conversion", ["Kilograms To Ponds", "Pond To Kilograms"])
elif category == "Time":
    unit =st.selectbox ("Select Conversion", ["Seconds To Minutes", "Minutes To Seconds" ,"Minutes To Hours", "Hours To Minutes" , "Hours To Days", "Days To Hours"])

value = st.number_input ("Enter to convert the value")

if st.button ("Convert") :
    result = convert_unit(category , value , unit)
    st.success (f"The result is {result:.2f}")