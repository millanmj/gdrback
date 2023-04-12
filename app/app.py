from flask import Flask
from flask_cors import CORS
from jiraModule.components.getAllProjects.view_getAllProjects import getAllProjects_bp
from jiraModule.components.test.test import test_bp
from jiraModule.components.createIssue.createIssue import createIssue_bp
from jiraModule.components.getIssues.getIssues import getIssues_bp
from jiraModule.components.getIssueForID.getIssueForID import getIssueForID_bp
from jiraModule.components.home.home import home_bp



app = Flask(__name__)
cors = CORS(app)  
  
app.register_blueprint(test_bp)
app.register_blueprint(createIssue_bp)
app.register_blueprint(getIssues_bp)
app.register_blueprint(getAllProjects_bp)
app.register_blueprint(getIssueForID_bp)
app.register_blueprint(home_bp)

app.static_folder = 'static'


 
if __name__ == '__main__':
    app.run(debug=True)
