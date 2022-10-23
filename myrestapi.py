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
    print(path_list[1])
    return send_from_directory(directory=uploads,filename=path_list[1])


