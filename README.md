# Djangoでreactを動かすMPA構成サンプル

DjangoのtemplateでReactのコンポーネントを使用する様にしたサンプルです。
<br>
SPAではなく、MPAとして動作します。<br>
バージョン管理をpoetryで行う様にしています。<br>

### プロジェクト構成
Django<br>
・Django 4.2.2<br>
・Python 3.10.8<br>
・django-vite 2.1.3<br>
React<br>
・React 18.2.0<br>
・React Router 6.4.4<br>
・axios 1.4.0<br>
・Vite 3.2.7<br>
・TypeScript 4.9.5<br>

<br>

### よく使うコマンド

```
# poetryをインストールしていない場合は、最初にpoetryをインストール
pip install poetry

# poetryからモジュールをインストール  
poetry install

# poetryのシェル
poetry shell

# 起動コマンド
python manage.py runserver

# マイグレーション
python manage.py makemigrations

# DBに反映
python manage.py migrate

# poetryからrequirements.txtを出力したい時
poetry export --format requirements.txt --output requirements.txt

# requirements.txtから環境をインストール
pip install -r requirements.txt

# pipの一覧表示
pip list

# Reactの起動
npm run dev

# Reactの環境構築
npm install
```
<br>

```poetry```にPATHが通らない場合は、下記のリンクを参考にしてPATHを通してください<br>

https://pleiades.io/help/pycharm/poetry.html#84a89960


<br>


### 参考
Djangoの公式<br>
https://docs.djangoproject.com/ja/4.0/

Poetry<br>
https://cocoatomo.github.io/poetry-ja/

pysen<br>
https://github.com/pfnet/pysen

プロジェクト参考元<br>

https://thinkami.hatenablog.com/entry/2022/12/06/232643