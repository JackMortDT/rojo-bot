import discord

client = discord.Client()

@client.event
async def on_message(message):
  	if message.author == client.user:
  		return

  	if message.content.startswith('Hola'):
  		msg = 'Hola {0.author.mention}'.format(message)
  		await client.send_message(message.channel, msg)

  	if message.content ==('beto'):
  		msg = 'Me caga el Beto'.format(message)
  		await client.send_message(message.channel, msg)

@client.event
async def on_member_join(member):
	server = member.server
	fmt = 'Bienvenido {0.mention} a {1.name}'
	await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------------')

client.run('NDY3MTU3NzgwMzMyMjgxODc0.DimjDQ.hCWIn4KWJg0mOikcHGlqFIvJVoU')