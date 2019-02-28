#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import discord
import re
import time
import tabulate
from wow import *
from util import *
from settings import *
from invasions import InvasionTimer
from spiderQueen import SpiderQueen

client = discord.Client()

@client.event
async def on_message(message):
    """Listens for specific user messages."""
    # Current time (Used for cache busting character thumbnails).
    epoch_time = int(time.time())

    # If the author is the bot do nothing.
    if message.author == client.user:
        return

    if message.content.startswith('!exen token'):
        split = split_query(message.content, 'wow_token')
        region = split[0]
        info = await wow_token_price(region)

        # Returns a message to the channel if there's an error fetching.
        if info == 'not_found':
            msg = GOLD_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'connection_error':
            msg = CONNECTION_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'credential_error':
            msg = CREDENTIAL_ERROR.format(message)
            await client.send_message(message.channel, msg)

        else:
            msg = '`WoW Tokenın %s realmlerindeki fiyatı şuan %s gold.` :moneybag:' % (region, info)
            await client.send_message(message.channel, msg)

    if message.content.startswith('!exen inv'):
        invasion_timer = InvasionTimer()
        next_invasion = invasion_timer.next_invasion_date()
        last_invasion = invasion_timer.last_invasion_date(next_invasion)
        invasion_running = invasion_timer.invasion_running(last_invasion)
        invasion_durration = invasion_timer.invasion_time_left(last_invasion,invasion_running)
        invasion_until_next = invasion_timer.till_next_invasion(next_invasion)

        next_invasion_sarray = str(next_invasion).split("+")
        next_invasion_splitted = next_invasion_sarray[0]

        
        if(invasion_running):
            invasion_durr_sarray = str(invasion_durration).split(".")
            invasion_durr_sarray = invasion_durr_sarray[0]
            invasion_durr_sarray_hms = invasion_durr_sarray.split(":")
            invasion_durr_msg = invasion_durr_sarray_hms[0] + " saat " + invasion_durr_sarray_hms[1] + " dakika kaldı."

            msg = discord.Embed(title= "Invasion Şuan Aktif!", description="Koş koş lootunu al marklarını al. FOR THE ALLIANCE?!?!", color=0xe62020)
            msg.set_thumbnail(url="https://findicons.com/files/icons/1181/flurry_extras_2/128/alliance.png")
            msg.add_field(name="Invasionun bitmesine kalan süre", value=invasion_durr_msg, inline=False)
            msg.add_field(name="Bir sonraki invasion zamanı", value=next_invasion_splitted, inline=False)
        else:
            till_next_sarray = str(invasion_until_next).split(".")
            till_next_sarray = till_next_sarray[0]
            till_next_sarray_hms = till_next_sarray.split(":")
            till_next_msg = till_next_sarray_hms[0] + " saat " + till_next_sarray_hms[1] + " dakika kaldı."
    
            
            msg = discord.Embed(title="Invasion Şuanda Aktif Değil", description="Bir sonraki Invasion zamanı aşağıdaki gibidir.", color=0xe62020)
            msg.set_thumbnail(url="https://findicons.com/files/icons/1181/flurry_extras_2/128/alliance.png")
            msg.add_field(name="Bir sonraki invasiona kalan süre", value=till_next_msg, inline=True)
            msg.add_field(name="Bir sonraki invasion başlangıc zamanı", value=next_invasion_splitted, inline=False)

        await client.send_message((message.channel),embed=msg)

    if message.content.startswith('!exen rank dps'):
        sq = SpiderQueen()
        dps = sq.DPSSpiderCrawl()
        await client.send_message((message.channel),':crossed_swords:` DPS Parse Listesi ` :crossed_swords:' )
        #msg = discord.Embed(title = "DPS RANKINGLERI", description= tabulate.tabulate(dps,headers= "keys",tablefmt="simple"))
        for chunk in dps:
            await client.send_message((message.channel),"\n```\n" + tabulate.tabulate(chunk, headers="keys", tablefmt="simple") + "\n```")
    
    if message.content.startswith('!exen rank tank'):
        sq = SpiderQueen()
        tank = sq.TankSpiderCrawl()
        await client.send_message((message.channel),':shield: ` Tank Parse Listesi ` :shield: ' )
        #msg = discord.Embed(title = "DPS RANKINGLERI", description= tabulate.tabulate(dps,headers= "keys",tablefmt="simple"))
        for chunk in tank:
            await client.send_message((message.channel),"\n```\n" + tabulate.tabulate(chunk, headers="keys", tablefmt="simple") + "\n```")
    
    if message.content.startswith('!exen rank heal'):
        sq = SpiderQueen()
        heal = sq.HealSpiderCrawl()
        await client.send_message((message.channel),':syringe: ` Heal Parse Listesi ` :syringe: ' )
        #msg = discord.Embed(title = "DPS RANKINGLERI", description= tabulate.tabulate(dps,headers= "keys",tablefmt="simple"))
        for chunk in heal:
            await client.send_message((message.channel),"\n```\n" + tabulate.tabulate(chunk, headers="keys", tablefmt="simple") + "\n```")


    if message.content.startswith('!exen pve'):
        split = split_query(message.content, 'pve')

        # Assigns the 3rd index in the split to the region
        region = split[3]

        # Sends the returned data to the character_info function to build a character sheet.
        info = await character_info(split[0], split[1], split[2], region)

        # Returns a message to the channel if there's an error fetching.
        if info == 'not_found':
            msg = NOT_FOUND_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'connection_error':
            msg = CONNECTION_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'credential_error':
            msg = CREDENTIAL_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'unknown_error':
            msg = UNKNOWN_ERROR.format(message)
            await client.send_message(message.channel, msg)

        else:
            # Format the AOTC/CE strings if they exist.
            ud_feat = ''
            bod_feat = ''

            if info['ud_feat'] != '':
                ud_feat = '**`%s`**' % (info['ud_feat'])

            if info['bod_feat'] != '':
                bod_feat = '**`%s`**' % (info['bod_feat'])

            msg = discord.Embed(
                title='%s' % (info['name']),
                colour=discord.Colour(info['class_colour']),
                url='%s' % (info['armory']),
                description='%s %s %s %s' % (
                    info['level'], info['faction'], info['spec'], info['class_type']))
            msg.set_thumbnail(
                url='https://render-%s.worldofwarcraft.com/character/%s?_%s' % (
                    region, info['thumb'], epoch_time))
            msg.set_footer(
                text='!exen yardım | Feedback: https://github.com/umutterol/nembot/issues',
                icon_url='https://raw.githubusercontent.com/JamesIves/discord-wow-armory-bot/master/assets/icon.png')
            msg.add_field(
                name='Character',
                value='**`Name`:** `%s`\n**`Realm`:** `%s (%s)`\n**`Item Level`:** `%s`' % (
                    info['name'], info['realm'], region.upper(), info['ilvl']),
                inline=True)
            msg.add_field(
                name='Keystone Achievements (Season 2)',
                value='**`Conqueror (+10)`: ** `%s`\n**`Master (+15)`: ** `%s` \n' % (
                    info['keystone_season_conqueror'], info['keystone_season_master']),
                inline=True)
            msg.add_field(
                name='Uldir',
                value='**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s' % (
                    info['uldir']['normal'], info['uldir']['bosses'],
                    info['uldir']['heroic'], info['uldir']['bosses'],
                    info['uldir']['mythic'], info['uldir']['bosses'],
                    ud_feat),
                inline=True)
            msg.add_field(
                name="Battle of Dazar'alor",
                value='**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s' % (
                    info['battle_of_dazaralor']['normal'], info['battle_of_dazaralor']['bosses'],
                    info['battle_of_dazaralor']['heroic'], info['battle_of_dazaralor']['bosses'],
                    info['battle_of_dazaralor']['mythic'], info['battle_of_dazaralor']['bosses'],
                    bod_feat),
                inline=True)

            await client.send_message(message.channel, embed=msg)

    # Display a list of available commands and a set of credits.
    if message.content.startswith('!exen yardım'):
        msg = """Şu komutlar kullanılabilir:
            ```
            # PVE Progressi, dungeon killeri, mythic+ achivleri için.
            !exen pve <name> <realm>
            !exen pve <armory-link>

            # WoW Token Fiyatları için
            !exen token

            #WARCRAFTLOGS Ranking tabloları için.
            !exen rank dps
            !exen rank tank
            !exen rank heal

            #Battle for Azeroth Invasion zamanlayıcıları.
            !exen inv

            ```
            """

        msg = '%s'.format(message) % re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', msg, flags=re.M)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    if WOW_CLIENT_ID is None or WOW_CLIENT_ID == '' or WOW_CLIENT_SECRET is None or WOW_CLIENT_SECRET == '':
        print('Missing World of Warcraft Client ID/Secret. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')
        quit()

    if WOW_REGION is None or WOW_REGION == '':
        print('Missing World of Warcraft player region. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')
        quit()

    if LOCALE is None or LOCALE == '':
        print('Missing locale. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')
        quit()

    else:
        print('Launch Succesful! The bot is now listening for commands...')


if DISCORD_BOT_TOKEN is None or DISCORD_BOT_TOKEN == '':
    print('Missing Discord bot token. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')
    quit()

else:
    client.run(DISCORD_BOT_TOKEN)
