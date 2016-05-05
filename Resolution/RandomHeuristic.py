# Create Parking
# we subdivise the demand in timeframes
#   For each one we read in order of arrival the request ( arrival and departure)
#       if it's an arrival, we try to find a place
#           if no spot is found, we execute a routine to free a spot

#       if it's a departure, then we take the car out of her spot.
#           if it'snot possible we execute a routine to alow it.
