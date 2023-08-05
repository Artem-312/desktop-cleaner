# desktop-cleaner
This program tidies up your workspace. It sorts all of your files on your desktop and then puts them in specific folders every once in a while :)

You can also use Crontab instead of Scheduler to automate this program. You would have to comment out lines 60 to 75 and add a function call like below:
```
sort_files_by_extension(source_directory, destination_folders)
```
After that, go to your terminal and do the following:
1. Type "crontab -e" to open Crontab's special menu
2. Go to [Crontab's website](crontab.guru) to make your cron expression (for example, if I want it to run once in 6 hours, the expression would be 0 */6 * * *)
3. Paste your expression to the terminal
4. Press I to open Insert menu and paste the path to your .py file with the program after your cron expression
5. Press esc button to quit Insert menu
6. Press : button and type 'wq' below (write and quit)

That's it. Thanks for reading :)
