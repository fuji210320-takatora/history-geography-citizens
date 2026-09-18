from flask import Flask, render_template_string, request, redirect, url_for
import random

app = Flask(__name__)

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

# 登録されたデータを保存するリスト（※アプリ終了時にリセットされます）
registered_data = []

# Webページの見た目（HTML）を定義
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>課題ランダム割り当てサイト</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
        th { background-color: #f8f9fa; }
        .form-container { margin-bottom: 30px; padding: 20px; background-color: #e9ecef; border-radius: 8px; }
        input[type="text"] { padding: 8px; font-size: 16px; width: 200px; }
        button { padding: 8px 16px; font-size: 16px; cursor: pointer; background-color: #007bff; color: white; border: none; border-radius: 4px; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <h1>歴史の課題 ランダム割り当て</h1>
    
    <div class="form-container">
        <form action="/add" method="post">
            <label for="name">名前を入力してください:</label>
            <input type="text" id="name" name="name" required placeholder="例: 山田太郎">
            <button type="submit">登録</button>
        </form>
    </div>

    <h2>登録された割り当て一覧</h2>
    <table>
        <tr>
            <th>名前</th>
            <th>割り当てられたテーマ</th>
        </tr>
        {% for item in data %}
        <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.topic }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def index():
    # トップページにアクセスした際、HTMLと登録データを表示
    return render_template_string(HTML_TEMPLATE, data=registered_data)

@app.route('/add', methods=['POST'])
def add():
    # フォームから送信された名前を取得
    name = request.form.get('name')
    if name:
        # 節題リストからランダムに1つを選択
        assigned_topic = random.choice(topics)
        # 取得した名前と選ばれたテーマをリストに保存
        registered_data.append({'name': name, 'topic': assigned_topic})
    
    # 処理が終わったらトップページに戻る
    return redirect(url_for('index'))

if __name__ == '__main__':
    # サーバーを起動
    app.run(debug=True)
