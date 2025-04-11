import streamlit as st
#from PIL import Image

# ------------- CONFIG -------------
st.set_page_config(page_title="My Portfolio", layout="centered")

# Load profile photo
#profile_pic = Image.open("profile.jpg")  # Place your profile photo in the same folder

# ------------- HEADER / SUMMARY -------------
with st.container():
    col1, col2 = st.columns([1, 3])
   # with col1:
       # st.image(profile_pic, width=150)
    with col2:
        st.title("Your Full Name")
        st.subheader("Aspiring Data Analyst | Python Enthusiast")
        st.write("""
        📌 **Summary**:  
        Highly motivated data analyst skilled in extracting insights from data and translating them into actionable business strategies.
        Passionate about data visualization, machine learning, and continuous learning.
        """)

# ------------- SOCIAL LINKS -------------
with st.container():
    st.write("### 🌐 Connect with Me")
    st.markdown("""
    - 📧 Email: your_email@example.com  
    - 🔗 [LinkedIn](https://linkedin.com/in/your_id)  
    - 🐙 [GitHub](https://github.com/your_id)  
    - 🐦 [Twitter](https://twitter.com/your_id)
    """)

# ------------- EDUCATION -------------
with st.container():
    st.write("### 🎓 Education")
    st.markdown("""
    **Bachelor of Science in Data Science**, XYZ University (2020 - 2023)  
    - CGPA: 8.5 / 10  
    - Relevant coursework: Statistics, Python, Machine Learning, Data Visualization  
    """)

# ------------- EXPERIENCE -------------
with st.container():
    st.write("### 💼 Experience")
    st.markdown("""
    **Data Analyst Intern**, ABC Corp (Jun 2023 – Sep 2023)  
    - Cleaned and analyzed large datasets using Python & SQL  
    - Built dashboards with Power BI to track performance metrics  
    - Automated reports saving 10+ hours weekly

    **Freelance Data Analyst**, Upwork (Remote)  
    - Built custom data pipelines and visualization reports for small businesses  
    """)

# ------------- SKILLS -------------
with st.container():
    st.write("### 🛠 Skills")
    st.markdown("""
    - **Languages**: Python, SQL, R  
    - **Data Analysis**: Pandas, NumPy, Excel  
    - **Visualization**: Power BI, Matplotlib, Seaborn, Streamlit  
    - **Machine Learning**: Scikit-learn, Regression, Classification  
    - **Tools**: Git, Jupyter, VSCode, Tableau  
    """)

# ------------- PROJECTS -------------
with st.container():
    st.write("### 📁 Projects")
    st.markdown("""
    **1. Sales Dashboard in Power BI**  
    Created an interactive sales dashboard to visualize revenue trends across regions and products.

    **2. Customer Churn Prediction (ML)**  
    Built a logistic regression model with 85% accuracy to identify potential churn customers.

    **3. Personal Portfolio Website using Streamlit**  
    Created a responsive web app to showcase my achievements and resume.

    > 🔗 [GitHub Projects](https://github.com/your_id)
    """)

# ------------- CERTIFICATIONS -------------
with st.container():
    st.write("### 📜 Certifications")
    st.markdown("""
    - **Google Data Analytics** – Coursera  
    - **SQL for Data Science** – IBM  
    - **Power BI A-Z** – Udemy  
    """)

# ------------- ACHIEVEMENTS -------------
with st.container():
    st.write("### 🏆 Achievements")
    st.markdown("""
    - Top 10 finalist in National Data Hackathon 2023  
    - Secured 1st place in college analytics challenge  
    - Published 3 articles on Medium around data tips  
    """)

# ------------- HOBBIES -------------
with st.container():
    st.write("### 🎨 Hobbies")
    st.markdown("""
    - 🧘‍♂️ Meditation & Personal Development  
    - 📷 Photography & Design  
    - 📚 Reading non-fiction & tech blogs  
    - 🎮 Gaming & Chess  
    """)

# ------------- FOOTER -------------
st.write("---")
st.write("💼 Portfolio by Your Name — Made with ❤️ using Streamlit")
