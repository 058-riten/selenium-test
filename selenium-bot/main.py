from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.select_place_to_go('Pokhara')
    bot.select_dates(check_in_date='2024-05-18', check_out_date='2024-05-25')
    bot.click_search()