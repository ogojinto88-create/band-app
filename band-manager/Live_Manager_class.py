import json
#Livesクラスをインポート
from models import Lives
#ライブを管理するクラスを作成
class Live_Manager :
    def __init__(self):
        self.lives=[]
        self.load_lives()
    #①追加
    def create_live(self):
        live=Lives( '' , '' )
        for date_part in live.date:
            #日付をコンソールで入力
            value = input(f"{date_part}を入力：")
            live.date[date_part] = value
        #会場を入力
        live.venue=input('会場を入力：')
        #持ち時間を入力
        live.time=input('持ち時間を入力：')
        #演奏曲をコンソールで入力
        while True:
            song=input('演奏曲を入力（終了は終わり）：')
    
            #繰り返し修了の条件
            if song == '終わり':
                break
            live.songs.append(song)
        #パートの数だけ繰り返し(固定枠)
        for part in live.members:
            #メンバーをコンソールで入力
            name = input(f"{part}のメンバーを入力：")
            live.members[part] = name
        #追加枠
        while True:
            #パートを追加
            part=input('パートを入力（終了は終わり）：')
    
            #繰り返し修了の条件
            if part == '終わり':
                break
            #追加枠のメンバーを入力
            name = input(f"{part}のメンバーを入力：")
            live.members[part] = name
        self.lives.append(live)
        self.save_lives()
        #ライブ情報を出力
        print(live.info())
        print('追加完了')
    #②表示
    def list_lives(self):
        if not self.lives:
            print("ライブはありません")
            return

        for i, live in enumerate(self.lives):
            print(f"\n【{i}】")
            print(live.info())
    # ③ 編集
       # ③ 編集
    def update_live(self):
        self.list_lives()

        index = int(input("編集するライブ番号："))

        if 0 <= index < len(self.lives):
            live = self.lives[index]

            print("\n何を編集する？")
            print("1: 日付")
            print("2: 会場")
            print("3: 持ち時間")
            print("4: 曲")
            print("5: メンバー")

            choice = input("番号：")

            # 日付
            if choice == "1":
                for key in live.date:
                    live.date[key] = input(f"{key}：")

            # 会場
            elif choice == "2":
                live.venue = input("新しい会場：")

            # 持ち時間
            elif choice == "3":
                live.time = input("新しい持ち時間：")

            # 曲
            elif choice == "4":
                live.songs = []

                while True:
                    song = input("曲名（終了は終わり）：")

                    if song == "終わり":
                        break

                    live.songs.append(song)

            # メンバー
            elif choice == "5":
                for part in live.members:
                    live.members[part] = input(f"{part}：")

            else:
                print("無効な入力")
                return

            print("\n編集後の情報")
            print(live.info())
            self.save_lives()
        else:
            print("存在しない番号")

        
    # ④ 削除
    def delete_live(self):
        self.list_lives()

        index = int(input("削除するライブ番号："))

        if 0 <= index < len(self.lives):
            removed = self.lives.pop(index)

            self.save_lives()

            print("削除しました：")
            print(removed.info())
        else:
            print("存在しない番号")
    #⑤全消し
    def clear_lives(self):
        confirm = input("本当に全削除しますか？(y/n)：")

        if confirm == "y":
            self.lives.clear()
            self.save_lives()
            print("全て削除しました")
        else:
            print("キャンセルしました")
    # メニュー
    def menu(self):
        while True:
            print("\n===== LIVE MANAGER =====")
            print("1: 追加")
            print("2: 表示")
            print("3: 編集")
            print("4: 削除")
            print("5:全削除")
            print("6: 終了")

            choice = input("選択：")

            if choice == "1":
                self.create_live()
            elif choice == "2":
                self.list_lives()
            elif choice == "3":
                self.update_live()
            elif choice == "4":
                self.delete_live()
            elif choice == "5":
                self.clear_lives()
            elif choice == "6":
                print("終了")
                break
            else:
                print("無効な入力")
    def save_lives(self):
        data = []

        for live in self.lives:
            data.append({
                "date": live.date,
                "venue": live.venue,
                "time": live.time,
                "members": live.members,
                "songs": live.songs
            })

        with open("lives.json", "w", encoding="utf-8") as file:
           json.dump(data, file, ensure_ascii=False, indent=4)

        print("保存完了")
    def load_lives(self):
        try:
            with open("lives.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            for item in data:
                live = Lives(item["venue"], item["time"])

                live.date = item["date"]
                live.members = item["members"]
                live.songs = item["songs"]

                self.lives.append(live)

            print("読み込み完了")

        except FileNotFoundError:
            print("保存データなし")

