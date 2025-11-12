st.write("컬럼 이름 확인:", df.columns.tolist())
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="서울시 인구 통계", layout="wide")

st.title("📊 서울시 자치구별 연령별 인구 통계")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("population.csv")
    # object(문자열) 컬럼 중 숫자로 바꿀 수 있는 열만 변환
    for col in df.columns:
        if df[col].dtype == "object":
            try:
                df[col] = df[col].str.replace(",", "").astype(float)
            except Exception:
                pass  # 행정구 등 숫자가 아닌 열은 그냥 둔다
    return df

df = load_data()

# 행정구 선택
regions = df["행정구"].unique().tolist()
region = st.sidebar.selectbox("행정구 선택", regions)

st.subheader(f"🏙 {region} 인구 분포")

# 선택한 행정구 필터링
row = df[df["행정구"] == region].squeeze()

# 연령 컬럼 추출
age_columns_m = [col for col in df.columns if "남" in col and "~" in col]
age_columns_f = [col for col in df.columns if "여" in col and "~" in col]

ages = [col.split("_")[-1] for col in age_columns_m]
male_pop = [row[col] for col in age_columns_m]
female_pop = [row[col] for col in age_columns_f]
total_pop = [m + f for m, f in zip(male_pop, female_pop)]

# Plotly 그래프 생성
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=ages, y=male_pop, mode='lines+markers',
    name='남성', line=dict(color='blue', width=2)
))
fig.add_trace(go.Scatter(
    x=ages, y=female_pop, mode='lines+markers',
    name='여성', line=dict(color='lightgreen', width=2)
))
fig.add_trace(go.Scatter(
    x=ages, y=total_pop, mode='lines',
    name='총합', line=dict(color='gray', dash='dot', width=1.5)
))

fig.update_layout(
    xaxis_title="연령대",
    yaxis_title="인구수 (명)",
    xaxis=dict(showgrid=True, dtick=10),
    yaxis=dict(showgrid=True, dtick=100),
    template="plotly_white",
    height=500,
)

st.plotly_chart(fig, use_container_width=True)

# 표로 데이터 보여주기
table = pd.DataFrame({
    "연령대": ages,
    "남성": male_pop,
    "여성": female_pop,
    "총합": total_pop
})

st.dataframe(table, use_container_width=True)
