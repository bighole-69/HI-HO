import streamlit as st
import random

st.set_page_config(page_title="게임 장르 추천기 (완전체)", page_icon="🎮", layout="wide")

st.title("🎮 게임 장르 기반 추천기 — 완전체")
st.write("장르를 선택하면 해당 장르의 추천 게임 5개를 보여줍니다. 전체에서 랜덤 3개도 받아볼 수 있어요!")

# -----------------------
# 데이터: 9개 장르 × 5개 게임
# 각 항목: title, desc, score, good_for, strength, image
# -----------------------
game_data = {
    "RPG": [
        {"title": "메타포: 리판타지오",
         "desc": "왕위 계승과 사회 갈등을 배경으로 한 서사 중심 JRPG. 턴·실시간 혼합 전투와 아키타입 성장 시스템이 특징.",
         "score": "Steam: Very Positive | Metacritic: 94",
         "good_for": "서사와 전략적 전투를 즐기는 플레이어",
         "strength": "깊은 세계관, 전략적 전투, 음악",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/2679460/header.jpg"},

        {"title": "더 위쳐 3",
         "desc": "광대한 오픈월드에서 숙련된 괴물 사냥꾼의 이야기를 따라가는 성인 판타지 RPG.",
         "score": "Steam: Overwhelmingly Positive | Metacritic: 93",
         "good_for": "깊은 스토리와 선택을 좋아하는 사람",
         "strength": "풍부한 퀘스트, 선택 효과",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/292030/header.jpg"},

        {"title": "페르소나 5 ロイヤル",
         "desc": "학생의 일상과 괴도단 활동을 오가며 전투와 인간관계를 병행하는 독특한 JRPG.",
         "score": "Steam: Very Positive | Metacritic: 95",
         "good_for": "캐릭터성과 연출을 즐기는 사람",
         "strength": "스타일, 캐릭터성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1687950/header.jpg"},

        {"title": "발더스 게이트 3",
         "desc": "D&D 기반으로 깊은 선택지와 파티 상호작용을 제공하는 최신 전략 RPG.",
         "score": "Steam: Overwhelmingly Positive | Metacritic: 96",
         "good_for": "자유도 높은 스토리와 전략을 즐기는 사람",
         "strength": "선택 자유도, 파티 시너지",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1086940/header.jpg"},

        {"title": "파이널 판타지 XIV",
         "desc": "스토리 중심의 MMORPG로 확장팩마다 새로운 모험을 제공하는 장기형 온라인 RPG.",
         "score": "Steam: Very Positive | Metacritic: 90",
         "good_for": "협력 플레이와 긴 스토리를 즐기는 사람",
         "strength": "메인 스토리, 레이드 콘텐츠",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/39210/header.jpg"}
    ],

    "오픈월드": [
        {"title": "젤다의 전설: 브레스 오브 더 와일드",
         "desc": "환경과 물리 상호작용을 통한 자유로운 탐험이 중심인 오픈월드 명작.",
         "score": "콘솔 전용 | Metacritic: 97",
         "good_for": "자유 탐험을 즐기는 사람",
         "strength": "창의적 탐험, 물리 시스템",
         "image": "https://upload.wikimedia.org/wikipedia/en/0/0b/The_Legend_of_Zelda_Breath_of_the_Wild.jpg"},

        {"title": "엘든 링",
         "desc": "광대한 오픈월드와 도전적인 전투가 결합된 액션 RPG로, 탐험과 보스전이 핵심.",
         "score": "Steam: Very Positive | Metacritic: 96",
         "good_for": "탐험·난도 높은 전투를 즐기는 사람",
         "strength": "보스 디자인, 자유도",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1245620/header.jpg"},

        {"title": "레드 데드 리뎀션 2",
         "desc": "서부 시대의 섬세한 연출과 서사가 돋보이는 오픈월드 서사 게임.",
         "score": "Steam: Very Positive | Metacritic: 97",
         "good_for": "느긋한 몰입형 서사를 좋아하는 사람",
         "strength": "사실적 연출, 스토리",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1174180/header.jpg"},

        {"title": "GTA V",
         "desc": "도시를 무대로 한 자유도 높은 플레이와 풍부한 활동이 가능한 오픈월드.",
         "score": "Steam: Very Positive | Metacritic: 97",
         "good_for": "자유로운 놀이를 원하는 사람",
         "strength": "콘텐츠 다양성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/271590/header.jpg"},

        {"title": "호라이즌 제로 던",
         "desc": "기계 생물과의 전투가 중심인 미려한 그래픽의 오픈월드 액션 RPG.",
         "score": "Steam: Very Positive | Metacritic: 89",
         "good_for": "SF 배경·사냥 전투를 좋아하는 사람",
         "strength": "전투, 비주얼",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1151640/header.jpg"}
    ],

    "FPS": [
        {"title": "DOOM Eternal",
         "desc": "광속 같은 전투 리듬과 강렬한 타격감이 특징인 하이퍼 FPS.",
         "score": "Steam: Very Positive | Metacritic: 88",
         "good_for": "속도감 있는 격투형 FPS를 좋아하는 사람",
         "strength": "속도감·타격감",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/782330/header.jpg"},

        {"title": "레인보우 식스 시즈",
         "desc": "전술과 정보전 중심의 팀 기반 FPS로, 전략적 플레이가 핵심.",
         "score": "Steam: Very Positive | Metacritic: 79",
         "good_for": "전술적 팀워크와 계획을 즐기는 사람",
         "strength": "전술성, 협동",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/359550/header.jpg"},

        {"title": "CS2",
         "desc": "정밀한 에임과 맵 컨트롤이 중요한 클래식한 경쟁 FPS.",
         "score": "Steam: Mixed | Metacritic: N/A",
         "good_for": "정밀 조작과 경쟁을 좋아하는 사람",
         "strength": "에임 기반 경쟁성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/header.jpg"},

        {"title": "오버워치 2",
         "desc": "다양한 영웅의 역할과 스킬 조합으로 팀플레이를 즐기는 히어로 FPS.",
         "score": "Steam: Mixed | Metacritic: 79",
         "good_for": "캐릭터 기반 팀전을 즐기는 사람",
         "strength": "영웅 다양성, 팀플레이",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/2357570/header.jpg"},

        {"title": "메트로 엑소더스",
         "desc": "포스트아포칼립스 분위기 속에서 스토리와 생존 요소가 어우러진 FPS.",
         "score": "Steam: Very Positive | Metacritic: 82",
         "good_for": "스토리 중심 FPS를 원하는 사람",
         "strength": "분위기·스토리",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/412020/header.jpg"}
    ],

    "액션": [
        {"title": "갓 오브 워: 라그나로크",
         "desc": "서사와 강렬한 근접전투가 결합된 액션 어드벤처의 대표작.",
         "score": "Steam: Very Positive | Metacritic: 94",
         "good_for": "전투와 서사를 동시에 즐기는 사람",
         "strength": "전투 연출·스토리",
         "image": "https://upload.wikimedia.org/wikipedia/en/7/7f/God_of_War_Ragnar%C3%B6k_cover.jpg"},

        {"title": "세키로: 섀도우즈 다이 트와이스",
         "desc": "정교한 패링과 타이밍을 요구하는 높은 난도의 액션 게임.",
         "score": "Steam: Very Positive | Metacritic: 90",
         "good_for": "고난도 액션과 기술적 도전을 즐기는 사람",
         "strength": "패링 시스템·난이도",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/814380/header.jpg"},

        {"title": "데빌 메이 크라이 5",
         "desc": "콤보와 연출 중심의 스타일리시 액션 게임. 손맛이 좋음.",
         "score": "Steam: Very Positive | Metacritic: 89",
         "good_for": "콤보 액션과 연출을 즐기는 사람",
         "strength": "콤보 시스템·연출",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/601150/header.jpg"},

        {"title": "하데스",
         "desc": "로그라이크 요소를 가진 액션 게임으로, 반복 플레이의 재미와 서사가 잘 어우러짐.",
         "score": "Steam: Overwhelmingly Positive | Metacritic: 93",
         "good_for": "빠른 반복 플레이와 빌드 구성을 좋아하는 사람",
         "strength": "중독성있는 반복성·연출",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1145360/header.jpg"},

        {"title": "고스트 오브 쓰시마",
         "desc": "사무라이의 미학과 잠입·전투가 조화된 오픈 전투형 액션 어드벤처.",
         "score": "Steam: Very Positive | Metacritic: 87",
         "good_for": "사무라이 분위기와 연출을 좋아하는 사람",
         "strength": "연출·전투 디자인",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1245620/library_600x900.jpg"}
    ],

    "전략": [
        {"title": "문명 VI",
         "desc": "자신의 문명을 건설해 과학·문화·전쟁으로 승리를 쟁취하는 턴제 전략 게임.",
         "score": "Steam: Very Positive | Metacritic: 88",
         "good_for": "긴 호흡의 전략과 계획을 좋아하는 사람",
         "strength": "전략 깊이·다양한 승리 조건",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/289070/header.jpg"},

        {"title": "스타크래프트 II",
         "desc": "실시간 전략의 클래식, 빠른 판단과 멀티태스킹이 핵심.",
         "score": "Blizzard: 명성있는 타이틀 | Metacritic: 93",
         "good_for": "빠른 전략 판단과 경쟁을 즐기는 사람",
         "strength": "경쟁성·균형감",
         "image": "https://upload.wikimedia.org/wikipedia/en/2/2d/StarCraft_II_-_Box_Art.jpg"},

        {"title": "토탈 워: 삼국",
         "desc": "턴제 캠페인과 실시간 대규모 전투가 결합된 역사 전략 게임.",
         "score": "Steam: Very Positive | Metacritic: 85",
         "good_for": "대규모 전투와 전략을 즐기는 사람",
         "strength": "전투 스케일·전략성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/779340/header.jpg"},

        {"title": "크루세이더 킹즈 III",
         "desc": "가문을 중심으로 정치·혼인·암투를 통한 중세 시대 생존 전략 게임.",
         "score": "Steam: Very Positive | Metacritic: 85",
         "good_for": "정치적 시뮬레이션과 스토리 지향 전략을 즐기는 사람",
         "strength": "정치·스토리 요소",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1158310/header.jpg"},

        {"title": "플레닛사이드 2",
         "desc": "대규모 지속 전투를 특징으로 하는 MMO 규모의 전략·FPS 하이브리드(전략성 강조).",
         "score": "Steam: Very Positive",
         "good_for": "대규모 전투와 연합 전술을 즐기는 사람",
         "strength": "스케일·전술",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1322190/header.jpg"}
    ],

    "로그라이크": [
        {"title": "데드 셀",
         "desc": "빠른 템포와 액션 중심의 로그라이크, 반복 플레이로 실력이 쌓인다.",
         "score": "Steam: Overwhelmingly Positive | Metacritic: 89",
         "good_for": "속도감과 도전을 즐기는 사람",
         "strength": "조작성·재시도 가치",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/460690/header.jpg"},

        {"title": "슬레이 더 스파이어",
         "desc": "덱 빌딩형 로그라이크로 전략적 선택이 중요한 게임.",
         "score": "Steam: Very Positive | Metacritic: 89",
         "good_for": "카드 전략과 확장성을 좋아하는 사람",
         "strength": "전략성·리플레이성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/646570/header.jpg"},

        {"title": "리스크 오브 레인 2",
         "desc": "협동 요소가 있는 3D 로그라이크 슈터로 캐릭터별 플레이가 다채롭다.",
         "score": "Steam: Very Positive | Metacritic: 85",
         "good_for": "협동 플레이와 빠른 성장감을 원하는 사람",
         "strength": "아이템 조합·협동성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/632360/header.jpg"},

        {"title": "하데스",
         "desc": "그리스 신화를 바탕으로 한 액션 로그라이크, 빌드 조합의 재미가 크다.",
         "score": "Steam: Overwhelmingly Positive | Metacritic: 93",
         "good_for": "빌드 구성과 스토리 요소를 함께 즐기고 싶은 사람",
         "strength": "중독성·연출",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1145360/header.jpg"},

        {"title": "엔터 더 건전",
         "desc": "탄막과 샷건 감각이 조합된 로그라이크 던전 슈터.",
         "score": "Steam: Very Positive | Metacritic: 84",
         "good_for": "리듬감 있는 탄막 회피와 성장을 즐기는 사람",
         "strength": "무기 다양성·도전성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/311210/header.jpg"}
    ],

    "시뮬레이션": [
        {"title": "심즈 4",
         "desc": "인물과 집, 삶의 이벤트를 자유롭게 구성하는 일상 시뮬레이션.",
         "score": "Steam: Very Positive | Metacritic: 85",
         "good_for": "창의적 커스터마이징과 느긋한 플레이를 좋아하는 사람",
         "strength": "자유도·커스터마이징",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1222670/header.jpg"},

        {"title": "시티즈: 스카이라인",
         "desc": "도로, 교통, 예산을 직접 설계해 자신만의 도시를 만드는 도시 경영 시뮬.",
         "score": "Steam: Very Positive | Metacritic: 85",
         "good_for": "도시 설계와 시스템을 좋아하는 사람",
         "strength": "모듈성·시뮬레이션 깊이",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/255710/header.jpg"},

        {"title": "플래닛 주",
         "desc": "동물원 경영 시뮬레이션으로 전시와 동물 복지를 관리하는 재미가 있다.",
         "score": "Steam: Very Positive | Metacritic: 81",
         "good_for": "관리형 시뮬과 꾸미기를 좋아하는 사람",
         "strength": "디테일·꾸미기",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/443150/header.jpg"},

        {"title": "파밍 시뮬레이터 22",
         "desc": "현실적인 농장 운영과 기계 운용을 체험할 수 있는 시뮬레이션.",
         "score": "Steam: Very Positive | Metacritic: 78",
         "good_for": "느긋한 운영과 수집을 좋아하는 사람",
         "strength": "현실감·관리성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1237970/header.jpg"},

        {"title": "풋볼 매니저 2024",
         "desc": "팀 운영과 전술 설정을 통해 클럽을 성장시키는 축구 감독 시뮬레이션.",
         "score": "Steam: Very Positive | Metacritic: 85",
         "good_for": "데이터 기반 전술과 팀 관리를 좋아하는 사람",
         "strength": "데이터·전술 관리",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1074100/header.jpg"}
    ],

    "인디": [
        {"title": "스타듀 밸리",
         "desc": "농장 운영, 마을 사람들과의 교류, 광산 탐험 등 힐링 요소가 많은 인디 게임.",
         "score": "Steam: Overwhelmingly Positive | Metacritic: 89",
         "good_for": "힐링형 플레이와 루틴을 즐기는 사람",
         "strength": "힐링·자유도",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg"},

        {"title": "할로우 나이트",
         "desc": "음울하지만 아름다운 2D 탐험 액션으로 난도와 보상이 균형잡힌 작품.",
         "score": "Steam: Overwhelmingly Positive | Metacritic: 90",
         "good_for": "도전적 탐험과 분위기를 즐기는 사람",
         "strength": "아트·탐험성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/367520/header.jpg"},

        {"title": "셀레스트",
         "desc": "정교한 점프와 컨트롤이 요구되는 플랫포머로 감정 서사도 깊다.",
         "score": "Steam: Very Positive | Metacritic: 94",
         "good_for": "컨트롤 도전과 서사를 좋아하는 사람",
         "strength": "정밀한 조작·스토리",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/504230/header.jpg"},

        {"title": "언더테일",
         "desc": "선택에 따라 변화하는 이야기와 독특한 연출로 사랑받는 인디 RPG.",
         "score": "Steam: Very Positive | Metacritic: 92",
         "good_for": "스토리와 연출을 중시하는 사람",
         "strength": "감성·연출",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/391540/header.jpg"},

        {"title": "바바 이즈 유",
         "desc": "게임 규칙 자체를 조작해 퍼즐을 푸는 독창적 콘셉트의 인디 게임.",
         "score": "Steam: Very Positive | Metacritic: 87",
         "good_for": "논리 퍼즐과 창의적 사고를 즐기는 사람",
         "strength": "창의적 규칙 조작",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/736260/header.jpg"}
    ],

    "퍼즐": [
        {"title": "Portal 2",
         "desc": "포탈로 공간을 연결해 문제를 해결하는 창의적 퍼즐 어드벤처.",
         "score": "Steam: Overwhelmingly Positive | Metacritic: 95",
         "good_for": "논리적 사고와 창의적 해결을 즐기는 사람",
         "strength": "퍼즐 디자인·유머",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/620/header.jpg"},

        {"title": "테트리스 이펙트",
         "desc": "음악과 비주얼이 결합된 몰입형 테트리스 경험을 제공하는 퍼즐 게임.",
         "score": "Steam: Very Positive | Metacritic: 89",
         "good_for": "리듬감과 몰입을 함께 즐기고 싶은 사람",
         "strength": "음악·몰입감",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/558100/header.jpg"},

        {"title": "더 위트니스",
         "desc": "섬 전체가 거대한 논리 퍼즐로 구성된 탐구형 퍼즐 게임.",
         "score": "Steam: Very Positive | Metacritic: 87",
         "good_for": "관찰력과 추론을 즐기는 사람",
         "strength": "탐구·논리성",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/210970/header.jpg"},

        {"title": "림보",
         "desc": "흑백 분위기의 미스테리한 플랫포머로 간결한 퍼즐과 연출이 돋보인다.",
         "score": "Steam: Very Positive | Metacritic: 88",
         "good_for": "분위기와 단순 퍼즐을 즐기는 사람",
         "strength": "연출·분위기",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/48000/header.jpg"},

        {"title": "바바 이즈 유 (퍼즐 장르 재배치)",
         "desc": "규칙을 직접 바꿔 풀어가는 독특한 퍼즐로, 사고의 전환을 요구한다.",
         "score": "Steam: Very Positive | Metacritic: 87",
         "good_for": "창의적 사고와 규칙 실험을 좋아하는 사람",
         "strength": "창의성·깊이",
         "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/736260/header.jpg"}
    ]
}

# -----------------------
# UI: 장르 선택 -> 2열 카드형 출력
# -----------------------
genres = list(game_data.keys())
selected_genre = st.selectbox("게임 장르를 선택하세요:", genres)

st.subheader(f"🎯 {selected_genre} 장르 추천 (5개)")

games = game_data[selected_genre]

# 두 열 레이아웃으로 카드 표시 (반씩)
for i, g in enumerate(games):
    # create two-column layout per item to keep consistent spacing
    col1, col2 = st.columns([1, 2])
    with col1:
        # 안전하게 이미지 로드 — 실패하면 빈 공간 표시
        try:
            st.image(g["image"], use_column_width=True)
        except:
            st.write("")  # 이미지 로드 실패 시 빈칸 유지
    with col2:
        st.markdown(f"### {g['title']}")
        st.write(g["desc"])
        st.write(f"**점수:** {g['score']}")
        st.write(f"**추천 대상:** {g['good_for']}")
        st.write(f"**장점:** {g['strength']}")
    st.markdown("---")

# -----------------------
# 랜덤 3개 추천 (전체 장르에서)
# -----------------------
st.subheader("🎲 전체에서 랜덤 게임 3개 추천")

if st.button("🔀 랜덤 3개 추천 받기"):
    # flatten all games
    all_games = []
    for lst in game_data.values():
        all_games.extend(lst)
    # sample 3 unique games
    sample_count = min(3, len(all_games))
    picks = random.sample(all_games, sample_count)

    # show picks in a row of three (responsive)
    cols = st.columns(len(picks))
    for col, g in zip(cols, picks):
        with col:
            try:
                st.image(g["image"], use_column_width=True)
            except:
                pass
            st.markdown(f"### {g['title']}")
            st.write(g["desc"])
            st.write(f"**점수:** {g['score']}")
            st.write(f"**장점:** {g['strength']}")
else:
    st.info("버튼을 눌러서 전체 장르에서 랜덤으로 3개의 게임을 추천받아보세요!")
