import nextcord,json,os
from nextcord.ext import commands
from core.classes import Cog_Extension
from core.card import Game

class Card(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    game = Game()
              
    @commands.command()
    async def battle(self, ctx, member: nextcord.Member):
        channel = await member.create_dm()
        author_channel = await ctx.author.create_dm()
        await channel.send(f"{member.mention}, 你被 {ctx.author.mention} 邀请参加七胜召唤！")
        await author_channel.send(f"{ctx.author.mention}, 你邀请 {member.mention} 参加七圣召唤！请前往私信与对方联系。")
        
        await channel.send("是否接受邀请？请输入 `yes` 或 `no`。")
        
        def check(m):
            return m.author == member and m.channel == channel
        
        try:
            msg = await self.bot.wait_for('message', timeout=60.0, check=check)
        except nextcord.TimeoutError:
            await ctx.send(f"{member.mention} 没有在规定时间内回复。")
            return
        
        if msg.content.lower() == 'no':
            await ctx.send(f"{member.mention} 拒绝了邀请，命令已取消。")
            return
        elif msg.content.lower() != 'yes':
            await ctx.send(f"{member.mention} 回复了无效的消息，命令已取消。")
            return
        
        category = ctx.guild.get_channel(988774327002480740)
        if category is None:
            await ctx.send("找不到指定的分类频道。")
            return
            
        overwrites = {
            ctx.guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: nextcord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        overwrites[member] = nextcord.PermissionOverwrite(read_messages=True, send_messages=True)
        overwrites[ctx.author] = nextcord.PermissionOverwrite(read_messages=True, send_messages=True)
            
        channel = await category.create_text_channel(f'{ctx.author.display_name}-{member.display_name}', overwrites=overwrites)
        await ctx.send(f"私人频道创建成功：{channel.mention}")
        
        message = f"欢迎来到七圣召唤私人频道 如果你还没选着你的卡组着无法开始对战噢\n如果要选者你的卡组请前往选着"
        await channel.send(message)
        
    @commands.command()
    async def show_cards(self, ctx):
        # Load JSON file with card data
        with open('utilis/cards.json', 'r',encoding='utf8') as file:
            cards = json.load(file)

        # Display available cards to the user
        response = "选择三张角色卡\n"
        for i, card in enumerate(cards, 1):
            response += f"{i}. {card['name']} - {card['description']}\n"

        await ctx.send(response)

    @commands.command()
    async def choose_character_cards(self, ctx, *card_numbers: str):
        if len(card_numbers) != 3:
            await ctx.send("只可以选择三张噢")
            return

        # Load JSON file with card data
        with open('utilis/cards.json', 'r', encoding='utf8') as file:
            cards = json.load(file)

        # Check if the chosen card numbers are valid
        for card_number in card_numbers:
            if not any(card["name"] == card_number for card in cards):
                await ctx.send("错误号码，请选择正确的号码")
                return

        # Get the chosen cards as main characters
        main_characters = [card for card in cards if card["name"] in card_numbers]

        # Save the chosen cards to a new JSON file
        await self.save_chosen_cards(ctx.author.id, main_characters)

        # Display the main characters to the user
        response = "你的新角色卡已更新:\n"
        for i, card in enumerate(main_characters, 1):
            response += f"{i}. {card['name']} - {card['description']}\n"

        await ctx.send(response)

    async def save_chosen_cards(self, user_id, main_characters):
        chosen_cards = {}

        # Load the chosen cards if the file exists
        if os.path.exists('utilis/chosen_cards.json'):
            with open('utilis/chosen_cards.json', 'r', encoding='utf8') as file:
                try:
                    chosen_cards = json.load(file)
                except json.JSONDecodeError:
                    chosen_cards = {}
                    
        chosen_cards[str(user_id)] = main_characters
        with open('utilis/chosen_cards.json', 'w', encoding='utf8') as file:
            json.dump(chosen_cards, file, ensure_ascii=False, indent=4)
            
    @commands.command()
    async def my_cards(self, ctx):
        user_id = str(ctx.author.id)

        # Load the chosen cards if the file exists
        if os.path.exists('utilis/chosen_cards.json'):
            with open('utilis/chosen_cards.json', 'r', encoding='utf8') as file:
                try:
                    chosen_cards = json.load(file)
                except json.JSONDecodeError:
                    chosen_cards = {}

            # Check if the user has chosen cards
            if user_id not in chosen_cards:
                await ctx.send("你还没有选择角色卡。")
                return

            # Display the chosen cards for the user
            main_characters = chosen_cards[user_id]
            response = "以下是你的角色卡:\n"
            for i, card in enumerate(main_characters, 1):
                response += f"{i}. {card['name']} - {card['description']}\n"

            await ctx.send(response)
        else:
            await ctx.send("你还没有选择角色卡。")
                        
def setup(bot):
        bot.add_cog(Card(bot))