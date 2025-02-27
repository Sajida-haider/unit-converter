import streamlit as st

# Custom CSS for colorful UI
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .stButton>button {
        background-color: #ff6347 !important; /* Tomato */
        color: white !important;
        border-radius: 8px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }
    .stButton>button:hover {
        background-color: #ff4500 !important; /* Orange Red */
    }
    .stTextInput, .stNumberInput, .stSelectbox {
        background-color: #ffffe0 !important; /* Light Yellow */
        color: black !important;
        border-radius: 5px;
    }
    .stSuccess {
        background-color: #32cd32 !important; /* Lime Green */
        color: white !important;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Length Conversion Function
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701,
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Temperature Conversion Function
def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value

    if to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:
        return celsius

# Word Converter Function
def word_converter(text, conversion_type):
    if conversion_type == "Uppercase":
        return text.upper()
    elif conversion_type == "Lowercase":
        return text.lower()
    elif conversion_type == "Title Case":
        return text.title()
    elif conversion_type == "Reverse Text":
        return text[::-1]
    return text

# Main Function
def main():
    st.title("🎨 🔄 Multi-Purpose Converter 🌟")
    st.sidebar.header("⚙️ Settings")

    conversion_type = st.sidebar.selectbox("🔽 Select conversion type",
                                           ["Length", "Temperature", "Word Converter"])

    st.markdown("---")

    if conversion_type == "Length":
        st.header("📏 **Length Converter**")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("🔢 Enter value:", min_value=0.0, step=0.1)
            from_unit = st.selectbox("📌 From unit", [
                "Meter", "Kilometer", "Centimeter", "Millimeter",
                "Mile", "Yard", "Foot", "Inch"
            ])
        with col2:
            to_unit = st.selectbox("🎯 To unit", [
                "Meter", "Kilometer", "Centimeter", "Millimeter",
                "Mile", "Yard", "Foot", "Inch"
            ])

        if st.button("🔄 Convert Length"):
            result = length_converter(value, from_unit, to_unit)
            st.success(f"✅ **{value:.2f} {from_unit} = {result:.2f} {to_unit}**")

    elif conversion_type == "Temperature":
        st.header("🌡️ **Temperature Converter**")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("🌡️ Enter temperature:", step=0.1)
            from_unit = st.selectbox("📌 From unit", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            to_unit = st.selectbox("🎯 To unit", ["Celsius", "Fahrenheit", "Kelvin"])

        if st.button("🔄 Convert Temperature"):
            result = temperature_converter(value, from_unit, to_unit)
            st.success(f"🌟 **{value:.2f}°{from_unit[0]} = {result:.2f}°{to_unit[0]}**")

    elif conversion_type == "Word Converter":
        st.header("🔠 **Word Converter**")
        text = st.text_area("✍️ Enter text to convert:")
        conversion_type = st.selectbox("🎨 Select conversion type",
                                       ["Uppercase", "Lowercase", "Title Case", "Reverse Text"])

        if st.button("🔄 Convert Text"):
            result = word_converter(text, conversion_type)
            st.success(f"📝 **Converted Text:** {result}")

if __name__ == "__main__":
    main()
