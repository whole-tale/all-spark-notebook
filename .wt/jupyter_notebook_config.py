import os
csp = os.environ.get(
    'CSP_HOSTS', 'https://dashboard.dev.wholetale.org http://localhost:4200'
)
c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors {} 'self' ".format(csp.replace('"', ''))
    }
}
