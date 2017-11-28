from crontab import
CronTab my_cron = CronTab(user='root')
job = my_cron.new(command='python /*path*/LINE/Bagasbot.py')
job.minute.every(1)
my_cron.write()
