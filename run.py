from time import sleep
from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    print('Girdim')
    sleep(5)
    print('bekledim')
    bot.search_review("A structured methodical process for populating a crime script of organized crime activity using OSINT")
    print('yazdim')
    bot.search_click()
    
    print('Exiting...')
    sleep(10000)


