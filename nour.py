import pandas as pd
import streamlit as st

# إعداد الصفحة وتنسيقها
st.set_page_config(
    page_title="Expert Course Recommender System", page_icon="🤖", layout="centered"
)

st.title("🤖 Advanced Expert Course Recommender System")
st.write(
    "أهلاً بك! أنا النظام الخبير الذكي لمساعدتك في اختيار المسار التعليمي والكورسات الأكاديمية والمهنية الأنسب لمستقبلك."
)

# قاعدة بيانات موسعة جداً للكورسات والمجالات
data = {
    "Course_Name": [
        "Python for Beginners",
        "Advanced Python Programming",
        "Machine Learning A-Z",
        "Deep Learning Specialization",
        "Natural Language Processing (NLP)",
        "Web Development Bootcamp",
        "Full-Stack JavaScript Masterclass",
        "Data Science Fundamentals",
        "Data Analysis with Pandas & NumPy",
        "Artificial Intelligence Essentials",
        "Database Management Systems & SQL",
        "Cybersecurity Fundamentals",
        "Cloud Computing with AWS",
        "Mobile App Development with Flutter",
        "UI/UX Design Principles",
    ],
    "Category": [
        "Programming",
        "Programming",
        "AI & Data",
        "AI & Data",
        "AI & Data",
        "Web Development",
        "Web Development",
        "AI & Data",
        "AI & Data",
        "AI & Data",
        "Database",
        "Security",
        "Cloud",
        "Mobile Development",
        "Design",
    ],
    "Level": [
        "Beginner",
        "Advanced",
        "Intermediate",
        "Advanced",
        "Advanced",
        "Beginner",
        "Intermediate",
        "Beginner",
        "Intermediate",
        "Beginner",
        "Intermediate",
        "Beginner",
        "Intermediate",
        "Intermediate",
        "Beginner",
    ],
    "Learning_Style": [
        "Interactive Projects",
        "Code-heavy",
        "Hands-on Labs",
        "Research & Math",
        "Practical AI",
        "Building Websites",
        "Full Projects",
        "Data Analysis",
        "Coding Practice",
        "Conceptual & Practical",
        "SQL Queries",
        "Security Labs",
        "Cloud Deployment",
        "App Building",
        "Design & Wireframing",
    ],
    "Description": [
        "Learn python programming from scratch, variables, loops, functions, and OOP concepts.",
        "Master advanced python concepts, decorators, generators, algorithms, and efficient coding.",
        "Master machine learning algorithms, data preprocessing, regression, and scikit-learn models.",
        "Explore neural networks, computer vision, TensorFlow, PyTorch, and deep learning architectures.",
        "Process text data, sentiment analysis, transformers, and large language models fundamentals.",
        "Build modern full-stack web applications using HTML, CSS, JavaScript, and backend tools.",
        "Create dynamic web apps with Node.js, Express, React, and MongoDB databases.",
        "Learn data analysis, pandas, data visualization, statistics, and exploratory data analysis.",
        "Deep dive into data manipulation, cleaning, and aggregation using Python pandas and NumPy.",
        "Understand core artificial intelligence concepts, expert systems, and intelligent agents.",
        "Understand SQL, relational databases, database design, indexing, and efficient querying.",
        "Learn network security, ethical hacking, cryptography, and vulnerability assessment.",
        "Deploy and manage scalable cloud applications and services using Amazon Web Services.",
        "Build cross-platform mobile applications for iOS and Android using Flutter and Dart.",
        "Learn user interface and user experience fundamentals, wireframing, and Figma tools.",
    ],
}

df = pd.DataFrame(data)

# شريط جانبي لعرض معلومات النظام الخبير
st.sidebar.header("📊 لوحة تحكم النظام الخبير")
st.sidebar.write(f"إجمالي الكورسات المتاحة: **{len(df)}**")
st.sidebar.write(f"عدد المجالات الرئيسية: **{df['Category'].nunique()}**")
st.sidebar.markdown("---")
st.sidebar.info("هذا النظام يعتمد على تفضيلات المستخدم لتقديم استشارات وتوصيات دقيقة.")

# واجهة الأسئلة التفاعلية (Expert System Q&A)
st.subheader("🎯 أجب عن الأسئلة التالية لنقوم بتصميم مسارك التعليمي:")

# السؤال الأول: المجال
selected_category = st.selectbox(
    "1. ما هو المجال الأساسي الذي تود التخصص فيه؟",
    df["Category"].unique(),
)

# السؤال الثاني: المستوى
selected_level = st.selectbox(
    "2. ما هو مستواك الحالي في هذا المجال؟", df["Level"].unique()
)

# السؤال الثالث: أسلوب التعلم المفضل
selected_style = st.selectbox(
    "3. ما هو أسلوب التعلم المفضل لديك؟", df["Learning_Style"].unique()
)

# زر تحليل الإجابات وإعطاء التوصية الخبيرة
if st.button("🚀 توليد الترشيح الخبير والمخصص"):
  # تصفية الكورسات بناءً على إجابات المستخدم
  expert_recommendations = df[
      (df["Category"] == selected_category)
      & (df["Level"] == selected_level)
      & (df["Learning_Style"] == selected_style)
  ]

  st.success(
      "✨ تم إتمام عملية التحليل المعرفي وإيجاد الكورسات المطابقة تماماً لتفضيلاتك!"
  )

  if not expert_recommendations.empty:
    st.subheader("📌 المسارات والكورسات الموصى بها لك:")
    for index, row in expert_recommendations.iterrows():
      st.markdown(f"**🎓 {row['Course_Name']}**")
      st.write(
          f"- **التصنيف:** `{row['Category']}` | **المستوى:** `{row['Level']}`"
      )
      st.write(f"- **الوصف:** {row['Description']}")
      st.markdown("---")
  else:
    # خيار بديل ذكي في حال لم يوجد تطابق تام بالثلاث شروط
    st.warning(
        "⚠️ لم نجد تطابقاً كاملاً بالثلاث شروط، ولكن إليك أفضل الكورسات المتاحة في نفس المجال والمستوى:"
    )
    fallback_recommendations = df[
        (df["Category"] == selected_category)
        & (df["Level"] == selected_level)
    ]
    if not fallback_recommendations.empty:
      for index, row in fallback_recommendations.iterrows():
        st.markdown(f"**🎓 {row['Course_Name']}**")
        st.write(
            f"- **التصنيف:** `{row['Category']}` | **المستوى:** `{row['Level']}`"
        )
        st.write(f"- **الوصف:** {row['Description']}")
        st.markdown("---")
    else:
      # بديل نهائي في نفس المجال فقط
      general_recommendations = df[df["Category"] == selected_category]
      for index, row in general_recommendations.iterrows():
        st.markdown(f"**🎓 {row['Course_Name']}**")
        st.write(f"- **التصنيف:** `{row['Category']}`")
        st.write(f"- **الوصف:** {row['Description']}")
        st.markdown("---")
