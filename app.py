#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def nitintitt():
    return render_template('project.html')
@app.route('/info',methods=['POST'])
def gkjgkj():
    if(request.method=='POST'):
        ex=float(request.form['exp'])
        import pickle
        file=open('almonds.pkl','rb')
        table=pickle.load(file)
        file.close()
        res=table.predict([[ex]])
        return render_template('project.html',answer=res)
if __name__=='__main__':
    app.run()


# In[ ]:




