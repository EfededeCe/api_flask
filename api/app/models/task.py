from . import db
from sqlalchemy.event import listen



class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.Text, nullable = False)
    deadline = db.Column(db.DateTime(), nullable = False)
    created_at = db.Column(db.DateTime(), nullable = False,\
                            default = db.func.current_timestamp())

    def __str__(self):
        return self.title

def inserte_tasks(*args, **kwargs):
    db.session.add(
        Task(title="Titulo1", description="descripcion 1",
        deadline= "2023-25-01 12:00:00")
    )
    db.session.add(
        Task(title="Titulo2", description="descripcion 2",
        deadline= "2023-25-01 12:00:00")
    )
    db.session.commit()

listen(Task.__table__,"after_create", inserte_tasks)

