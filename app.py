import streamlit as st

colors = ["빨강", "주황", "노랑", "초록", "파랑"]


def result_color(color):
    if color == "빨강":
        return "초록"
    elif color == "주황":
        return "파랑"
    elif color == "노랑":
        return "보라"
    elif color == "초록":
        return "빨강"
    elif color == "파랑":
        return "주황"
    else:
        return "알 수 없음"


st.title("🎨 보색 가이드 웹 앱")
st.write("원하는 색상을 선택하고 **[알아보기]** 버튼을 눌러보세요!")

if "steps" not in st.session_state:
    st.session_state.steps = [
        {"selected": "빨강", "checked": False, "answer": None}
    ]

i = 0
while i < len(st.session_state.steps):
    step = st.session_state.steps[i]
    is_last = i == len(st.session_state.steps) - 1

    st.write("---")
    selected = st.selectbox(
        "색상을 선택하세요:",
        colors,
        index=colors.index(step["selected"]),
        key=f"select_{i}",
        disabled=not is_last,
    )
    step["selected"] = selected

    if st.button("알아보기", key=f"check_{i}", disabled=not is_last):
        step["checked"] = True

    if step["checked"]:
        comp_color = result_color(step["selected"])
        st.success(
            f"사용자님이 고르신 **{step['selected']}**색의 보색은"
            f" **{comp_color}**입니다."
        )
        st.write("계속하시겠습니까? (Y/N)")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Y", key=f"yes_{i}", disabled=not is_last):
                step["answer"] = "Y"
                st.session_state.steps.append(
                    {"selected": "빨강", "checked": False, "answer": None}
                )
                st.rerun()
        with col2:
            if st.button("N", key=f"no_{i}", disabled=not is_last):
                step["answer"] = "N"
                st.rerun()

        if step["answer"] == "N":
            st.info("보색 가이드 앱을 종료합니다. 이용해 주셔서 감사합니다!")
            if st.button("다시 시작하기", key="restart"):
                st.session_state.steps = [
                    {"selected": "빨강", "checked": False, "answer": None}
                ]
                st.rerun()
            break

    i += 1
