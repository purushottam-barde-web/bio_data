import streamlit as st

st.set_page_config(
    page_title="Marriage Biodata - Purushottam Barde",
    layout="centered"
)

st.title("Purushottam Vyankatrao Barde")

# ---------------- PERSONAL DETAILS ----------------
st.header("🧑 Personal Details")

st.markdown("""
**Birth Date:** 17/10/1997  
**Birth Time:** 06:00 PM  
**Birth Place:** Jalna, Maharashtra  
**Height:** 5.9 ft  
**Blood Group:** O+ve  
**Maternal Gotra (Mamekul):** Zingade (Dharashiv)  
**Caste:** Bhavsar  
""")

st.divider()

# ---------------- EDUCATION & CAREER ----------------
st.header("🎓 Education & Career")

st.markdown("""
**Education:** BE (Mechanical), MBA  
**Profession:** Data Scientist  
**Job Location:** Pune  
**Annual Income:** ₹11.20 LPA  
""")

st.divider()

# ---------------- FAMILY DETAILS ----------------
st.header("👨‍👩‍👧‍👦 Family Details")

st.markdown("""
**Father's Name:** Late Vyankatrao Ramchandra Barde  
**Mother's Name:** Aruna Vyankatrao Barde  
**Mother's Occupation:** Housewife  

**Siblings:**  
• Sister – Bhagyashree Vyankatrao Barde  
• Brother – Vishnu Vyankatrao Barde  
""")

st.divider()

# ---------------- CONTACT DETAILS ----------------
st.header("Contact Details")

st.markdown("""
**Vishnu vyankatrao Barde**
📞 **9420911612**  
            
  
Vyankateshwara Nagar, Ring Road, Nanded  
Maharashtra  
""")

# ----------------------------------------------
address_text = "Vyankateshwara Nagar, Ring Road, Nanded, Maharashtra"

maps_link = f"https://maps.app.goo.gl/3VByqbxsmYaKo4d16"

# ---------------- CONTACT DETAILS ----------------
st.markdown(f"""
<div class="card">
<div class="section-title">🏡Google map link </div>
<div class="text">
<a href="{maps_link}" target="_blank">
📍Vyankateshwara Nagar, Ring Road, Nanded, Maharashtra 
</a><br><br>
</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------
st.divider()

