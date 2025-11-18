import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="지하철 이용 현황 분석", layout="wide")

st.title("🚇 2025년 10월 지하철 이용 현황 분석")

# CSV 파일 로딩 (프로젝트 최상위 폴더)
@st.cache_data
def load_data():
    return pd.read_csv("subway.csv", encoding="cp949")

# 디버깅용 파일 확인 기능 (필요하면 주석 해제)
# st.write("Current directory:", os.getcwd())
# st.write("Available files:", os.listdir())

df = load_data()

# 날짜를 datetime으로 변환
df["사용일자"] = pd.to_datetime(df["사용일자"], format="%Y%m%d")

# 2025년 10월만 필터
october_data = df[df["사용일자"].dt.month == 10]
date_list = sorted(october_data["사용일자"].unique())

# 날짜 & 노선 선택 UI
selected_date = st.selectbox(
    "날짜 선택",
    date_list,
    format_func=lambda x: pd.to_datetime(x).strftime("%Y-%m-%d")
)

selected_line = st.selectbox(
    "노선 선택",
    sorted(df["노선명"].unique())
)

# 선택 조건에 맞게 필터링
filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)].copy()

# 승하차 합산
filtered["총이용객"] = filtered["승차총승객수"] + filtered["하차총승객수"]

# 내림차순 정렬
filtered = filtered.sort_values(by="총이용객", ascending=False)

st.subheader(f"{pd.to_datetime(selected_date).strftime('%Y-%m-%d')} · {selected_line} 이용객 순위")

# 그래프 색상 정의
colors = ["red", "blue", "yellow"]

# Plotly 막대그래프 생성
fig = px.bar(
    filtered,
    x="역명",
    y="총이용객",
    title=f"{selected_line} 승하차 총합 TOP 역",
    color="역명",
    color_discrete_sequence=colors * (len(filtered) // 3 + 1)
)

fig.update_layout(
    xaxis_title="역명",
    yaxis_title="총 이용객 수",
    template="simple_white",
    legend_title="역명"
)

st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블 보기
st.dataframe(filtered[["역명", "승차총승객수", "하차총승객수", "총이용객"]])
