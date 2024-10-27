from flask import Flask, render_template,request,session,redirect, url_for

app = Flask(__name__)
app.secret_key = "unaclavesecreta"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/inscripciones")
def inscripciones():
    if 'inscritos' not in session:
        # Inicializar inscritos como lista
        session['inscritos'] = []

    return render_template('inscripciones.html',inscritos = session['inscritos'])

@app.route("/registrousuarios")
def registrousuarios():
    if 'usuarios' not in session:
        # Inicializar usuarios como lista
        session['usuarios'] = []

    return render_template('registrousuarios.html',usuarios = session['usuarios'])

@app.route("/registroproductos")
def registroproductos():
    if 'productos' not in session:
        # Inicializar productos como lista
        session['productos'] = []

    return render_template('registroproductos.html',productos = session['productos'])

@app.route("/registrolibros")
def registrolibros():
    if 'libros' not in session:
        # Inicializar libros como lista
        session['libros'] = []

    return render_template('registrolibros.html',libros = session['libros'])

@app.route("/inscribir", methods=['POST'])
def inscribir():
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    curso = request.form.get('curso')

    if 'inscritos' not in session:
        # Inicializar inscritos como lista
        session['inscritos'] = []

    # Agregar el producto al carrito
    session['inscritos'].append({'nombre':nombre,'apellidos':apellidos,'curso':curso})
    session.modified = True

    return redirect(url_for("inscripciones"))

@app.route("/reg_usuarios", methods=['POST'])
def reg_usuarios():
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    correo = request.form.get('correo')
    contrasena = request.form.get('contrasena')

    if 'usuarios' not in session:
        # Inicializar usuarios como lista
        session['usuarios'] = []

    # Agregar el producto al carrito
    session['usuarios'].append({'nombre':nombre,'apellidos':apellidos,'correo':correo,'contrasena':contrasena})
    session.modified = True

    return redirect(url_for("registrousuarios"))

@app.route("/reg_productos", methods=['POST'])
def reg_productos():
    producto = request.form.get('producto')
    categoria = request.form.get('categoria')
    existencia = request.form.get('existencia')
    precio = float(request.form.get('precio'))

    if 'productos' not in session:
        # Inicializar productos como lista
        session['productos'] = []

    # Agregar el producto al carrito
    session['productos'].append({'producto':producto,'categoria':categoria,'existencia':existencia,'precio':precio})
    session.modified = True

    return redirect(url_for("registroproductos"))

@app.route("/reg_libros", methods=['POST'])
def reg_libros():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    resumen = request.form.get('resumen')
    medio = request.form.get('medio')

    if 'libros' not in session:
        # Inicializar libros como lista
        session['libros'] = []

    # Agregar el libros 
    session['libros'].append({'titulo':titulo,'autor':autor,'resumen':resumen,'medio':medio})
    session.modified = True

    return redirect(url_for("registrolibros"))
    

@app.route("/vaciar_inscritos")
def vaciar_inscritos():
    # Elimina la session
    session.pop('inscritos', None)
    return redirect(url_for("inscripciones"))

@app.route("/vaciar_usuarios")
def vaciar_usuarios():
    # Elimina la session
    session.pop('usuarios', None)
    return redirect(url_for("registrousuarios"))

@app.route("/vaciar_productos")
def vaciar_productos():
    # Elimina la session
    session.pop('productos', None)
    return redirect(url_for("registrouproductos"))

@app.route("/vaciar_libros")
def vaciar_libros():
    # Elimina la session
    session.pop('libros', None)
    return redirect(url_for("registrolibros"))
    
if __name__ == "__main__":
    app.run(debug = True)