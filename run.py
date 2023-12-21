from api_manga import *
from api_get_home import *
from api_account_management import *
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
cors = CORS(app, resource={
        r"/*":{
                    "origins":"*"
                        }
        })

with app.app_context():
    db.create_all()

if __name__ =="__main__":
	app.run(host='0.0.0.0', port=7979, debug=True)
