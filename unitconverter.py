import streamlit as st
st.title("📏Smart Unit Converter")
st.markdown("### Convert Length, Weight, and Temperature units")
Units={
    "Length":["CM","Inch","Feet","Meter"],
    "Temperature":["Celsius", "Fahrenheit", "Kelvin"],
    "Weight": ["Gm","Kilogram","Pound"]
}
st.markdown("<h4 style='color: teal; font-weight: bold;'>Choose a Category</h4>", unsafe_allow_html=True)
category = st.selectbox("",list(Units.keys()))
from_unit = st.selectbox("Convert from", Units[category])
to_unit = st.selectbox("Convert to", Units[category])
value = st.number_input("Enter the value", value=0.0)

def unit_conversion(category, from_unit, to_unit, value):
    # Length Conversion
    if category == "Length":
        conversions = {
            "CM": 1,
            "Inch": 2.54,
            "Feet": 30.48,
            "Meter": 100
        }
        result = value * conversions[from_unit] / conversions[to_unit]
        return result

    # Weight Conversion
    elif category == "Weight":
        conversions = {
            "Gm": 1,
            "Kilogram": 1000,
            "Pound": 453.592
        }
        result = value * conversions[from_unit] / conversions[to_unit]
        return result

    # Temperature Conversion
    elif category == "Temperature":
        if from_unit == to_unit:
            return value

        # Celsius conversions
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15

        # Fahrenheit conversions
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15

        # Kelvin conversions
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32

    return None  # fallback if category or units don't match

        
if st.button("Convert"):
    result = unit_conversion(category, from_unit, to_unit, value)
    if result is not None:
        st.success(f"{result:.2f} {to_unit}")
        st.markdown("<h3 style='color: teal;'>✅Your Conversion Result</h3>", unsafe_allow_html=True)
    else:
        st.error("Conversion not possible.")

