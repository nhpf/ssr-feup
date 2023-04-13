# ROADMAP

## VULNERABLE
 - Create routes + templates (front + back)
 	- User sign up page [R]
	- Login page [R]
	- General page (see list of users) [C]
	- User page (see secret and image) [V]
 	- Debug page (only in dev - list all contents) [V]
 - Deployment script [N]

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
 - Create Firebase project [N]
 - Create Nuxt3 SPA or Static site [N]
	- Login and signup with Firebase auth [N]
	- Image storage with Firebase storage [N]
	- Add user data with Firebase firestore [N]
 - Create deployment script [N]
