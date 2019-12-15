from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'custom-mysql.gamification.svc.cluster.local'
app.config['MYSQL_USER'] = 'xxuser'
app.config['MYSQL_PASSWORD'] = 'welcome1'
app.config['MYSQL_DB']= 'sampledb'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def employees():
	cur = mysql.connection.cursor()
	res = cur.execute("SELECT ITEM_NUMBER, DESCRIPTION, LONG_DESCRIPTION FROM sampledb.XXIBM_PRODUCT_STYLE")
	if res > 0:
		userDetails = cur.fetchall()
		return render_template('employee.html',userDetails=userDetails)
	else
		return '''<h1>Database Information Missing</h1>
<p>A prototype API </p>'''
	
		
if __name__ == "__main__":
    app.run()

