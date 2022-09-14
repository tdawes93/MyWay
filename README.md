django was crashing when loggin in as super user or submitting forms - Forbidden (403) CSRF verification failed. Request aborted. 
This was fixed by adding CSRF_TRUSTED_ORIGINS=['https://*.8000-tdawes93-myway-i3ih4wshlts.ws-us63.gitpod.io']
The url kept changing everytime a session ended causing the bug to return. This was resolved by downgrading django to 3.2


increment/decrement quantity buttons JQuery code - Code from CI would not work as each tour has a different max quantity therefore could not use preset numbers. Solved by passing through disable buttons at min/max function with additional parameter tour.max_num_of_guests, on click of each  button. This parameter was then used as the max number in the logic. Due to this extra parameter, the current value variable was not calculated before the buttons were pressed so the min and max num logic had to be altered slightly

bootstrap toasts not showing - used BS v5, ensured all data-attributes were data-bs-attributes, still not showing. Found that the JQuery needed to  be wrapped in a function jQuery(document).ready(function($){

// jQuery code is in here

}); 

to ensure it could be used in the script tags

different tours had different locations they could choose, some can only have one others multiple. This caused issues when sending the location selector form to the view with only the last checkbox read by the post request. This was resolved by naming each checkbox with the value using django template tags, then iterating through the available choices and if there is a match adding that value into a list. This list was then passed to the context so it could be iterated and each item used in the front end. If there is only one choice, or only one location allowed the value was treated as a string. 