import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="지하철 이용 현황 분석", layout="wide")

st.title("🚇 2025년 10월 지하철 이용 현황 분석")

# CSV 파일 로딩 (상위 폴더)
@st.cache_data
def load_data():
    return pd.read_csv("../subway.csv", encoding="cp949")

df = load_data()

# 날짜 필터 (2025년 10월만)
df["사용일자"] = pd.to_datetime(df["사용일자"], format="%Y%m%d")
october_dates = sorted(df[df["사용일자"].dt.month == 10]["사용일자"].unique())

selected_date = st.selectbox("날짜 선택", october_dates, format_func=lambda x: x.strftime("%Y-%m-%d"))
selected_line = st.selectbox("노선 선택", sorted(df["노선명"].unique()))

# 선택된 조건 필터링
filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)].copy()

# 승하차 합계 컬럼 생성
filtered["총이용객"] = filtered["승차총승객수"] + filtered["하차총승객수"]

# 내림차순 정렬
filtered = filtered.sort_values(by="총이용객", ascending=False)

st.subheader(f"{selected_date.strftime('%Y-%m-%d')} / {selected_line} 이용객 상위 역")

# 색상 조합 (빨강, 파랑, 노랑 순환)
colors = ["red", "blue", "yellow"]

fig = px.bar(
    filtered,
    x="역명",
    y="총이용객",
    title=f"{selected_line} 이용객 순위 (승차+하차)",
    color="역명",
    color_discrete_sequence=colors * (len(filtered) // 3 + 1)
)

fig.update_layout(
    xaxis_title="역명",
    yaxis_title="총 이용객 수",
    legend_title="역명",
    template="simple_white"
)

st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블 표시
st.dataframe(filtered[["역명", "승차총승객수", "하차총승객수", "총이용객"]])
