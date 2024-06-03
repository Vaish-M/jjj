from flask import Flask,request,jsonify
from flask_cors import CORS
import random
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib,ssl
import numpy as np
import mysql.connector
import joblib
import csv
import json
import os
from werkzeug.utils import secure_filename
import pandas as pd



app=Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'myfiles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="placement"
)

# create a mycursor object
mycursor = mydb.cursor()


#Define the list of required skills along with their required threshold values
required_skills = {
    "PYTHON": 5,
    "JAVA": 5,
    "DBMS": 5,
    "COMPUTER NETWORKS": 5,
    "MACHINE LEARNING": 5,
    "APTITUDE SKILLS": 5,
    "FULL STACK DEVELOPMENT": 5,
    "COMMUNICATION SKILLS": 5
}

# Function to identify skill gaps for a student
def identify_skill_gaps(student):
    gaps = []
    for skill, threshold in required_skills.items():
        if student[skill] < threshold:
            gaps.append(skill)
    return gaps


def mail_send(otp,mail):
    try:
        s = smtplib.SMTP('smtp.office365.com', 587)
    except Exception as e:
        s = smtplib.SMTP_SSL('smtp.office365.com', 465)
    s.ehlo()
    s.starttls()
    s.login("abbijananee.20it@sonatech.ac.in", "Mother5abbi")
        
    msg = MIMEMultipart()
    msg['From']='abbijananee.20it@sonatech.ac.in'
    msg['To']=mail
    msg['Subject']="Registration Confirmation"

    html=f'''\
        <!DOCTYPE html>
<html>

<head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <style type="text/css">
        body,
        table,
        td,
        a {"-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;"}
        table,td {"mso-table-lspace: 0pt;mso-table-rspace: 0pt;"}
        img {"-ms-interpolation-mode: bicubic;"}
        /* RESET STYLES */
        img {"border: 0;height: auto;line-height: 100%;outline: none;text-decoration: none;"}

        table {"border-collapse: collapse !important;"}

        body {"height: 100% !important;margin: 0 !important;padding: 0 !important;width: 100% !important;"}

        /* iOS BLUE LINKS */
        a[x-apple-data-detectors] {"color: inherit !important;text-decoration: none !important;font-size: inherit !important;font-family: inherit !important;font-weight: inherit !important;line-height: inherit !important;"}

        /* MOBILE STYLES */
        /* ANDROID CENTER FIX */
        div[style*="margin: 16px 0;"] {"margin: 0 !important;"}
    </style>
</head>

<body style="background-color: #f4f4f4; margin: 0 !important; padding: 0 !important;">
    <!-- HIDDEN PREHEADER TEXT -->
    <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"> Here is your One Time Password
    </div>
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <!-- LOGO -->
        
        <tr>
            <td bgcolor="#bf1591" align="center" style="padding: 60px 10px 0px 10px; background-color: linear-gradient(135deg, #f26ace 10%, #bf1591 100%)">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">
                            <h1 style="font-size: 48px; font-weight: 400; margin: 2;">Hey there!</h1> <img src="https://i.ibb.co/G0t2czh/logo.jpg" width="125" height="120" srcset="" style="display: block; border: 0px;" alt="Logo" />
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 20px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 10px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <h3 style="margin: 0; " align="center">Here is your One Time Password</h3>
                        </td>
                    </tr>
					<tr>
                        <td bgcolor="#ffffff" align="left" style=" color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0; " align="center">to validate your email address</p>
                        </td>
                    </tr>
					
                    <tr>
                        <td bgcolor="#ffffff" align="left">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td bgcolor="#ffffff" align="center" style="padding: 0px 5px 0px 20px;">
                                        <table border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td align="center" style="border-radius: 3px; " ><h1 style="font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 70px; letter-spacing: 15px;">{otp}</h1></td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr> <!-- COPY -->
                    <tr>
                        <td bgcolor="#ffffff" align="left" style=" color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px; padding-bottom: 20px;">
                            <p style="margin: 0; color: #ff4d4d;" align="center" >Valid for 5 minutes only</p>
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor="#ffffff" align="left" style="padding: 0px 30px 20px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0;" align="center">If you didn't request this , you can ignore this email.</p>
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor="#ffffff" align="left" style="padding: 0px 30px 40px 30px; border-radius: 0px 0px 4px 4px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0; "align="center">Thanks!<br>CB Team</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        
    </table>
</body>
</html>
        
        '''
    msg.attach(MIMEText(html, 'html'))
    
    s.send_message(msg)
    return "Success"

def otp_gen():
    digit="0123456789"
    password=""
    i=0
    for i in range(6):
        password=password+random.choice(digit)
        i+1
    print("Your password is "+str(password))
    file1 = open("myfile.txt","w")
    file1.write(password)
    file1.close()
    return password

@app.route('/register',methods=["POST"])
def register():
    mail=request.json['umail']
    pwd=request.json['upwd']
    opt=otp_gen()
    mm=mail_send(opt, mail)
    sql = "INSERT INTO login_table (user_mail,user_password) VALUES (%s, %s)"
    values = (mail, pwd)
    mycursor.execute(sql, values)
    mydb.commit()
    
    return jsonify(opt)

@app.route('/sregister',methods=["POST"])
def sregister():
    mail=request.json['umail']
    pwd=request.json['upwd']
    opt=otp_gen()
    mm=mail_send(opt, mail)
    sql = "INSERT INTO login_table (user_mail,user_password) VALUES (%s, %s)"
    values = (mail, pwd)
    mycursor.execute(sql, values)
    mydb.commit()
    
    return jsonify(opt)

@app.route('/otp',methods=["GET"])
def otp():
    file1 = open("myfile.txt","r+")
    myotp=file1.read()
    return jsonify(myotp)

@app.route('/student_data',methods=["GET"])
def data():
    sql = "SELECT * FROM student_data"
    mycursor.execute(sql)
    result = mycursor.fetchall()  
    if result:
        data = [dict(zip([key[0] for key in mycursor.description], row)) for row in result]
        return jsonify(data)
    else:
        return jsonify('Not')
    
@app.route('/login',methods=["POST"])
def login():
    mail=request.json['umail']
    pwd=request.json['upwd']
    sql = "SELECT * FROM login_table WHERE user_mail = %s AND user_password = %s"
    values = (mail, pwd)
    mycursor.execute(sql, values)
    result = mycursor.fetchone()
    if result:
        return jsonify('Success')
    else:
        return jsonify('Not')

@app.route('/upload_students', methods=['POST'])
def upload_students():
    # Get the uploaded CSV file
    csv_file = request.files['file']

    if not csv_file:
        return jsonify({'error': 'No file provided'}), 400

    if not csv_file.filename.endswith('.csv'):
        return jsonify({'error': 'Invalid file format. Please upload a CSV file'}), 400

    try:
        
        filename = secure_filename(csv_file.filename)
        # Save the file to the specified folder
        csv_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data = pd.read_csv('./myfiles/'+str(filename))
        data['REMARKS'] = ""

        for index, row in data.iterrows():
            student_name = row['NAMES']
            gaps = identify_skill_gaps(row)
            if not gaps:
                data.at[index, 'REMARKS'] = "Well-prepared"
            else:
                missing_skills = ', '.join(gaps)
                data.at[index, 'REMARKS'] = f"Missing skills: {missing_skills}"


        data.to_csv('./myfiles/updated.csv', index=False)

        with open('./myfiles/updated.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                # Check if the 'NAMES' value already exists in the database
                sql_check = "SELECT NAMES FROM student_data WHERE NAMES = %s"
                values_check = (row['NAMES'],)
                mycursor.execute(sql_check, values_check)
                result_check = mycursor.fetchone()

                if result_check:
                    # If 'NAMES' already exists, update the existing record
                    sql_update = """
                    UPDATE student_data
                    SET ACADEMICS = %s, `MOCK INTERVIEW` = %s, PYTHON = %s, JAVA = %s,
                        DBMS = %s, `COMPUTER NETWORKS` = %s, `MACHINE LEARNING` = %s,
                        `APTITUDE SKILLS` = %s, `FULL STACK DEVELOPMENT` = %s,
                        `COMMUNICATION SKILLS` = %s, INTERNSHIPS = %s,
                        `NUMBER OF CERTIFICATIONS` = %s, `CERTIFICATIONS DOMAIN` = %s,
                        `NUMBER OF PROJECTS` = %s, `PROJECT DOMAIN` = %s, SKILLS = %s,
                        STATUS = %s, REMARKS = %s
                    WHERE NAMES = %s
                    """
                    values_update = (row['ACADEMICS'], row['MOCK INTERVIEW'], row['PYTHON'],
                                    row['JAVA'], row['DBMS'], row['COMPUTER NETWORKS'],
                                    row['MACHINE LEARNING'], row['APTITUDE SKILLS'],
                                    row['FULL STACK DEVELOPMENT'], row['COMMUNICATION SKILLS'],
                                    row['INTERNSHIPS'], row['NUMBER OF CERTIFICATIONS'],
                                    row['CERTIFICATIONS DOMAIN'], row['NUMBER OF PROJECTS'],
                                    row['PROJECT DOMAIN'], row['SKILLS'], row['STATUS'],
                                    row['REMARKS'], row['NAMES'])
                    mycursor.execute(sql_update, values_update)
                else:
                    # If 'NAMES' does not exist, insert a new record
                    sql_insert = """
                    INSERT INTO student_data (NAMES, ACADEMICS, `MOCK INTERVIEW`, PYTHON,
                        JAVA, DBMS, `COMPUTER NETWORKS`, `MACHINE LEARNING`, `APTITUDE SKILLS`,
                        `FULL STACK DEVELOPMENT`, `COMMUNICATION SKILLS`, INTERNSHIPS,
                        `NUMBER OF CERTIFICATIONS`, `CERTIFICATIONS DOMAIN`, `NUMBER OF PROJECTS`,
                        `PROJECT DOMAIN`, SKILLS, STATUS, REMARKS)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    values_insert = (row['NAMES'], row['ACADEMICS'], row['MOCK INTERVIEW'], row['PYTHON'],
                                    row['JAVA'], row['DBMS'], row['COMPUTER NETWORKS'],
                                    row['MACHINE LEARNING'], row['APTITUDE SKILLS'],
                                    row['FULL STACK DEVELOPMENT'], row['COMMUNICATION SKILLS'],
                                    row['INTERNSHIPS'], row['NUMBER OF CERTIFICATIONS'],
                                    row['CERTIFICATIONS DOMAIN'], row['NUMBER OF PROJECTS'],
                                    row['PROJECT DOMAIN'], row['SKILLS'], row['STATUS'], row['REMARKS'])
                    mycursor.execute(sql_insert, values_insert)

                mydb.commit()


            return jsonify({'message': 'Student data uploaded successfully'}), 200
        return jsonify({'message': 'Student data uploaded successfully'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred while processing the file'}), 500

# @app.route('/delete_student',methods=['POST'])
# def delete_student():
#     mail=request.json['id']
   
#     sql = "DELETE FROM student_data WHERE id= %s"
#     values = (mail,)
#     print(mail)
#     mycursor.execute(sql, values)
#     return jsonify('Success')

# @app.route('/edit_student', methods=['POST'])
# def edit_student():
#     if request.method == 'POST':
#         data = request.json 

#         name = data.get('name')
#         academics = data.get('academics')
#         mock = data.get('mock')
#         python = data.get('python')
#         java = data.get('java')
#         dbms = data.get('dbms')
#         cn = data.get('cn')
#         ml = data.get('ml')
#         aptitude = data.get('aptitude')
#         fsd = data.get('fsd')
#         communication = data.get('communication')
#         intern = data.get('intern')
#         certifications = data.get('certfications')
#         cert_domain = data.get('certdomain')
#         projects = data.get('projects')
#         pro_domain = data.get('prodomain')
#         skills = data.get('skills')
#         id = data.get('id')

#         sql_query = """
#             UPDATE student_data
#             SET NAMES=?, ACADEMICS=?, `MOCK INTERVIEW`=?, PYTHON=?, JAVA=?, DBMS=?, 
#                 `COMPUTER NETWORKS`=?, `MACHINE LEARNING`=?, `APTITUDE SKILLS`=?, 
#                 `FULL STACK DEVELOPMENT`=?, `COMMUNICATION SKILLS`=?, INTERNSHIPS=?, 
#                 `NUMBER OF CERTIFICATIONS`=?, `CERTIFICATIONS DOMAIN`=?, `NUMBER OF PROJECTS`=?, 
#                 `PROJECT DOMAIN`=?, SKILLS=?
#             WHERE id=?
#             """

#             # Executing the SQL query
#         mycursor.execute(sql_query, (name, academics, mock, python, java, dbms, cn, ml, aptitude,
#                                     fsd, communication, intern, certifications, cert_domain,
#                                     projects, pro_domain, skills,id))

#         return jsonify({'message': 'Student updated successfully'})

if '__main__'== __name__:
    app.run(debug=True)
