from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
#functionality part

def employee_form():
    global back_image
    employee_frame=Frame(window,width=1200,height=567,bg='white')
    employee_frame.place(x=200,y=100)
    heading_label=Label(employee_frame,text='Manage Employee Details',font=('times new roman',16,'bold'),bg='#0f4d7d',fg='white')
    heading_label.place(x=0,y=0,relwidth=1)
    back_image=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\backbutton.png')
    
   
    
    top_frame=Frame(employee_frame)
    top_frame.place(x=0,y=40,relwidth=1,height=235)
    back_button=Button(top_frame,image=back_image,bd=0,cursor='hand2',bg='white',command=lambda:employee_frame.place_forget())
    back_button.place(x=10,y=0)
    search_frame=Frame(top_frame,bg='white')
    search_frame.pack()
    search_combobox=ttk.Combobox(search_frame,values=('Id','Name','Email'),font=('times new roman',12),state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(row=0,column=0,padx=20)
    search_entry=Entry(search_frame,font=('times new roman',12),bg='lightyellow')
    search_entry.grid(row=0,column=1)
    
   
    search_button=Button(search_frame,text='Search',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    search_button.grid(row=0,column=2,padx=20)
    show_button=Button(search_frame,text='Show All',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    show_button.grid(row=0,column=3)
    
    #code formatted cntrl+alt+l
    
    # Horozontal and vertical Scrollbar
    
    horizontal_scrollbar=Scrollbar(top_frame,orient=HORIZONTAL)
    vertical_scrollbar=Scrollbar(top_frame,orient=VERTICAL)
    
    
    #Tree view
    
    employee_treeview=ttk.Treeview(top_frame,columns=('empid','name','email','gender','dob','contact','employement_type','education',
                                            'work_shift','address','doj','salary','usertype'),show='headings',
                                   yscrollcommand=vertical_scrollbar.set,xscrollcommand=horizontal_scrollbar.set) #set scrollbars
    horizontal_scrollbar.pack(side=BOTTOM,fill=X)
    vertical_scrollbar.pack(side=RIGHT,fill=Y,pady=(10,0))
    horizontal_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)
    employee_treeview.pack(pady=(10,0))
    
    employee_treeview.heading('empid',text='EmpId')
    employee_treeview.heading('name',text='Name')
    employee_treeview.heading('email',text='Email')
    employee_treeview.heading('gender',text='Gender')
    employee_treeview.heading('dob',text='Date of Birth')
    employee_treeview.heading('contact',text='Contact')
    employee_treeview.heading('employement_type',text='Employement Type')
    employee_treeview.heading('education',text='Education')
    employee_treeview.heading('work_shift',text='Work Shift')
    employee_treeview.heading('address',text='Address')
    employee_treeview.heading('doj',text='Date of Joining')
    employee_treeview.heading('salary',text='Salary')
    employee_treeview.heading('usertype',text='User Type')
    employee_treeview.column('empid',width=60)
    employee_treeview.column('name',width=140)
    employee_treeview.column('email',width=180)
    employee_treeview.column('gender',width=80)
    employee_treeview.column('contact',width=100)
    employee_treeview.column('dob',width=100)
    employee_treeview.column('employement_type',width=120)
    employee_treeview.column('education',width=120)
    employee_treeview.column('work_shift',width=100)
    employee_treeview.column('address',width=200)
    employee_treeview.column('doj',width=100)
    employee_treeview.column('salary',width=140)
    employee_treeview.column('usertype',width=120)
    
    
#creating Frame
    detail_frame=Frame(employee_frame,bg='white')
    detail_frame.place(x=20,y=280)
    
    empid_label=Label(detail_frame,text='EmpId',font=('times new roman',12),bg='white')
    empid_label.grid(row=0,column=0,padx=20,pady=10,sticky='W')
    empid_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    empid_entry.grid(row=0,column=1,padx=20,pady=10)
    
    name_label=Label(detail_frame,text='Name',font=('times new roman',12),bg='white')
    name_label.grid(row=0,column=2,padx=20,pady=10,sticky=W)
    name_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    name_entry.grid(row=0,column=3,padx=20,pady=10)
    
    email_label=Label(detail_frame,text='Email',font=('times new roman',12),bg='white')
    email_label.grid(row=0,column=4,padx=20,pady=10)
    email_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    email_entry.grid(row=0,column=5,padx=20,pady=10)
    
    gender_label=Label(detail_frame,text='Gender',font=('times new roman',12))
    gender_label.grid(row=1,column=0,padx=20,pady=10)
    
    gender_combobox=ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=1,column=1)
    
    dob_label=Label(detail_frame,text='Date Of Birth',font=('times new roman',12),bg='white')
    dob_label.grid(row=1,column=2,padx=20,pady=10)
    
    dob_date_entry=Entry(detail_frame,width=18,font=('times new roman',12))
    dob_date_entry.grid(row=1,column=3,padx=20,pady=10)
    
    contact_label=Label(detail_frame,text='Contact',font=('times new roman',12),bg='white')
    contact_label.grid(row=1,column=4,padx=20,pady=10)
    contact_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    contact_entry.grid(row=1,column=5,padx=20,pady=10)
    
    #combobox is also as checkbox
    employement_type_label=Label(detail_frame,text='Employment Type',font=('times new roman',12),bg='white')
    employement_type_label.grid(row=2,column=0,padx=20,pady=10)
        
    employement_type_combobox=ttk.Combobox(detail_frame,values=('Full Time','Part Time','Casual','Contract','Intern'),font=('times new roman',12),width=18,state='readonly')
    employement_type_combobox.set('Select Type')
    employement_type_combobox.grid(row=2,column=1)
    
    education_label=Label(detail_frame,text='Gender',font=('times new roman',12),bg='white')
    education_label.grid(row=2,column=2,padx=20,pady=10)
        
    education_options=["B.Tech","B.com","BCA","MCA","M.Tech","M.com","B.Sc","MBA","LLM","LLB","B.Arch","M.Arch"]
    education_combobox=ttk.Combobox(detail_frame,values=education_options,font=('times new roman',12),width=18,state='readonly')
    education_combobox.set('Select Education')
    education_combobox.grid(row=2,column=3)
    
    work_shift_label=Label(detail_frame,text='Work Shift',font=('times new roman',12),bg='white')
    work_shift_label.grid(row=2,column=4,padx=20,pady=10)     
    work_shift_combobox=ttk.Combobox(detail_frame,values=('Morning','Afternoon','Evening','Night'),font=('times new roman',12),width=18,state='readonly')
    work_shift_combobox.set('Select Work Shift')
    work_shift_combobox.grid(row=2,column=5)
    
    # Add Textarea
    
    address_label=Label(detail_frame,text='Address',font=('times new roman',12),bg='white')
    address_label.grid(row=3,column=0,padx=20,pady=10,sticky='W')
    address_text=Text(detail_frame,width=20,height=3,font=('times new roman',12),bg='lightyellow')
    address_text.grid(row=3,column=1,rowspan=2)     

    
    doj_label=Label(detail_frame,text='Date Of Joining',font=('times new roman',12),bg='white')
    doj_label.grid(row=3,column=2,padx=20,pady=10,sticky='W')
        
    doj_date_entry=Entry(detail_frame,width=18,font=('times new roman',12))
    doj_date_entry.grid(row=3,column=3)
    
    user_type_label=Label(detail_frame,text='User Type',font=('times new roman',12),bg='white')
    user_type_label.grid(row=4,column=2,padx=20,pady=10,sticky='W')     
    user_type_combobox=ttk.Combobox(detail_frame,values=('Admin','Employee'),font=('times new roman',12),width=18,state='readonly')
    user_type_combobox.set('Select user Type')
    user_type_combobox.grid(row=4,column=3)
    
    
    salary_label=Label(detail_frame,text='Salary',font=('times new roman',12),bg='white')
    salary_label.grid(row=3,column=4,padx=20,pady=10,sticky='W')
    salary_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    salary_entry.grid(row=3,column=5,padx=20,pady=10)
    
    
    password_label=Label(detail_frame,text='Password',font=('times new roman',12),bg='white')
    password_label.grid(row=4,column=4,padx=20,pady=10,sticky='W')
    password_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    password_entry.grid(row=4,column=5,padx=20,pady=10)
    
    Button_frame=Frame(employee_frame,bg='white')
    Button_frame.place(x=200,y=520)
    
    add_button=Button(Button_frame,text='Add',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    add_button.grid(row=0,column=0,padx=20)
    
    update_button=Button(Button_frame,text='Update',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    update_button.grid(row=0,column=1,padx=20)
    
    delete_button=Button(Button_frame,text='Text',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    delete_button.grid(row=0,column=2,padx=20)
    
    clear_button=Button(Button_frame,text='Clear',font=('times new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    clear_button.grid(row=0,column=3,padx=20)
    
#GUI part
window=Tk()    #object of the tk class


window.title('Dashboard')
window.geometry('1350x668+0+0')
window.resizable(0,0)  #window of fix size
window.config(bg='white')

bg_image=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\Inventory.png')
titleLabel=Label(window,image=bg_image,compound=LEFT,text=' Inventory Management System' , font=('times new roman',40,'bold'),bg='#010c48',fg='white',anchor='w',padx=100)
titleLabel.place(x=0,y=0,relwidth=1)

logoutButton=Button(window,text='Logout',font=('times new roman',20,'bold'),fg='#010c48')
logoutButton.place(x=1100,y=10)

subtitleLabel=Label(window,text='Welcome Admin \t\t Date:08-07-2026\t\t Time:12:36:17 pm',font=('times new roman',15),bg='#4d636d',fg='white')
subtitleLabel.place(x=0,y=70,relwidth=1)

leftFrame=Frame(window)
leftFrame.place(x=0,y=102,width=200,height=555)

logoimage=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\logo.png')
ImageLabel=Label(leftFrame,image=logoimage)
ImageLabel.pack()

menuLabel=Label(leftFrame,text='Menu',font=('times new roman',20),bg='#009688')
menuLabel.pack(fill=X)

employee_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\employee.png')
employee_button=Button(leftFrame,image=employee_icon,compound=LEFT,text= 'Employees',font=('times new roman',20,'bold'),anchor='w',padx=10,command=employee_form)
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\supplier.png')
supplier_button=Button(leftFrame,image=supplier_icon,compound=LEFT,text=  'Supplier',font=('times new roman',20,'bold'),anchor='w',padx=10)
supplier_button.pack(fill=X)

category_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\category.png')
category_button=Button(leftFrame,image=category_icon,compound=LEFT,text= 'Categories',font=('times new roman',20,'bold'),anchor='w',padx=10)
category_button.pack(fill=X)

product_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\Product.png')
product_button=Button(leftFrame,image=product_icon,compound=LEFT,text= 'Products',font=('times new roman',20,'bold'),anchor='w',padx=10)
product_button.pack(fill=X)

sales_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\sales.png')
sales_button=Button(leftFrame,image=sales_icon,compound=LEFT,text= 'Sales',font=('times new roman',20,'bold'),anchor='w',padx=10)
sales_button.pack(fill=X)

exit_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\exit.png')
exit_button=Button(leftFrame,image=exit_icon,compound=LEFT,text= 'Exit',font=('times new roman',20,'bold'),anchor='w',padx=10)
exit_button.pack(fill=X)

emp_frame=Frame(window,bg='#2c3E50',bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280)

total_emp_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\TotalEmployees.png')
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg='#2c3E50')
total_emp_icon_label.pack(pady=10)

total_emp_label=Label(emp_frame,text='Total Employees',bg='#2c3e50',fg='white',font=('times new roman',15,'bold'))
total_emp_label.pack()

total_emp_count_label=Label(emp_frame,text='0',bg='#2c3e50',fg='white',font=('times new roman',30,'bold'))
total_emp_count_label.pack()


supplier_frame=Frame(window,bg='#8E44AD',bd=3,relief=RIDGE)
supplier_frame.place(x=800,y=125,height=170,width=280)

total_supplier_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\TotalSuppliers.png')
total_suplier_icon_label=Label(supplier_frame,image=total_supplier_icon,bg='#8E44AD')
total_suplier_icon_label.pack(pady=10)

total_suplier_label=Label(supplier_frame,text='Total Suppliers',bg='#8E44AD',fg='white',font=('times new roman',15,'bold'))
total_suplier_label.pack()

total_suplier_count_label=Label(supplier_frame,text='10',bg='#8E44AD',fg='white',font=('times new roman',30,'bold'))
total_suplier_count_label.pack()


cat_frame=Frame(window,bg='#27ae60',bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,height=170,width=280)

total_cat_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\TotalCategories.png')
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg='#27ae60')
total_cat_icon_label.pack(pady=10)

total_cat_label=Label(cat_frame,text='Total Categories',bg='#27ae60',fg='white',font=('times new roman',15,'bold'))
total_cat_label.pack()

total_cat_count_label=Label(cat_frame,text='30',bg='#27ae60',fg='white',font=('times new roman',30,'bold'))
total_cat_count_label.pack()



prod_frame=Frame(window,bg='#2c3E50',bd=3,relief=RIDGE)
prod_frame.place(x=800,y=310,height=170,width=280)

total_prod_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\TotalProducts.png')
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg='#2c3E50')
total_prod_icon_label.pack(pady=10)

total_prod_label=Label(prod_frame,text='Total Products',bg='#2c3e50',fg='white',font=('times new roman',15,'bold'))
total_prod_label.pack()

total_prod_count_label=Label(prod_frame,text='25',bg='#2c3e50',fg='white',font=('times new roman',30,'bold'))
total_prod_count_label.pack()


sales_frame=Frame(window,bg='#E74c3d',bd=3,relief=RIDGE)
sales_frame.place(x=600,y=495,height=170,width=280)

total_sales_icon=PhotoImage(file='D:\\python practice\\InventoryManagementSystem\\TotalSales.png')
total_sales_icon_label=Label(sales_frame,image=total_sales_icon,bg='#E74c3d')
total_sales_icon_label.pack(pady=10)

total_sales_label=Label(sales_frame,text='Total Sales',bg='#E74c3d',fg='white',font=('times new roman',15,'bold'))
total_sales_label.pack()

total_sales_count_label=Label(sales_frame,text='20',bg='#E74c3d',fg='white',font=('times new roman',30,'bold'))
total_sales_count_label.pack()

window.mainloop()