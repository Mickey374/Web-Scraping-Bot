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
        #print(len(bot.return_results()))   // Checking the total elements in the parent box for our filtered search results
        bot.return_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    
    else:
        raise

