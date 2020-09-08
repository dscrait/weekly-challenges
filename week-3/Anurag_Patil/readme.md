## Dependencies 

```shell
# nitrogen: https://wiki.archlinux.org/index.php/Nitrogen

# ArchLinux
sudo pacman -S nitrogen

# Debian / Ubuntu
sudo apt-get install -y nitrogen
```
## Running & Scheduling

You can schedule the script yourself or you can setup a schedular job (for ArchLinux) using systemd/Timer like so:

```shell
# Make the timer config
sudo touch /etc/systemd/system/foo.timer

# edit the file according to your need

[Unit]
Description=Change wallpaper daily

[Timer]
OnCalendar=*-*-* 13:00:00
Persistent=true
```

Or just run it like a normal python scrypt whenever you want.
```shell
python wallpaperChanger.py
```