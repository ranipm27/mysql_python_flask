from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["DEBUG"] = True

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'xxuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'welcome'
app.config['MYSQL_DATABASE_DB'] = 'sampledb'
app.config['MYSQL_DATABASE_HOST'] = 'custom-mysql.gamification.svc.cluster.local'
mysql.init_app(app)

#app.config["MYSQL_HOST"] = 'custom-mysql.gamification.svc.cluster.local'
#app.config["MYSQL_USER"] = 'xxuser'
#app.config["MYSQL_PASSWORD"] = 'welcome1'
#app.config["MYSQL_DB"]= 'sampledb'
#mysql = MySQL(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/products')
def products():
	conn = mysql.connect()
	cur = conn.cursor()
	res = cur.execute("SELECT ITEM_NUMBER, DESCRIPTION, LONG_DESCRIPTION FROM sampledb.XXIBM_PRODUCT_STYLE")
	if len(res) > 0:
		userDetails = cur.fetchall()
		return render_template('employee.html',userDetails=userDetails)
	cur.close()
	conn.close()
				       
		
if __name__ == "__main__":
    app.run(port=8080)

