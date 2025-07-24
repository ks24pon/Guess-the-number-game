import random
import sys

def write(msg):
    # バイナリに変換
    sys.stdout.buffer.write(msg.encode())
    # すぐに表示
    sys.stdout.flush()

def read():
    # 標準入力をバイナリで読み取り、文字列に変換して整数として返す
    return int(sys.stdin.buffer.readline().decode().strip())

def main():
    try:
        # 最小値と最大値の入力
        print("======================")
        print("最小値を入力してください： ")
        min_n = read()
        print("======================")

        print("最大値を入力してください： ")
        max_n = read()
        print("======================")
        # 入力のバリデーション
        if min_n >= max_n:
          print("エラー： 最小値は最大値以下でなければなりません")
          # 条件に合わない時は終了
          sys.exit(1)
        # 指定範囲で乱数生成
        answer = random.randint(min_n, max_n)
        # 数字を当てられる最大値の回数
        max_attempts = 5
        print(f"{min_n}から{max_n}の範囲で数字を当ててください")

        for attempt in range(1, max_attempts + 1):
            print(f"{attempt} 回目の試行: ")
            try:
                guess = read()
            except ValueError:
                print("無効な入力です。数字を入力してください。")
                continue
            # 入力した数字が正解と一致していたら
            if guess == answer:
                print(f"正解！{attempt}回目で当てました！🎊\n")
                break
            # 入力が正解より小さければヒント表示
            elif guess < answer:
                print("もっと大きい数字です。")
            # 入力が正解より大きければヒントを表示
            else:
                print("もっと小さい数字です。")
        else:
            print(f"残念！正解は {answer}でした\n")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}\n")

if __name__ == "__main__":
    main()