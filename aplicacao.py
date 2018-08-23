from flask import Flask, render_template, request, session, redirect
import time


app = Flask(__name__)
app.secret_key = 'Luan'


@app.route('/')
def home():
	turma = 'TURMA 2018.1 A + X'
	alunos = ['ELITON', 'SIM', 'PVABCDE', 'ISAIS']

	alunos2 = ['RONIEL', 'Gui', 'PH', 'Elcy']
	return render_template('ads.html', turma=turma, 
		tops=alunos, massas=alunos2)


@app.route('/entrar', methods=['POST'])
def entrar():
	usuario = request.form['usuario']
	senha = request.form.get('senha', '7654')

	session['user'] = usuario

	time.sleep(3)
	return redirect('/')


@app.route('/sair')
def sair():
	del session['user']
	time.sleep(2)

	return redirect('/')









