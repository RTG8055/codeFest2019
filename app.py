# -*- coding: utf-8 -*-
# import traceback, warnings
# warnings.filterwarnings("ignore")
import requests, datetime
# import sqlite3
# from mysql.connector import MySQLConnection, Error

from flask import Flask, render_template, redirect, json, request, session, Markup, flash
# from flaskext.mysql import MySQL

# mysql = MySQL()
app = Flask(__name__)

# # MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'kodamr13_inquiz'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'rtg8055'
# app.config['MYSQL_DATABASE_DB'] = 'kodamr13_inquizitive'
# app.config['MYSQL_DATABASE_HOST'] = '103.50.162.66'
    
# mysql.init_app(app)

# app.secret_key = '8bf9547569cd5a638931a8639cf9f86237931e92' 

@app.route('/')
@app.route('/home')
def main():
    # if(session.get('user_id')):
    return render_template('dashboard.html')

@app.route('/demo')
def demo():
    # if(session.get('user_id')):
    return render_template('demo.html')



@app.route('/examples/icons.html')
def icon():
    table=""
    file = open("Abcd.csv")
    for line in file:
        line=line.split(',')
        table+="<tr><td>"+line[1]+"</td></tr>"

    return render_template('icons.html', table=table)
# @app.route('/login')
# def showSignUp():
#     if(session.get('user_id')):
#         return redirect('/')
#     else:
#         return render_template('signin.html')

# @app.route('/signup')
# def showSignIn():
#     if(session.get('user_id')):
#         return redirect('/')
#     else:
#         return render_template('signup.html')

# @app.route('/developer')
# def developer():
#     return render_template('developer.html')

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/')
    
# @app.route('/rules')
# def rules():
#     return render_template('rules.html')

# @app.route('/instructions')
# def instr():
#     return render_template('instructions.html')

# @app.route('/signup',methods=['POST'])
# def signUp():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     try:
#         _name = request.form['inputName']
#         _email = request.form['inputEmail']
#         _password = request.form['inputPassword']
#         _reg = request.form['inputRegno']
#         _phone = request.form['inputPhone']
#         # captcha_response = request.form['g-recaptcha-response']

#         # validate the received values
#         if _name and _email and _password and _reg and _phone:
#             # All Good, let's call MySQL
#             #validate captcha from api
#             # r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {'secret':captcha_secret_key ,'response':captcha_response})
#             # is_success_captcha = r.json()['success']
            
#             # if not is_success_captcha:
#             #     return render_template("404.html",error = 'The captcha couldnt be verified')
#             try:
#                 cursor.callproc('insert_player_inquizitive',(_name, _reg, _email, _phone, _password))
#                 data = cursor.fetchall()
#                 if len(data) is 0:
#                     conn.commit()
#                     return render_template('signin.html')

#                 else:
#                     return render_template('404.html', error="not unique")            
#             except Exception as e:
#                 return render_template('404.html', error = "Uh-huh! Some error. Please retry with valid fields")
#         else:
#             return render_template('404.html',error = "Enter all the values. Please :(")

#     except Exception as e:
#         return json.dumps({'errory':str(e)})
#     finally:
#         cursor.close()
#         conn.close()


# @app.route('/login',methods=['POST'])
# def validateLogin():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     try:
#         _email = request.form['inputEmail']
#         _password = request.form['inputPassword']
#        # captcha_response = request.form['g-recaptcha-response']

#         # validate the received values
#         if _email and _password:

            
#             # All Good, let's call MySQL
#             #validate captcha from api
#             #r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {'secret':captcha_secret_key ,'response':captcha_response})
#             #is_success_captcha = r.json()['success']
            
#             #if not is_success_captcha:
#             #    return render_template("404.html",error = 'The captcha couldnt be verified')
#             try:
#                 data = cursor.callproc('validate_login_inquizitive',(_email, _password))
#                 data = cursor.fetchall()
#                 if len(data) > 0:
#                     conn.commit()
#                     session['user_id'] = str(data[0][0])
#                     session['name'] = str(data[0][1])
#                     session['email'] = str(data[0][3])
#                     session['curr_ques'] = str(data[0][6])
#                     return redirect('/')
#                 else:
#                     print 'not validated'
#                     return render_template('signin.html', error="not validated")            
#             except Exception as e:
#                 return json.dumps({'errory':str(e)})
#         else:
#             return render_template('404.html',error = "Enter all the values. Please :(")

#     except Exception as e:
#         return json.dumps({'errory':str(e)})
#     finally:
#         cursor.close()
#         conn.close()

# def updateScore(isAnswerCorrect):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     try:
#         cursor.execute("SELECT * FROM scores WHERE user_id = %s", (session['user_id']))
#         data = cursor.fetchall()
#         score = 0
#         if(session['curr_difficulty'] == 1):
#             points_to_be_added = 20
#         elif(session['curr_difficulty'] == 2):
#             points_to_be_added = 30
#         elif(session['curr_difficulty'] == 3):
#             points_to_be_added = 50

#         if(not isAnswerCorrect):
#             points_to_be_added = 0

#         for player in data:
#             score = int(player[1]) + points_to_be_added
#             session['curr_score'] = score
#         cursor.execute("UPDATE scores SET points = %s WHERE user_id = %s", (str(score), session['user_id']))
#         conn.commit()
#     except Exception as e:
#         print str(e)
#     return update()

# def updateScoreRapid(isAnswerCorrect):
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     try:
#         if(isAnswerCorrect):
#             session['correct_rapid'] +=1
#         try:
#             columnName = 'rapid' + str(session['curr_rapid_q'].split('_')[0]) + 'score'
#             cursor.execute("UPDATE scores SET " + columnName + " = %s WHERE user_id = %s", (session['correct_rapid'], session['user_id']))
#             conn.commit()
#         except Exception as e:
#             print str(e)   ## to be commented in the end
#             pass
#     except Exception as e:
#         print str(e)
#     return updateRapid()

# def updateRapid():
#     if(session.get('user_id')):
#         session['curr_rapid_q'] = session['curr_rapid_q'].split('_')[0]+ '_' + str(int(session['curr_rapid_q'].split('_')[1]) + 1)
#     return True

# def update():
#     if(session.get('user_id')):
#         session['curr_rapid'] = 0
#         if(session['curr_ques'] == '1_20'):
#             makeRapidZero()
#             session['curr_rapid'] = 1
#             session['correct_rapid'] = 0
#             # session['curr_ques'] = str(int(session['curr_ques'].split('_')[0]) + 1) + '_0'
#             session['curr_rapid_q'] = '1_1'
#         elif(session['curr_ques'] == '2_20'):
#             makeRapidZero()
#             # session['curr_ques'] = str(int(session['curr_ques'].split('_')[0]) + 1) + '_0'
#             session['curr_rapid'] = 2
#             session['correct_rapid'] = 0
#             session['curr_rapid_q'] = '2_1'
#         elif(session['curr_ques'] == '3_20'):
#             makeRapidZero()
#             # session['curr_ques'] = str(int(session['curr_ques'].split('_')[0]) + 1) + '_0'
#             session['curr_rapid'] = 3
#             session['correct_rapid'] = 0
#             session['curr_rapid_q'] = '3_1'
#         elif(session['curr_ques'] == '4_20'):
#             makeRapidZero()
#             # session['curr_ques'] = str(int(session['curr_ques'].split('_')[0]) + 1) + '_0'
#             session['curr_rapid'] = 4
#             session['correct_rapid'] = 0
#             session['curr_rapid_q'] = '4_1'
#         session['curr_ques'] = session['curr_ques'].split('_')[0]+ '_' + str(int(session['curr_ques'].split('_')[1]) + 1)
#         conn = mysql.connect()
#         try:
#             cursor = conn.cursor()
#             cursor.execute("UPDATE players SET curr_ques = %s, curr_rapid = %s WHERE user_id = %s", (session['curr_ques'], session['curr_rapid'], session['user_id']))
#             conn.commit()
#         except Exception as e:
#             print str(e)
#         return True

# def getRapidQuestion():
#     if(session.get('user_id')):
#         conn=mysql.connect()
#         try:
#             cursor=conn.cursor()
#             cursor.execute("SELECT * FROM rapid WHERE question_id = %s", (session['curr_rapid_q']))
#         except Exception as e:
#             print str(e)
#         data = cursor.fetchall()
#         for value in data:
#             question = value[1]
#             option1 = value[2]
#             option2 = value[3]
#             option3 = value[4]
#             option4 = value[5]
#             session['curr_ans'] = value[6]
#         params = {'ques':question, 'option1':option1, 'option2':option2, 'option3':option3, 'option4':option4, 'ans':session['curr_ans']}
#         conn.close()
#         return params


# def getQuestion():
#     if(session.get('user_id')):
#         conn=mysql.connect()
#         try:
#             cursor=conn.cursor()
#             cursor.execute("SELECT * FROM questions WHERE question_id = %s", (session['curr_ques']))
#         except Exception as e:
#             print str(e)
#         data = cursor.fetchall()
#         for value in data:
#             question = value[1]
#             option1 = value[2]
#             option2 = value[3]
#             option3 = value[4]
#             option4 = value[5]
#             quesImage = value[6]
#             session['curr_difficulty'] = value[8]
#             if(quesImage == 'False'):
#                 quesImage = False
#             session['curr_ans'] = value[7]
#         params = {'ques':question, 'option1':option1, 'option2':option2, 'option3':option3, 'option4':option4, 'difficulty':session['curr_difficulty'], 'quesImage':quesImage, 'ans':session['curr_ans']}
#         conn.close()
#         return params

# @app.route('/newLevel')
# def newLevel():
#     if(session.get('user_id')):
#         if(session['curr_ques'] == '1_1'):
#             bg = "url('../static/image/level_1_storyline.jpg')"
#             session['transition_video'] = "../static/video/welcome-level1.mp4"
#             session['curr_rapid_q'] = '1_1'
#             session['correct_rapid'] = 0
#             return render_template('newLevel1.html', bg=bg)
#         elif(session['curr_ques'] == '2_1'):
#             bg = "url('../static/image/level_2_storyline.jpg')"
#             session['transition_video'] = "../static/video/welcome-level1.mp4"
#             session['curr_rapid_q'] = '1_2'
#             session['correct_rapid'] = 0
#             return render_template('newLevel2.html', bg=bg)
#         elif(session['curr_ques'] == '3_1'):
#             bg = "url('../static/image/level_3_storyline.jpg')"
#             session['transition_video'] = "../static/video/welcome-level1.mp4"
#             session['curr_rapid_q'] = '1_3'
#             session['correct_rapid'] = 0
#             return render_template('newLevel3.html', bg=bg)
#         elif(session['curr_ques'] == '4_1'):
#             bg = "url('../static/image/level_4_storyline.jpeg')"
#             session['transition_video'] = "../static/video/welcome-level1.mp4"
#             session['curr_rapid_q'] = '1_4'
#             session['correct_rapid'] = 0
#             return render_template('newLevel4.html', bg=bg)
#         else:
#             session['curr_rapid_q'] = str(int(rapidLevel())) + '_1'
#             return redirect('/question')

# def makeRapidZero():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     try:
#         cursor.execute("UPDATE players SET curr_rapid = 0 WHERE user_id = %s", (session['user_id']))
#         conn.commit()
#     except Exception as e:
#         print str(e)

# def rapidLevel():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     try:
#         cursor.execute("SELECT curr_rapid FROM players WHERE user_id = %s", (session['user_id']))
#         data = cursor.fetchall()
#         for player in data:
#             curr_rapid = int(player[0])
#         return curr_rapid
#     except Exception as e:
#         print str(e)
#         return 0

# def rapidFireEnd():
#     if(session['curr_ques'] == '21'):
#         session['curr_ques'] = str(int(session['curr_ques'].split('_')[0]) + 1) + '_1'
#     conn = mysql.connect()
#     try:
#         cursor = conn.cursor()
#         cursor.execute("UPDATE players SET curr_ques = %s, curr_rapid = %s WHERE user_id = %s", (session['curr_ques'], session['curr_rapid'], session['user_id']))
#         conn.commit()
#     except Exception as e:
#         print str(e)
#     return True


# @app.route('/rapidfire')
# def rapidfire():
#     if(session.get('user_id')):
#         makeRapidZero()
#         if(request.args.get('startRapid') == 'True'):
#             session['rapid_start_time'] = int(datetime.datetime.now().strftime("%s")) * 1000
#         if(request.args.get('endRapid') == 'True'):
#             return redirect('/question')
#         # if(rapidLevel() != 0):
#         if('11' in session['curr_rapid_q']):
#             # rapidFireEnd()
#             return redirect('/question')
#         params = getRapidQuestion()
#         params['level'] = session['curr_rapid_q'].split('_')[0]
#         params['question_number'] = session['curr_rapid_q'].split('_')[1]
#         params['timeElapsed'] = 2000 + (int(datetime.datetime.now().strftime("%s")) * 1000) - session['rapid_start_time']
#         return render_template('rapid.html', params = params)
#         # else:
#             # return redirect('/question')
#     else:
#         return redirect('/login')

# @app.route('/rapidfire', methods=['POST'])
# def validateAnsx():
#     if(session.get('user_id')):
#         _inputAns = int(request.form['answer'])
#         updateScoreRapid(_inputAns == int(session['curr_ans']))
#         return redirect('/rapidfire')
#     else:
#         return redirect('/signup')

# def fetchCurrentScore():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     try:
#         cursor.execute("SELECT * FROM scores WHERE user_id = %s", (session['user_id']))
#         data = cursor.fetchall()
#         for player in data:
#             score = int(player[1])
#             session['curr_score'] = score
#             session['rapid1score'] = int(player[2])
#             session['rapid2score'] = int(player[3])
#             session['rapid3score'] = int(player[4])
#             session['rapid4score'] = int(player[5])
#             session['pointsinlevel1'] = int(player[6])
#             session['pointsinlevel2'] = int(player[7]) - int(player[6]);
#             session['pointsinlevel3'] = int(player[8]) - int(player[7]);
#             session['pointsinlevel4'] = int(player[9]) - int(player[8]);
#     except Exception as e:
#         print str(e)

# def updateLevelWiseScore():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     try:
#         columnName = 'pointsafterlevel' + str(session['curr_ques'].split('_')[0])
#         cursor.execute("UPDATE scores SET " + columnName + " = %s WHERE user_id = %s", (session['curr_score'], session['user_id']))
#         conn.commit()
#     except Exception as e:
#         print str(e)   ## to be commented in the end
#         pass

# @app.route('/question')
# def question():
#     if(session.get('user_id')):
#         if(request.args.get('skipRapid') == 'True'):
#             session['curr_ques'] = str(int(session['curr_ques'].split('_')[0]) + 1) + '_1'
#             makeRapidZero()
#             return redirect('/newLevel')
#         if(session['curr_ques'] == '1_21'):
#             fetchCurrentScore()
#             updateLevelWiseScore()
#             session['correct_rapid'] = 0
#             return render_template('levelEnd1.html', score=session['curr_score'], showRapid=rapidLevel(), numberOfRapidPlayedCorrectly = session['rapid1score'])
#         elif(session['curr_ques'] == '2_21'):
#             fetchCurrentScore()
#             updateLevelWiseScore()
#             session['correct_rapid'] = 0
#             return render_template('levelEnd2.html', score=session['curr_score'], showRapid=rapidLevel(), numberOfRapidPlayedCorrectly = session['rapid2score'])
#         elif(session['curr_ques'] == '3_21'):
#             fetchCurrentScore()
#             updateLevelWiseScore()
#             session['correct_rapid'] = 0
#             return render_template('levelEnd3.html', score=session['curr_score'], showRapid=rapidLevel(), numberOfRapidPlayedCorrectly = session['rapid3score'])
#         elif(session['curr_ques'] == '4_21'):
#             fetchCurrentScore()
#             updateLevelWiseScore()
#             session['correct_rapid'] = 0
#             return render_template('levelEnd4.html', score=session['curr_score'], showRapid=rapidLevel(), numberOfRapidPlayedCorrectly = session['rapid4score'])
#         params = getQuestion()
#         params['level'] = session['curr_ques'].split('_')[0]
#         if(params['level'] == '1'):
#             bg = "url('../static/image/level_1_questions.jpg')"
#         elif(params['level'] == '2'):
#             bg = "url('../static/image/level_2_questions.jpg')"
#         elif(params['level'] == '3'):
#             bg = "url('../static/image/level_3_questions.jpg')"
#         elif(params['level'] == '4'):
#             bg = "url('../static/image/level_4_questions.jpeg')"
#         params['question_number'] = session['curr_ques'].split('_')[1]
#         return render_template('questionfib.html', params = params, bg=bg)
#     else:
#         return redirect('/login')

# @app.route('/question', methods=['POST'])
# def validateAns():
#     if(session.get('user_id')):
#         _inputAns = int(request.form['answer'])
#         updateScore(_inputAns == int(session['curr_ans']))
#         return redirect('/question')
#     else:
#         return redirect('/signup')

# @app.route('/admin')
# def admin():
#     return redirect('https://i0.kym-cdn.com/photos/images/original/000/232/114/e39.png', code=302)

# @app.route('/otherevents')
# def otherevents():
#     return render_template('otherEvents.html')

# @app.route('/transition')
# def trans():
#     return render_template('transition.html', transVideo = session['transition_video'])    

# def calcEfficiency(level, score):
#     if(level == 1):
#         if(0 <= score <= 200):
#             eff = 33
#         elif(201 <= score <= 400):
#             eff = 66
#         else:
#             eff = 100
#     elif(level == 2):
#         if(0 <= score <= 220):
#             eff = 33
#         elif(221 <= score <= 450):
#             eff = 66
#         else:
#             eff = 100
#     elif(level == 3):
#         if(0 <= score <= 250):
#             eff = 33
#         elif(251 <= score <= 500):
#             eff = 66
#         else:
#             eff = 100
#     elif(level == 4):
#         if(0 <= score <= 300):
#             eff = 33
#         elif(301 <= score <= 600):
#             eff = 66
#         else:
#             eff = 100
#     else:
#         eff = 0
#     return eff

# @app.route('/result')
# def result():
#     fetchCurrentScore()
#     finalEff = (calcEfficiency(1, session['pointsinlevel1']) + calcEfficiency(2, session['pointsinlevel2']) + calcEfficiency(3, session['pointsinlevel3']) + calcEfficiency(4, session['pointsinlevel4'])) / 4
#     return render_template('result.html', efficiency = finalEff, score = session['curr_score'])

# @app.errorhandler(404)
# def page_not_found(e):
    # return render_template('404.html', error="The page you requested was not found!")

if __name__ == "__main__":
    app.run(debug=True,port=10002,use_evalex=False)
    # app.run(debug=True,host='192.168.43.53',port=5007,use_evalex=False)
