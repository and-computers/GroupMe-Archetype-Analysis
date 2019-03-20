#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Conversation():

    def __init__(self):
        self.participants = []


class Participant():

    def __init__(self):
        self.messages = []

    def add_message(message):
        self.messages += message

    def compute_total_likes():
        return sum([m.likes for m in self.message])


class Message():

    def __init__(self, text, time, sender):
        self.time = time
        self.text = text
        self.sender = sender
        self.likes = 0
