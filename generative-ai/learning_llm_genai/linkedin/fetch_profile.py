from requests_oauthlib import OAuth2Session

# Your client credentials
client_id = '86vucz7yrx0krk'
# client_secret = 'your_client_secret'
client_secret = 'AQXBiLB4u_TIg79zVxtQFTQGRcQkpdiBs3R3tMGBzO3eS8j4JaBidrkhNYRSBOxFx5SJ1ZDGagBjn20vuXJ9eG6BSSSot2NH8rFyEvnkxw_vYHY1J_XUjeA4XUhC_WiyqXSJKskSMv726Zbh3dgFHx9Ervbl-fqnoRHQOBqfz7T0vyM7bHX_5DfOvAJR-Mm_NmkLyMKM2Wejn4YqJhunu09tWFzAbkBxpQAAvUtm8LUdsDrNKHeOoJD9d9t_60HXt0r4g4neVIXVmcPyO4NlZ2AQt9vyTz-jQ15JrfeLIZqD1EsbBHJgFHpASo2BFSViHaAYr7JZWTuzyZ7YJco6f8nBEXvZEw'

# LinkedIn's authorization base url
authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization'

# LinkedIn's token url
token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

# Your redirect URI (must be the same as the one set in your app settings)
redirect_uri = 'https://www.linkedin.com/company/fractionalservices/'

# Create a new OAuth2 session
linkedin = OAuth2Session(client_id, redirect_uri=redirect_uri)

# Get the authorization url and state
authorization_url, state = linkedin.authorization_url(authorization_base_url)

# Print the authorization url so the user can click on it
print('Please go here and authorize,', authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('Paste the full redirect URL here:')

# Fetch the access token
linkedin.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

# Fetch the user's specific profile information
r = linkedin.get('https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,profilePicture(displayImage~:playableStreams))')

print(r.content)