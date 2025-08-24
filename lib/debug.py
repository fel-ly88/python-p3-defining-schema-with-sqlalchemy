#!/usr/bin/env python3

from sqlalchemy import create_engine , sessionmaker 

from sqlalchemy_sandbox import Student

engine = create_engine('sqlite:///students.db')

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()




Session = sessionmaker(bind=engine)
session = Session()

# create
new_student = Student(name="Alice")
session.add(new_student)
session.commit()

# read
students = session.query(Student).all()
