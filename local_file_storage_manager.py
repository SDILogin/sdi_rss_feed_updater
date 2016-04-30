import os

directory = os.path.dirname(os.path.abspath(__file__)) + "/data/"
file_name_format = directory + "%s"


def add_rss_feed_to_channel(channel_name, rss_title, rss_feed):
    file_path = file_name_format % (channel_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    f = open(file_path, 'a')
    f.write(rss_title + " " + rss_feed + "\n")
    f.close()


def get_channels():
    return os.listdir(directory)


def read_feeds_from_file(channel_name):
    result = []
    with open(file_name_format % (channel_name), 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(" ")
            result.append({'title': ' '.join(parts[:-1]), 'url': parts[-1]})
    return result


def get_enumerated_list_feed(channel_name):
    with open(file_name_format % (channel_name), 'r') as file:
        return ["%d) %s" % (ind, val) for ind, val in enumerate(file.readlines())]


def remove_rss_feed_from_channel(channel_name, index):
    file_path = file_name_format % (channel_name)
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()

    with open(file_path, 'w') as file:
        file.writelines(lines[:index] + lines[index+1:])
