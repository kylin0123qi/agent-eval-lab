"""Day 1 脚本：读取用户输入，输出格式化结果。"""

def userinfo(name,age,city):
    return(
        "="*30+"\n"
        f"  姓名:{name}\n"
        f"  年龄:{age}\n"
        f"  城市:{city}\n"
        +"="*30
    )
def main():
    name=input("请输入你的姓名：").strip()
    age=input("请输入你的年龄").strip()
    city=input("请输入你的城市：").strip()
    if not age.isdigit():
        print("输入的年龄不是数字，请重新输入")
        return
    result=userinfo(name,age,city)
    print(result)

if __name__=="__main__":
    main()
