import streamlit as st

def main():
    st.title("간단한 Streamlit 앱")

    # 사용자 입력을 받기
    user_input = st.text_input("이름을 입력하세요", "여기에 이름을 입력하세요")

    # 입력된 내용 출력
    st.write("안녕하세요,", user_input, "님!")

if __name__ == "__main__":
    main()
