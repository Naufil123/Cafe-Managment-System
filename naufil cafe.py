from tkinter import *
from tkinter import messagebox
import random
import datetime


screen=Tk()
screen.geometry("1350x750+0+0")
screen.title("NAUFIL CAFE MANAGMENT SYSTEM")
screen.configure(background='black')

top_frame=Frame(screen,width=1400,height=100, bd=14, relief='raise')
top_frame.pack(side=TOP)

left_frame=Frame(screen,width=900,height=650, bd=8, relief='raise')
left_frame.pack(side=LEFT)
############################################child frame of left###############################
t_frame=Frame(left_frame,width=900,height=330, bd=8, relief='raise')
t_frame.pack(side=TOP)



b_frame=Frame(left_frame,width=900,height=320, bd=6, relief='raise')
b_frame.pack(side=BOTTOM)

##################################Child of t_ftame#############################
L_top_frame=Frame(t_frame,width=400,height=330, bd=16, relief='raise')
L_top_frame.pack(side=LEFT)

R_top_frame=Frame(t_frame,width=400,height=330, bd=16, relief='raise')
R_top_frame.pack(side=RIGHT)
#################################Child of b_Frame#####################################
Ll_top_frame=Frame(b_frame,width=400,height=330, bd=14, relief='raise')
Ll_top_frame.pack(side=LEFT)

Rr_top_frame=Frame(b_frame,width=400,height=330, bd=14, relief='raise')
Rr_top_frame.pack(side=RIGHT)
################################right Frame##############################################
right_frame=Frame(screen,width=515,height=650,bd=8,  relief='raise')
right_frame.pack(side=RIGHT)
##############################RIGHT FRAME CHILDREN###############################################
R_t_frame=Frame(right_frame,width=440,height=450, bd=12, relief='raise')
R_t_frame.pack(side=TOP)



R_b_frame=Frame(right_frame,width=440,height=250, bd=16, relief='raise')
R_b_frame.pack(side=BOTTOM)

#################################Top Label######################################################
Top_Label=Label(top_frame,font=('arial',70,'bold'), text="Naufil Cafe's")
Top_Label.grid(row=0,column=0)
############################Check button of L_t_Frame###############################
# IN L_top_frame THERE IS ONLY DRINKS
varr1=StringVar()
varr2=StringVar()
varr3=StringVar()
varr4=StringVar()
varr5=StringVar()
varr6=StringVar()
varr7=StringVar()
varr8=StringVar()




varr1.set("0")
varr2.set("0")
varr3.set("0")
varr4.set("0")
varr5.set("0")
varr6.set("0")
varr7.set("0")
varr8.set("0")









var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()


#DateofOrder.set(time.strftime("%d/%m/%Y"))
var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")



Cold_Drink=Checkbutton(L_top_frame,text="Cold Drink \t" , variable=var1,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=0,sticky=W)
Expreeso_Coffee=Checkbutton(L_top_frame,text="Expresso Coffee \t\t" , variable=var2,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=1,sticky=W)
PinaColada=Checkbutton(L_top_frame,text="PinaColada \t\t" , variable=var3,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=2,sticky=W)
Falouda=Checkbutton(L_top_frame,text="Falouda \t\t" , variable=var4,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=3,sticky=W)
Cold_Coffee=Checkbutton(L_top_frame,text="Cold Coffee \t\t" , variable=var5,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=4,sticky=W)
Tea=Checkbutton(L_top_frame,text="Tea \t\t" , variable=var6,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=5,sticky=W)
Milk_Shakes=Checkbutton(L_top_frame,text="Milk Shakes \t\t" , variable=var7,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=6,sticky=W)
Choclate_Milk=Checkbutton(L_top_frame,text="Choclate Milk \t\t" , variable=var8,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=7,sticky=W)

###########################################CheckButton of R_t_Frame################################
# IN R_top_frame THERE IS ONLY CAKES    

varr9=StringVar()
varr10=StringVar()
varr11=StringVar()
varr12=StringVar()
varr13=StringVar()
varr14=StringVar()
varr15=StringVar()
varr16=StringVar()



varr9.set("0")
varr10.set("0")
varr11.set("0")
varr12.set("0")
varr13.set("0")
varr14.set("0")
varr15.set("0")
varr16.set("0")














var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()



var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")




Choclate_Fudge_Cake=Checkbutton(R_top_frame,text="Choclate Fudge Cake \t" , variable=var9,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=0,sticky=W)
Red_valvet=Checkbutton(R_top_frame,text="Red Valavet Cake \t\t" , variable=var10,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=1,sticky=W)
Brownie=Checkbutton(R_top_frame,text="Brownie  \t\t" , variable=var11,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=2,sticky=W)
Strawberry_cake=Checkbutton(R_top_frame,text="Strawberry Cake \t\t" , variable=var12,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=3,sticky=W)
Dark_Choclate=Checkbutton(R_top_frame,text="Dark Choclate Cake \t\t" , variable=var13,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=4,sticky=W)
Pineapple=Checkbutton(R_top_frame,text="PineApple Cake \t\t" , variable=var14,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=5,sticky=W)
Pasetries=Checkbutton(R_top_frame,text="Pasetries \t\t" , variable=var15,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=6,sticky=W)
Naufil=Checkbutton(R_top_frame,text="Naufil Special Cakes \t\t" , variable=var16,onvalue=1,offvalue=0,
                  font=('arial',18,'bold')).grid(row=7,sticky=W)

######################################Entry Widget for L_top_frame#######################
Cold_Drink_E=Entry(L_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr1)
Cold_Drink_E.grid(row=0,column=1)
Expreeso_Coffee_E=Entry(L_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr2)
Expreeso_Coffee_E.grid(row=1,column=1)
PinaColada_E=Entry(L_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr3)
PinaColada_E.grid(row=2,column=1)
Falouda_E=Entry(L_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr4)
Falouda_E.grid(row=3,column=1)
Cold_Coffee_E=Entry(L_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr5)
Cold_Coffee_E.grid(row=4,column=1)
Tea_E=Entry(L_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr6)
Tea_E.grid(row=5,column=1)
Milk_Shakes_E=Entry(L_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr7)
Milk_Shakes_E.grid(row=6,column=1)
Choclate_Milk_E=Entry(L_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr8)
Choclate_Milk_E.grid(row=7,column=1)


######################################Entry Widget for R_top_frame#######################

Choclate_Fudge_Cake_E=Entry(R_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr9)
Choclate_Fudge_Cake_E.grid(row=0,column=1)
Red_valvet_E=Entry(R_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr10)
Red_valvet_E.grid(row=1,column=1)
Brownie_E=Entry(R_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr11)
Brownie_E.grid(row=2,column=1)
Strawberry_cake_E=Entry(R_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr12)
Strawberry_cake_E.grid(row=3,column=1)
Dark_Choclate_E=Entry(R_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr13)
Dark_Choclate_E.grid(row=4,column=1)
Pineapple_E=Entry(R_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr14)
Pineapple_E.grid(row=5,column=1)
Pasetries_E=Entry(R_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr15)
Pasetries_E.grid(row=6,column=1)
Naufil_E=Entry(R_top_frame,font=('arial',16,'bold'),bd=10,width=6,justify='left',textvariable=varr16)
Naufil_E.grid(row=7,column=1)
#######################################RIGHT FRAME INFO#######################################3
Recipt=Label(R_t_frame,font=('arial',12,'bold'),text="Receipt:",bd=2,anchor="w")
Recipt.grid(row=0,column=0,sticky=W)
txt_Recipt=Text(R_t_frame,width=50,height=18,bg="white",bd=8 ,font=('arial',11,'bold'))
txt_Recipt.grid(row=1,column=0)
#########################################RIGHT FRAME BUTTON#################################3
Total_button=Button(R_b_frame,padx=16,pady=1,bd=4,fg="Black",font=('arial',16,'bold'),width=5,
                    text="Total").grid(row=0,column=0)
Receipt_button=Button(R_b_frame,padx=16,pady=1,bd=4,fg="Black",font=('arial',16,'bold'),width=5,
                    text="Receipt").grid(row=0,column=1)
###########################################Reset###############################################
def Reset():
    
    varr1.set("0")
    varr2.set("0")
    varr3.set("0")
    varr4.set("0")
    varr5.set("0")
    varr6.set("0")
    varr7.set("0")
    varr8.set("0")
    varr9.set("0")
    varr10.set("0")
    varr11.set("0")
    varr12.set("0")
    varr13.set("0")
    varr14.set("0")
    varr15.set("0")
    varr16.set("0")
    #DRINK_COST.set("0")
    #CAKES_COST.set("0")
    #SERVICE_COST.set("0")
    #GST_COST.set("0")
    #TOTAL_COST.set("0")
    
    
    
    
    



    
Reset_button=Button(R_b_frame,padx=16,pady=1,bd=4,fg="Black",font=('arial',16,'bold'),width=5,
                    text="Reset",command=Reset).grid(row=1,column=0)
###############################################Exit############################################################################
def QExit():
    QExit=messagebox.askyesno("Quit System","Do You Want To Quit System")
    if QExit>0:
        screen.destroy()

Exit_button=Button(R_b_frame,padx=16,pady=1,bd=4,fg="Black",font=('arial',16,'bold'),width=5,
                    text="Exit",command=QExit).grid(row=1,column=1)

#################################Cost ItemInformation################################################
Drink_cost=Label(Ll_top_frame,font=('arial',16,'bold'),text="Cost of Drinks",bd=8)
Drink_cost.grid(row=0,column=0,sticky=W)
DRINK_COST=Entry(Ll_top_frame,font=('arial',16,'bold'),bd=8,justify="left")
DRINK_COST.grid(row=0,column=1,sticky=W)

Cakes_cost=Label(Ll_top_frame,font=('arial',16,'bold'),text="Cost of Cakes",bd=8)
Cakes_cost.grid(row=1,column=0,sticky=W)
CAKES_COST=Entry(Ll_top_frame,font=('arial',16,'bold'),bd=8,justify="left")
CAKES_COST.grid(row=1,column=1,sticky=W)


Service_cost=Label(Ll_top_frame,font=('arial',16,'bold'),text="Service Charges",bd=8)
Service_cost.grid(row=2,column=0,sticky=W)
SERVICE_COST=Entry(Ll_top_frame,font=('arial',16,'bold'),bd=8,justify="left")
SERVICE_COST.grid(row=2,column=1,sticky=W)


Gst_cost=Label(Rr_top_frame,font=('arial',16,'bold'),text="GST ",bd=8)
Gst_cost.grid(row=0,column=0,sticky=W)
GST_COST=Entry(Rr_top_frame,font=('arial',16,'bold'),bd=8,justify="left")
GST_COST.grid(row=0,column=1,sticky=W)

Total_cost=Label(Rr_top_frame,font=('arial',16,'bold'),text="Cost of Cakes",bd=8)
Total_cost.grid(row=1,column=0,sticky=W)
TOTAL_COST=Entry(Rr_top_frame,font=('arial',16,'bold'),bd=8,justify="left")
TOTAL_COST.grid(row=1,column=1,sticky=W)






























































screen.mainloop()
