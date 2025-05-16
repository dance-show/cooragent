class WorkflowCache:
    def __init__(self, cache_size: int = 100):
        self.cache_size = cache_size
        self.cache = {}
        self.store = {}
        
    @classmethod
    def init_cache(self, polish_id: str):
        self.cache[polish_id] = []
        
    def add_agent_nodes(self, polish_id: str, state: dict):
        self.cache[polish_id].append(state)
        
    def add_graph(self, polish_id: str, state: dict):
        self.cache[polish_id].append(state)
        
    def add_global_variables(self, polish_id: str, state: dict):
        self.cache[polish_id].append(state)
        
        