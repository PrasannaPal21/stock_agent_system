from flask import Flask, request, jsonify
from agent import route_query

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    if request.is_json:
        data = request.get_json()
        query = data.get('query', '')
    else:
        query = request.form.get('query', '')
    response = route_query(query)
    return jsonify({'response': response})

@app.route('/', methods=['GET'])
def home():
    return '''
        <h2>Stock Query Web Interface</h2>
        <form action="/query" method="post" id="queryForm">
    <input type="text" id="query" name="query">
    <input type="submit" value="Submit">
</form>
<script>
document.getElementById('queryForm').onsubmit = async function(e) {
    e.preventDefault();
    const query = document.getElementById('query').value;
    const response = await fetch('/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
    });
    const data = await response.json();
    document.getElementById('result').innerHTML = '<b>Response:</b> ' + data.response.replace(/\n/g, '<br>');
};
</script>
    '''

if __name__ == '__main__':
    app.run(port=5000)