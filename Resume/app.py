from flask import Flask,request,jsonify
from flask_cors import CORS
from config import db ,SECRET_KEY
from os import path,getcwd,environ
from dotenv import load_dotenv
from models.user import User
from models.projects import Projects
from models.experiences import Experiences
from models.educations import Educations
from models.skills import Skills
from models.certificates import Certificates
from models.personaldetails import PersonalDetails

load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key=SECRET_KEY

    db.init_app(app)
    print("DB Initialized successfully")

    with app.app_context():
        @app.route("/signup",methods=['POST'])
        def signup():
            data=request.form.to_dict(flat=True)

            new_user=User(
                username=data['username']
            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg="User added successfully")

        @app.route("/add_personal_details",methods=['POST'])
        def add_personal_details():
            recv_username=request.args.get('username')
            user=User.query.filter_by(username=recv_username).first()

            data=request.get_json()

            new_personal_details=PersonalDetails(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                address=data['address'],
                linkedin_url=data['linkedin_url'],
                user_id=user.id
            )

            db.session.add(new_personal_details)
            db.session.commit()

            return jsonify(msg="Personal details added successfully")

        @app.route('/add_projects',methods=['POST'])
        def add_projects():
            recv_username=request.args.get('username')
            user=User.query.filter_by(username=recv_username).first()

            projectlist=request.get_json()

            for project in projectlist["data"]:
                new_projects=Projects(
                    name=project['name'],
                    desc=project['desc'],
                    start_date=project['start_date'],
                    end_date=project['end_date'],
                    user_id=user.id
                )
                db.session.add(new_projects)
                db.session.commit()

                return jsonify(msg="Project added successfully")

        @app.route('/add_experiences',methods=['POST'])
        def add_experiences():
            recv_username=request.args.get('username')
            user=User.query.filter_by(username=recv_username).first()

            experiencelist=request.get_json()

            for experience in experiencelist["data"]:
                new_experiences=Experiences(
                    company_name=experience['company_name'],
                    role=experience['role'],
                    role_desc=experience['role_desc'],
                    start_date=experience['start_date'],
                    end_date=experience['end_date'],
                    user_id=user.id
                )
                db.session.add(new_experiences)
                db.session.commit()

                return jsonify(msg="Experience added successfully")

        @app.route('/add_educations',methods=['POST'])
        def add_educations():
            recv_username=request.args.get('username')
            user=User.query.filter_by(username=recv_username).first()

            educationlist=request.get_json()

            for education in educationlist["data"]:
                new_educations=Educations(
                    school_name=education['school_name'],
                    degree_name=education['degree_name'],
                    start_date=education['start_date'],
                    end_date=education['end_date'],
                    user_id=user.id
                )
                db.session.add(new_educations)
                db.session.commit()

                return jsonify(msg="Education added successfully")

        @app.route("get_resume_json", methods=["GET"])
        def get_resume_json():
            recv_username=request.args.get('username')
            user=User.query.filter_by(username=recv_username).first()

            personal_details=PersonalDetails.query.filter_by(user_id=user.id).first()
            experiences=Experiences.query.filter_by(user_id=user.id).all()
            projects=Projects.query.filter_by(user_id=user.id).all()
            educations=Educations.query.filter_by(user_id=user.id).all()
            certificates=Certificates.query.filter_by(user_id=user.id).all()
            skills=Skills.query.filter_by(user_id=user.id).all()
            
            resume_data={
                "name":personal_details.name,
                "email":personal_details.email,
                "phone":personal_details.phone,
                "address":personal_details.address,
                "LinkedIn_url": personal_details.linkedin_url
            }

            experiences_data=[]
            projects_data=[]
            educations_data=[]
            certificates_data=[]
            skills_data=[]
            

            #Experience
            for exp in experiences:
                experiences_data.append({
                "comapny_name":exp.company_name,
                "role":exp.role,
                "role_desc":exp.role_desc,
                "start_date":exp.start_date,
                "end_date":exp.end_date,
            })

            resume_data["experiences"]=experiences_data
            return resume_data
            



        #db.drop_all()
        db.create_all()
        db.session.commit()

        return app
if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)
    
