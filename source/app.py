# from flask import Flask
# from flask_cors import CORS
# from app.jiraModule.components.getAllProjects.view_getAllProjects import getAllProjects_bp
# from app.jiraModule.components.test.test import test_bp
# from app.jiraModule.components.createIssue.view_createIssue import createIssue_bp
# from app.jiraModule.components.getIssues.getIssues import getIssues_bp
# from app.jiraModule.components.getIssueForID.getIssueForID import getIssueForID_bp
# from app.jiraModule.components.home.home import home_bp

# app = Flask(__name__)
# cors = CORS(app)  
# app.url_map.strict_slashes = False
# app.register_blueprint(test_bp)
# app.register_blueprint(createIssue_bp)
# app.register_blueprint(getIssues_bp)
# app.register_blueprint(getAllProjects_bp)
# app.register_blueprint(getIssueForID_bp)
# app.register_blueprint(home_bp)

# app.static_folder = 'static'
# app.template_folder='templates'

 
# if __name__ == '__main__':
#     try:    
#         app.run()
#     except Exception as e:
#         print(f'Ocurrio un error en la ejecución: {e}') 