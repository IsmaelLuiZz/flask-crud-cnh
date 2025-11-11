from flask import Flask, request, jsonify
from service.cnh_service import CNHService

app = Flask(__name__)
service = CNHService()

@app.route('/cnh', methods=['POST'])
def create_cnh():
    data = request.get_json()
    nova_cnh = service.create_cnh(data)
    return jsonify(nova_cnh), 201

@app.route('/cnh', methods=['GET'])
def get_all_cnhs():
    cnhs = service.get_all_cnhs()
    return jsonify(cnhs), 200

@app.route('/cnh/<int:id>', methods=['GET'])
def get_cnh_by_id(id):
    cnh = service.get_cnh_by_id(id)
    if cnh:
        return jsonify(cnh), 200
    return jsonify({'message': 'CNH não encontrada'}), 404

@app.route('/cnh/<int:id>', methods=['PUT'])
def update_cnh(id):
    data = request.get_json()
    cnh_atualizada = service.update_cnh(id, data)
    if cnh_atualizada:
        return jsonify(cnh_atualizada), 200
    return jsonify({'message': 'CNH não encontrada'}), 404

@app.route('/cnh/<int:id>', methods=['DELETE'])
def delete_cnh(id):
    deleted = service.delete_cnh(id)
    if deleted:
        return jsonify({'message': 'CNH excluída com sucesso'}), 200
    return jsonify({'message': 'CNH não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
