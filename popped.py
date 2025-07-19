def get_valid_amount(player_name):
    while True:
        try:
            amount = int(input(f"{player_name}，请输入1-100之间的金额: "))
            if 1 <= amount <= 100:
                return amount
            else:
                print("金额必须在1到100之间，请重新输入！")
        except ValueError:
            print("输入无效，请输入一个整数！")


def determine_winner(amount1, amount2, player1, player2):
    if amount1 > amount2:
        print(f"\n{player1}输入了{amount1}，{player2}输入了{amount2}")
        print(f"{player1}的金额更大，需要支付给{player2} {amount2}元！")
        return (player2, player1, amount2)
    elif amount2 > amount1:
        print(f"\n{player1}输入了{amount1}，{player2}输入了{amount2}")
        print(f"{player2}的金额更大，需要支付给{player1} {amount1}元！")
        return (player1, player2, amount1)
    else:
        print(f"\n两人都输入了{amount1}，金额相同，平局！")
        return (None, None, 0)


def play_game():
    print("欢迎来到金额博弈游戏！")
    print("游戏规则：两人各输入1-100之间的金额，金额大的一方要赔给金额小的一方与金额小的一方所输入金额相等的钱数\n")
    player1 = input("请输入第一位玩家的名字: ")
    player2 = input("请输入第二位玩家的名字: ")
    amount1 = get_valid_amount(player1)
    amount2 = get_valid_amount(player2)
    winner, loser, payout = determine_winner(amount1, amount2, player1, player2)
    play_again = input("\n是否想再玩一次？(y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("谢谢参与，游戏结束！")


if __name__ == "__main__":
    play_game()
