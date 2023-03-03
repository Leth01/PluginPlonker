from typing import Any

class Resource:

    def __init__(self, **kwargs):
        self.supported_types = {}
        self.supported_types.update(kwargs)

    def __getattr__(self, name: str) -> Any:
        return self.supported_types.get(name)

    def __repr__(self):
        return str(self.supported_types)

class HostnameResource(Resource):
    def __init__(self, hostname):
        super().__init__(hostname=hostname)

class IpAddressResource(Resource):
    def __init__(self, ip):
        super().__init__(ip=ip)

class ServiceResource(Resource):
    def __init__(self, ip, port, service):
        super().__init__(ip=ip, port=port, service=service)

class HashResource(Resource):
    def __init__(self, password_hash, hash_type):
        super().__init__(hash=password_hash, hash_type=hash_type)





