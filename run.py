from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.currency_convert(currency='GHS')
    bot.place_to_go('Pisa')