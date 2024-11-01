import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f9f9f9;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3 {
        color: #333;
    }
    h1 {
        text-align: center;
        margin-top: 20px;
        font-size: 3em;
    }
    h2 {
        margin-top: 40px;
        border-bottom: 2px solid #FF5733;
    }
    p {
        line-height: 1.6;
    }
    .contact-info {
        text-align: center;
        margin-bottom: 40px;
        font-size: 1.2em;
    }
    .section {
        margin: 40px 0;
        padding: 20px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .button {
        background-color: #FF5733;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #C70039;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("NANDINI KUPPALA")
st.markdown("<div class='contact-info'>+91 7569056212 | knandini7816@gmail.com | [LinkedIn](#) | [GitHub](#) | [LeetCode](#) | [GeeksForGeeks](#) | [HackerRank](#)</div>", unsafe_allow_html=True)

# Experience Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Experience")
st.markdown("""
**Campus Ambassador**  
*E-Cell IIT Bombay*  
August 2024 – Present  
- Led entrepreneurial initiatives in collaboration with E-Cell IIT Bombay, fostering innovation and startups among students.
- Organized workshops, events, and competitions that reached over 200+ participants, promoting entrepreneurship in college.
- Coordinated with teams to ensure smooth execution of events and increased student engagement by 30%.

**Founder & Project Lead**  
*Nurture Sync - in collaboration with NASSCOM Foundation*  
June 2024 – Present  
- Developed a comprehensive health management platform aimed at individuals managing thyroid and diabetes.
- Secured mentorship and funding through ThingQbator-NASSCOM Foundation.
- Led a team of 4 developers to create features like medical report analysis, AI-driven personalized health recommendations, and an AI chatbot for patient support.
- Collaborated with healthcare professionals to enhance the accuracy and relevance of the platform’s insights.

**Research Experience: Machine Learning, Remote Sensing, Image Processing**  
*Dr. Ramesh Sivanpillai*  
October 2023 – Present  
- Worked on real-time machine learning projects using LANDSAT data to monitor rangeland vegetation.
- Improved model accuracy by 15% using ensemble techniques, contributing to a 30% increase in profitability for Wyoming farmers.
- Collaborated with experts from the University of Wyoming and Amrita School of AI to analyze and interpret large datasets.

**Security and Software Testing Intern**  
*Baavlibuch*  
February 2024 – April 2024  
- Participated in all stages of the Software Development Lifecycle (SDLC), including analysis, design, development, and testing of a healthcare chatbot.
- Automated testing procedures, reducing manual testing effort by 40% and accelerating test case execution by 20%.
- Debugged and fixed critical application bugs, enhancing stability and performance by 25%.
- Implemented and managed testing environments in Linux, significantly improving security and data protection.
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Projects Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Projects")
st.markdown("""
**[Cash Flow Minimizer using Graph Data Structure](#)**  
- Developed a web application for financial optimization, minimizing transaction costs using graph data structures.
- Designed an algorithm that reduced transaction volume by 30%, effectively lowering operational costs.

**[Real-Time DeepFake Detection Chrome Extension](#)**  
- Built a Chrome extension for real-time detection of deep fake images and videos.
- Integrated backend machine learning algorithms, achieving 80% detection accuracy.

**Marine Vision: Early Warning System for Oil Spill Detection**  
- Developed an early warning system to detect oil spills using Synthetic Aperture Radar (SAR) imagery and Automatic Identification System (AIS) data.
- Utilized machine learning algorithms to classify oil spills with high accuracy and minimize false positives.
- Integrated AIS data to monitor vessel movements and correlate them with potential spill events.
- Enhanced environmental monitoring capabilities, significantly improving response times to oil spill incidents.
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Education Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Education")
st.markdown("""
**Bachelor of Engineering in Artificial Intelligence**  
*Amrita Vishwa Vidyapeetham, Coimbatore, Tamil Nadu*  
2022 – 2026  
- CGPA: 7.91
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Skills Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Skills")
st.markdown("""
- **Programming Languages:** Python, Java, JavaScript, SQL.
- **Web Development:** HTML5, CSS, Node.js, React, Flask, RESTful APIs.
- **Mobile App Development:** Flutter.
- **Database Management:** PostgreSQL, MongoDB, SQL.
- **DevOps Tools:** Git, Docker, Linux.
- **Testing:** Automated Testing, Software and Security Testing, Selenium.
- **Cloud Technologies:** Azure.
- **AI & Machine Learning:** Deep Learning, Natural Language Processing, Generative AI, Computer Vision.
- **Methodologies:** Agile Development, Scrum.
- **Soft Skills:** Analytical Thinking, Adaptability, Problem-Solving, Effective Communication, Team Collaboration, Quick Learner.
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Achievements Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Achievements")
st.markdown("""
- Research Internship: Enhanced profitability potential for Wyoming farmers by delivering actionable insights.
- Presented research work titled ”Mapping Vegetation Dynamics in Wyoming: A Multi-Temporal Analysis using Landsat NDVI and Clustering” at the ASPRS International Technical Symposium 2024.
- Solved 250+ Data Structures and Algorithms (DSA) problems.
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Certifications Section
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("Certifications")
st.markdown("""
- Python Basic : Hacker Rank
- Problem Solving Basic : Hacker Rank
- Object Oriented Programming in Java - Specialization Duke University (Coursera)
- Artificial Intelligence Course Series (118 hr length) : Infosys Springboard
- Data Structures and Performance : Coursera
- Agile Scrum in Practice : Infosys Springboard
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<footer style='text-align: center; padding: 20px;'><p>© 2024 Nandini Kuppala. All Rights Reserved.</p></footer>", unsafe_allow_html=True)
