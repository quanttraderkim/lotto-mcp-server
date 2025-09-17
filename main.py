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


@mcp.tool
def get_lucky_number() -> dict:
    """행운의 숫자를 추천합니다. 1부터 100까지의 숫자 중에서 선택합니다.
    
    Returns:
        dict: {"lucky_number": 숫자, "message": "행운의 메시지"} 형태의 JSON 객체
    """
    lucky_number = random.randint(1, 100)
    
    # 행운의 메시지 생성
    messages = [
        "오늘은 정말 행운이 가득한 날이 될 것 같아요! 🍀",
        "이 숫자가 당신에게 큰 행운을 가져다줄 거예요! ✨",
        "믿음과 함께 이 숫자를 기억하세요! 🌟",
        "행운의 여신이 당신을 도와줄 거예요! 💫",
        "이 숫자와 함께 좋은 일들이 생길 거예요! 🌈"
    ]
    
    message = random.choice(messages)
    
    return {
        "lucky_number": lucky_number,
        "message": message
    }


if __name__ == "__main__":
    mcp.run()
