import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

DATA_FILE = "courses_data.csv"


# 1. دالة تنظيف وتوحيد النص العربي (Arabic Preprocessing)
def clean_arabic_text(text):
    if not isinstance(text, str):
        return ""
    # إزالة التشكيل والتطويل
    text = re.sub(r"[\u0617-\u061A\u064B-\u0652]", "", text)
    text = re.sub(r"ـ+", "", text)
    # توحيد الحروف
    text = re.sub(r"[إأآا]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ؤ", "ء", text)
    text = re.sub(r"ئ", "ء", text)
    text = re.sub(r"ة", "ه", text)
    # إزالة ال التعريف في بداية الكلمات والرموز الخاصة
    text = re.sub(r"\bال", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    return text.strip().lower()


# 2. إنشاء بيانات افتراضية لو الملف مش موجود
def create_default_data():
    data = {
        "title": [
            "أساسيات البرمجة بلغة بايثون",
            "كورس الذكاء الاصطناعي للمبتدئين",
            "تعلم معالجة اللغات الطبيعية NLP",
            "تحليل البيانات باستخدام Pandas و Python",
            "مقدمة في تعلم الآلة Machine Learning",
            "تطوير تطبيقات الويب بـ Flask",
        ],
        "category": [
            "البرمجة",
            "الذكاء الاصطناعي",
            "الذكاء الاصطناعي",
            "تحليل البيانات",
            "تعلم الآلة",
            "تطوير الويب",
        ],
        "description": [
            "تعلم بايثون من الصفر الشاملة المتغيرات والدوال والمصفوفات للمبتدئين",
            "مقدمة شاملة عن الذكاء الاصطناعي وتطبيقاته والشبكات العصبية",
            "معالجة النصوص العربية والانجليزية وتحليل المشاعر باستخدام NLP وبايثون",
            "تعلم تنظيف وتحليل البيانات واستخراج الإحصائيات بـ pandas و python",
            "شرح خوارزميات تعلم الآلة التصنيف والتوقع Machine Learning algorithms",
            "بناء مواقع وتطبيقات ويب خفيفة وسريعة باستخدام بايثون وفلاسك Flask",
        ],
        "level": [
            "مبتدئ",
            "مبتدئ",
            "متوسط",
            "مبتدئ",
            "متوسط",
            "مبتدئ",
        ],
        "link": [
            "https://example.com/python",
            "https://example.com/ai",
            "https://example.com/nlp",
            "https://example.com/data",
            "https://example.com/ml",
            "https://example.com/flask",
        ],
    }
    df = pd.DataFrame(data)
    df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
    return df


# تحميل البيانات
if not os.path.exists(DATA_FILE):
    df = create_default_data()
else:
    df = pd.read_csv(DATA_FILE)

# 3. إعداد واجهة Streamlit
st.set_page_config(
    page_title="نظام ترشيح الكورسات الذكي", page_icon="🎓", layout="wide"
)

st.title("🎓 نظام ترشيح المصادر التعليمية الذكي (Smart Recommender System)")
st.caption(
    "مشروع يعتمد على معالجة اللغات الطبيعية (NLP) وخوارزمية Cosine Similarity لترشيح الكورسات."
)
st.write("---")

# القائمة الجانبية (Sidebar) للفلاتر ورفع الملفات
st.sidebar.header("⚙️ لوحة التحكم والفلاتر")

# رفع ملف CSV جديد
uploaded_file = st.sidebar.file_uploader(
    "رفع قاعدة بيانات جديدة (CSV):", type=["csv"]
)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
    st.sidebar.success("تم تحديث البيانات بنجاح!")

# إمكانية إضافة كورس جديد من الواجهة
with st.sidebar.expander("➕ إضافة كورس جديد"):
    new_title = st.text_input("اسم الكورس")
    new_cat = st.selectbox(
        "المجال",
        ["البرمجة", "الذكاء الاصطناعي", "تحليل البيانات", "تعلم الآلة", "عام"],
    )
    new_desc = st.text_area("وصف الكورس")
    new_level = st.selectbox("المستوى", ["مبتدئ", "متوسط", "متقدم"])
    new_link = st.text_input("الرابط", "https://example.com")

    if st.button("حفظ الكورس"):
        if new_title and new_desc:
            new_row = {
                "title": new_title,
                "category": new_cat,
                "description": new_desc,
                "level": new_level,
                "link": new_link,
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=False)
            df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
            st.sidebar.success("تمت الإضافة بنجاح!")
            st.rerun()

# فلاتر التصفية
st.sidebar.write("---")
categories = ["الكل"] + list(df["category"].unique())
selected_category = st.sidebar.selectbox("تصفية حسب المجال:", categories)

levels = ["الكل"] + list(df["level"].unique())
selected_level = st.sidebar.selectbox("تصفية حسب المستوى:", levels)

# 4. الواجهة الرئيسية والبحث
col1, col2 = st.columns([3, 1])

with col1:
    user_query = st.text_input(
        "🔍 ماذا تريد أن تتعلم اليوم؟",
        placeholder="مثال: بايثون للمبتدئين، معالجة نصوص، تحليل البيانات...",
    )

with col2:
    num_recommendations = st.number_input(
        "عدد النتائج:", min_value=1, max_value=10, value=3
    )

if st.button("بحث وترشيح"):
    if not user_query.strip():
        st.warning("الرجاء كتابة كلمة البحث أولاً.")
    else:
        # تطبيق الفلاتر أولاً على البيانات
        filtered_df = df.copy()
        if selected_category != "الكل":
            filtered_df = filtered_df[
                filtered_df["category"] == selected_category
            ]
        if selected_level != "الكل":
            filtered_df = filtered_df[filtered_df["level"] == selected_level]

        if filtered_df.empty:
            st.error("لا توجد كورسات تطابق الفلاتر المحددة!")
        else:
            # دمج النصوص وتنظيفها
            filtered_df["combined"] = (
                filtered_df["title"]
                + " "
                + filtered_df["category"]
                + " "
                + filtered_df["description"]
            )
            cleaned_corpus = [
                clean_arabic_text(text)
                for text in filtered_df["combined"].tolist()
            ]
            cleaned_query = clean_arabic_text(user_query)

            # تحويل النصوص إلى Vector عبر TF-IDF
            vectorizer = TfidfVectorizer()
            all_texts = cleaned_corpus + [cleaned_query]
            tfidf_matrix = vectorizer.fit_transform(all_texts)

            # حساب التشابه Cosine Similarity
            cosine_sim = cosine_similarity(
                tfidf_matrix[-1], tfidf_matrix[:-1]
            ).flatten()

            # ترتيب النتائج
            related_indices = cosine_sim.argsort()[::-1][:num_recommendations]

            st.subheader("📌 النتائج والمرشحات الأكثر تطابقاً:")
            st.write("---")

            found = False
            for idx in related_indices:
                score = cosine_sim[idx]
                if score > 0:  # عرض الكورسات ذات التشابه الإيجابي فقط
                    found = True
                    row = filtered_df.iloc[idx]
                    with st.container():
                        st.markdown(f"### 📘 {row['title']}")
                        st.write(
                            f"**المجال:** {row['category']} | **المستوى:** {row['level']}"
                        )
                        st.write(f"**الوصف:** {row['description']}")
                        st.write(f"**نسبة التطابق الذكي:** `{int(score * 100)}%`")
                        st.markdown(f"[🔗 رابط المصدر]({row['link']})")
                        st.write("---")

            if not found:
                st.info(
                    "لم نجد كورسات متطابقة تماماً. جرب استخدام كلمات مفتاحية أخرى."
                )

# عرض كل البيانات المتاحة أسفل الصفحة
with st.expander("📋 عرض جميع الكورسات المسجلة في النظام"):
    st.dataframe(df[["title", "category", "level", "description"]])