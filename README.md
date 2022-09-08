django admin was crashing when loggin in as super user - Forbidden (403) CSRF verification failed. Request aborted. 
This was fixed by adding CSRF_TRUSTED_ORIGINS=['https://*.8000-tdawes93-myway-i3ih4wshlts.ws-us63.gitpod.io']


increment/decrement quantity buttons JQuery code - Code from CI would not work as each tour has a different max quantity therefore could not use preset numbers. Solved by passing through disable buttons at min/max function with additional parameter tour.max_num_of_guests, on click of each  button. This parameter was then used as the max number in the logic. Due to this extra parameter, the current value variable was not calculated before the buttons were pressed so the min and max num logic had to be altered slightly