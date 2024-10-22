def batch_api(page)-> dict :
    return {
        "nextPage": page + 1,
        "results": [page*10+n for n in range(10)],
    }

class API:
    def __init__(self) -> None:
        self.buffer = []
        self.next_batch = 0
    
    def stream_api(self, n: int) -> list[str]:
        while len(self.buffer) < n:
            api_result = batch_api(self.next_batch)
            self.buffer.extend(api_result["results"])
            self.next_batch = api_result["nextPage"]
        answer = self.buffer[0 : n]
        self.buffer = self.buffer[n: len(self.buffer)]
        return answer


a = API()    
print(a.stream_api(3))
print(a.stream_api(20))
print(a.stream_api(32))
print(a.stream_api(14))
print(a.stream_api(12))
print(a.stream_api(33))
print(a.stream_api(25))