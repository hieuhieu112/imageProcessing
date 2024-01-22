from tkinter import *
from PIL import ImageTk,Image
from speed import *
from test2 import *
# win = Tk()
# win.title("Mặc Nhiên")
# win.geometry('500x500')
# # win['bg']='#99FFFF'    BG của frame
# name = Label(win,text= "Sĩ đẹp trai", font = ('Times New Roman', 14))
# name.place(x=30,y=30)
# entry = Entry(win, width =10, font= ("Times New Roman",30),bg='red',fg='white')
# entry.place(x=200,y=20)
# entry.focus()
# def anvao():
#     name1 = Label(win, text="Bãn đã gõ vào nút", font=('Times New Roman', 14))
#     name1.place(x=80, y=90)
# but = Button(win,text='CLick vào đây',command=anvao)
# but.place(x=50,y=50)
#
# win.mainloop()


# #tạo ra cửa rổ khung chương trình
# a = Tk()
# a.title("Mặc Nhiên")
# a.geometry("300x400")
# a.attributes("-topmost", True)
# #tạo ra label
# lb_name = Label(a,font= ("Arial",10),text ="Họ và tên: ")
# lb_name.place(x=10,y=10)
# #tạo ô text nhập iệu
# txt = Entry(a,width = 20, font =("Times New Roman",10))
# txt.insert(END,"HEHE")
# txt.place(x=80,y=10)
# txt.focus()
#
# #hàm xử lí button
# def anvao():
#     name1 = Label(a, text="Bạn đã nhập người xinh đẹp nhất : "+txt.get(), font=('Times New Roman', 10))
#     name1.place(x=20, y=80)
#
# #Tạo ra button
# but = Button(a,text='CLick vào đây',command=anvao)
# but.place(x=80,y=50)
# #import hình ảnh
# img = (Image.open("C:\\Users\\LENOVO\\OneDrive\\Pictures\\be.jpg"))
# resize = img.resize((100,100),Image.ANTIALIAS)
# img1=ImageTk.PhotoImage(resize)
# but1 = Button(a,text='CLick vào đây',image=img1)
# but1.place(x=20,y=80)
# a.mainloop()

main = Tk()
main.title("Đồ án xử lí ảnh")
main.geometry("700x400")
main.attributes("-topmost", False)
main.config(bg="#f0f0f0")  # Đặt màu nền cho cửa sổ chính

lb_title = Label(main, font=("Arial", 14, "bold"), text="ĐỒ ÁN XỬ LÍ ẢNH\nXỬ LÍ CÁC TÍNH NĂNG VỀ PHƯƠNG TIỆN GIAO THÔNG", bg="#f0f0f0")
lb_title.place(relx=0.5, rely=0.3, anchor=CENTER)

but = Button(main, text='Đếm và đo tốc độ', command=run_speed, font=("Arial", 12), bg="#4CAF50", fg="white")
but.place(relx=0.5, rely=0.5, anchor=CENTER)

but1 = Button(main, text='Nhận diện chỗ trống bãi đổ xe', command=baidoxe, font=("Arial", 12), bg="#4CAF50", fg="white")
but1.place(relx=0.5, rely=0.7, anchor=CENTER)

main.mainloop()

