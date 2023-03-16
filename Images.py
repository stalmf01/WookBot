import pickle
from datetime import datetime, timezone
import os
import discord


class Image:
    def __init__(self, url=''):
        self.url = url
        self.timestamp = datetime.now(tz=timezone.utc).timestamp()

    def __repr__(self):
        return f'{self.url} {self.timestamp}'

    def __eq__(self, other):
        return self.url == other.url and self.timestamp == other.timestamp


class ImageList:
    def __init__(self, list_count):
        self.list_count = list_count
        if os.path.exists('image_sources/imagelist.pkl'):
            # load image list
            with open('image_sources/imagelist.pkl', 'rb') as f:
                self.image_list = pickle.load(f)
        else:
            self.image_list = []

    def __repr__(self):
        return f'{len(self.image_list)} {self.image_list}'

    def save(self):
        with open('image_sources/imagelist.pkl', 'wb') as f:
            pickle.dump(self.image_list, f, pickle.HIGHEST_PROTOCOL)

    def find_oldest_image(self):
        oldest_image = self.image_list[0]
        oldest_image_index = 0
        for index, current_image in enumerate(self.image_list):
            if oldest_image.timestamp > current_image.timestamp:
                oldest_image = current_image
                oldest_image_index = index

        return oldest_image_index

    def item_in_list(self, url):
        for item in self.image_list:
            if url == item.url:
                return True
        return False

    def add(self, url):
        # need to see if item is in list before adding item
        if self.item_in_list(url):
            return False
        self.image_list.append(Image(url))
        if len(self.image_list) > self.list_count:
            # remove oldest item from list
            print(f'removing {self.image_list[self.find_oldest_image()]}')
            self.image_list.remove(self.image_list[self.find_oldest_image()])
        self.save()
        return True

    def __len__(self):
        return len(self.image_list)
