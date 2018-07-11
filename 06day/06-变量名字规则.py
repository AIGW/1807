#格式化输出
name = input("请输入您的名字")
sex = input("请输入您的性别")
age = input("请输入您的年龄")
height = float(input("请输入您的身高"))
addr = input("请输入您的家庭地址")
phone = input("请输入您的电话")
hobby = input("请输入您的爱好")
weight = input("请输入您的体重")


print("我的名字是%s,我的性别是%s,我的年龄是%s,我的身高是%.02f,我的家庭地址是%s,我的电话是%s,我的爱好是%s,我的体重是%s"%(name,sex,age,height,addr,phone,hobby,weight))
