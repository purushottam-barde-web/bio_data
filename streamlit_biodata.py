import streamlit as st
from PIL import Image
import base64

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Purushottam's Personal Portfolio",
    page_icon="🧑‍💼")

# -------------------------------------------------
# CUSTOM CSS (Premium UI Styling)
# -------------------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #1f4037, #99f2c8);
}

.main {
    background-color: rgba(255,255,255,0.95);
    padding: 2rem;
    border-radius: 20px;
}

.profile-card {
    text-align: center;
    padding: 20px;
}

.profile-img {
    border-radius: 50%;
    width: 220px;
    border: 5px solid #00c6ff;
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
    color: #0f2027;
}

.social-btn {
    display: inline-block;
    padding: 10px 18px;
    margin: 5px;
    border-radius: 10px;
    text-decoration: none;
    color: white;
    font-weight: bold;
}

.linkedin {background-color:#0077b5;}
.youtube {background-color:#FF0000;}
.whatsapp {background-color:#25D366;}
.github {background-color:#333;}

.project-card {
    background-color: #f7f7f7;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER SECTION
# -------------------------------------------------
col1, col2 = st.columns([0.4,0.6])

with col1:
    image = Image.open(r"Profile_image.jpg")  
    st.image(image, use_container_width=True)

with col2:
    st.title("Purushottam Vyankatrao Barde 🚀")
    st.subheader("Data Scientist | GenAI Engineer | ML Enthusiast")
    st.write("Building Intelligent Systems with AI, LLMs & Cloud ☁️")

# -------------------------------------------------
st.divider()

# -------------------------------------------------
# TABS FOR HIGH ENGAGEMENT
# -------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["🧑 Personal", "🎓 Career", "🚀 Projects", "📞 Contact"])

# -------------------------------------------------
# PERSONAL DETAILS
# -------------------------------------------------
with tab1:
    st.markdown("## 🧑 Personal Details")
    st.write("""
    **Birth Date:** 17/10/1997  
    **Birth Time:** 06:00 PM  
    **Birth Place:** Jalna, Maharashtra  
    **Height:** 5.9 ft  
    **Blood Group:** O+ve  
    **Caste:** Bhavsar  
    """)

    st.markdown("### 💡 About Me")
    st.info("""
    Passionate Data Scientist specializing in GenAI, RAG Systems,
    LLMOps, and Enterprise AI solutions. I love solving real-world
    problems using intelligent automation.
    """)
    
    st.download_button(
        label="📄 Download My Biodata",
        data="Purushottam Vyankatrao Barde - Data Scientist",
        file_name="Purushottam_Barde_Biodata.txt",
        mime="text/plain"
    )

# -------------------------------------------------
# EDUCATION & SKILLS
# -------------------------------------------------
with tab2:
    st.markdown("## 🎓 Education & Career")
    st.write("""
    **Education:** BE (Mechanical), MBA  
    **Profession:** Data Scientist  
    **Location:** Pune  
    **Annual Income:** ₹11.20 LPA  
    """)

    st.markdown("### 🛠 Skills")

    st.progress(90)
    st.write("Python, Machine Learning")

    st.progress(85)
    st.write("LLMs, RAG, LangChain")

    st.progress(80)
    st.write("Cloud (GCP), Docker, CI/CD")

# -------------------------------------------------
# PROJECT SHOWCASE
# -------------------------------------------------
with tab3:
    st.markdown("## 🚀 Featured Projects")

    st.markdown("""
    <div class="project-card">
    <h4>Charlie – Enterprise GenAI Chatbot</h4>
    <p>Built enterprise-grade chatbot using RAG, Vertex AI & BigQuery.
    Deployed on GCP with Docker & CI/CD automation.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
    <h4>Invoice NER Model</h4>
    <p>Custom Named Entity Recognition model to extract invoice numbers
    with high precision for financial automation.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
    <h4>Hybrid RAG Architecture</h4>
    <p>Implemented metadata filtering & embedding optimization
    for enterprise secure data retrieval.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# CONTACT & SOCIAL LINKS
# -------------------------------------------------
with tab4:
    st.markdown("## Vishnu Barde")

    st.write("""
    📍 Vyankateshwara Nagar, Ring Road, Nanded  
    📞 9420911612  
    """)

    st.markdown("### 🌐 Connect With Me")

    st.markdown("""
    <a href="https://www.linkedin.com/in/purushottam-barde-9687b51aa/" class="social-btn linkedin" target="_blank">LinkedIn</a>
    <a href="https://www.youtube.com/@purushottam_barde" class="social-btn youtube" target="_blank">YouTube</a>
    <a href="https://wa.me/919420911612" class="social-btn whatsapp" target="_blank">WhatsApp</a>
    <a href="https://github.com/purushottambarde17" class="social-btn github" target="_blank">GitHub</a>
    """, unsafe_allow_html=True)
    st.success("Thank you for visiting my personal portfolio!✨")
# -------------------------------------------------
# DOWNLOAD BIODATA BUTTON
# -------------------------------------------------
st.divider()








