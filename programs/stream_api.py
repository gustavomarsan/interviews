# requiring a list of pages, from a online book and generete from 10 to 10

def batch_api(page)-> dict :     # function generates a list of 10 elements in results, parameter is last package sent it
    return {
        "results": [page*10+n for n in range(10)],  # generate  list of new 10 numbers
        "nextpage": page + 1                        # update packagecor last page sent
    }

class API:
    def __init__(self) -> None:
        self.buffer = []
        self.next_batch = 0
    
    def stream_api(self, n: int) -> list[str]:
        while len(self.buffer) < n:                     # if len buffers < n (required) until buffer > n (pages required)
            api_result = batch_api(self.next_batch)     # ask to batch_api for a new page = dict{ "results": [..] , "nextpage:" int}
            self.buffer.extend(api_result["results"])   # append new list of pages to self.buffer from api_result
            self.next_batch = api_result["nextpage"]    # update value for next package of pages from api_result
        answer = self.buffer[0 : n]                     # value to return of n elements from de buffer
        self.buffer = self.buffer[n: len(self.buffer)]  # update buffer eliminating elements that were send it
        return answer


a = API()    
print(a.stream_api(3))
print(a.stream_api(20))
print(a.stream_api(2))
print(a.stream_api(12))
print(a.stream_api(5))
print(a.stream_api(22))
print(a.stream_api(18))
print(a.stream_api(7))
