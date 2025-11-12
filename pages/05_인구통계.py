import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="서울시 인구 통계", layout="wide")

st.title("📊 서울시 자치구별 연령별 인구 통계")

@st.cache_data
def load_data():
    df = pd.read_csv("population.csv")
    # 천 단위 구분기호 제거 및 숫자 변환
    for col in df.columns:
        if df[col].dtype == "object":
            try:
                df[col] = df[col].str.replace(",", "").astype(float)
            except:
                pass
    return df

df = load_data()

# ✅ 행정구 컬럼 자동 탐색
possible_names = ["행정구", "자치구", "지역", "구", "행정구역", "지역명"]
region_col = None
for name in possible_names:
    if name in df.columns:
        region_col = name
        break

if not region_col:
    st.error("❌ CSV 파일에서 '행정구' 또는 비슷한 이름의 열을 찾을 수 없습니다.")
    st.write("컬럼 목록:", df.columns.tolist())
    st.stop()

regions = df[region_col].unique().tolist()
region = st.sidebar.selectbox("행정구 선택", regions)

st.subheader(f"🏙 {region} 인구 분포")

# ✅ 선택한 행정구 행
row = df[df[region_col] == region].squeeze()

# ✅ 연령대 컬럼 자동 탐색
age_columns_m = [col for col in df.columns if "남" in col and "~" in col]
age_columns_f = [col for col in df.columns if "여" in col and "~" in col]

if not age_columns_m or not age_columns_f:
    st.error("❌ 연령대별 남녀 인구 데이터 열을 찾을 수 없습니다.")
    st.write("현재 컬럼 목록:", df.columns.tolist())
    st.stop()

ages = [col.split("_")[-1] for col in age_columns_m]
male_pop = [row[col] for col in age_columns_m]
female_pop = [row[col] for col in age_columns_f]
total_pop = [m + f for m, f in zip(male_pop, female_pop)]

# ✅ Plotly 그래프
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=ages, y=male_pop, mode='lines+markers', name='남성',
    line=dict(color='blue', width=2)
))
fig.add_trace(go.Scatter(
    x=ages, y=female_pop, mode='lines+markers', name='여성',
    line=dict(color='lightgreen', width=2)
))
fig.update_layout(
    xaxis_title="연령대 (세)",
    yaxis_title="인구수 (명)",
    xaxis=dict(showgrid=True, dtick=10),
    yaxis=dict(showgrid=True, dtick=100),
    template="plotly_white",
    height=500,
)
st.plotly_chart(fig, use_container_width=True)

# ✅ 표 표시
table = pd.DataFrame({
    "연령대": ages,
    "남성": male_pop,
    "여성": female_pop,
    "총합": total_pop
})
st.dataframe(table, use_container_width=True)
