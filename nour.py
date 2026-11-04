import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# إعداد الصفحة وتنسيقها
st.set_page_config(
    page_title="Smart Course Recommender", page_icon="🎓", layout="centered"
)

st.title("🎓 Smart Course Recommender")
st.write(
الأوامر الذكية لترشيح الكورسات الأكاديمية والمهنية بناءً على محتوى وصف الكورس.
)

# إنشاء قاعدة بيانات الكورسات مباشرة داخل الكود لضمان العمل الفوري
data = {
    "Course_Name": [
        "Python for Beginners",
        "Machine Learning A-Z",
        "Web Development Bootcamp",
        "Data Science Fundamentals",
        "Artificial Intelligence and Deep Learning",
        "Database Management Systems",
    ],
    "Category": [
        "Programming",
        "AI & Data",
        "Web Development",
        "AI & Data",
        "AI & Data",
        "Database",
    ],
    "Description": [
        "Learn python programming from scratch, variables, loops, and functions.",
        "Master machine learning algorithms, data preprocessing, and scikit-learn models.",
        "Build modern full-stack web applications using HTML, CSS, JavaScript, and backend tools.",
        "Learn data analysis, pandas, data visualization, and statistics fundamentals.",
        "Explore neural networks, computer vision, deep learning frameworks, and AI concepts.",
        "Understand SQL, relational databases, design, and efficient data querying.",
    ],
}

df = pd.DataFrame(data)

# استخدام TF-IDF وحساب التشابه (Content-based Filtering)
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["Description"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


# دالة الترشيح
def get_recommendations(title):
  idx = df[df["Course_Name"] == title].index[0]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1:4]  # أفضل 3 كورسات مشابهة
  course_indices = [i[0] for i in sim_scores]
  return df.iloc[course_indices]


# واجهة المستخدم على Streamlit
selected_course = st.selectbox(
    "اختر كورس تفضله لمعرفة كورسات مشابهة:", df["Course_Name"]
)

if st.button("عرض الترشيحات الذكية"):
  recommendations = get_recommendations(selected_course)
  st.success("تم إيجاد الكورسات المشابهة بنجاح بناءً على محتوى الكورس!")
  st.subheader("الكورسات المقترحة لك:")
  for index, row in recommendations.iterrows():
    st.markdown(f"**📌 {row['Course_Name']}** ({row['Category']})")
    st.write(f"الوصف: {row['Description']}")
    st.markdown("---")
