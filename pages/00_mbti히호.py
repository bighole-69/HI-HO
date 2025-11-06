import streamlit as st

# MBTI to career mapping data
CAREER_DATA = {
    "INTJ": [
        {"career": "데이터 분석가", "department": "통계학, 컴퓨터공학, 산업공학", "fit": "논리적으로 문제를 분석하고 전략을 세우는 걸 좋아하는 사람", "salary": "연봉 약 4,000만원 ~ 7,000만원"},
        {"career": "전략기획가", "department": "경영학, 경제학", "fit": "큰 그림을 그리고 장기적 계획을 세우는 걸 잘하는 사람", "salary": "연봉 약 4,000만원 ~ 8,000만원"}
    ],
    "INTP": [
        {"career": "연구원", "department": "물리학, 화학, 컴퓨터공학", "fit": "원리와 개념을 깊게 파고드는걸 좋아하는 사람", "salary": "연봉 약 3,500만원 ~ 6,500만원"},
        {"career": "프로그래머", "department": "컴퓨터공학", "fit": "논리적으로 문제 해결하는 걸 즐기는 사람", "salary": "연봉 약 3,000만원 ~ 7,000만원"}
    ],
    "INFJ": [
        {"career": "심리 상담가", "department": "심리학과", "fit": "사람의 감정에 공감하고 깊게 이해하려는 사람", "salary": "연봉 약 3,000만원 ~ 5,000만원"},
        {"career": "사회복지사", "department": "사회복지학과", "fit": "타인을 돕는 것에서 보람을 느끼는 사람", "salary": "연봉 약 2,800만원 ~ 4,800만원"}
    ],
    "INFP": [
        {"career": "작가", "department": "문예창작과, 국문학과", "fit": "자신만의 감성과 이야기 표현을 좋아하는 사람", "salary": "연봉 약 2,500만원 ~ 5,000만원"},
        {"career": "예술가", "department": "미술학과, 디자인학과", "fit": "감정 표현과 창작 활동을 좋아하는 사람", "salary": "연봉 다양 (실력/활동에 따라 큰 차이)"}
    ],
    "ISTJ": [
        {"career": "공무원", "department": "행정학, 법학", "fit": "규칙과 절차를 잘 따르고 성실한 사람", "salary": "연봉 약 3,000만원 ~ 6,000만원"},
        {"career": "회계사", "department": "회계학, 경영학", "fit": "정확함과 꼼꼼함을 중요시하는 사람", "salary": "연봉 약 4,000만원 ~ 9,000만원"}
    ],
    "ISFJ": [
        {"career": "간호사", "department": "간호학과", "fit": "타인을 돕고 배려하는 성향이 강한 사람", "salary": "연봉 약 3,000만원 ~ 6,000만원"},
        {"career": "교사", "department": "교육학과", "fit": "학생을 보살피고 성장시키는 데 보람을 느끼는 사람", "salary": "연봉 약 3,000만원 ~ 6,000만원"}
    ],
    "ISTP": [
        {"career": "정비사", "department": "기계공학과", "fit": "만지작거리며 고치는 걸 좋아하는 사람", "salary": "연봉 약 3,000만원 ~ 5,500만원"},
        {"career": "엔지니어", "department": "기계/전기/전자공학", "fit": "문제를 실제로 해결하는 걸 즐기는 사람", "salary": "연봉 약 3,500만원 ~ 7,000만원"}
    ],
    "ISFP": [
        {"career": "디자이너", "department": "시각디자인, 산업디자인", "fit": "감각적이고 미적인 표현을 좋아하는 사람", "salary": "연봉 약 2,800만원 ~ 5,500만원"},
        {"career": "바리스타", "department": "특별 전공 요구 X", "fit": "차분하고 부드러운 분위기를 좋아하는 사람", "salary": "연봉 약 2,500만원 ~ 4,000만원"}
    ],
    "ENTJ": [
        {"career": "경영자", "department": "경영학, 경제학", "fit": "리더십 강하고 목표 지향적인 사람", "salary": "연봉 약 5,000만원 ~ 상한 없음"},
        {"career": "투자 분석가", "department": "경제학, 금융학", "fit": "결단력 있고 합리적 판단을 잘하는 사람", "salary": "연봉 약 4,000만원 ~ 1억원+"}
    ],
    "ENTP": [
        {"career": "기획자", "department": "미디어학, 경영학", "fit": "새로운 아이디어를 떠올리는 걸 즐기는 사람", "salary": "연봉 약 3,000만원 ~ 6,000만원"},
        {"career": "스타트업 창업자", "department": "무관", "fit": "도전과 변화를 즐기는 사람", "salary": "연봉 다양 (성공에 따라 매우 큼)"}
    ],
    "ENFJ": [
        {"career": "강사/교육자", "department": "교육학과", "fit": "사람들을 이끌고 소통 잘하는 사람", "salary": "연봉 약 3,000만원 ~ 6,000만원"},
        {"career": "홍보/커뮤니케이션 매니저", "department": "미디어/홍보학과", "fit": "타인을 동기부여하고 조화롭게 만드는 사람", "salary": "연봉 약 3,200만원 ~ 6,500만원"}
    ],
    "ENFP": [
        {"career": "크리에이터", "department": "무관", "fit": "아이디어 많고 표현하는 걸 좋아하는 사람", "salary": "연봉 다양"},
        {"career": "마케팅 기획자", "department": "경영학, 광고홍보학", "fit": "사람의 관심을 끌고 공감하는 걸 잘하는 사람", "salary": "연봉 약 3,000만원 ~ 6,500만원"}
    ],
    "ESTJ": [
        {"career": "프로젝트 매니저", "department": "경영학, 산업공학", "fit": "조직하고 실행하는 걸 잘하는 사람", "salary": "연봉 약 4,000만원 ~ 7,500만원"},
        {"career": "군 간부", "department": "국방 관련 학과", "fit": "책임감 강하고 규율을 중요시하는 사람", "salary": "연봉 약 3,000만원 ~ 7,000만원"}
    ],
    "ESFJ": [
        {"career": "유치원/초등 교사", "department": "교육학과", "fit": "따뜻하게 돌보고 소통 잘하는 사람", "salary": "연봉 약 3,000만원 ~ 6,000만원"},
        {"career": "간호/의료 보조직", "department": "보건계열", "fit": "사람을 돕는 데서 보람을 느끼는 사람", "salary": "연봉 약 2,800만원 ~ 5,500만원"}
    ],
    "ESTP": [
        {"career": "영업/세일즈", "department": "경영학, 무관 가능", "fit": "사람과 즉흥적으로 소통 잘하는 사람", "salary": "연봉 약 3,000만원 ~ 성과에 따라 크게 상승"},
        {"career": "스포츠 트레이너", "department": "체육학과", "fit": "직접 몸으로 활동하는걸 좋아하는 사람", "salary": "연봉 약 2,800만원 ~ 5,500만원"}
    ],
    "ESFP": [
        {"career": "연예인/공연 예술가", "department": "연극영화과, 무용과", "fit": "사람 앞에서 에너지 발산하는 걸 즐기는 사람", "salary": "연봉 매우 다양"},
        {"career": "이벤트 플래너", "department": "호텔관광, 이벤트 기획 관련", "st.title("🌟 MBTI 진로 추천 앱")

mbti = st.selectbox("MBTI를 선택해줘!", list(CAREER_DATA.keys()))

if mbti:
    st.write(f"### 당신의 MBTI **{mbti}** 에 어울리는 진로는...")

    jobs = CAREER_DATA[mbti]
    for job in jobs:
        st.write(f"---")
        st.write(f"#### 💼 직업 추천: **{job['career']}**")
        st.write(f"- 관련 학과: {job['department']}")
        st.write(f"- 이런 사람에게 잘 맞아요: {job['fit']}")
        st.write(f"- 예상 연봉: {job['salary']}")

st.write("\n✨ 너무 정답이라고 생각하지 말고 참고만 해줘! 자신에게 맞는 길은 직접 찾는거니까!")
