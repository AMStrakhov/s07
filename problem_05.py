"""
Description:
Cover the given class with unit tests and fix the problems.
"""
from typing import Dict, List


class TradeStatistics:
    def __init__(self, deals: List[Dict]) -> None:
        self._deals = deals

    def get_prices_list(self) -> List[float]:
        self._calculate_prices_for_deals(self._deals)
        return [d["price"] for d in self._deals]

    @classmethod
    def _calculate_prices_for_deals(cls, deals: List[Dict]) -> None:
        for deal in deals:
            deal["price"] = cls._calculate_price(deal["value"], deal["volume"])

    @staticmethod
    def _calculate_price(value: float, volume: float) -> float:
        return value / volume


if __name__ == "__main__":
    deals_case = [
        {"value": 100, "volume": 50},
        {"value": 50, "volume": 10},
        {"value": 1000, "volume": 500},
    ]
    ts = TradeStatistics(deals_case)
    print(ts.get_prices_list())
