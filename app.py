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

if "keep_going" not in st.session_state:
    st.session_state.keep_going = True
if "checked" not in st.session_state:
    st.session_state.checked = False
if "history" not in st.session_state:
    st.session_state.history = []

while st.session_state.keep_going:
    selected_color = st.selectbox("색상을 선택하세요:", colors)

    if st.button("알아보기"):
        st.session_state.checked = True
        comp_color = result_color(selected_color)
        st.session_state.history.append((selected_color, comp_color))

    if st.session_state.checked:
        comp_color = result_color(selected_color)
        st.success(
            f"사용자님이 고르신 **{selected_color}**색의 보색은"
            f" **{comp_color}**입니다."
        )

        st.write("---")
        st.write("계속하시겠습니까? (Y/N)")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Y (계속하기)"):
                st.session_state.checked = False
                st.rerun()
        with col2:
            if st.button("N (종료하기)"):
                st.session_state.keep_going = False
                st.rerun()

    break

if st.session_state.history:
    st.write("---")
    st.subheader("📜 지금까지 선택한 색상 기록")
    for idx, (sel, comp) in enumerate(st.session_state.history, 1):
        st.write(f"{idx}. **{sel}**색 ➔ 보색: **{comp}**")

if not st.session_state.keep_going:
    st.info("보색 가이드 앱을 종료합니다. 이용해 주셔서 감사합니다!")
    if st.button("다시 시작하기"):
        st.session_state.keep_going = True
        st.session_state.checked = False
        st.session_state.history = []
        st.rerun()
