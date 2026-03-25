import logging
from binance.enums import *

logger = logging.getLogger(__name__)

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        logger.info(f"Attempting {order_type} {side} for {quantity} {symbol}")

        if order_type == "LIMIT":
            if not price:
                raise ValueError("Price is required for LIMIT orders.")
            
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)
            )
        else:
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )

        logger.info(f"Order Successful: ID {response.get('orderId')}")
        return response

    except Exception as e:
        logger.error(f"Order Failed: {str(e)}")
        return {"error": str(e)}