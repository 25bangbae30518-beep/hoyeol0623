import streamlit as st

st.set_page_config(page_title="귀멸의 칼날 상현 성격 테스트", page_icon="🌙")

st.title("🌙 귀멸의 칼날 상현 성격 테스트")
st.write("당신의 성향을 통해 어떤 상현 캐릭터와 가장 잘 맞는지 진단해드립니다!")

st.markdown("---")

# 질문 리스트
questions = [
    {
        "question": "1. 갈등 상황이 생기면 당신은?",
        "options": {
            "감정을 드러내지 않고 조용히 상황을 분석한다.": "kokushibo",
            "상대에게 친절하게 다가가며 감정을 부드럽게 중재한다.": "douma",
            "절대 물러서지 않고 정면으로 맞선다.": "akaza",
            "감정을 예술적으로 승화시키며 독창적인 방식으로 해결한다.": "gyokko"
        }
    },
    {
        "question": "2. 당신의 가장 큰 강점은?",
        "options": {
            "강한 집중력과 일관성": "kokushibo",
            "사교성, 유연한 사고, 분위기 파악 능력": "douma",
            "불굴의 투지와 강렬한 열정": "akaza",
            "창의력과 남들이 떠올리지 못하는 발상": "gyokko"
        }
    },
    {
        "question": "3. 사람들과의 관계에서 당신은?",
        "options": {
            "말보다는 행동과 묵직한 존재감으로 신뢰를 얻는다.": "kokushibo",
            "누구와도 쉽게 친해지고 다정하게 대한다.": "douma",
            "자신보다 약하거나 억울한 사람을 보면 돕고 싶어진다.": "akaza",
            "독특한 취향을 가진 사람들과 교류하는 것을 즐긴다.": "gyokko"
        }
    },
    {
        "question": "4. 중요한 결정을 내릴 때 당신은?",
        "options": {
            "철저하게 분석하고 장기적인 결과를 고려한다.": "kokushibo",
            "감정의 영향을 거의 받지 않고 실용적으로 판단한다.": "douma",
            "자신의 신념과 열정을 기반으로 즉각 결단한다.": "akaza",
            "본능적인 영감과 예술적 직감을 따른다.": "gyokko"
        }
    }
]

# 점수 초기화
scores = {
    "kokushibo": 0,
    "douma": 0,
    "akaza": 0,
    "gyokko": 0
}

answers = []

st.subheader("📋 질문")

# 질문 출력
for idx, q in enumerate(questions):
    st.write(f"### {q['question']}")
    choice = st.radio(
        "",
        list(q["options"].keys()),
        key=f"q_{idx}"
    )
    answers.append(choice)

# 결과 계산
if st.button("결과 보기"):
    for i, q in enumerate(questions):
        selected = answers[i]
        char = q["options"][selected]
        scores[char] += 1

    result = max(scores, key=scores.get)

    st.markdown("---")
    st.header("🔥 당신과 가장 잘 맞는 상현 캐릭터는…")

    if result == "kokushibo":
        st.subheader("🌙 **코쿠시보**")
        st.write("""
        깊고 무거운 성찰을 가진 당신은 조용하지만 누구보다 강한 내면을 지닌 사람입니다.  
        고독을 즐기고, 한 번 마음먹은 목표는 흔들리지 않는 집중력으로 밀고 나갑니다.
        """)
    elif result == "douma":
        st.subheader("❄️ **도우마**")
        st.write("""
        차분하고 친화적이며 감정적으로 흔들리지 않는 당신은  
        타인을 편안하게 만드는 능력을 지녔습니다.  
        이성적이고 가벼운 분위기를 즐기며 사람들과 자연스럽게 어울립니다.
        """)
    elif result == "akaza":
        st.subheader("🔥 **아카자**")
        st.write("""
        열정적이고 정의감이 강하며 쉽게 물러서지 않는 강단 있는 성격!  
        스스로의 신념을 중요시하고, 약한 이들을 보면 돕고 싶어 합니다.  
        강함을 추구하지만 따뜻한 면도 함께 지닌 타입입니다.
        """)
    elif result == "gyokko":
        st.subheader("🎨 **굣코**")
        st.write("""
        예술적 감각이 뛰어나며 독창적인 사고를 가진 창의적인 타입!  
        남들과 다른 시각에서 세상을 바라보고, 기발한 아이디어를 즐깁니다.  
        실험적이고 유니크한 것을 사랑합니다.
        """)

    st.markdown("---")
    st.write("🎉 친구에게 공유하고 비교해보세요!")

