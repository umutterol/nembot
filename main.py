from invasions import InvasionTimer
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from warcraftlogs.warcraftlogs.spiders import tankSpider

process = CrawlerProcess(get_project_settings())

process.crawl(tankSpider)
process.start()


invasion_timer = InvasionTimer()
next_invastion = invasion_timer.next_invasion_date()
last_invasion = invasion_timer.last_invasion_date(next_invastion)
invasion_running = invasion_timer.invasion_running(last_invasion)
invasion_durr = invasion_timer.invasion_time_left(last_invasion,invasion_running)
till_next = invasion_timer.till_next_invasion(next_invastion)

next_invasion_sarray = str(next_invastion).split("+")
next_invasion_splitted = next_invasion_sarray[0]

last_invasion_sarray = str(last_invasion).split("+")
last_invasion_splitted = last_invasion_sarray[0]

invasion_durr_sarray = str(invasion_durr).split(".")
invasion_durr_sarray = invasion_durr_sarray[0]
invasion_durr_sarray_hms = invasion_durr_sarray.split(":")
invasion_durr_msg = invasion_durr_sarray_hms[0] + " saat " + invasion_durr_sarray_hms[1] + " dakika kaldı."

till_next_sarray = str(till_next).split(".")
till_next_sarray = till_next_sarray[0]
till_next_sarray_hms = till_next_sarray.split(":")
till_next_msg = till_next_sarray_hms[0] + " saat " + till_next_sarray_hms[1] + " dakika kaldı."

print("Next Invasion: " + str(next_invasion_splitted))
print("Last Invasion: " + str(last_invasion_splitted))
print("Is invasion running: " + str(invasion_running))
print("Invasion left duration: " + str(invasion_durr_msg))
print("Duration till next: " + str(till_next_msg))

