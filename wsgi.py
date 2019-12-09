from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'jdbc:mysql://mysql.gamification.svc.cluster.local:3306/sampledb'
app.config['MYSQL_USER'] = 'xxuser'
app.config['MYSQL_PASSWORD'] = 'welcome1'
app.config['MYSQL_DB']= 'sampledb'

@app.route('/')
def employees():
	cur = mysql.connection.cursor()
	res = cur.execute("SELECT ITEM_NUMBER, DESCRIPTION, LONG_DESCRIPTION FROM XXXIBM_PRODUCT_STYLE LIMIT 10")
	if res > 0:
		userDetails = cur.fetchall()
		return render_template('employee.html',userDetails=userDetails)
		
if __name__ == "__main__":
    app.run()
