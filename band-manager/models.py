#Liveクラスを作成
class Lives:
    #日程、場所、メンバー、曲、曲数、持ち時間をクラスに追加する
    def __init__(self,venue,time):
        self.date = {
            "年": '',
            "月": '',
            "日": '',
            "曜日": ''
            }
        self.venue = venue
        self.time = time
        self.members = {'Vo':'','Gt':'','Ba':'','Dr':'','Key':''}
        self.songs = []
    #ライブの曲数を計算
    def get_song_count (self) :
        return len (self.songs)
    #各ライブ情報のリストを返す
    def info(self):
        date_str = f"{self.date['年']}年{self.date['月']}月{self.date['日']}日（{self.date['曜日']}）"
        member_str = "\n".join([f"{role}：{name}" for role, name in self.members.items() if name != ""])
        song_str = "、".join(self.songs) if self.songs else '未登録'
        return (
            f"日程：{date_str}\n"
            f"会場：{self.venue}\n"
            f"持ち時間：{self.time}\n"
            f"メンバー：\n{member_str}\n"
            f"曲：{song_str}\n"
            f"曲数：{self.get_song_count()}"
            )