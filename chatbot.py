from ued import senti
import ued
from nltk import tokenize
import tkinter as tk
alist={}
vs={}
def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res
def get_response():
        if(len(vs)>=1):
                vs.clear()
        result=senti(e1.get())
        tok(e1.get(),result)
def tok(a,b):
        sentence_list = tokenize.sent_tokenize(e1.get())
        analyzer=ued.SentimentIntensityAnalyzer()
        for sentence in sentence_list:
                vs[sentence] = analyzer.polarity_scores(sentence)
        alist["The Sentence is NEGATIVE(%)"]=b['neg']*100
        alist["The Sentence is NEUTRAL(%)"]=b['neu']*100
        alist["The Sentence is POSITIVE(%)"]=b['pos']*100
        alist["COMPOUND SCORE"]=b['compound']
        dict3 = Merge(vs, alist)
        f=open('data.txt','a')
        f.write("%s\n"%dict3)
        f.close()
        master = tk.Tk()
        msg = tk.Message(master, text =dict3)
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack()
        tk.mainloop()
master = tk.Tk()
master.geometry("500x100+300+300")
tk.Label(master, text="Message").grid(row=0)
e1 = tk.Entry(master)

e1.grid(row=0, column=1)
tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Show', command=get_response).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)

master.mainloop()
tk.mainloop()
