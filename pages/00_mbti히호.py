import streamlit as st

# MBTI 별 추천 진로 데이터 (연봉 추가)
MBTI_CAREERS = {
    "ISTJ": [
        {
            "career": "공무원 / 행정직",
            "majors": ["행정학", "경영학", "법학"],
            "salary": "연 2,800만 ~ 4,000만 (초봉), 근속・직급에 따라 증가",
            "fit": "규칙적이고 책임감 강한 사람, 세부사항을 정확히 챙기는 걸 좋아하는 친구에게 잘 맞아요. ✍️"
        },
        {
            "career": "회계 / 세무",
            "majors": ["회계학", "경영학", "세무학"],
            "salary": "연 3,000만 ~ 5,000만 (초봉), 경력에 따라 크게 상승",
            "fit": "수치와 정리 정돈을 좋아하고 꾸준히 집중할 수 있는 타입에게 추천해요. 🧾"
        }
    ],
    "INFP": [
        {
            "career": "작가 / 콘텐츠 창작",
            "majors": ["문예창작", "국어국문학", "미디어커뮤니케이션"],
            "salary": "초기 수입 다양 (자기 브랜딩에 따라 연 0 ~ 1억 이상 가능)",
            "fit": "내면이 풍부하고 생각을 글로 풀어내는 걸 좋아하는 친구에게 잘 맞아요. ✒️"
        },
        {
            "career": "인권·문화예술 분야",
            "majors": ["사회학", "문화콘텐츠학", "인문학"],
            "salary": "연 2,500만 ~ 4,000만 수준 (기관과 역할에 따라 차이 큼)",
            "fit": "가치와 의미를 중시하고 창의적인 방식으로 표현하길 좋아하는 분께 추천해요. 🎭"
        }
    ],
    # 👉 나머지 MBTI는 필요하면 알려주면 같은 방식으로 추가해줄게!
}


def main():
    st.set_page_config(page_title="MBTI 진로 추천 💡", page_icon="🧭")
    st.title("MBTI로 찾는 진로 추천")
    st.write("MBTI를 골라봐! 그 유형에 잘 맞는 진로와 예상 연봉까지 보여줄게. 😊")

    mbti_list = list(MBTI_CAREERS.keys())
    mbti = st.selectbox("MBTI 선택", mbti_list)

    if st.button("추천 보기 👀"):
        careers = MBTI_CAREERS.get(mbti)
        if not careers:
            st.write("해당 MBTI 데이터가 없어요. 추가 요청 가능해! ✨")
            return

        st.subheader(f"{mbti} 유형의 추천 진로")
        for idx, item in enumerate(careers, start=1):
            st.markdown(f"### {idx}. {item['career']}")
            st.write(f"**추천 학과:** {', '.join(item['majors'])}")
            st.write(f"**예상 연봉:** {item['salary']}")
            st.write(f"**어떤 사람이 잘 맞을까?** {item['fit']}")
            st.write("---")

        st.info("연봉은 지역, 경력, 회사 규모, 본인의 실력에 따라 달라진다는 점 참고해줘! 😉")

    st.caption("진로는 MBTI가 전부가 아니에요. 경험과 흥미도 정말 중요해! 💫")


if __name__ == '__main__':
    main()
