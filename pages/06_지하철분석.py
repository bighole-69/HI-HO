import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="지하철 이용 현황 분석", layout="wide")

st.title("🚇 2025년 10월 지하철 이용 현황 분석")

# CSV 로딩
@st.cache_data
def load_data():
    return pd.read_csv("subway.csv", encoding="cp949")

df = load_data()

# 날짜 변환
df["사용일자"] = pd.to_datetime(df["사용일자"], format="%Y%m%d")

# 2025년 10월만
october_data = df[df["사용일자"].dt.month == 10]
date_list = sorted(october_data["사용일자"].unique())

# UI
selected_date = st.selectbox(
    "날짜 선택",
    date_list,
    format_func=lambda x: pd.to_datetime(x).strftime("%Y-%m-%d")
)

selected_line = st.selectbox(
    "노선 선택",
    sorted(df["노선명"].unique())
)

# 선택 조건 반영
filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)].copy()

# 합산
filtered["총이용객"] = filtered["승차총승객수"] + filtered["하차총승객수"]

# 정렬
filtered = filtered.sort_values(by="총이용객", ascending=False).reset_index(drop=True)

st.subheader(f"{pd.to_datetime(selected_date).strftime('%Y-%m-%d')} · {selected_line} 이용객 순위")

# 색상 목록 (1위 파랑, 2위 노랑, 3위 빨강, 나머지 None)
color_map = {
    0: "blue",
    1: "yellow",
    2: "red"
}

# rank별 색상 부여
bar_colors = [color_map.get(i, None) for i in range(len(filtered))]

# Plotly 그래프
fig = px.bar(
    filtered,
    x="역명",
    y="총이용객",
    title=f"{selected_line} 승하차 총합 상위 역",
)

# trace 업데이트로 색상 적용
fig.update_traces(marker_color=bar_colors)

fig.update_layout(
    xaxis_title="역명",
    yaxis_title="총 이용객 수",
    template="simple_white"
)

st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블
st.dataframe(filtered[["역명", "승차총승객수", "하차총승객수", "총이용객"]])
