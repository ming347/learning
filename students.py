def main():
    students = []  # 存储学生信息的列表

    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 录入学生成绩")
        print("2. 显示前三名学生")
        print("3. 退出系统")
        choice = input("请选择功能 (1-3): ")

        if choice == "1":
            while True:
                name = input("请输入学生姓名 (输入q返回菜单): ")
                if name.lower() == 'q':
                    break
                try:
                    score = float(input(f"请输入{name}的成绩: "))
                    students.append({"name": name, "score": score})
                    print(f"{name}的成绩已录入成功！")
                except ValueError:
                    print("输入无效，请输入有效的数字成绩！")

        elif choice == "2":
            if not students:
                print("暂无学生成绩，请先录入成绩！")
                continue

            # 按成绩降序排序
            sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
            print("\n===== 成绩前三名学生 =====")
            print("排名\t姓名\t成绩")

            # 输出前三名
            for i, student in (sorted_students[:3], 1):
                print(f"{i}\t{student['name']}\t{student['score']}")

        elif choice == "3":
            print("感谢使用成绩管理系统，再见！")
            break
        else:
            print("无效选择，请输入1-3之间的数字！")


if __name__ == "__main__":
    main()