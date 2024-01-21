
async def tache_toutes_les_5_minutes():

async def tache_quotidienne_8h():

async def planificateur():
    aioschedule.every(1).minutes.do(tache_toutes_les_5_minutes)
    aioschedule.every().day.at("21:44").do(tache_quotidienne_8h)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1) 

if __name__ == "__main__":
    asyncio.run(planificateur())
