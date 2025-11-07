import streamlit as st
import folium
from streamlit_folium import st_folium
from math import sqrt

st.set_page_config(page_title="서울 관광지도 🌏", layout="wide")

st.title("🌆 외국인이 좋아하는 서울 관광지 Top 10 지도")
st.write("마커를 클릭하면 해당 관광지 정보가 아래에 표시됩니다! 👇")

# 관광지 데이터 (이름, 위도, 경도, 설명, 지하철역)
places = [
    ("경복궁 🏯", 37.579617, 126.977041, "조선의 정궁으로 가장 대표적인 궁궐. 전통문화 체험 가능.", "🚇 경복궁역 (3호선) 도보 3분"),
    ("명동 쇼핑거리 🛍️", 37.563757, 126.982684, "외국인 관광객들이 가장 많이 찾는 쇼핑 거리.", "🚇 명동역 (4호선) 도보 1분"),
    ("남산타워 🗼", 37.551169, 126.988227, "서울 전망 명소. 야경이 아름다움.", "🚇 명동역 → 케이블카 이용"),
    ("홍대 거리 🎶", 37.557192, 126.923895, "젊음·예술·공연문화 중심 지역.", "🚇 홍대입구역 (2호선) 도보 3분"),
    ("북촌 한옥마을 🏘️", 37.582604, 126.983998, "전통 한옥이 보존된 조용한 산책 명소.", "🚇 안국역 (3호선) 도보 5분"),
    ("DDP 🏙️", 37.566295, 127.009308, "현대적 건축미 + 전시/디자인 명소.", "🚇 동대문역사문화공원역 도보 1분"),
    ("광장시장 🍜", 37.570030, 127.000178, "빈대떡, 마약김밥 등 전통 먹거리 명소.", "🚇 종로5가역 (1호선) 도보 4분"),
    ("롯데월드타워 전망대 🏙️", 37.512558, 127.102623, "대한민국 최고층 빌딩 전망대.", "🚇 잠실역 (2/8호선) 도보 3분"),
    ("청계천 🌿", 37.568941, 126.977220, "도심 속 산책 힐링 명소.", "🚇 종각/광화문/을지로입구 도보 접근"),
    ("코엑스 아쿠아리움 🐠", 37.511307, 127.059019, "실내 수족관 데이트/가족 인기.", "🚇 삼성역 (2호선) 도보 5분"),
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
for name, lat, lon, desc, subway in places:
    folium.Marker(
        location=[lat, lon],
        tooltip=name,
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 표시 + 클릭 정보 받아오기
map_data = st_folium(m, width=850, height=600)

selected_place = None

# 마커 클릭했을 때만 처리
if map_data and map_data.get("last_object_clicked"):
    click_lat = map_data["last_object_clicked"]["lat"]
    click_lon = map_data["last_object_clicked"]["lng"]

    # 클릭 지점과 가장 가까운 관광지 계산
    selected_place = min(
        places,
        key=lambda p: sqrt((p[1] - click_lat) ** 2 + (p[2] - click_lon) ** 2)
    )

# 결과 출력 영역
st.subheader("📍 선택한 관광지 정보")

if selected_place:
    name, lat, lon, desc, subway = selected_place
    st.markdown(f"""
### {name}
- {desc}
- **가장 가까운 지하철역:** {subway}
    """)
else:
    st.write("👆 관광지 마커를 클릭해보세요!")
