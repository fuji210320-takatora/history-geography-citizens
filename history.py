import streamlit as st
import random

# 指定された節題のリスト
topics = [
    "2章 p24、人類の出現の進化",
    "2章 p34、旧石器時代と縄文時代の暮らし",
    "2章 p42、聖徳太子の政治改革",
    "3章 p66、武士の成長",
    "3章 p76、中世のユーラシア大陸",
    "4章 p100、ヨーロッパ世界の変化",
    "4章 p112、江戸幕府の成立と支配の仕組み",
    "4章 p124、農業や諸産業の発展",
    "5章 p146、イギリスとアメリカの革命",
    "5章 p156、欧米のアジア侵略",
    "5章 p166、新政府の成立",
    "5章 p184、欧米列強の侵略と条約改正",
    "6章 p204、第一次世界大戦",
    "6章 p212、大正デモクラシーと政党内閣の成立",
    "6章 p220、世界恐慌と各国の対策",
    "6章 p230、第二次世界大戦の始まり",
    "7章 p246、占領下の日本",
    "7章 p250、冷戦の開始と植民地の解放",
    "7章 p260、冷戦後の国際社会"
]

# 登録データを保持するための設定（画面が更新されてもデータが消えないようにする）
if 'registered_data' not in st.session_state:
    st.session_state['registered_data'] = []

st.title("歴史の課題 ランダム割り当て")

# 入力フォーム（登録ボタンを押すと入力欄がクリアされる設定）
with st.form("register_form", clear_on_submit=True):
    name = st.text_input("名前を入力してください (例: 山田太郎)")
    submitted = st.form_submit_button("登録")

    # 登録ボタンが押され、かつ名前が入力されている場合の処理
    if submitted and name:
        assigned_topic = random.choice(topics)
        # データをリストに追加
        st.session_state['registered_data'].append({
            "名前": name,
            "割り当てられたテーマ": assigned_topic
        })

st.header("登録された割り当て一覧")

# データがあれば表として表示
if st.session_state['registered_data']:
    st.table(st.session_state['registered_data'])
else:
    st.write("まだ誰も登録されていません。")
