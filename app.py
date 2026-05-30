import streamlit as st
import re
import random
import string
import math

# Page Config
st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Strength Analyzer")

# Common weak passwords
common_passwords = [
    "password",
    "123456",
    "password123",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "abc123",
    "iloveyou"
]

# Password Generator
def generate_strong_password(length=12):
    chars = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*"
    )

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]

    password += [random.choice(chars) for _ in range(length - 4)]

    random.shuffle(password)

    return "".join(password)

# Password Input
password = st.text_input(
    "Enter Password",
    type="password"
)

if password:

    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Common Password Detection
    if password.lower() in common_passwords:
        st.error("⚠️ This is a commonly used password and is highly insecure.")

    # Result
    st.subheader("Result")

    if score <= 2:
        st.error("🔴 Weak Password")
    elif score <= 4:
        st.warning("🟡 Medium Password")
    else:
        st.success("🟢 Strong Password")

    # Progress Bar
    st.progress(score / 5)

    # Password Analysis
    st.subheader("Password Analysis")

    st.write(f"**Length:** {len(password)} characters")
    st.write(f"**Strength Score:** {score}/5")

    # Entropy Calculation
    entropy = len(password) * math.log2(94)

    st.write(f"**Estimated Entropy:** {entropy:.2f} bits")

    # Suggestions
    if suggestions:
        st.subheader("Suggestions")

        for suggestion in suggestions:
            st.write(f"• {suggestion}")

    else:
        st.success("Excellent! Your password follows strong security practices.")

    # Suggested Strong Password
    if score < 5:
        st.subheader("Suggested Strong Password")

        strong_password = generate_strong_password()

        st.code(strong_password)

# Password Generator Section
st.markdown("---")

st.subheader("🔑 Generate Strong Password")

if st.button("Generate Password"):
    generated = generate_strong_password()

    st.code(generated)

    st.success("Strong password generated successfully!")
