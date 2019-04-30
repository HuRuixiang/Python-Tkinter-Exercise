import tkinter as tk
import pickle
import tkinter.messagebox

#创建窗体
window = tk.Tk()
window.title("Welcome to Ruixiang's Python")
window.geometry("360x200")

#创建标签
tk.Label(window,text="User Name").place(x=50,y=50)
tk.Label(window,text="Password").place(x=50,y=90)

#创建输入框
var_user_name = tk.StringVar()
var_user_name.set("ruixianghu@foxmail.com")
var_user_passwd = tk.StringVar()
entry_user_name=tk.Entry(window,textvariable=var_user_name).place(x=160,y=50)
entry_user_password=tk.Entry(window,textvariable=var_user_passwd,show="*").place(x=160,y=90)

#创建按钮事件
def user_login():
    user_name = var_user_name.get()
    user_pwd = var_user_passwd.get()
    #打开账户字典
    with open("account.pickle","rb") as user_file:
        #将账户字典赋值给user_info
        user_info = pickle.load(user_file)
    #判断输入的用户名是否在账户字典  
    if user_name in user_info:
        #如果在，判断输入的密码是否等于该用户名对应的密码
        if user_pwd == user_info[user_name]:
            tk.messagebox.showinfo(title="Welcome",message="How are you?"+user_name)
        else:
            tk.messagebox.showinfo(title="Error",message="your password is wrong")
    else:
        is_sign_up = tk.messagebox.askyesno(title="Welcome",message="You have not sign up yet, Sign up now?")
        if is_sign_up:
            user_signup()

def user_signup():
    #创建二级窗口
    window_signup = tk.Toplevel(window)
    window_signup.geometry("350x200")
    window_signup.title("Sign up window")
        
    #新用户名
    tk.Label(window_signup,text="User name:").place(x=10,y=10)
    new_name = tk.StringVar()
    new_name.set("example@python.com")
    entry_new_name = tk.Entry(window_signup,textvariable=new_name).place(x=150,y=10)

    #新密码
    tk.Label(window_signup,text="Password:").place(x=10,y=50)
    new_pwd = tk.StringVar()
    entry_new_pwd = tk.Entry(window_signup,textvariable=new_pwd).place(x=150,y=50)

    #确认新密码
    tk.Label(window_signup,text="Comfirm password:").place(x=10,y=90)
    new_pwd_comfirm = tk.StringVar()
    entry_new_pwd_comfirm = tk.Entry(window_signup,textvariable=new_pwd_comfirm).place(x=150,y=90)
    
    def sign_to_accout():
        nn = new_name.get() 
        np = new_pwd.get()
        npc = new_pwd_comfirm.get()
        with open("account.pickle","rb") as user_file:
            exist_user_info = pickle.load(user_file)
        if nn in exist_user_info:
            tk.messagebox.showinfo("Error","The user has already signed up")
        elif nn=="":
            tk.messagebox.showinfo("Error","The user name can't be none")
        elif np=="":
            tk.messagebox.showinfo("Error","Please enter your password")
        elif np != npc or npc=="":
            tk.messagebox.showinfo("Error","Password and comfirm password must be same")
        else:
            exist_user_info[nn] = np
            with open("account.pickle","wb")as user_file:
                pickle.dump(exist_user_info,user_file)
            tk.messagebox.showinfo("Welcome","You hava signed up")
            window_signup.destroy()

    tk.Button(window_signup,text="Sign up",command=sign_to_accout).place(x=150,y=135)
    
#创建按钮
btn_login = tk.Button(window,text="Login",command=user_login).place(x=110,y=130)
btn_signup = tk.Button(window,text="Sign up",command=user_signup).place(x=210,y=130)

#刷新窗口
window.mainloop()
