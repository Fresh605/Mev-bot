import os, requests
from neynar_sdk import NeynarClient

c = NeynarClient(os.getenv("NEYNAR_API_KEY"))
s = os.getenv("SIGNER_UUID")

amount = 10**18
a = requests.get(f"https://api.1inch.io/v5.0/8453/quote?fromTokenAddress=0x4200000000000000000000000000000000000006&toTokenAddress=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913&amount={amount}").json()
b = requests.get(f"https://api.1inch.io/v5.0/8453/quote?fromTokenAddress=0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913&toTokenAddress=0x4200000000000000000000000000000000000006&amount={a['toTokenAmount']}").json()

profit = (int(b["toTokenAmount"]) - amount) / 10**18
if profit > 0.005:
    c.publish_cast(signer_uuid=s, text=f"MEV Alert – Base\nWETH↔USDC profit: {profit:.5f} ETH\nBot by @fresh605 – 100% free forever\n#MEV #Farcaster")
