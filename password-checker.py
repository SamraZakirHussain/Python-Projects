import streamlit as st

# Title 
st.markdown(
    """<h2 style='color: purple;'>🔐 Password Strength Meter.</h2>""",
    unsafe_allow_html=True
)
st.markdown("""
**A strong password should:**
- ✅ Be at least 8 characters long  
- ✅ Contain uppercase & lowercase letters  
- ✅ Include at least one digit (0-9)  
- ✅ Have one special character
""")

# Input Field
password = st.text_input("🔑 Enter Your Password", type="password")

# 📦 Check when the user enters a password
if password:
    feedback = []
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❗ Password must be at least 8 characters long.")

    # Uppercase Letter
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("❗ Add at least one uppercase letter (A-Z).")

    # Lowercase Letter
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("❗ Add at least one lowercase letter (a-z).")

    # Digit
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("❗ Add at least one digit (0-9).")

    # Special Character
    if any(char in "!@#$%^&*()_+-=~" for char in password):
        score += 1
    else:
        feedback.append("❗ Add at least one special character (!@#$%^&* etc.).")

    # Strength Evaluation
    if score == 5:
        st.success("✅ Your password is strong!")
    elif score >= 3:
        st.warning("⚠️ Your password is moderate. Consider making it stronger.")
    else:
        st.error("❌ Your password is weak. Please improve it.")
