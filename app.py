import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
        scroll-behavior: smooth;
    }
    .hero {
        background: url('https://your-hero-image-url.jpg') no-repeat center center/cover;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
    }
    h1 {
        font-size: 3rem;
        margin-bottom: 0;
    }
    h2 {
        font-size: 2rem;
        color: #f39c12;
    }
    .section {
        padding: 60px 20px;
        text-align: center;
    }
    .card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin: 20px;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .fade-in {
        opacity: 0;
        animation: fadeIn 1s forwards;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Smooth scrolling links
st.sidebar.title("Navigation")
st.sidebar.markdown("[Introduction](#introduction)")
st.sidebar.markdown("[Experience](#experience)")
st.sidebar.markdown("[Education](#education)")
st.sidebar.markdown("[Projects](#projects)")
st.sidebar.markdown("[Certifications](#certifications)")

# Introduction Section
st.markdown("<div id='introduction' class='hero'><h1>NANDINI KUPPALA</h1><h2>Your Catchy Tagline Here</h2></div>", unsafe_allow_html=True)

# Experience Section
st.markdown("<div id='experience' class='section fade-in'><h2>Experience</h2></div>", unsafe_allow_html=True)
experience_data = [
    {"title": "Campus Ambassador", "company": "E-Cell IIT Bombay", "duration": "August 2024 – Present", "description": "Led entrepreneurial initiatives and organized workshops."},
    {"title": "Founder & Project Lead", "company": "Nurture Sync", "duration": "June 2024 – Present", "description": "Developed a health management platform."},
    {"title": "Research Intern", "company": "Dr. Ramesh Sivanpillai", "duration": "October 2023 – Present", "description": "Worked on machine learning projects."},
    {"title": "Intern", "company": "Baavlibuch", "duration": "February 2024 – April 2024", "description": "Participated in all stages of SDLC."},
]
for job in experience_data:
    st.markdown(f"""
    <div class='card fade-in'>
        <h3>{job['title']} at {job['company']}</h3>
        <p>{job['duration']}</p>
        <p>{job['description']}</p>
    </div>
    """, unsafe_allow_html=True)

# Education Section
st.markdown("<div id='education' class='section fade-in'><h2>Education</h2></div>", unsafe_allow_html=True)
education_data = [
    {"degree": "Bachelor of Engineering in Artificial Intelligence", "institution": "Amrita Vishwa Vidyapeetham", "duration": "2022 – 2026", "cgpa": "CGPA: 7.91"},
]
for edu in education_data:
    st.markdown(f"""
    <div class='card fade-in'>
        <h3>{edu['degree']}</h3>
        <p>{edu['institution']} ({edu['duration']})</p>
        <p>{edu['cgpa']}</p>
    </div>
    """, unsafe_allow_html=True)

# Projects Section
st.markdown("<div id='projects' class='section fade-in'><h2>Projects</h2></div>", unsafe_allow_html=True)
projects_data = [
    {"title": "Cash Flow Minimizer", "description": "Developed a web application for financial optimization.", "image": "https://via.placeholder.com/150"},
    {"title": "Real-Time DeepFake Detection", "description": "Built a Chrome extension for detecting deep fakes.", "image": "https://via.placeholder.com/150"},
    {"title": "Marine Vision: Oil Spill Detection", "description": "Developed a system for early oil spill detection.", "image": "https://via.placeholder.com/150"},
]
for project in projects_data:
    st.markdown(f"""
    <div class='card fade-in'>
        <h3>{project['title']}</h3>
        <img src='{project['image']}' alt='Project Image' style='width:100%; height:auto; border-radius: 8px;'>
        <p>{project['description']}</p>
    </div>
    """, unsafe_allow_html=True)

# Certifications Section
st.markdown("<div id='certifications' class='section fade-in'><h2>Certifications</h2></div>", unsafe_allow_html=True)
certifications_data = [
    {"title": "Python Basic", "issuer": "Hacker Rank"},
    {"title": "Object Oriented Programming in Java", "issuer": "Duke University (Coursera)"},
    {"title": "AI Course Series", "issuer": "Infosys Springboard"},
]
for cert in certifications_data:
    st.markdown(f"""
    <div class='card fade-in'>
        <h3>{cert['title']}</h3>
        <p>{cert['issuer']}</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<footer class='section'>Contact: +91 7569056212 | Email: knandini7816@gmail.com</footer>", unsafe_allow_html=True)
