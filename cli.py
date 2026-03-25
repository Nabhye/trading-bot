import argparse
import json
from bot.client import get_binance_client
from bot.orders import place_order
from bot.logging_config import setup_logging

def main():
    logger = setup_logging()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty","--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    client = get_binance_client()
    
    result = place_order(
        client, 
        args.symbol, 
        args.side, 
        args.type, 
        args.qty, 
        args.price
    )

    # Print summary to CLI
    if "error" in result:
        print(f"\n❌ FAILURE: {result['error']}")
    else:
        print("\n✅ ORDER PLACED SUCCESSFULLY")
        summary = {
            "orderId": result.get("orderId"),
            "status": result.get("status"),
            "executedQty": result.get("executedQty"),
            "avgPrice": result.get("avgPrice", "N/A")
        }
        print(json.dumps(summary, indent=4))

if __name__ == "__main__":
    main()