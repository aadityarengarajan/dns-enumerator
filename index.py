'''
                                                                                                                                               
 _|_|_|    _|      _|    _|_|_|      _|_|_|_|                                                                      _|                          
 _|    _|  _|_|    _|  _|            _|        _|_|_|    _|    _|  _|_|_|  _|_|      _|_|    _|  _|_|    _|_|_|  _|_|_|_|    _|_|    _|  _|_|  
 _|    _|  _|  _|  _|    _|_|        _|_|_|    _|    _|  _|    _|  _|    _|    _|  _|_|_|_|  _|_|      _|    _|    _|      _|    _|  _|_|      
 _|    _|  _|    _|_|        _|      _|        _|    _|  _|    _|  _|    _|    _|  _|        _|        _|    _|    _|      _|    _|  _|        
 _|_|_|    _|      _|  _|_|_|        _|_|_|_|  _|    _|    _|_|_|  _|    _|    _|    _|_|_|  _|          _|_|_|      _|_|    _|_|    _|        
                                                                                                                                               
                                                                                                                                               
Python-based web application that accepts hostname in the text field and all the dns records are shown. 
BY AADITYA RENGARAJAN
CREATION TIMESTAMP : 23:19 03/07/22 07 03 2022
'''
#==============IMPORTING MODULES======================================================
#/- see 'requirements.txt' to install extra modules via pip
from flask import redirect, render_template, Flask, request, url_for, send_file
from modules.dns_enum import get_records as enumerate

#==============DEFINING BASIC FUNCTIONS======================================================
app = Flask(__name__)
#==============ROUTES======================================================
#/- routes are defined by @app.route decorator

@app.route('/favicon.ico')
def favicon():
    return send_file("thumb.png")

@app.route('/')
def index():
    if request.args.get("domain"):
        records = enumerate(request.args.get("domain"))
        return render_template("index.html",records=records,domain=request.args.get("domain"))
    return render_template("index.html")

#==============PROGRAM RUN======================================================
if __name__=="__main__":
    #/- note : remove debuggers and change port respectively
    #/- on production deployment.
    app.run(
        debug=True,
        use_reloader=True,
        use_debugger=True,
        port=8080,
        use_evalex=True,
        threaded=True,
        passthrough_errors=False
        )
#==============END OF WEBAPP======================================================
#/- COMPLETION TIMESTAMP : 23:37 03/07/22 07 03 2022 -/#