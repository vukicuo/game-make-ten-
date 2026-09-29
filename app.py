from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# giao diện
@app.route('/')
def home():
    return render_template('index.html')

# cơ chế
@app.route('/nop-diem', methods=['POST'])
def nop_diem():
    data = request.get_json()
    diem_so = data.get('score', 0)
    
   
    print(f"\n---> HOÀN THÀNH LƯỢT CHƠI! Người chơi đạt: {diem_so} điểm <--- \n")
    
    return jsonify({"status": "thành công"})

if __name__ == '__main__':
    app.run(debug=True)