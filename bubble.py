def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("请输入0-100之间的分数！")
        except ValueError:
            print("输入无效，请输入数字！")


def get_student_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("姓名不能为空！")


def bubble_sort(scores):
    n = len(scores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if scores[j][1] < scores[j + 1][1]:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
    return scores


def main():
    students = []

    print("=" * 30)
    print("  学生成绩录入系统")
    print("=" * 30)

    while True:
        name = get_student_name("\n请输入学生姓名（输入q结束）：")
        if name.lower() == 'q':
            break

        score = get_valid_score(f"请输入{name}的成绩：")
        students.append((name, score))

        print(f"✓ {name}的成绩({score})已录入")

    if not students:
        print("\n未录入任何成绩！")
        return

    # 排序
    sorted_students = bubble_sort(students.copy())

    # 输出结果
    print("\n" + "=" * 30)
    print("  成绩排名（升序）")
    print("=" * 30)
    print("排名\t姓名\t成绩")
    print("-" * 30)

    for rank, (name, score) in enumerate(sorted_students, 1):
        print(f"{rank}\t{name}\t{score}")


if __name__ == "__main__":
    main()