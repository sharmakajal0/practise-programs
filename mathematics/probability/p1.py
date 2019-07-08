#!/usr/bin/env python

''' module for probability'''
from sys import argv

def probability(event, events):

  '''Function Definition for finding probability in a list of events'''
  event_count = 0

  for i in events:
    if i == event:
      event_count += 1

  return event_count / len(events)

def main(args):
  events = [1, 2, 3, 4, 5, 4, 2, 2, 4, 56, 6, 3, 2, 12, 3, 4, 5]
  event = int(args[1])
  print(probability(event, events))

if __name__ == "__main__":
  main(argv)
