from alpaca_trade_api import StreamConn
import threading


# conn = tradeapi.stream2.StreamConn('YOUR API KEY','API SECRET',base_url)

conn = StreamConn('YOUR API KEY','API SECRET',base_url)


@conn.on(r'^account_updates$')
async def on_account_updates(conn,channel,account):
    print("The account displayed is :",account)


@conn.on(r'^trade_updates$')
async def on_trade_updates(conn,channel,trade):
    print("The account displayed is :",trade)


def ws_start():

    conn.run(['account_updates','trade_updates'])

ws_thread = threading.Thread(target=ws_start,daemon=True)

ws_thread.start()