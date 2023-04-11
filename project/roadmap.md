# ROADMAP

## VULNERABLE
 - Create routes + templates (front + back)
 	- User sign up page
	- Login page
	- General page (see list of users)
	- User page (see secret and image)
 	- Debug page (only in dev - list all contents)
 - Deployment script

## EXPLOITS
 - Create scripts and/or demonstrations
   - SQL injection on sign up
   - Some exploit on login
   - Image content exploit
   - XSS on sign up
   - Timing attacks?
   - Server access compromising?

## SECURE
 - Clone the vulnerable application and perform enhancements
	- Sanitize input
	- Disallow arbitrary JS execution on page
 	- Server security - UFW, SSH auth, etc. 

## ENTERPRISE
 - Create Firebase project
 - Create Nuxt3 SPA or Static site
	- Login and signup with Firebase auth
	- Image storage with Firebase storage
	- Add user data with Firebase firestore
 - Create deployment script
