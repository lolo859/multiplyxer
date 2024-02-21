import os,tkinter,tkinter.filedialog,tkinter.messagebox,time as tm,subprocess
def new_process(listeprocess):
    processfile=tkinter.filedialog.askopenfilename(title="Open process file")
    if not processfile=="":
        liste=open(processfile,"r",encoding="utf-8").readlines()
        for i in range(len(liste)):
            liste[i]=liste[i].rstrip("\n")
        for i in range(len(liste)):
            listeprocess.insert(listeprocess.size(),liste[i])
def new_path(listepath):
    pathfile=tkinter.filedialog.askopenfilename(title="Open path file")
    if not pathfile=="":
        liste=open(pathfile,"r",encoding="utf-8").readlines()
        for i in range(len(liste)):
            liste[i]=liste[i].rstrip("\n")
        for i in range(len(liste)):
            listepath.insert(listepath.size(),(liste[i]))
def change_execute_mode(button):
    if button.cget("text")=="Execute mode : single":
        button.config(text="Execute mode : loop")
    else:
        button.config(text="Execute mode : single")
def change_output_mode(button):
    if button.cget("text")=="Output mode : terminal":
        button.config(text="Output mode : file")
        return
    if button.cget("text")=="Output mode : file":
        button.config(text="Output mode : nothing")
        return
    else:
        button.config(text="Output mode : terminal")
        return
def launch(listeprocess,listepath,butexecute,butoutput,launcht,repet,time,times):
    launcht.config(text="Executing...",)
    launcht.config(state="disabled")
    try:
        if butexecute.cget("text")=="Execute mode : loop" and not repet=="":
            int(repet)
    except:
        tkinter.messagebox.showerror(title="Error",text="Please specify a number in the loop text box.")
        launcht.config(text="Launch",state="active")
        return
    try:
        if not time=="":
            int(time)
    except:
        tkinter.messagebox.showerror(title="Error",text="Please specify a number in the time between command text box.")
        launcht.config(text="Launch",state="active")
        return
    try:
        if not times=="":
            int(times)
    except:
        tkinter.messagebox.showerror(title="Error",text="Please specify a number in the time between sequence text box.")
        launcht.config(text="Launch",state="active")
        return
    if butexecute.cget("text")=="Execute mode : single":
        if butoutput.cget("text")=="Output mode : terminal":
            for i in range(listeprocess.size()):
                if not listepath.get(i)=="":
                    os.chdir(listepath.get(i))
                os.system(listeprocess.get(i))
                tm.sleep(int(time))
        elif butoutput.cget("text")=="Output mode : file":
            textpath=os.path.abspath("result.txt")
            textfile=open(textpath,"w")
            for i in range(listeprocess.size()):
                if not listepath.get(i)=="":
                    os.chdir(listepath.get(i))
                out=subprocess.run(listeprocess.get(i), shell = True, text = True, stdout = subprocess.PIPE, check = False).stdout
                textfile.write(out)
                tm.sleep(int(time))
            textfile.close()
        elif butoutput.cget("text")=="Output mode : nothing":
            for i in range(listeprocess.size()):
                if not listepath.get(i)=="":
                    os.chdir(listepath.get(i))
                out=subprocess.run(listeprocess.get(i), shell = True, text = True, stdout = subprocess.PIPE, check = False).stdout
                tm.sleep(int(time))
    elif butexecute.cget("text")=="Execute mode : loop":
        if butoutput.cget("text")=="Output mode : terminal":
            if repet=="" or repet=="0" or repet.startswith("-"):
                if tkinter.messagebox.askyesno("Launching loop ?","If you launch the command in infinite loop mode, the only way to stop it is to close Multiplyxer. Would you really like to do that ?",icon="warning")==False:
                    launcht.config(text="Launch",state="active")
                    return
                while True:
                    for i in range(listeprocess.size()):
                        if not listepath.get(i)=="":
                            os.chdir(listepath.get(i))
                        os.system(listeprocess.get(i))
                        tm.sleep(int(time))
                    tm.sleep(int(times))
            else:
                for i in range(int(repet)):
                    for i in range(listeprocess.size()):
                        if not listepath.get(i)=="":
                            os.chdir(listepath.get(i))
                        os.system(listeprocess.get(i)) 
                        tm.sleep(int(time))
                    tm.sleep(int(times))
        elif butoutput.cget("text")=="Output mode : file":
            if repet=="" or repet=="0" or repet.startswith("-"):
                if tkinter.messagebox.askyesno("Launching loop ?","If you launch the command in infinite loop mode, the only way to stop it is to close Multiplyxer. Would you really like to do that ?",icon="warning")==False:
                    launcht.config(text="Launch",state="active")
                    return
                textpath=os.path.abspath("result.txt")
                textfile=open(textpath,"w")
                while True:
                    for i in range(listeprocess.size()):
                        if not listepath.get(i)=="":
                            os.chdir(listepath.get(i))
                        out=subprocess.run(listeprocess.get(i), shell = True, text = True, stdout = subprocess.PIPE, check = False).stdout
                        textfile.write(out)
                        tm.sleep(int(time))
                    tm.sleep(int(times))
            else:
                textpath=os.path.abspath("result.txt")
                textfile=open(textpath,"w")
                for i in range(int(repet)):
                    for i in range(listeprocess.size()):
                        if not listepath.get(i)=="":
                            os.chdir(listepath.get(i))
                        out=subprocess.run(listeprocess.get(i), shell = True, text = True, stdout = subprocess.PIPE, check = False).stdout
                        textfile.write(out)
                        tm.sleep(int(time))
                    tm.sleep(int(times))
        elif butoutput.cget("text")=="Output mode : nothing":
            if repet=="" or repet=="0" or repet.startswith("-"):
                if tkinter.messagebox.askyesno("Launching loop ?","If you launch the command in infinite loop mode, the only way to stop it is to close Multiplyxer. Would you really like to do that ?",icon="warning")==False:
                    launcht.config(text="Launch",state="active")
                    return
                while True:
                    for i in range(listeprocess.size()):
                        if not listepath.get(i)=="":
                            os.chdir(listepath.get(i))
                        out=subprocess.run(listeprocess.get(i), shell = True, text = True, stdout = subprocess.PIPE, check = False).stdout
                        tm.sleep(int(time))
                    tm.sleep(int(times))
            else:
                textpath=os.path.abspath("result.txt")
                textfile=open(textpath,"w")
                for i in range(int(repet)):
                    for i in range(listeprocess.size()):
                        if not listepath.get(i)=="":
                            os.chdir(listepath.get(i))
                        out=subprocess.run(listeprocess.get(i), shell = True, text = True, stdout = subprocess.PIPE, check = False).stdout
                        tm.sleep(int(time))
                    tm.sleep(int(times))
    launcht.config(text="Launch",state="active")
main=tkinter.Tk()
main.title("Multiplyxer v1.0")
main.geometry("400x625")
main.resizable(width=False,height=False)
listeprocess=tkinter.Listbox(main,selectmode="SINGLE")
listeprocess.place(width=200,height=350,x=0,y=0)
listepath=tkinter.Listbox(main,selectmode="SINGLE")
listepath.place(width=200,height=350,x=200,y=0)
addprocess=tkinter.Button(main,text="Add process file",command=lambda:new_process(listeprocess))
addprocess.place(width=200,height=50,x=0,y=350)
addpath=tkinter.Button(main,text="Add path file",command=lambda:new_path(listepath))
addpath.place(width=200,height=50,x=200,y=350)
changeexecute=tkinter.Button(main,text="Execute mode : single",command=lambda:change_execute_mode(changeexecute))
changeexecute.place(width=400,height=50,x=0,y=400)
changeoutput=tkinter.Button(main,text="Output mode : terminal",command=lambda:change_output_mode(changeoutput))
changeoutput.place(width=400,height=50,x=0,y=450)
looprepetlabel=tkinter.Label(main,text="Number of repetition (0 if you want an infinite loop) : ")
looprepetlabel.place(width=300,height=25,x=0,y=500)
looprepetentry=tkinter.Entry(main)
looprepetentry.place(width=100,height=25,x=300,y=500)
delaicommandlabel=tkinter.Label(main,text="Time to wait between command : ")
delaicommandlabel.place(width=300,height=25,x=0,y=525)
delaicommand=tkinter.Entry(main)
delaicommand.place(width=100,height=25,x=300,y=525)
delaicommand.insert(string="0",index=0)
delaisequancelabel=tkinter.Label(main,text="Time to wait between sequence : ")
delaisequancelabel.place(width=300,height=25,x=0,y=550)
delaisequece=tkinter.Entry(main)
delaisequece.place(width=100,height=25,x=300,y=550)
delaisequece.insert(string="0",index=0)
launcht=tkinter.Button(main,text="Launch",command=lambda:launch(listeprocess,listepath,changeexecute,changeoutput,launcht,looprepetentry.get(),delaicommand.get(),delaisequece.get()))
launcht.place(width=400,height=50,x=0,y=575)
main.mainloop()