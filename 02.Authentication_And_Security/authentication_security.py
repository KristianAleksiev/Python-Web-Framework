"""
1. The identity in the Web
- Identification (unique username), authentication (Who is the user) and authorization (What can the user do)

2. Authentication
- Provided credentials by the user are compared to those in a database of authorized users
- If the credentials match, the user is granted access
- ID and PW are the most basic type of auth
- Single-factor authentication
- Multi-factor authentication (possession factor)
-
-
3. Authentication in Django
- It handles both authentication and authorization
- It handles cookie-based user sessions
- Users, groups and permissions
- Cookie-based authentication - csrf token, session id (request.user)

Django User:
- Core of the authentication system
- User model - Inherits AbstractUser
- User attrs -> is_authenticated, is_anonymous

4. Permissions and Authorization
- User permissions / Group permissions
- Permission control -> Built-in decorators
- @login_required(login_url="/login" -> For function based views
- class IndexView(LoginRequiredMixin, views.View) -> class based views
- custom decorators for validation -> decorators.py in app

5. Security
- SQL injection - SQL search always True condition, manipulating the queries
- Cross Site Scripting - Injected code into the database, which is visualized on the site (forms), Direct into DOM tree
- Cross Site Request Forgery - Phishing - Attack over HTTP protocol, redirect, collect user credentials (CSRF TOKEN)
- Parameter tampering - Altered query strings in the url, cookies
- Brute Force Attacks (DDoS) - Denial of service


"""