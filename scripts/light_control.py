def main(cont):
    own = cont.owner
    sun = own.children["sun"]
    moon = own.children["moon"]
    sun_sky = sun.children["sun_sky"]
    moon_sky = moon.children["moon_sky"]
    delay = cont.sensors["Delay"]
    hour = own["hour"]
    minute = own["minute"]
    daytime = own["daytime"]

    if delay.positive:
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0
    daytime = 6 <= hour < 18
    if daytime:
        moon.energy = 0.0
        sun.energy = 1.0
        moon_sky.energy = 0.0
        sun_sky.energy = 1.0
    else:
        moon.energy = 0.05
        sun.energy = 0.0
        moon_sky.energy = 0.05
        sun_sky.energy = 0.0

    own["hour"] = hour
    own["minute"] = minute
    own["daytime"] = daytime
