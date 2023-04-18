from csv import DictReader, DictWriter
from flask import jsonify, Flask, request
from os import chdir
from os.path import dirname
from traceback import format_exc
import re

SERVER = Flask(__name__)
DATABASE = []
RELATIVE_THRESHOLD = 0.9

@SERVER.after_request
def after_request(response):
	response.headers.update({
		'Access-Control-Allow-Credentials': 'true',
		'Access-Control-Allow-Headers': 'content-type',
		'Access-Control-Allow-Origin': '*'
	})
	return response

@SERVER.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@SERVER.route('/<path:path>', methods=['GET', 'POST'])
def api(path):
	data = request.get_json()
	try:
		if path == 'order':
			res = order(data)
		elif path == 'topgc':
			res = top_gc(data)
		elif path == 'roots':
			res = roots(data)
		else:
			res = {'error': 'Invalid path.'}
	except Exception as e:
		res = {
			'error': str(e),
			'trace': format_exc().split('\n')
		}
	return jsonify(res)

def order(data):
	# TODO form validation
	name_regex = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
	assert 'name' in data and re.match(name_regex, data['name']) and 4 <= len(data['name']) <= 32, 'Full name should be 4-32 characters long and have exactly two words, capitalized.'
    # Validate password
	password_regex = r'^(?=.*\d)(?=.*[A-Z]{2})(?=.*[\W_])[A-Za-z\d@$!%*#?&]{11,31}$'
	assert 'password' in data and re.match(password_regex, data['password']), 'Password should be 12-32 characters long, start with a number, contain two uppercase letters one after another, and at least one symbol.'
	# Validate age
	assert 'age' not in data or (isinstance(data['age'], str) and data['age'].isdigit() and 18 <= int(data['age']) <= 125), 'Age should be an integer between 18 and 125.'
    # Validate x
	assert 'x' in data and re.match(r'^\d+(\.\d+)?%?$', str(data['x'])) and (data['x'].endswith('%') and (0 <= float(data['x'].replace("%", "")) <= 100)), 'Location X should be a percentage with optional decimals that represents your relative position in a Robinson projection of the world.'
    # Validate y
	assert 'y' in data and re.match(r'^\d+(\.\d+)?%?$', str(data['y'])) and (data['y'].endswith('%') and (0 <= float(data['y'].replace("%", "")) <= 100)), 'Location Y should be a percentage with optional decimals that represents your relative position in a Robinson projection of the world.'
	# Validate description
	assert 'description' not in data or (isinstance(data['description'], str) and 10 <= len(data['description']) <= 500), 'Description must be a string with 10-500 characters.'
	# Validate public
	assert 'public' not in data or isinstance(data['public'], bool), 'Public must be a boolean.'
	# Validate sell
	assert 'sell' not in data or isinstance(data['sell'], bool), 'Sell must be a boolean.'
	# Validate terms
	assert 'terms' in data and data['terms'] == True, 'You must agree to the terms.'
	return {'id': insert({
		'name': data['name'],
		'password': data['password'],
		'age': data['age'] if 'age' in data else '',
		'x': float(data['x'].rstrip("%")) / 100,
		'y': float(data['y'].rstrip("%")) / 100,
		'description': data['description'] if 'description' in data else '',
		'public': data['public'],
		'sell': data['sell'],
		'genome': ''
	})}

def top_gc(data):
	res = []
	for user in DATABASE:
		if len(user['genome']) == 0: continue
		res.append({
			'name': user['name'],
			'age': user['age'],
			'description': user['description'],
			'score': '%.2f%%' % (100 * (user['genome'].count('G') + user['genome'].count('C')) / len(user['genome']))
		})
	res.sort(key=lambda x: float(x['score'][:-1]), reverse=True)
	return res

def roots(data):
	assert 'genome' in data and len(data['genome']) == 100 and all(c in 'ATCG' for c in data['genome']), 'Invalid genome.'
	res = [{
		'name': user['name'],
		'x': user['x'],
		'y': user['y'],
		'score': score(data['genome'], user['genome'])
	} for user in DATABASE if len(user['genome'])]
	return sorted(res, key=lambda user: -user['score'])[:5]

def score(genome1, genome2):
    if not genome1 or not genome2:  # if any of the genomes is empty, return 0
        return 0
    # Finding the longest common sequence
    max_seq_length = 0
    for i in range(len(genome1)):
        for j in range(len(genome2)):
            seq_length = 0
            while genome1[i] == "G" and i + seq_length < len(genome1) and j + seq_length < len(genome2) and genome1[i + seq_length] == genome2[j + seq_length]:
                seq_length += 1
            if seq_length > max_seq_length:
                max_seq_length = seq_length
    # Computing the match percentage
    match_percentage = max_seq_length / len(genome1)
    return match_percentage

def insert(data):
	global MAX_ID
	assert type(data) is dict, 'Data must be a dictionary.'
	for key in KEYS:
		if key == 'id': continue
		assert key in data, 'Missing value for "%s".' % key
	for key in data:
		assert key in KEYS, 'Key "%s" is not allowed.' % key
	MAX_ID += 1
	data['id'] = str(MAX_ID)
	DATABASE.append(data)
	with open('database.csv', 'a', newline='', encoding='utf-8') as f:
		writer = DictWriter(f, KEYS)
		writer.writerow(data)
	return MAX_ID

if __name__ == '__main__':
	chdir(dirname(__file__))
	with open('database.csv', 'r', encoding='utf-8') as f:
		DATABASE = [row for row in DictReader(f)]
		KEYS = DATABASE[0].keys()
		MAX_ID = int(DATABASE[-1]['id'])
	SERVER.run(host='0.0.0.0', port=20230)