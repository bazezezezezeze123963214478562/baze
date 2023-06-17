import customtkinter
import random
app = customtkinter.CTk()
app.title('ซ้ายที ขวาที พ่องๆๆๆๆ')
app.geometry('500x500')

# แสดงผล
label = customtkinter.CTkLabel(app, text="อันไหนสีแดง ", fg_color = 'transparent', font = ('Aria',40), text_color='red')
label.pack(pady=(20,0))

show_result = customtkinter.CTkLabel(app, text=" ", fg_color = 'transparent', font = ('Aria',40), text_color='black')
show_result.pack(pady=(20,0))


# รับ input
#entry = customtkinter.CTkEntry(app, placeholder_text="ใส่ Input ของคุณตรงนี้")
#entry.pack(pady=(15,0))
        #ans_label = customtkinter.CTkLabel(app, text = 'ตาปกติ', font = ('Aria', 40))

def button_event(ans):
    # if ans == 'gray': 
    #     result = "ตาบอดสีนะจ๊ะะะะะะะะะะะะะะะะะะะะะะะะะะะะ"  
    #     show_result.configure(text=result)
    #     #ans_label = customtkinter.CTkLabel(app, text = 'ตาบอดสี', font = ('Aria', 40))
    # elif ans == 'red':
    #     result = "ตาปกติดีครับบบบบบบบบบบบบบบบบบบบบบบบบบบบบบบบบบบบ"
    #     show_result.configure(text=result)
    #     result = "ตาปกติ"
    #     show_result.configure(text=result)
    # elif ans == 'blue':
    #     result = "ตาบอกสีมากกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกกก"
    #     show_result.configure(text=result)
    # elif ans == 'green':
    #     result = "ตาบอดสีห้าบฟู่วววววววววววววววววววววววววววววววววววววววววววววววววววววววววววววววววววววววววว"
    #     show_result.configure(text=result)

    if ans == 'red':
        result = "ตาปกติ"
        show_result.configure(text=result)
    else:
        result = "ตาบอดสี"
        show_result.configure(text=result)


button = customtkinter.CTkButton(app, text="", command=lambda :button_event('gray'), fg_color=random.choice(['gray', 'green', 'blue', 'pink']))
button.pack(pady=(20,0))

button = customtkinter.CTkButton(app, text="", command=lambda :button_event('red'), fg_color='red')
button.pack(pady=(20,0))

button = customtkinter.CTkButton(app, text="", command=lambda :button_event('blue'), fg_color=random.choice(['gray', 'green', 'blue', 'pink']))
button.pack(pady=(20,0))

button = customtkinter.CTkButton(app, text="", command=lambda :button_event('green'), fg_color=random.choice(['gray', 'green', 'blue', 'pink']))
button.pack(pady=(20,0))


app.mainloop()
