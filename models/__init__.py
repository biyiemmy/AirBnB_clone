i#!/usr/bin/python3
'''Initializes the package'''
from .engine.file_storage import FileStorage


storage = file_storage.FileStorage()
storage.reload()
