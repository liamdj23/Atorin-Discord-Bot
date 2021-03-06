import math


def bool_to_state(value: bool):
    if value:
        return "✅ Włączone"
    else:
        return "❌ Wyłączone"


def state_to_bool(value: str):
    if value.lower() == "on":
        return True
    elif value.lower() == "off":
        return False
    else:
        return None


def get_weather_emoji(weather_id):
    thunderstorm = u"\U0001F4A8"  # Code: 200's, 900, 901, 902, 905
    drizzle = u"\U0001F4A7"  # Code: 300's
    rain = u"\U00002614"  # Code: 500's
    snowflake = u"\U00002744"  # Code: 600's snowflake
    snowman = u"\U000026C4"  # Code: 600's snowman, 903, 906
    atmosphere = u"\U0001F301"  # Code: 700's foogy
    clear_sky = u"\U00002600"  # Code: 800 clear sky
    few_clouds = u"\U000026C5"  # Code: 801 sun behind clouds
    clouds = u"\U00002601"  # Code: 802-803-804 clouds general
    hot = u"\U0001F525"  # Code: 904
    default = u"\U0001F300"  # default emojis

    weather_id_str = str(weather_id)

    if weather_id_str[:1] == "2" or weather_id == 900 or weather_id == 901 or weather_id == 902 or weather_id == 905:
        return thunderstorm
    elif weather_id_str[:1] == "3":
        return drizzle
    elif weather_id_str[:1] == "5":
        return rain
    elif weather_id_str[:1] == "6" or weather_id == 903 or weather_id == 906:
        return snowflake + " " + snowman
    elif weather_id_str[:1] == "7":
        return atmosphere
    elif weather_id == 800:
        return clear_sky
    elif weather_id == 801:
        return few_clouds
    elif weather_id == 802 or weather_id == 803 or weather_id == 804:
        return clouds
    elif weather_id == 904:
        return hot
    else:
        return default


def progress_bar(percent, text):
    j = percent / 100
    return f"[{'|' * int(10 * j):{10}s}] {int(100 * j)}%  {text}"


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p)
    return "%s %s" % (s, size_name[i])
