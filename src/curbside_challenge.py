import aiohttp
import asyncio
import json

async def fetch(session, url, session_id):
	async with session.get(url, headers={'Session': session_id}) as response:
		try:
			return await response.json()
		except:
			return await response.text()

async def main(host, path, session_id):
	async with aiohttp.ClientSession() as session:
		data = await fetch(session, host + path, session_id)
		print(data)
		return data

host = 'http://challenge.curbside.com'
secrets = ''

async def crawl(queue, path, session_id):
	queue = asyncio.Queue()
	# fetch url
	data = await main(host, path, session_id)
	if 'secret' in data:
		secrets += data['secret']
	if 'next' in data:
		for n in data['next']:
			queue.put(n)


loop = asyncio.get_event_loop()
loop.run_until_complete(crawl('/start', '97e2d5104d8b46f79d70f707b3c7116f'))