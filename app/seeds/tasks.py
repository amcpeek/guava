from app.models import db, Task, environment, SCHEMA


def seed_tasks():
    task1=Task(projectId=1, name='Curriculum Reviewing Event',
    description='Invite teachers across the district to review curriculum at the science dept' )
    task2=Task(projectId=1, name='School Board Meeting to Select Curriculum',
    description='Analyze the result from the teacher curriculum viewing event to create a slide deck for the school board meeting' )
    task3=Task(projectId=1, name='Finalize purchase of curriculum with curriculum company',
    description='Go over the budge internally with the district and sign contract with the curriculum company' )
    task4=Task(projectId=1, name='Plan for teacher leaders to be trained in the new curriculum',
    description='Work with school district to create a summer training program for teacher leaders and fall training for all teachers' )
    task5=Task(projectId=2, name='Review grant application',
    description='Evaluate if our school can meet the restrictions of the grant application, and if funds are worth the expense of applying for the grant' )
    task6=Task(projectId=2, name='Create budget for grant application',
    description='Develop a list of all items we would like to purchase with the grant funds that meet the requirements of the grant' )
    task7=Task(projectId=2, name='Get permission from parents to include photos of students for the grant application',
    description='Photos are required for the application, and the form to get parents to consent is on their website' )
    task8=Task(projectId=2, name='Write the application content and get the grant reviewed',
    description='Ask another team member to review the content of the application.' )
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)
    db.session.add(task6)
    db.session.add(task7)
    db.session.add(task8)
    db.session.commit()






# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_tasks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM tasks")

    db.session.commit()