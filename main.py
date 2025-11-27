import streamlit as st

st.set_page_config(page_title="Hollow Knight Silksong 성격 테스트", page_icon="🦗")

st.title("🦗 Hollow Knight: Silksong 성격 테스트")
st.write("선택지를 고르면 어떤 실크송 캐릭터와 가장 잘 맞는지 알려드립니다!")

st.markdown("---")

questions = [
    {
        "question": "1. 모험을 시작할 때 당신의 스타일은?",
        "options": {
            "A": ("정면 돌파! 도전을 두려워하지 않는다.", "hornet"),
            "B": ("분석부터 한다. 계획을 세워 신중하게 움직인다.", "shadewyrm"),
            "C": ("일단 주변부터 탐색하며 느긋하게 진행한다.", "lace"),
            "D": ("사람들과 함께 협력하며 조심스레 나아간다.", "shrumal")
        }
    },
    {
        "question": "2. 위기 상황이 왔을 때 당신은?",
        "options": {
            "A": ("즉시 행동해 해결하려고 한다.", "hornet"),
            "B": ("최악의 경우까지 상상하며 대응 전략을 세운다.", "shadewyrm"),
            "C": ("대담하게 돌파구를 만든다.", "lace"),
            "D": ("주변을 안정시키고 협동을 이끈다.", "shrumal")
        }
    },
    {
        "question": "3. 다른 이들과의 관계에서 당신은?",
        "options": {
            "A": ("독립적이지만 필요한 순간엔 강력한 동맹이 된다.", "hornet"),
            "B": ("조용하지만 깊은 신뢰를 쌓는다.", "shadewyrm"),
            "C": ("활발하고 경쟁적이며 분위기를 주도한다.", "lace"),
            "D": ("따뜻하고 배려심이 많아 모두를 돕는다.", "shrumal")
        }
    },
    {
        "question": "4. 당신의 장점은?",
        "options": {
            "A": ("강인함과 추진력", "hornet"),
            "B": ("지적 탐구심과 통찰력", "shadewyrm"),
            "C": ("카리스마와 에너지", "lace"),
            "D": ("이해심과 협력능력", "shrumal")
        }
    }
]

# 점수 저장
scores = {"hornet": 0, "shadewyrm": 0, "lace": 0, "shrumal": 0}

answers = []

st.subheader("📋 질문")

for idx, q in enumerate(questions):
    st.write(f"### {q['question']}")
    choice = st.radio(
        "",
        list(q["options"].keys()),
        key=f"q_{idx}"
    )
    answers.append(choice)

if st.button("결과 보기"):
    for i, q in enumerate(questions):
        char = q["options"][answers[i]][1]
        scores[char] += 1

    result = max(scores, key=scores.get)

    st.markdown("---")
    st.header("🧿 당신과 가장 잘 맞는 실크송 캐릭터는…")

    if result == "hornet":
        st.subheader("🕷️ **Hornet**")
        st.write("""
        결단력 있고 강인한 당신은 어떤 어려움도 헤쳐나갈 힘을 가진 타입입니다.
        독립적이면서도 필요한 순간엔 누구보다 강한 동료가 됩니다.
        """)
    elif result == "shadewyrm":
        st.subheader("🐉 **Shadewyrm**")
        st.write("""
        분석적이고 깊이 있는 사고를 가진 당신!
        겉으론 조용해 보여도 누구보다 상황을 꿰뚫어 보는 통찰력을 지녔습니다.
        """)
    elif result == "lace":
        st.subheader("🪡 **Lace**")
        st.write("""
        카리스마 넘치고 활발하며 대담한 타입!
        주변을 밝게 만들고 때로는 경쟁심으로 모두를 끌어올립니다.
        """)
    elif result == "shrumal":
        st.subheader("🍄 **Shrumal Warrior**")
        st.write("""
        따뜻하고 협동을 중시하는 당신은 모두가 의지하는 동료입니다.
        안정감과 배려로 팀을 하나로 만드는 조력자 타입!
        """)

    st.markdown("---")
    st.write("🎉 테스트를 공유해서 친구들과 비교해보세요!")

