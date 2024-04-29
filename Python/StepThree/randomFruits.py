import random

items = ['яблуко', 'банан', 'вишня', 'диня', 'апельсин', 'полуниця']

for cycles in range(7):
    chosen_item = random.choices(items,  k=6, weights=[15, 100, 70, 50, 22, 99.39]) # weights - шанс випадіння
    print(chosen_item)  

'''
['диня', 'вишня', 'диня', 'апельсин', 'диня', 'вишня']
['диня', 'вишня', 'диня', 'диня', 'яблуко', 'вишня']
['диня', 'полуниця', 'полуниця', 'полуниця', 'полуниця', 'полуниця']
['банан', 'полуниця', 'банан', 'вишня', 'яблуко', 'яблуко']
['банан', 'яблуко', 'вишня', 'полуниця', 'яблуко', 'банан']
['полуниця', 'банан', 'банан', 'вишня', 'вишня', 'полуниця']
['банан', 'вишня', 'полуниця', 'полуниця', 'диня', 'вишня']
'''