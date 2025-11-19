import streamlit as st
import random

st.set_page_config(page_title="게임 장르 추천기", layout="wide")

st.title("🎮 게임 장르 기반 추천기")
st.write("좋아하는 장르를 선택하면, 해당 장르의 추천 게임 5개를 보여줍니다.")

# 게임 데이터 (Metaphor: ReFantazio 최신 정보 반영)
game_data = {
    "RPG": [
        {
            "name": "Metaphor: ReFantazio",
            "who": "정치적 메시지, 깊은 세계관, JRPG 특유의 전략 전투를 즐기는 사람",
            "desc": (
                "Studio Zero가 제작한 본격 판타지 RPG로, 왕이 암살된 뒤 혼란에 빠진 왕국에서 "
                "왕위를 결정하기 위한 '선거전'이 벌어지는 독특한 세계를 담고 있습니다. "
                "플레이어는 엘다 부족 소년 '윌'이 되어 광대한 대륙을 여행하며 동료들을 모으고, "
                "직업(아키타입)을 성장시키며 전투 방식도 실시간 + 턴 기반이 섞인 독창적 구조를 가집니다. "
                "세계관 밀도, 음악, 캐릭터 표현 등이 특히 높게 평가받고 있습니다."
            ),
            "steam": "Very Positive",
            "meta": 94,
            "strength": "전략 + 실시간 혼합 전투, 풍부한 세계관, 강렬한 연출"
        },
        {
            "name": "더 위쳐 3",
            "who": "방대한 세계와 진중한 스토리를 좋아하는 사람",
            "desc": (
                "괴물 사냥꾼 게롤트의 여정을 중심으로 펼쳐지는 다층적인 스토리 RPG입니다. "
                "세계 곳곳의 사건들은 작은 선택조차 큰 변화를 만드는 구조로 설계되어 있어, "
                "여러 번 플레이해도 다른 흐름을 경험할 수 있는 장점이 있습니다."
            ),
            "steam": "Overwhelmingly Positive",
            "meta": 93,
            "strength": "몰입감 있는 스토리, 강력한 선택지, 높은 자유도"
        },
        {
            "name": "페르소나 5",
            "who": "캐릭터 중심 스토리와 스타일리시한 연출을 좋아하는 사람",
            "desc": (
                "도시 속 부조리와 왜곡된 욕망에 맞서는 ‘괴도단’의 이야기를 담은 JRPG로, "
                "학교 생활과 비일상적인 전투를 넘나드는 독특한 구조가 특징입니다. "
                "세련된 UI와 음악 연출이 높은 평가를 받습니다."
            ),
            "steam": "Overwhelmingly Positive",
            "meta": 95,
            "strength": "압도적인 스타일, 몰입감 있는 캐릭터성"
        },
        {
            "name": "파이널 판타지 14",
            "who": "긴 호흡의 MMORPG와 풍부한 시나리오를 좋아하는 사람",
            "desc": (
                "강렬한 스토리, 탄탄한 레이드 구조, 높은 자유도를 가진 글로벌 MMORPG입니다. "
                "특히 확장팩마다 새로운 세계와 테마가 추가되어 오랜 시간 즐길 수 있습니다."
            ),
            "steam": "Very Positive",
            "meta": 90,
            "strength": "대규모 스토리, 강력한 파티 플레이, 높은 완성도"
        },
        {
            "name": "드래곤즈 도그마 2",
            "who": "자유로운 탐험과 협력 전투를 좋아하는 사람",
            "desc": (
                "광활한 대지를 탐험하며 포획, 전투, 이동 요소가 유기적으로 이어지는 액션 RPG입니다. "
                "AI 동료 ‘폰’ 시스템으로 함께 싸우는 느낌이 강하며, 몬스터를 직접 타고 공격하는 등 "
                "전투의 손맛이 돋보입니다."
            ),
            "steam": "Mostly Positive",
            "meta": 80,
            "strength": "자유도 높은 탐험, 생동감 있는 전투"
        },
    ],

    "오픈월드": [
        {
            "name": "젤다의 전설 브레스 오브 더 와일드",
            "who": "탐험과 자유를 중요하게 여기는 사람",
            "desc": (
                "어떤 길로 가도 자유로운 거대한 필드를 배경으로, 플레이어의 창의성을 시험하는 퍼즐과 "
                "탐험 요소가 가득한 게임입니다."
            ),
            "steam": "– (Nintendo 전용)",
            "meta": 97,
            "strength": "압도적인 자유도, 뛰어난 퍼즐 디자인"
        },
        {
            "name": "GTA V",
            "who": "현대 도시 기반의 자유도 높은 게임을 좋아하는 사람",
            "desc": (
                "거대한 로스 산토스를 무대로, 스토리/액션/운전/총격 등이 뒤섞인 복합 오픈월드 게임입니다."
            ),
            "steam": "Very Positive",
            "meta": 97,
            "strength": "콘텐츠 방대함, 강한 자유도"
        },
        {
            "name": "레드 데드 리뎀션 2",
            "who": "서부극 분위기와 몰입감 있는 서사를 좋아하는 사람",
            "desc": (
                "몰락해가는 무법자 조직의 마지막 여정을 훌륭한 연출로 담아낸 작품입니다. "
                "광활한 자연과 디테일한 세계 표현이 특징입니다."
            ),
            "steam": "Very Positive",
            "meta": 97,
            "strength": "영화 같은 스토리, 사실적인 세계"
        },
        {
            "name": "원신",
            "who": "가벼운 탐험과 캐릭터 수집 요소를 좋아하는 사람",
            "desc": (
                "대륙을 여행하며 캐릭터를 수집하고 전투를 즐길 수 있는 애니 스타일 오픈월드 게임입니다."
            ),
            "steam": "Very Positive",
            "meta": 81,
            "strength": "캐릭터 다양성, 비주얼 완성도"
        },
        {
            "name": "호라이즌 제로 던",
            "who": "SF 세계관과 기계 생물을 좋아하는 사람",
            "desc": (
                "기계 생물이 지배한 세계에서, 활을 기반으로 한 전략적 전투를 통한 사냥 플레이가 중심입니다."
            ),
            "steam": "Very Positive",
            "meta": 89,
            "strength": "미려한 그래픽, 전략적 전투"
        }
    ],

    "FPS": [
        {"name": "오버워치 2", "who": "빠른 팀전 FPS를 좋아하는 사람",
         "desc": "영웅 기반의 팀 슈팅 게임으로 역할 조합과 협력이 중요합니다.",
         "steam": "Mixed", "meta": 79, "strength": "빠른 템포, 다양한 영웅"},

        {"name": "콜 오브 듀티 모던 워페어", "who": "현대전 FPS를 좋아하는 사람",
         "desc": "현실적인 무기 감각과 빠른 전투가 특징인 대표적인 FPS 시리즈입니다.",
         "steam": "Very Positive", "meta": 81, "strength": "타격감, 캠페인 완성도"},

        {"name": "레인보우 식스 시즈", "who": "전략 + FPS를 좋아하는 사람",
         "desc": "맵 파괴와 정보전이 핵심인 전술 FPS로 팀워크가 중요합니다.",
         "steam": "Very Positive", "meta": 79, "strength": "전략성, 협동성"},

        {"name": "CS2", "who": "정교한 에임 전투를 좋아하는 사람",
         "desc": "클래식한 팀전 전투를 현대적으로 재구성한 경쟁 FPS입니다.",
         "steam": "Mixed", "meta": 79, "strength": "정밀한 조작, e스포츠 기반"},

        {"name": "메트로 엑소더스", "who": "포스트 아포칼립스 FPS를 좋아하는 사람",
         "desc": "荒폐한 러시아 대지를 종단하며 펼쳐지는 스토리 중심 FPS입니다.",
         "steam": "Very Positive", "meta": 82, "strength": "분위기, 스토리" }
    ],

    "액션": [
        {"name": "세키로", "who": "도전적인 전투를 좋아하는 사람",
         "desc": "검술과 패링 중심의 고난도 액션 게임입니다.",
         "steam": "Very Positive", "meta": 90, "strength": "타격감, 긴장감"},

        {"name": "데빌메이크라이 5", "who": "콤보 액션을 좋아하는 사람",
         "desc": "세련된 전투 연출과 속도감 있는 기술표현이 특징입니다.",
         "steam": "Very Positive", "meta": 89, "strength": "콤보 시스템"},

        {"name": "하데스", "who": "빠른 템포의 액션 로그라이크를 좋아하는 사람",
         "desc": "지하세계 왕자의 탈출기를 그린 스타일리시 액션입니다.",
         "steam": "Overwhelmingly Positive", "meta": 93, "strength": "중독성, 연출"},

        {"name": "바이오네타", "who": "고속 액션과 판타지 전투를 좋아하는 사람",
         "desc": "마녀 베요네타의 화려한 전투를 중심으로 한 액션 게임입니다.",
         "steam": "Very Positive", "meta": 86, "strength": "화려함"},

        {"name": "고스트 오브 쓰시마", "who": "사무라이 세계와 몰입을 좋아하는 사람",
         "desc": "몽골 침략기를 배경으로 한 사실적 전투 중심의 액션입니다.",
         "steam": "Very Positive", "meta": 87, "strength": "연출, 전투감" }
    ],

    "전략": [
        {"name": "문명 6", "who": "긴 호흡의 전략 플레이를 좋아하는 사람",
         "desc": "하나의 문명을 이끌어 세계 지배를 목표로 하는 턴 전략 게임입니다.",
         "steam": "Very Positive", "meta": 88, "strength": "깊은 전략성"},

        {"name": "스타크래프트 2", "who": "빠른 멀티 전략을 좋아하는 사람",
         "desc": "3종족의 밸런스를 바탕으로 한 대표적인 RTS 게임입니다.",
         "steam": "–", "meta": 93, "strength": "전략 다양성"},

        {"name": "토탈 워: 삼국", "who": "대규모 전투를 좋아하는 사람",
         "desc": "실시간 전투와 전략 턴제가 조합된 대규모 전략 게임입니다.",
         "steam": "Very Positive", "meta": 85, "strength": "대규모 전투"},

        {"name": "유로파 유니버설리스4", "who": "역사 시뮬레이션 전략을 좋아하는 사람",
         "desc": "국가를 운영하며 외교·전쟁·무역을 총괄하는 깊은 전략 게임입니다.",
         "steam": "Very Positive", "meta": 87, "strength": "깊은 시스템"},

        {"name": "하츠 오브 아이언 4", "who": "전쟁 시뮬레이션을 좋아하는 사람",
         "desc": "2차 세계대전을 배경으로 한 병력·공업·전략 중심 게임입니다.",
         "steam": "Very Positive", "meta": 83, "strength": "세밀한 조정" }
    ],

    "로그라이크": [
        {"name": "데드 셀", "who": "빠른 액션을 좋아하는 사람",
         "desc": "유려한 움직임과 반복 도전이 핵심인 액션 로그라이크입니다.",
         "steam": "Overwhelmingly Positive", "meta": 89, "strength": "조작감"},

        {"name": "엔터 더 건전", "who": "탄막 액션을 좋아하는 사람",
         "desc": "탄막과 랜덤 요소가 강한 하드 난이도 로그라이크입니다.",
         "steam": "Overwhelmingly Positive", "meta": 84, "strength": "재미있는 패턴"},

        {"name": "리스크 오브 레인 2", "who": "빠른 성장과 전투를 좋아하는 사람",
         "desc": "빠르게 강해지며 몬스터를 쓰러뜨리는 3D 로그라이크입니다.",
         "steam": "Overwhelmingly Positive", "meta": 85, "strength": "성장감"},

        {"name": "슬레이 더 스파이어", "who": "카드 전략을 좋아하는 사람",
         "desc": "카드 덱을 구성하며 도전하는 전략 로그라이크 게임입니다.",
         "steam": "Overwhelmingly Positive", "meta": 89, "strength": "전략성"},

        {"name": "하데스", "who": "스토리 있는 로그라이크를 좋아하는 사람",
         "desc": "지하세계 탈출을 반복하며 스토리도 함께 발전하는 독특한 구조입니다.",
         "steam": "Overwhelmingly Positive", "meta": 93, "strength": "중독성" }
    ],

    "시뮬레이션": [
        {"name": "심즈 4", "who": "일상 꾸미기를 좋아하는 사람",
         "desc": "가상 세계에서 인물의 삶을 꾸미는 생활 시뮬레이션입니다.",
         "steam": "Very Positive", "meta": 70, "strength": "자유도"},

        {"name": "파밍 시뮬레이터 22", "who": "농장 운영을 좋아하는 사람",
         "desc": "농사를 짓고 수확과 판매를 반복하는 현실적인 농장 시뮬입니다.",
         "steam": "Very Positive", "meta": 78, "strength": "현실감"},

        {"name": "시티즈: 스카이라인", "who": "도시 건설을 좋아하는 사람",
         "desc": "자신만의 도시를 설계하고 관리하는 대규모 시티 빌더입니다.",
         "steam": "Very Positive", "meta": 85, "strength": "자유도"},

        {"name": "플래닛 주", "who": "동물 관리와 테마파크를 좋아하는 사람",
         "desc": "동물원을 직접 경영하며 관리하는 시뮬레이션입니다.",
         "steam": "Very Positive", "meta": 81, "strength": "디테일한 시스템"},

        {"name": "유로 트럭 시뮬레이터 2", "who": "여유로운 운전 게임을 좋아하는 사람",
         "desc": "유럽 전역을 트럭으로 누비는 힐링 운전 시뮬입니다.",
         "steam": "Overwhelmingly Positive", "meta": 79, "strength": "힐링감" }
    ],

    "인디": [
        {"name": "셀레스트", "who": "감정 서사와 고난도 플랫폼을 좋아하는 사람",
         "desc": "주인공의 심리적 성장과 도전을 그린 감성 인디 게임입니다.",
         "steam": "Overwhelmingly Positive", "meta": 94, "strength": "스토리"},

        {"name": "스타듀 밸리", "who": "편안한 농장 플레이를 좋아하는 사람",
         "desc": "농사, 채광, 낚시, 교류 등 다양한 활동을 즐길 수 있는 힐링 인디 게임입니다.",
         "steam": "Overwhelmingly Positive", "meta": 89, "strength": "자유도"},

        {"name": "언더테일", "who": "독특한 스토리 연출을 좋아하는 사람",
         "desc": "선택에 따라 완전히 다른 흐름이 펼쳐지는 감성 RPG입니다.",
         "steam": "Overwhelmingly Positive", "meta": 92, "strength": "유니크한 구성"},

        {"name": "할로우 나이트", "who": "메트로바니아 스타일을 좋아하는 사람",
         "desc": "광대한 지하 세계를 탐험하며 보스와 싸우는 액션 인디 게임입니다.",
         "steam": "Overwhelmingly Positive", "meta": 87, "strength": "도전성"},

        {"name": "하데스", "who": "빠른 액션과 반복 도전을 좋아하는 사람",
         "desc": "지하세계 탈출 스토리를 담은 액션 로그라이크 게임입니다.",
         "steam": "Overwhelmingly Positive", "meta": 93, "strength": "중독성" }
    ],

    "퍼즐": [
        {"name": "포탈 2", "who": "창의적 퍼즐을 좋아하는 사람",
         "desc": "포탈 건을 이용해 공간을 이동하며 퍼즐을 해결하는 독특한 구조입니다.",
         "steam": "Overwhelmingly Positive", "meta": 95, "strength": "창의성"},

        {"name": "바바 이즈 유", "who": "논리 퍼즐을 좋아하는 사람",
         "desc": "단어 규칙을 변경해 문제를 해결하는 혁신적 퍼즐 게임입니다.",
         "steam": "Overwhelmingly Positive", "meta": 87,
         "strength": "창의적 구조"},

        {"name": "림보", "who": "어두운 분위기의 퍼즐을 좋아하는 사람",
         "desc": "미니멀한 연출과 분위기로 퍼즐을 풀어가는 아트 스타일 게임입니다.",
         "steam": "Very Positive", "meta": 88, "strength": "감성"},

        {"name": "인사이드", "who": "감정 몰입을 좋아하는 사람",
         "desc": "무언가에 쫓기는 소년의 여정을 담은 퍼즐 플랫포머입니다.",
         "steam": "Overwhelmingly Positive", "meta": 93, "strength": "연출"},

        {"name": "테트리스 이펙트", "who": "요소 단순 + 몰입을 좋아하는 사람",
         "desc": "시각과 음악이 조화를 이루는 몰입형 퍼즐 게임입니다.",
         "steam": "Very Positive", "meta": 89, "strength": "몰입감" }
    ]
}


genres = list(game_data.keys())

# 장르 선택
selected_genre = st.selectbox("게임 장르를 선택하세요:", genres)

st.subheader(f"🎮 {selected_genre} 장르 추천 게임")

# 랜덤 장르 버튼
if st.button("🎲 랜덤 장르"):
    selected_genre = random.choice(genres)
    st.write(f"랜덤 선택된 장르: **{selected_genre}**")

# 랜덤 게임 버튼
if st.button("🔀 랜덤 게임 추천"):
    game = random.choice(game_data[selected_genre])
    st.subheader("오늘의 추천 게임 🎯")
    st.markdown(f"### **{game['name']}**")
    st.write(f"**어떤 사람에게 추천?** {game['who']}")
    st.write(f"**소개:** {game['desc']}")
    st.write(f"**Steam 평가:** {game['steam']}")
    st.write(f"**Metacritic 점수:** {game['meta']}")
    st.write(f"**장점:** {game['strength']}")
else:
    # 장르별 게임 리스트 출력
    for g in game_data[selected_genre]:
        st.markdown(f"### **{g['name']}**")
        st.write(f"**추천 대상:** {g['who']}")
        st.write(f"**소개:** {g['desc']}")
        st.write(f"**Steam 평가:** {g['steam']}")
        st.write(f"**Metacritic 점수:** {g['meta']}")
        st.write(f"**장점:** {g['strength']}")
        st.markdown("---")
