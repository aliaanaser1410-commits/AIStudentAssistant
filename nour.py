import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="EduMind AI",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# 2. CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

[data-testid="stSidebar"] {
    background-color: #172554;
}

[data-testid="stSidebar"] * {
    color: white;
}

h1, h2, h3 {
    color: #172554;
}

.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    height: 45px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #1d4ed8;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. KNOWLEDGE BASE - DATABASE
# ==========================================

courses = [

{
"name":"Python Fundamentals",
"category":"Programming",
"level":"Beginner",
"style":"Practical",
"duration":30,
"skills":["Python","Programming","Problem Solving"],
"description":"Learn Python from zero, variables, loops, functions and OOP.",
"prerequisites":[],
"career":["Data Scientist","AI Engineer","Software Developer"]
},

{
"name":"Advanced Python",
"category":"Programming",
"level":"Advanced",
"style":"Practical",
"duration":40,
"skills":["Python","OOP","Algorithms"],
"description":"Advanced Python, decorators, generators and algorithms.",
"prerequisites":["Python Fundamentals"],
"career":["AI Engineer","Software Developer","Data Scientist"]
},

{
"name":"HTML & CSS",
"category":"Web Development",
"level":"Beginner",
"style":"Visual",
"duration":25,
"skills":["HTML","CSS","Web Design"],
"description":"Create responsive websites using HTML and CSS.",
"prerequisites":[],
"career":["Web Developer"]
},

{
"name":"JavaScript",
"category":"Web Development",
"level":"Intermediate",
"style":"Practical",
"duration":35,
"skills":["JavaScript","Programming","Web Development"],
"description":"Learn JavaScript and interactive web applications.",
"prerequisites":["HTML & CSS"],
"career":["Web Developer"]
},

{
"name":"React Development",
"category":"Web Development",
"level":"Advanced",
"style":"Projects",
"duration":45,
"skills":["React","JavaScript","Frontend"],
"description":"Build modern frontend applications with React.",
"prerequisites":["JavaScript"],
"career":["Web Developer"]
},

{
"name":"SQL Fundamentals",
"category":"Database",
"level":"Beginner",
"style":"Practical",
"duration":25,
"skills":["SQL","Database"],
"description":"Learn SQL queries and database fundamentals.",
"prerequisites":[],
"career":["Data Analyst","Data Scientist","Software Developer"]
},

{
"name":"Advanced SQL",
"category":"Database",
"level":"Advanced",
"style":"Practical",
"duration":30,
"skills":["SQL","Database","Data Analysis"],
"description":"Advanced queries, joins and database optimization.",
"prerequisites":["SQL Fundamentals"],
"career":["Data Analyst","Data Scientist"]
},

{
"name":"Data Analysis Fundamentals",
"category":"AI & Data",
"level":"Beginner",
"style":"Practical",
"duration":30,
"skills":["Data Analysis","Statistics","Excel"],
"description":"Understand data analysis and statistical concepts.",
"prerequisites":[],
"career":["Data Analyst","Data Scientist"]
},

{
"name":"Pandas & NumPy",
"category":"AI & Data",
"level":"Intermediate",
"style":"Practical",
"duration":35,
"skills":["Python","Pandas","NumPy","Data Analysis"],
"description":"Data cleaning, manipulation and numerical computing.",
"prerequisites":["Python Fundamentals"],
"career":["Data Analyst","Data Scientist"]
},

{
"name":"Data Visualization",
"category":"AI & Data",
"level":"Intermediate",
"style":"Visual",
"duration":25,
"skills":["Python","Data Visualization","Statistics"],
"description":"Create charts and dashboards from real datasets.",
"prerequisites":["Data Analysis Fundamentals"],
"career":["Data Analyst","Data Scientist"]
},

{
"name":"Statistics for Data Science",
"category":"AI & Data",
"level":"Intermediate",
"style":"Theory",
"duration":30,
"skills":["Statistics","Mathematics","Data Analysis"],
"description":"Probability, distributions and statistical analysis.",
"prerequisites":[],
"career":["Data Analyst","Data Scientist","AI Engineer"]
},

{
"name":"Machine Learning",
"category":"AI & Data",
"level":"Advanced",
"style":"Practical",
"duration":50,
"skills":["Python","Machine Learning","Statistics"],
"description":"Regression, classification and clustering algorithms.",
"prerequisites":["Pandas & NumPy","Statistics for Data Science"],
"career":["Data Scientist","AI Engineer"]
},

{
"name":"Deep Learning",
"category":"AI & Data",
"level":"Advanced",
"style":"Theory",
"duration":60,
"skills":["Python","Deep Learning","Neural Networks"],
"description":"Neural networks and deep learning architectures.",
"prerequisites":["Machine Learning"],
"career":["AI Engineer"]
},

{
"name":"Natural Language Processing",
"category":"AI & Data",
"level":"Advanced",
"style":"Practical",
"duration":40,
"skills":["Python","NLP","Machine Learning"],
"description":"Text processing and language models fundamentals.",
"prerequisites":["Machine Learning"],
"career":["AI Engineer"]
},

{
"name":"Computer Vision",
"category":"AI & Data",
"level":"Advanced",
"style":"Projects",
"duration":45,
"skills":["Python","Computer Vision","Deep Learning"],
"description":"Image processing and computer vision applications.",
"prerequisites":["Deep Learning"],
"career":["AI Engineer"]
},

{
"name":"Artificial Intelligence",
"category":"AI & Data",
"level":"Beginner",
"style":"Theory",
"duration":25,
"skills":["AI","Problem Solving"],
"description":"Introduction to artificial intelligence and expert systems.",
"prerequisites":[],
"career":["AI Engineer"]
},

{
"name":"Expert Systems",
"category":"AI & Data",
"level":"Intermediate",
"style":"Practical",
"duration":30,
"skills":["AI","Python","Problem Solving"],
"description":"Knowledge bases, inference engines and rule-based systems.",
"prerequisites":["Python Fundamentals"],
"career":["AI Engineer"]
},

{
"name":"Cybersecurity Fundamentals",
"category":"Security",
"level":"Beginner",
"style":"Theory",
"duration":30,
"skills":["Networking","Security","Cryptography"],
"description":"Introduction to cybersecurity and security principles.",
"prerequisites":[],
"career":["Cybersecurity Specialist"]
},

{
"name":"Network Security",
"category":"Security",
"level":"Intermediate",
"style":"Practical",
"duration":35,
"skills":["Networking","Security"],
"description":"Network security concepts and defensive practices.",
"prerequisites":["Cybersecurity Fundamentals"],
"career":["Cybersecurity Specialist"]
},

{
"name":"Cloud Computing",
"category":"Cloud",
"level":"Intermediate",
"style":"Practical",
"duration":35,
"skills":["Cloud","AWS","Deployment"],
"description":"Cloud computing concepts and AWS services.",
"prerequisites":[],
"career":["Software Developer","AI Engineer"]
},

{
"name":"Flutter Development",
"category":"Mobile Development",
"level":"Intermediate",
"style":"Projects",
"duration":45,
"skills":["Flutter","Dart","Mobile Development"],
"description":"Build cross-platform mobile applications.",
"prerequisites":[],
"career":["Mobile Developer"]
},

{
"name":"UI UX Design",
"category":"Design",
"level":"Beginner",
"style":"Visual",
"duration":25,
"skills":["UI","UX","Figma","Design"],
"description":"Learn design principles and user experience.",
"prerequisites":[],
"career":["UI UX Designer"]
},

{
"name":"Git & GitHub",
"category":"Programming",
"level":"Beginner",
"style":"Practical",
"duration":15,
"skills":["Git","GitHub","Programming"],
"description":"Version control and collaborative development.",
"prerequisites":[],
"career":["Software Developer","AI Engineer","Web Developer"]
},

{
"name":"Power BI",
"category":"AI & Data",
"level":"Intermediate",
"style":"Visual",
"duration":30,
"skills":["Power BI","Data Visualization","Data Analysis"],
"description":"Build interactive business intelligence dashboards.",
"prerequisites":["Data Analysis Fundamentals"],
"career":["Data Analyst"]
},

{
"name":"Excel for Data Analysis",
"category":"AI & Data",
"level":"Beginner",
"style":"Practical",
"duration":20,
"skills":["Excel","Data Analysis"],
"description":"Data analysis using Excel and spreadsheets.",
"prerequisites":[],
"career":["Data Analyst"]
},

{
"name":"Software Engineering",
"category":"Programming",
"level":"Intermediate",
"style":"Theory",
"duration":35,
"skills":["Software Engineering","OOP","Algorithms"],
"description":"Software development methodologies and design.",
"prerequisites":["Python Fundamentals"],
"career":["Software Developer"]
},

{
"name":"Algorithms & Data Structures",
"category":"Programming",
"level":"Advanced",
"style":"Practical",
"duration":40,
"skills":["Algorithms","Data Structures","Problem Solving"],
"description":"Learn efficient algorithms and data structures.",
"prerequisites":["Python Fundamentals"],
"career":["Software Developer","AI Engineer"]
},

{
"name":"Big Data Fundamentals",
"category":"AI & Data",
"level":"Advanced",
"style":"Theory",
"duration":40,
"skills":["Big Data","Python","Data Analysis"],
"description":"Introduction to big data technologies.",
"prerequisites":["Pandas & NumPy"],
"career":["Data Scientist"]
},

{
"name":"MLOps Fundamentals",
"category":"AI & Data",
"level":"Advanced",
"style":"Practical",
"duration":40,
"skills":["Python","Machine Learning","Deployment"],
"description":"Deploy and monitor machine learning models.",
"prerequisites":["Machine Learning"],
"career":["AI Engineer","Data Scientist"]
},

{
"name":"Mobile UI Design",
"category":"Design",
"level":"Intermediate",
"style":"Visual",
"duration":25,
"skills":["UI","UX","Design"],
"description":"Design modern mobile application interfaces.",
"prerequisites":["UI UX Design"],
"career":["UI UX Designer","Mobile Developer"]
}

]

df = pd.DataFrame(courses)


# ==========================================
# 4. CAREER KNOWLEDGE BASE
# ==========================================

career_skills = {

"Data Scientist":[
"Python","Statistics","Pandas","NumPy",
"Data Analysis","Machine Learning","SQL"
],

"AI Engineer":[
"Python","AI","Machine Learning",
"Deep Learning","NLP","Algorithms"
],

"Data Analyst":[
"Excel","SQL","Data Analysis",
"Statistics","Power BI","Data Visualization"
],

"Web Developer":[
"HTML","CSS","JavaScript","React",
"Frontend","Programming"
],

"Software Developer":[
"Python","OOP","Algorithms",
"Data Structures","Git","Software Engineering"
],

"Cybersecurity Specialist":[
"Networking","Security","Cryptography"
],

"Mobile Developer":[
"Flutter","Dart","Mobile Development","UI"
],

"UI UX Designer":[
"UI","UX","Figma","Design"
]

}


# ==========================================
# 5. SESSION STATE
# ==========================================

defaults = {
    "profile": {},
    "progress": {},
    "quiz_score": None,
    "recommendations": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ==========================================
# 6. SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("🎓 EduMind AI")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Main Navigation",
    [
        "Home",
        "User Profile",
        "Placement Test",
        "Smart Recommendation",
        "Skill Gap Analysis",
        "Learning Roadmap",
        "Career Advisor",
        "Course Comparison",
        "Progress Tracker",
        "Dashboard"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "EduMind AI helps students discover "
    "their ideal learning and career paths."
)


# ==========================================
# 7. HOME PAGE
# ==========================================

if page == "Home":

    st.title("🎓 Welcome to EduMind AI")

    st.subheader(
        "Your Intelligent Learning & Career Advisor"
    )

    st.write(
        "نظام خبير ذكي يساعدك على اكتشاف مهاراتك "
        "واختيار الكورسات المناسبة وبناء مستقبلك المهني."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Courses", len(df))

    col2.metric(
        "Career Paths",
        len(career_skills)
    )

    col3.metric(
        "Learning Categories",
        df["category"].nunique()
    )

    st.markdown("---")

    st.subheader("✨ What Can EduMind AI Do?")

    features = [
        "🎯 Analyze your learning personality",
        "🧠 Evaluate your current skills",
        "📚 Recommend suitable courses",
        "📊 Identify missing skills",
        "🛣️ Generate learning roadmaps",
        "💼 Recommend career paths",
        "📈 Track your learning progress"
    ]

    for feature in features:
        st.write("• " + feature)

    st.markdown("---")

    st.success(
        "ابدئي من User Profile لإنشاء ملفك التعليمي."
    )


# ==========================================
# 8. USER PROFILE
# ==========================================

elif page == "User Profile":

    st.title("👤 Learner Profile")

    st.write(
        "أجيبي عن الأسئلة التالية لتحليل احتياجاتك التعليمية."
    )

    with st.form("profile_form"):

        name = st.text_input("Your Name")

        age = st.number_input(
            "Your Age",
            min_value=13,
            max_value=100,
            value=20
        )

        interest = st.selectbox(
            "Choose Your Main Interest",
            df["category"].unique()
        )

        level = st.selectbox(
            "Your Current Level",
            ["Beginner", "Intermediate", "Advanced"]
        )

        learning_style = st.selectbox(
            "Preferred Learning Style",
            ["Practical", "Visual", "Theory", "Projects"]
        )

        goal = st.selectbox(
            "Your Main Goal",
            [
                "Getting a Job",
                "Freelancing",
                "Academic Development",
                "Personal Development"
            ]
        )

        hours = st.slider(
            "Available Study Hours Per Week",
            1, 40, 10
        )

        skills = st.multiselect(
            "Select Your Existing Skills",
            sorted(set(
                skill
                for course in courses
                for skill in course["skills"]
            ))
        )

        submitted = st.form_submit_button(
            "Save My Profile"
        )

        if submitted:

            st.session_state.profile = {
                "name": name,
                "age": age,
                "interest": interest,
                "level": level,
                "style": learning_style,
                "goal": goal,
                "hours": hours,
                "skills": skills
            }

            st.success(
                "Your profile has been created successfully!"
            )


# ==========================================
# 9. PLACEMENT TEST
# ==========================================

elif page == "Placement Test":

    st.title("📝 Placement Test")

    st.write(
        "اختبري معلوماتك الأساسية في البرمجة."
    )

    questions = [

        {
            "question": "What is Python?",
            "options": [
                "Programming Language",
                "Operating System",
                "Database",
                "Browser"
            ],
            "answer": "Programming Language"
        },

        {
            "question": "Which keyword defines a function?",
            "options": [
                "function",
                "def",
                "func",
                "define"
            ],
            "answer": "def"
        },

        {
            "question": "What is the output of 2 + 3?",
            "options": [
                "23",
                "5",
                "6",
                "Error"
            ],
            "answer": "5"
        },

        {
            "question": "Which data type stores True or False?",
            "options": [
                "String",
                "Integer",
                "Boolean",
                "Float"
            ],
            "answer": "Boolean"
        },

        {
            "question": "Which structure repeats code?",
            "options": [
                "Loop",
                "Variable",
                "String",
                "Function"
            ],
            "answer": "Loop"
        },

        {
            "question": "Which structure stores key-value pairs?",
            "options": [
                "List",
                "Dictionary",
                "Tuple",
                "Integer"
            ],
            "answer": "Dictionary"
        },

        {
            "question": "What does OOP stand for?",
            "options": [
                "Object Oriented Programming",
                "Open Online Program",
                "Object Output Process",
                "Online Operating Program"
            ],
            "answer": "Object Oriented Programming"
        },

        {
            "question": "Which keyword is used for inheritance in Python?",
            "options": [
                "extends",
                "class",
                "Inheritance",
                "Parent"
            ],
            "answer": "class"
        },

        {
            "question": "Which library is used for data analysis?",
            "options": [
                "Pandas",
                "HTML",
                "CSS",
                "React"
            ],
            "answer": "Pandas"
        },

        {
            "question": "What is Machine Learning?",
            "options": [
                "A database",
                "A type of printer",
                "A field of AI",
                "An operating system"
            ],
            "answer": "A field of AI"
        }

    ]

    with st.form("quiz_form"):

        answers = []

        for i, q in enumerate(questions):

            st.write(f"### Question {i+1}")

            answer = st.radio(
                q["question"],
                q["options"],
                key=f"quiz_{i}"
            )

            answers.append(answer)

        submit_quiz = st.form_submit_button(
            "Submit Test"
        )

        if submit_quiz:

            score = sum(
                answers[i] == questions[i]["answer"]
                for i in range(len(questions))
            )

            st.session_state.quiz_score = score

    if st.session_state.quiz_score is not None:

        score = st.session_state.quiz_score

        percentage = score * 10

        st.metric(
            "Your Score",
            f"{score}/10"
        )

        st.progress(percentage / 100)

        if percentage < 40:

            st.warning(
                "Your level is Beginner. Start with fundamentals."
            )

        elif percentage < 80:

            st.info(
                "Your level is Intermediate. Continue practicing."
            )

        else:

            st.success(
                "Your level is Advanced. You can explore advanced topics."
            )


# ==========================================
# 10. SMART RECOMMENDATION ENGINE
# ==========================================

elif page == "Smart Recommendation":

    st.title("🧠 Smart Course Recommendation")

    if not st.session_state.profile:

        st.warning(
            "Please create your User Profile first."
        )

    else:

        p = st.session_state.profile

        st.write(
            f"Recommendations for {p['name']}"
        )

        results = []

        level_points = {
            "Beginner": 100,
            "Intermediate": 80,
            "Advanced": 60
        }

        for course in courses:

            score = 0

            reasons = []

            # Category matching

            if course["category"] == p["interest"]:

                score +=
