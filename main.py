"""
로또 번호 생성기 MCP 서버
"""

from fastmcp import FastMCP
import random
from typing import List

# Create server
mcp = FastMCP("LottoServer")


@mcp.tool
def generate_lotto_numbers(count: int = 1) -> dict:
    """로또 번호를 생성합니다. 1부터 45까지의 숫자 중 중복 없이 6개를 선택합니다.
    
    Args:
        count: 생성할 로또 번호 조합의 개수 (기본값: 1)
    
    Returns:
        dict: {"lotto_numbers": [[...], ...]} 형태의 JSON 객체
    """
    lotto_combinations = []
    
    for _ in range(count):
        # 1부터 45까지의 숫자 중 중복 없이 6개 선택
        numbers = random.sample(range(1, 46), 6)
        # 오름차순 정렬
        numbers.sort()
        lotto_combinations.append(numbers)
    
    return {"lotto_numbers": lotto_combinations}


if __name__ == "__main__":
    mcp.run()
