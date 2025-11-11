from model.cnh_model import CNHModel

class CNHService:
    def __init__(self):
        self.model = CNHModel()

    def create_cnh(self, data):
        cnh_id = self.model.insert(data)
        return self.model.fetch_by_id(cnh_id)

    def get_all_cnhs(self):
        return self.model.fetch_all()

    def get_cnh_by_id(self, id):
        return self.model.fetch_by_id(id)

    def update_cnh(self, id, data):
        updated = self.model.update(id, data)
        if updated:
            return self.model.fetch_by_id(id)
        return None

    def delete_cnh(self, id):
        return self.model.delete(id)
