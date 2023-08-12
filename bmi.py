import streamlit as st

def calculate_bmi(height_feet, height_inches, weight_kg):
    total_height_inches = height_feet * 12 + height_inches
    bmi = weight_kg / ((total_height_inches / 39.37) ** 2)
    return round(bmi, 1)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")
    st.markdown("Body mass index (BMI) is a person’s weight in kilograms divided by the square of height in meters. BMI is an inexpensive and easy screening method for weight category—underweight, healthy weight, overweight, and obesity.")
    st.write("BMI Categories:")
    st.write("- Underweight: BMI less than 18.5")
    st.write("- Normal weight: BMI 18.5 - 24.9")
    st.write("- Overweight: BMI 25 - 29.9")
    st.write("- Obese: BMI 30 or more")

    st.write("Check yours: ")
    
    height_feet = st.number_input("Height (feet)", min_value=0, value=5)
    height_inches = st.number_input("Height (inches)", min_value=0, max_value=11, value=6)
    weight_kg = st.number_input("Weight (kg)", min_value=0, value=70)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(height_feet, height_inches, weight_kg)
        bmi_category = get_bmi_category(bmi)

        st.write(f"Hey there, your BMI is: {bmi}")
        st.write(f"BMI Category: {bmi_category}")
        st.write('Please share with your contacts if you find it easy and useful')
        st.write('Know more about BMI: https://www.cdc.gov/healthyweight/assessing/index.html')
        st.markdown('Find the full code on my Github:  https://github.com/imShashanKashyap/BMI_Calculator')
        st.markdown('Visit to know more about me: https://imshashankashyap.github.io/')
if __name__ == "__main__":
    main()
