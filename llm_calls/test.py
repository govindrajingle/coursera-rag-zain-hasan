from openai import OpenAI, DefaultHttpxClient
import httpx

base_url = get_proxy_url()
transport = httpx.HTTPTransport(local_address="0.0.0.0", verify=False)
http_client = DefaultHttpxClient(transport=transport, headers=get_proxy_headers())

client = OpenAI(api_key=get_together_key(), base_url=base_url, http_client=http_client)

messages = [
    {"role": "user", "content": "Hello, who won the FIFA world cup in 2018?"},
    {"role": "assistant", "content": "France won the 2018 FIFA World Cup."},
    {"role": "user", "content": "Who was the captain?"},
]

response = client.chat.completions.create(
    messages=messages, model="Qwen/Qwen3.5-9B", extra_body={"reasoning": False}
)

print(response)
