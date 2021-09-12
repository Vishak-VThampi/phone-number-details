#phone number details using python

#pip install phonenumbers

import phonenumbers
from phonenumbers import timezone,carrier,geocoder

mob_num= input(" Enter mobile number including country code : ")
mob_num = phonenumbers.parse(mob_num) #string to phone number

print("Mobile number: ", mob_num)
print("Timezone: ",timezone.time_zones_for_number(mob_num))
print("Carrier: ", carrier.name_for_number(mob_num,"en"))
print("Region: ",geocoder.description_for_number(mob_num,"en"))
print("Valid mobile number: ", phonenumbers.is_valid_number(mob_num))
