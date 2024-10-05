from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Base class for declarative models
Base = declarative_base()

# Department class (One-to-Many with Employee)
class Department(Base):
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationship to the Employee class
    employees = relationship('Employee', back_populates='department')



# Employee class (One-to-Many with Project)
class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    salary = Column(Numeric, nullable=False)
    
    # ForeignKey to the Department table
    department_id = Column(Integer, ForeignKey('departments.id'))
    
    # Relationship to Department and Project classes
    department = relationship('Department', back_populates='employees')
    projects = relationship('Project', back_populates='employee')

# Project class (One-to-Many with Employee)
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    
    # ForeignKey to the Employee table
    employee_id = Column(Integer, ForeignKey('employees.id'))
    
    # Relationship to the Employee class
    employee = relationship('Employee', back_populates='projects')

# Create engine and session
engine = create_engine('postgresql://postgres:roop@localhost/mydb')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)

# Example Insertion:
# Creating Department
it_department = Department(name='IT')
session.add(it_department)

# Creating Employee and linking to the IT department
employee1 = Employee(name='John Doe', salary=70000, department=it_department)
session.add(employee1)

# Creating Project and linking it to Employee
project1 = Project(title='Cloud Migration', employee=employee1)
session.add(project1)

# Commit all changes
session.commit()

# Query Example: Retrieve all projects of an employee
employee = session.query(Employee).filter_by(name='John Doe').first()
for project in employee.projects:
    print(f"Employee {employee.name} is working on project {project.title}")

# Close session
session.close()
