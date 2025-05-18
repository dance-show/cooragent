from config.global_functions import func_map

class WorkflowCache:
    def __init__(self, cache_size: int = 100):
        self.cache_size = cache_size
        self.cache = {}
        self.store = {}
        
    @classmethod
    def init_cache(self, polish_id: str, lap: int, mode: str, workflow_id: str, version: int, user_input_messages: list, deep_thinking_mode: bool, search_before_planning: bool, coor_agents: list[str]):
        self.cache[polish_id] = {lap: {  
                                "workflow_id": workflow_id,
                                "mode": mode,
                                "version": version,
                                "user_input_messages": user_input_messages,
                                "deep_thinking_mode": deep_thinking_mode,
                                "search_before_planning": search_before_planning,
                                "coor_agents": coor_agents,
                                "global_variables": {
                                        "has_lauched": "true" if lap==1 else "false",
                                        "user_input": user_input_messages,
                                        "history_messages":[]
                                    },
                                "glabal_functions": [func_map[func_name] for func_name in func_map.keys()]
                                }
                            }
        
    def restore_node(self, polish_id: str, node: str):
        self.cache[polish_id][node] = self.cache[polish_id][node]
        
    def add_graph(self, polish_id: str, state: dict):
        self.cache[polish_id].append(state)
        
    def add_global_variables(self, polish_id: str, state: dict):
        self.cache[polish_id].append(state)
        
        