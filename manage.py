# -×- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from app import app
from app.models import Todo

manager = Manager(app)

manager.add_command("runserver",
                    Server(host='0.0.0.0',
                           port=5000,
                           use_debugger=True))


@manager.command
def save_todo(twits):
    todo = Todo(content=twits)
    todo.save()


if __name__ == '__main__':
    manager.run()