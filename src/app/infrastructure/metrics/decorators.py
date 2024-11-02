from typing import Callable, Any
from functools import wraps
import time


def measure_time(func: Callable) -> Any:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        start_time: float = time.time()
        try:
            response: Any = await func(*args, **kwargs)
            end_time: float = time.time()
            
            execution_time: float = end_time - start_time
            print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")

            return response
        
        except Exception as e:
            end_time: float = time.time()
            execution_time: float = end_time - start_time
            print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
            raise e
    return wrapper