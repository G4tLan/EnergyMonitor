from flask import flash, redirect, render_template, request, session, abort, url_for


class Admin():

    def login(id):
        session['logged_in'] = False
        obj = {
        'title' : 'Signin',
        'attribute': 'login',
        'alert': id
        }
        return render_template("login.html",obj = obj)


    def resetPassword(id):
        session['logged_in'] = False
        obj = {
        'title' : 'Reset Password',
        'attribute': 'resetPassword',
        'alert': id
        }
        return render_template("login.html",obj = obj)
        

    def verifyUser():
        session['logged_in'] = False
        #implement method to query username and password in db
        if request.form['password'] == 'G4t' and request.form['username'] == 'Gift':
            session['logged_in'] = True
            return redirect('/analytics')
        else:
            flash('wrong password!')
            return redirect('/login/1')

    def sendPassword():
        session['logged_in'] = False
        #implement method to query email in the db
        if request.form['email'] == 'a@g.com': #if email exist
            return redirect('/login')
        else:
            return redirect('/resetpassword/1')

    def widget():
        try:
            if session['logged_in']:
                obj = {
			        'attribute' : 'Dashboard',
			        'title': 'Widget View',
                    'name': 'widget',
                    'graph': 'LINE_CHART'
		        };
                return render_template("widget.html",obj = obj)
    
            return redirect('/home')
        except KeyError:
            return redirect('/home')

    def analytics():
        try:
            if session['logged_in']:
                obj = {
			        'attribute' : 'Analytics',
			        'title': 'Analytics',
                    'name': 'Analytics'
		        };
                return render_template("analytics.html",obj = obj)
            
            return redirect('/home')
        except KeyError:
            return redirect('/home')

    def logout():
        session['logged_in'] = False
        return redirect('/home')


    