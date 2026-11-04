
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# EduMind AI - Intelligent Learning & Career Advisor
# تشغيل المشروع:
# pip install streamlit pandas plotly
# streamlit run app.py
# =========================================================

st.set_page_config(
    page_title="EduMind AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------- التصميم -------------------------
st.markdown(
    """
    <style>
    .stApp { background-color: #f7f8fc; }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #172554, #1e3a8a);
    }
    [data-testid="stSidebar"] * { color: white; }
    h1, h2, h3 { color: #172554; }
    .hero {
        padding: 24px;
        border-radius: 16px;
        background: linear-gradient(120deg, #dbeafe, #eef2ff);
        border: 1px solid #bfdbfe;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------- قاعدة البيانات -------------------------
COURSES = [
    {
        "name": "Python Fundamentals", "category": "Programming",
        "level": "Beginner", "style": "Practical", "duration": 30,
        "skills": ["Python", "Programming", "Problem Solving"],
        "description": "تعلم أساسيات Python والمتغيرات والشروط والحلقات والدوال.",
        "prerequisites": [], "careers": ["Data Scientist", "AI Engineer", "Software Developer"],
    },
    {
        "name": "Advanced Python", "category": "Programming",
        "level": "Advanced", "style": "Practical", "duration": 40,
        "skills": ["Python", "OOP", "Algorithms"],
        "description": "موضوعات Python المتقدمة والبرمجة كائنية التوجه والخوارزميات.",
        "prerequisites": ["Python Fundamentals"],
        "careers": ["AI Engineer", "Software Developer", "Data Scientist"],
    },
    {
        "name": "HTML & CSS", "category": "Web Development",
        "level": "Beginner", "style": "Visual", "duration": 25,
        "skills": ["HTML", "CSS", "Web Design"],
        "description": "إنشاء صفحات ويب وتنسيقها وتصميم صفحات متجاوبة.",
        "prerequisites": [], "careers": ["Web Developer"],
    },
    {
        "name": "JavaScript", "category": "Web Development",
        "level": "Intermediate", "style": "Practical", "duration": 35,
        "skills": ["JavaScript", "Programming", "Web Development"],
        "description": "إضافة التفاعل والوظائف إلى مواقع الويب.",
        "prerequisites": ["HTML & CSS"], "careers": ["Web Developer"],
    },
    {
        "name": "React Development", "category": "Web Development",
        "level": "Advanced", "style": "Projects", "duration": 45,
        "skills": ["React", "JavaScript", "Frontend"],
        "description": "بناء واجهات ويب حديثة باستخدام React.",
        "prerequisites": ["JavaScript"], "careers": ["Web Developer"],
    },
    {
        "name": "SQL Fundamentals", "category": "Database",
        "level": "Beginner", "style": "Practical", "duration": 25,
        "skills": ["SQL", "Database"],
        "description": "أساسيات قواعد البيانات والاستعلامات باستخدام SQL.",
        "prerequisites": [], "careers": ["Data Analyst", "Data Scientist", "Software Developer"],
    },
    {
        "name": "Advanced SQL", "category": "Database",
        "level": "Advanced", "style": "Practical", "duration": 30,
        "skills": ["SQL", "Database", "Data Analysis"],
        "description": "الربط بين الجداول والاستعلامات المتقدمة وتحسين الأداء.",
        "prerequisites": ["SQL Fundamentals"], "careers": ["Data Analyst", "Data Scientist"],
    },
    {
        "name": "Data Analysis Fundamentals", "category": "AI & Data",
        "level": "Beginner", "style": "Practical", "duration": 30,
        "skills": ["Data Analysis", "Statistics", "Excel"],
        "description": "مبادئ تحليل البيانات والإحصاء وفهم البيانات.",
        "prerequisites": [], "careers": ["Data Analyst", "Data Scientist"],
    },
    {
        "name": "Pandas & NumPy", "category": "AI & Data",
        "level": "Intermediate", "style": "Practical", "duration": 35,
        "skills": ["Python", "Pandas", "NumPy", "Data Analysis"],
        "description": "تنظيف البيانات ومعالجتها وتحليلها باستخدام Pandas وNumPy.",
        "prerequisites": ["Python Fundamentals"],
        "careers": ["Data Analyst", "Data Scientist"],
    },
    {
        "name": "Data Visualization", "category": "AI & Data",
        "level": "Intermediate", "style": "Visual", "duration": 25,
        "skills": ["Python", "Data Visualization", "Statistics"],
        "description": "عرض البيانات بصريًا وإنشاء الرسوم البيانية.",
        "prerequisites": ["Data Analysis Fundamentals"],
        "careers": ["Data Analyst", "Data Scientist"],
    },
    {
        "name": "Statistics for Data Science", "category": "AI & Data",
        "level": "Intermediate", "style": "Theory", "duration": 30,
        "skills": ["Statistics", "Mathematics", "Data Analysis"],
        "description": "الاحتمالات والتوزيعات والإحصاء المستخدم في علم البيانات.",
        "prerequisites": [], "careers": ["Data Analyst", "Data Scientist", "AI Engineer"],
    },
    {
        "name": "Machine Learning", "category": "AI & Data",
        "level": "Advanced", "style": "Practical", "duration": 50,
        "skills": ["Python", "Machine Learning", "Statistics"],
        "description": "التعلم الخاضع وغير الخاضع للإشراف وخوارزميات التنبؤ.",
        "prerequisites": ["Pandas & NumPy", "Statistics for Data Science"],
        "careers": ["Data Scientist", "AI Engineer"],
    },
    {
        "name": "Deep Learning", "category": "AI & Data",
        "level": "Advanced", "style": "Theory", "duration": 60,
        "skills": ["Python", "Deep Learning", "Neural Networks"],
        "description": "الشبكات العصبية وبنى التعلم العميق.",
        "prerequisites": ["Machine Learning"], "careers": ["AI Engineer"],
    },
    {
        "name": "Natural Language Processing", "category": "AI & Data",
        "level": "Advanced", "style": "Practical", "duration": 40,
        "skills": ["Python", "NLP", "Machine Learning"],
        "description": "معالجة النصوص وتحليل المشاعر ومبادئ نماذج اللغة.",
        "prerequisites": ["Machine Learning"], "careers": ["AI Engineer"],
    },
    {
        "name": "Computer Vision", "category": "AI & Data",
        "level": "Advanced", "style": "Projects", "duration": 45,
        "skills": ["Python", "Computer Vision", "Deep Learning"],
        "description": "معالجة الصور وتطبيقات الرؤية الحاسوبية.",
        "prerequisites": ["Deep Learning"], "careers": ["AI Engineer"],
    },
    {
        "name": "Artificial Intelligence", "category": "AI & Data",
        "level": "Beginner", "style": "Theory", "duration": 25,
        "skills": ["AI", "Problem Solving"],
        "description": "مقدمة في الذكاء الاصطناعي والأنظمة الذكية.",
        "prerequisites": [], "careers": ["AI Engineer"],
    },
    {
        "name": "Expert Systems", "category": "AI & Data",
        "level": "Intermediate", "style": "Practical", "duration": 30,
        "skills": ["AI", "Python", "Problem Solving"],
        "description": "قواعد المعرفة ومحرك الاستدلال والأنظمة المعتمدة على القواعد.",
        "prerequisites": ["Python Fundamentals"], "careers": ["AI Engineer"],
    },
    {
        "name": "Cybersecurity Fundamentals", "category": "Security",
        "level": "Beginner", "style": "Theory", "duration": 30,
        "skills": ["Networking", "Security", "Cryptography"],
        "description": "مبادئ الأمن السيبراني والشبكات والحماية.",
        "prerequisites": [], "careers": ["Cybersecurity Specialist"],
    },
    {
        "name": "Network Security", "category": "Security",
        "level": "Intermediate", "style": "Practical", "duration": 35,
        "skills": ["Networking", "Security"],
        "description": "مفاهيم حماية الشبكات والممارسات الدفاعية.",
        "prerequisites": ["Cybersecurity Fundamentals"],
        "careers": ["Cybersecurity Specialist"],
    },
    {
        "name": "Cloud Computing", "category": "Cloud",
        "level": "Intermediate", "style": "Practical", "duration": 35,
        "skills": ["Cloud", "AWS", "Deployment"],
        "description": "مفاهيم الحوسبة السحابية وخدمات AWS.",
        "prerequisites": [], "careers": ["Software Developer", "AI Engineer"],
    },
    {
        "name": "Flutter Development", "category": "Mobile Development",
        "level": "Intermediate", "style": "Projects", "duration": 45,
        "skills": ["Flutter", "Dart", "Mobile Development"],
        "description": "إنشاء تطبيقات موبايل تعمل على أكثر من نظام.",
        "prerequisites": [], "careers": ["Mobile Developer"],
    },
    {
        "name": "UI UX Design", "category": "Design",
        "level": "Beginner", "style": "Visual", "duration": 25,
        "skills": ["UI", "UX", "Figma", "Design"],
        "description": "أساسيات تصميم واجهات وتجربة المستخدم.",
        "prerequisites": [], "careers": ["UI UX Designer"],
    },
    {
        "name": "Git & GitHub", "category": "Programming",
        "level": "Beginner", "style": "Practical", "duration": 15,
        "skills": ["Git", "GitHub", "Programming"],
        "description": "إدارة إصدارات الكود والعمل التعاوني على المشروعات.",
        "prerequisites": [], "careers": ["Software Developer", "AI Engineer", "Web Developer"],
    },
    {
        "name": "Power BI", "category": "AI & Data",
        "level": "Intermediate", "style": "Visual", "duration": 30,
        "skills": ["Power BI", "Data Visualization", "Data Analysis"],
        "description": "إنشاء لوحات معلومات تفاعلية لتحليل الأعمال.",
        "prerequisites": ["Data Analysis Fundamentals"], "careers": ["Data Analyst"],
    },
    {
        "name": "Excel for Data Analysis", "category": "AI & Data",
        "level": "Beginner", "style": "Practical", "duration": 20,
        "skills": ["Excel", "Data Analysis"],
        "description": "تحليل البيانات وتنظيمها باستخدام Excel.",
        "prerequisites": [], "careers": ["Data Analyst"],
    },
    {
        "name": "Software Engineering", "category": "Programming",
        "level": "Intermediate", "style": "Theory", "duration": 35,
        "skills": ["Software Engineering", "OOP", "Algorithms"],
        "description": "منهجيات تطوير البرمجيات وتحليل وتصميم الأنظمة.",
        "prerequisites": ["Python Fundamentals"], "careers": ["Software Developer"],
    },
    {
        "name": "Algorithms & Data Structures", "category": "Programming",
        "level": "Advanced", "style": "Practical", "duration": 40,
        "skills": ["Algorithms", "Data Structures", "Problem Solving"],
        "description": "الخوارزميات وهياكل البيانات وطرق تحسين الحلول.",
        "prerequisites": ["Python Fundamentals"],
        "careers": ["Software Developer", "AI Engineer"],
    },
    {
        "name": "Big Data Fundamentals", "category": "AI & Data",
        "level": "Advanced", "style": "Theory", "duration": 40,
        "skills": ["Big Data", "Python", "Data Analysis"],
        "description": "مقدمة في البيانات الضخمة وتقنياتها.",
        "prerequisites": ["Pandas & NumPy"], "careers": ["Data Scientist"],
    },
    {
        "name": "MLOps Fundamentals", "category": "AI & Data",
        "level": "Advanced", "style": "Practical", "duration": 40,
        "skills": ["Python", "Machine Learning", "Deployment"],
        "description": "نشر نماذج تعلم الآلة ومتابعتها وصيانتها.",
        "prerequisites": ["Machine Learning"], "careers": ["AI Engineer", "Data Scientist"],
    },
    {
        "name": "Mobile UI Design", "category": "Design",
        "level": "Intermediate", "style": "Visual", "duration": 25,
        "skills": ["UI", "UX", "Design"],
        "description": "تصميم واجهات تطبيقات الموبايل.",
        "prerequisites": ["UI UX Design"], "careers": ["UI UX Designer", "Mobile Developer"],
    },
]

df = pd.DataFrame(COURSES)

CAREER_SKILLS = {
    "Data Scientist": ["Python", "Statistics", "Pandas", "NumPy", "Data Analysis", "Machine Learning", "SQL"],
    "AI Engineer": ["Python", "AI", "Machine Learning", "Deep Learning", "NLP", "Algorithms"],
    "Data Analyst": ["Excel", "SQL", "Data Analysis", "Statistics", "Power BI", "Data Visualization"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Frontend", "Programming"],
    "Software Developer": ["Python", "OOP", "Algorithms", "Data Structures", "Git", "Software Engineering"],
    "Cybersecurity Specialist": ["Networking", "Security", "Cryptography"],
    "Mobile Developer": ["Flutter", "Dart", "Mobile Development", "UI"],
    "UI UX Designer": ["UI", "UX", "Figma", "Design"],
}

# ------------------------- حالة التطبيق -------------------------
if "profile" not in st.session_state:
    st.session_state.profile = None
if "progress" not in st.session_state:
    st.session_state.progress = {}
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = None
if "quiz_level" not in st.session_state:
    st.session_state.quiz_level = None

# ------------------------- القائمة الجانبية -------------------------
st.sidebar.title("🎓 EduMind AI")
st.sidebar.caption("Intelligent Learning & Career Advisor")
page = st.sidebar.radio(
    "القائمة الرئيسية",
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
        "Dashboard",
    ],
)
st.sidebar.markdown("---")
st.sidebar.write(f"📚 عدد الكورسات: {len(df)}")
st.sidebar.write(f"💼 عدد المسارات المهنية: {len(CAREER_SKILLS)}")
st.sidebar.info("البيانات الموجودة داخل المشروع تجريبية ومُعدة لأغراض العرض والتعلم.")

# =========================================================
# HOME
# =========================================================
if page == "Home":
    st.markdown(
        """
        <div class="hero">
            <h1>🎓 Welcome to EduMind AI</h1>
            <h3>Your Intelligent Learning & Career Advisor</h3>
            <p>نظام إرشاد تعليمي يساعدك على تحليل مهاراتك واختيار الكورسات
            وبناء خطة تعلم مناسبة لهدفك المهني.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Courses", len(df))
    c2.metric("Career Paths", len(CAREER_SKILLS))
    c3.metric("Categories", df["category"].nunique())
    st.subheader("ماذا يقدم النظام؟")
    features = [
        "تحليل الملف التعليمي للمستخدم.",
        "اختبار مبدئي لتحديد مستوى البرمجة.",
        "ترشيح الكورسات باستخدام نظام نقاط واضح.",
        "اكتشاف المهارات الناقصة للمسار الوظيفي.",
        "إنشاء خريطة تعلم ومتابعة التقدم.",
        "تفسير سبب ترشيح كل كورس.",
    ]
    for item in features:
        st.write(f"✅ {item}")
    st.info("ابدئي من صفحة User Profile واحفظي بياناتك أولًا.")

# =========================================================
# USER PROFILE
# =========================================================
elif page == "User Profile":
    st.title("👤 Learner Profile")
    st.write("أدخلي تفضيلاتك حتى يستطيع النظام تخصيص التوصيات.")
    categories = sorted(df["category"].unique().tolist())
    all_skills = sorted({skill for item in COURSES for skill in item["skills"]})
    with st.form("profile_form"):
        name = st.text_input("الاسم (اختياري)")
        interest = st.selectbox("المجال الذي تهتمين به", categories)
        level = st.selectbox("مستواك الحالي", ["Beginner", "Intermediate", "Advanced"])
        style = st.selectbox("أسلوب التعلم المفضل", ["Practical", "Visual", "Theory", "Projects"])
        goal = st.selectbox(
            "هدفك الأساسي",
            ["Getting a Job", "Freelancing", "Academic Development", "Personal Development"],
        )
        hours = st.slider("عدد ساعات التعلم المتاحة أسبوعيًا", 1, 40, 10)
        skills = st.multiselect("المهارات التي تمتلكينها بالفعل", all_skills)
        save_profile = st.form_submit_button("💾 حفظ الملف الشخصي")
    if save_profile:
        st.session_state.profile = {
            "name": name.strip() or "Learner",
            "interest": interest,
            "level": level,
            "style": style,
            "goal": goal,
            "hours": hours,
            "skills": skills,
        }
        st.success("تم حفظ ملفك التعليمي بنجاح.")
    if st.session_state.profile:
        st.subheader("الملف المحفوظ")
        st.json(st.session_state.profile)

# =========================================================
# PLACEMENT TEST
# =========================================================
elif page == "Placement Test":
    st.title("📝 اختبار تحديد المستوى")
    st.write("اختبار مبدئي من 10 أسئلة في أساسيات البرمجة وPython.")
    questions = [
        ("What is Python?", ["Programming Language", "Operating System", "Database", "Browser"], "Programming Language"),
        ("Which keyword defines a function in Python?", ["function", "def", "func", "define"], "def"),
        ("What is the result of 2 + 3?", ["23", "5", "6", "Error"], "5"),
        ("Which type stores True or False?", ["String", "Integer", "Boolean", "Float"], "Boolean"),
        ("Which structure repeats code?", ["Loop", "Variable", "String", "Comment"], "Loop"),
        ("Which structure stores key-value pairs?", ["List", "Dictionary", "Tuple", "Integer"], "Dictionary"),
        ("What does OOP stand for?", ["Object Oriented Programming", "Open Online Program", "Object Output Process", "Online Operating Program"], "Object Oriented Programming"),
        ("Which keyword is used to create a class?", ["class", "define", "object", "new"], "class"),
        ("Which library is commonly used for data analysis?", ["Pandas", "HTML", "CSS", "React"], "Pandas"),
        ("Machine Learning is a field of:", ["Database", "Artificial Intelligence", "Web Design", "Networking"], "Artificial Intelligence"),
    ]
    with st.form("quiz_form"):
        answers = []
        for i, (question, options, correct) in enumerate(questions):
            answers.append(st.radio(f"{i + 1}. {question}", options, key=f"question_{i}"))
        submit_test = st.form_submit_button("تصحيح الاختبار")
    if submit_test:
        score = sum(
            1 for answer, question in zip(answers, questions)
            if answer == question[2]
        )
        st.session_state.quiz_score = score
        percentage = score * 10
        if percentage < 40:
            st.session_state.quiz_level = "Beginner"
        elif percentage < 80:
            st.session_state.quiz_level = "Intermediate"
        else:
            st.session_state.quiz_level = "Advanced"
    if st.session_state.quiz_score is not None:
        score = st.session_state.quiz_score
        percentage = score * 10
        st.metric("نتيجتك", f"{score}/10")
        st.progress(percentage / 100)
        st.success(f"المستوى المبدئي المقترح: {st.session_state.quiz_level}")
        st.caption("هذا اختبار تعريفي قصير وليس تقييمًا أكاديميًا معتمدًا.")
        if st.session_state.profile and st.button("استخدام المستوى في ملفي الشخصي"):
            st.session_state.profile["level"] = st.session_state.quiz_level
            st.success("تم تحديث مستوى ملفك الشخصي.")

# =========================================================
# SMART RECOMMENDATION
# =========================================================
elif page == "Smart Recommendation":
    st.title("🧠 Smart Course Recommendation")
    profile = st.session_state.profile
    if not profile:
        st.warning("احفظي ملفك الشخصي أولًا من صفحة User Profile.")
    else:
        st.write(f"التوصيات المخصصة لـ **{profile['name']}**")
        level_rank = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}
        results = []
        for course in COURSES:
            score = 0
            reasons = []
            if course["category"] == profile["interest"]:
                score += 40
                reasons.append("المجال مطابق لاهتمامك (+40)")
            if course["level"] == profile["level"]:
                score += 25
                reasons.append("الم
