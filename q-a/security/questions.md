# Security questions

| #   | Question                                                                                                                                                                        |
| :-- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | In what way computer security differs from everyday life security?                                                                                                              |
| 2   | Why salting helps making hashed password more secure?                                                                                                                           |
| 3   | If you have https web service url in web.config, why is it important to check ssl certificate validity?                                                                         |
| 4   | If all systems lock user after a few invalid login attempts, how can hackers brute force the password and why do passwords need to be strong?                                   |
| 5   | If ssl is needed in production app, what two places the certificate may be installed?                                                                                           |
| 6   | If private key is used, why certificate should be put in Personal store (not Trusted People)?                                                                                   |
| 7   | Cookies - http only flag - why the value of this property is questionable?                                                                                                      |
| 8   | If you try to make ajax request to other domain, will it work?                                                                                                                  |
| 9   | What is the key to avoid sql injection?                                                                                                                                         |
| 10  | What is the key against cross side scripting?                                                                                                                                   |
| 11  | Where permission checks should be?                                                                                                                                              |
| 12  | What two things should logoff button do?                                                                                                                                        |
| 13  | If browser has old session id coockie, but asp.net starts new session, will session id be different?                                                                            |
| 14  | What requests should be blocked, if they are under unsecure http protocol?                                                                                                      |
| 15  | If login page catches unsecure http request and redirects to https without doing anything else, what security hole do we have?                                                  |
| 16  | How can you tell asp.net web app to run like specific user (not default iusr account)?                                                                                          |
| 17  | If you perform js get to other domain and include picture with src in other domain - both times coockie info will not be sent. But what will be different about those requests? |
| 18  | What will js interaction between frame objects will be, if frames are in different domains?                                                                                     |
| 19  | If http form loaded in domain A is posted to domain B, will coockies (associated with domain B) be sent?                                                                        |
| 20  | If application uses certificate to sign and to verify, what is the main difference of storing in file and in windows certificate storage?                                       |
| 21  | By convention, where should certificates for signing reside in certificate storage?                                                                                             |
| 22  | By convention, where should certificates for verifying reside in certificate storage?                                                                                           |
| 23  | What is the difference of certificates, that can be used for signing and for verifying?                                                                                         |
| 24  | If my app does signing and verifying itself, is it important where certificate is put, or is it just convention?                                                                |
| 25  | .Net tool Makecert.exe for certificate generation - what is the main thing to do, so that certificate with private key would be generated?                                      |
| 26  | If browser loaded page in http and cached script, and then we get the same page in https - what the browser will do with the script?                                            |
| 27  | Scenario - login form in http page posts to https. Will it work at all?                                                                                                         |
| 28  | Scenario - login form in http page posts to https. Will credentials will be passed in encrypted format?                                                                         |
| 29  | Scenario - login form in http page posts to https. Is it safe?                                                                                                                  |
| 30  | Can javascript get value of input (type=password)?                                                                                                                              |
| 31  | Asp.Net authentication - what same action three authentication types (win, forms, custom) do to request context?                                                                |
| 32  | Asp.Net authentication - windows - how thread current user is set?                                                                                                              |
| 33  | Asp.Net authentication - forms - how thread current user is set?                                                                                                                |
| 34  | Asp.Net authentication - custom - how thread current user is set?                                                                                                               |
| 35  | To install SSL certificate on IIS (lets say using makecert) - are default options for primary key enough?                                                                       |
| 36  | Certificate thumbprint - will it be the same when exported and installed on different computer?                                                                                 |
| 37  | What two params must match when using forms auth?                                                                                                                               |
| 38  | What security risk do you have, if you let user upload files and do unzipping on the server.                                                                                    |
| 39  | When web app calls some exe file, how to correcttly set up needed user for running?                                                                                             |
| 40  | Is only <script tags dangerous for cross site scripting?                                                                                                                        |
