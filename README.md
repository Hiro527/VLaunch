# VLaunch
VALORANTの起動状況を検知してCLaunchを自動で起動/停止します。
CLaunchの影響でVALORANTが快適にプレイできない問題を解決できます。

動作イメージ動画: [YouTube](https://www.youtube.com/watch?v=5WK1WPt3qrg)
# メモ書き
- ~~ハイパー作り途中です。ベースは完成してるけどちょっとしょぼい~~
- 通知とかロゴとかいろいろ作ります: Done
- 設定で多少カスタムできるようにします: WIP
- exeにしてリリースします: Done
- そのうちGitHub Actionsでビルドを自動化します

# 使い方
1. ダウンロードした`VLaunch.exe`を好きな場所に置いてください。
2. exeファイルを実行すると、動作が開始します。

- VALORANTを検知すると自動でCLaunchがキルされます。
- VALORANTが検知されておらず、CLaunchも起動していない場合は自動でCLaunchを起動します。
- タスクトレイにあるアイコン<img src="./assets/img/VLaunch.svg" width="16px">を右クリックして終了することが出来ます。

# PC起動時に自動実行する方法
1. VLaunch.exeのショートカットを作成し、コピー(`Ctrl+C`)してください。
2. `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`にショートカットを貼り付けてください(`Ctrl+V`)
これで次回ログイン時からVLaunchが自動で起動します。

# ビルド方法
1. Anacondaなどの仮想環境を使用し、専用のインスタンスを建ててください。
2. インスタンス内で`requirements.txt`に従ってパッケージをインストールしてください。
```bash
$ pip install -r requirements.txt
```
3. 次のコマンドでビルドできます:
```bash
$ pyinstaller main.py --onefile --noconsole --icon="./assets/img/VLaunch.ico" --name VLaunch.exe --add-data="assets;assets"
```
4. ビルドの成果物は`dist/VLaunch.exe`に出力されています。
# 連絡先
Twitter: [@fps_Hiro527](https://twitter.com/fps_Hiro527)<br>
Discord: @Hiro527#7777