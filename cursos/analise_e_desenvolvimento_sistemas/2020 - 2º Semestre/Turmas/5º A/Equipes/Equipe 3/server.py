# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from views import *


app.add_url_rule('/signin', view_func=Signin.as_view('signin'))
app.add_url_rule('/signup', view_func=Signup.as_view('signup'))
app.add_url_rule('/account', view_func=AccountView.as_view('account'))
app.add_url_rule('/account/signout', view_func=Signout.as_view('signout'))
app.add_url_rule('/account/delete', view_func=AccountDelete.as_view('account-delete'))
app.add_url_rule('/data-report', view_func=CustomerDataReport.as_view('data-report'))