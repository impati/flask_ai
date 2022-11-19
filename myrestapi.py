from flask import Flask ,jsonify,request,send_from_directory,current_app
from flask_cors import CORS
import mydetect as md
import os
server = Flask(__name__)
CORS(server)



host_name ="http://localhost:9090/"
@server.route("/")
def home ():
    return {"resp" :"ok"}


@server.route('/v1/decision',methods =['POST'])
def main():
    data = request.get_json()
    print(data["image_path"])
    (result,filename) = md.main(data["image_path"])
    namelist = filename.split('/')
    image_url = host_name + "image/" + namelist[-2]+'_'+namelist[-1]
    print(image_url)
    return { "class_id" :result , "image_url" :image_url}
    
@server.route("/image/<path>")
def image_location(path):
    print(path)
    print(current_app.root_path)
    uploads = os.path.join(current_app.root_path+"/runs/detect/")
    path_list = path.split('_')
    uploads += path_list[0] 
    print(uploads)
    image_path =""
    path_len = len(path_list[1:]) 
    for i in range(path_len):
        image_path += path_list[1:][i]
        if i + 1 != path_len:
            image_path += '_'
    print(image_path)
    return send_from_directory(directory=uploads,filename=image_path)


