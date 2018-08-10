from flask import Flask, render_template
from jinja2 import ChoiceLoader, FileSystemLoader, ModuleLoader

app = Flask(__name__)

app.jinja_env.compile_templates(
    target='templates_compiled', zip=None,
    ignore_errors=False
)

loader = ChoiceLoader([
    ModuleLoader('templates_compiled'),
    FileSystemLoader('templates')
])
app.jinja_loader = loader

@app.route('/')
def hello_world():
    return render_template("index.jinja2")


if __name__ == '__main__':
    app.run(debug=True)
