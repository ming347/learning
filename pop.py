def get_valid_score(prompt):
    while True:
        score = input(prompt)
        if score.replace('.', '', 1).isdigit():
            score = float(score)
            if 0 <= score <= 100:
                return score
            else:
                print("请输入0-100之间的分数！")
        else:
            print("请输入有效的数字分数！")


def get_student_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("姓名不能为空！")


def judge(scores):
    if scores[0] > scores[1]:
        print(f"{scores[0][0]} 胜")
    elif scores[1] > scores[0]:
        print(f"{scores[1][0]} 胜")
    else:
        print("平局！双方成绩相同")


def main():
    students = []

    print("=" * 30)
    print("  猜数字对决 ")
    print("=" * 30)
    print('请分别输入你们想要的钱（100元内），如果金额超出对方10元，那么无法得到，反之，可以得到')

    while True:
        # 收集两位选手信息
        for i in range(2):
            name = get_student_name(f"\n请输入{i+1}号选手的名字：")
            score = get_valid_score(f"请输入{name}的选择的金额：")
            students.append({"name": name, "score": score})
            print(f"✓ {name}的成绩({score})已录入")

        print("\n本轮比赛结果：")
        judge(students)

        choice = input("\n是否继续下一轮比赛？(y/n)：")
        while not choice.strip() or choice.lower() not in ('y', 'n'):
            print("请输入有效的选择(y/n)！")
            choice = input("\n是否继续下一轮比赛？(y/n)：")

        if choice.lower() != 'y':
            break
        
        # 清空选手列表开始新的一轮
        students.clear()

    print("\n程序已结束，感谢使用！")
