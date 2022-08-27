django admin was crashing when loggin in as super user - Forbidden (403) CSRF verification failed. Request aborted. 
This was fixed by adding CSRF_TRUSTED_ORIGINS=['https://*.8000-tdawes93-myway-i3ih4wshlts.ws-us63.gitpod.io']

