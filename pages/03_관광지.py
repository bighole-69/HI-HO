import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지도 🌏", layout="wide")

st.title("🌆 외국인이 좋아하는 서울 관광지 Top 10 지도")
st.write("마커(빨간 아이콘)를 클릭하면 관광지 정보가 아래에 표시됩니다! 👇")

# 관광지 데이터 (이름, 위도, 경도, 설명, 지하철역)
places = [
    ("경복궁 🏯", 37.579617, 126.977041, "조선의 정궁으로 가장 대표적인 궁궐. 전통문화 체험도 가능함.", "🚇 경복궁역 (3호선) 5번 출구 도보 3분"),
    ("명동 쇼핑거리 🛍️", 37.563757, 126.982684, "외국인들이 가장 많이 찾는 쇼핑과 길거리 음식 중심지.", "🚇 명동역 (4호선) 도보 1분"),
    ("남산타워 (N서울타워) 🗼", 37.551169, 126.988227, "서울 전경을 감상할 수 있는 대표 전망 명소.", "🚇 명동역 (4호선) → 케이블카 이용"),
    ("홍대 거리 🎶", 37.557192, 126.923895, "젊음·예술·인디문화 중심지. 카페·공연·패션의 거리.", "🚇 홍대입구역 (2호선/공항철도) 도보 3분"),
    ("북촌 한옥마을 🏘️", 37.582604, 126.983998, "전통 한옥이 그대로 남아있는 조용하고 아름다운 동네.", "🚇 안국역 (3호선) 도보 5분"),
    ("동대문 디자인 플라자(DDP) 🏙️", 37.566295, 127.009308, "건축미와 전시·행사가 열리는 복합문화공간.", "🚇 동대문역사문화공원역 (2/4/5호선) 도보 1분"),
    ("광장시장 🍜", 37.570030, 127.000178, "빈대떡과 마약김밥으로 유명한 서울 대표 전통시장.", "🚇 종로5가역 (1호선) 도보 4분"),
    ("롯데월드타워 전망대 🏙️", 37.512558, 127.102623, "대한민국 최고층 빌딩, 서울 하늘을 볼 수 있는 전망 명소.", "🚇 잠실역 (2/8호선) 도보 3분"),
    ("청계천 🌿", 37.568941, 126.977220, "도심 속 자연이 흐르는 산책 힐링 명소.", "🚇 종각역 / 광화문역 / 을지로입구역 도보 접근 가능"),
    ("코엑스 아쿠아리움 🐠", 37.511307, 127.059019, "가족과 연인에게 인기 많은 실내 수족관.", "🚇 삼성역 (2호선) 도보 5분"),
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커에 식별 ID 태그 포함
for i, (name, lat, lon, desc, subway) in enumerate(places):
    folium.Marker(
        [lat, lon],
        tooltip=name,
        popup=name,  # 여기 popup의 텍스트가 ↓ 선택을 위한 key가 됨
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
map_data = st_folium(m, width=850, height=600)

# 선택된 관광지 찾기
selected_place = None
if map_data and map_data.get("last_object_clicked"):
    clicked_name = map_data["last_object_clicked"].get("popup")
    for place in places:
        if place[0] == clicked_name:
            selected_place = place
            break

# 상세정보 출력
st.subheader("📍 선택한 관광지 정보")

if selected_place:
    name, lat, lon, desc, subway = selected_place
    st.markdown(f"""
### {name}
- {desc}
- **가장 가까운 지하철역:** {subway}
    """)
else:
    st.write("👆 관광지 마커를 클릭하면 정보가 여기에 표시됩니다.")
