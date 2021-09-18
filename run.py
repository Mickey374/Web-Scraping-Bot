from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.currency_convert(currency='GHS')
        bot.place_to_go('Pisa')
        bot.select_dates(check_in_date='2021-09-16', check_out_date='2021-09-30')
        bot.choose_adults(10)
        bot.click_search()
        bot.apply_filterations()

except Exception as e:
    if 'in PATH' in str(e):
        print("There is a problem with the Driver PATH")
    
    else:
        raise

