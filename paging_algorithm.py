from collections import defaultdict, deque

def furthest_in_future_paging(k, requests):
    cache = set()
    future = defaultdict(deque)
    page_faults = 0
    
    for i in range(len(requests)):
        future[requests[i]].append(i)
    
    for i, app in enumerate(requests):
        if future[app]:
            future[app].popleft()  
        if app in cache:
            continue 
        
        page_faults += 1
        if len(cache) == k:
            furthest_use_app = None
            furthest_use_index = -1
            
            for cached_app in cache:
                if future[cached_app]:
                    next_use = future[cached_app][0]
                else:
                    next_use = float('inf') 
                
                if next_use > furthest_use_index:
                    furthest_use_index = next_use
                    furthest_use_app = cached_app
            
            if furthest_use_app is not None:
                cache.remove(furthest_use_app)
        
        cache.add(app)
    
    return page_faults
