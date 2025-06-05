import streamlit as st

st.title("🔍 Number Checker")
st.subheader("Check if a number is Positive/Negative, Odd/Even, and Prime 🔢")

# 📥 Take input from the user
num = st.number_input("Enter a number:", step=1, format="%d")

# ➕➖ Check Positive / Negative / Zero
if num > 0:
    st.write("✅ It's a **Positive** number.")
elif num == 0:
    st.write("⚪ It's **Zero**.")
else:
    st.write("❌ It's a **Negative** number.")

# 🔢 Check Odd or Even
if num % 2 != 0:
    st.write("🟠 It's an **Odd** number.")
else:
    st.write("🟢 It's an **Even** number.")

# 🔍 Prime number checker function
def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# ✅ Check if the number is Prime
if prime(num):
    st.write("🎉 It's a **Prime** number!")
else:
    st.write("ℹ️ It's **Not a Prime** number.")
