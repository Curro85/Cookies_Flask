from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    cookie_estado = request.cookies.get('cookie_estado')
    if request.method == 'POST':
        if request.form.get('btn') == 'aceptar':
            response = make_response(render_template('home.html', mostrar_cookies=False))
            response.set_cookie('cookie_estado', value='aceptada', max_age=3600, httponly=True, secure=True)
            response.set_cookie('usuario', 'Juan', max_age=3600, httponly=True, secure=True)
            return response
        elif request.form.get('btn') == 'rechazar':
            response = make_response(render_template('home.html', mostrar_cookies=False))
            response.set_cookie('cookie_estado', value='rechazada', max_age=3600, httponly=True, secure=True)
            return response
    mostrar_cookies = cookie_estado is None
    return render_template('home.html', mostrar_cookies=mostrar_cookies)


if __name__ == '__main__':
    app.run()
