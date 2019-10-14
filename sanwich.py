ordered_sanwiches = ['tuna','orange','beef','orange''chicken','orange','turcky','fish']
processing_sanwiches = []
finished_sanwiches = []

while ordered_sanwiches:
    current_sanwich = ordered_sanwiches.pop()
    print('I will make you a {} sanwich.'.format(current_sanwich))
    processing_sanwiches.append(current_sanwich)

print('\nSorry orange is out of inventory.\n')
while 'orange' in processing_sanwiches:
    processing_sanwiches.remove('orange')
finished_sanwiches = processing_sanwiches

for finished_sanwich in finished_sanwiches:
    print('Your {} sanwich is ready. '.format(finished_sanwich).center(10))
