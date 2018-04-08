nginx-https-base is an nginx role for andible with the following features:

1. Automatic zero-downtime Let's Encrypt support for automatic transparent
   HTTPS
2. Secure HTTPS related configuration (also redirects from HTTP)
3. Canonical reverse-proxy configuration
4. Canonical uwsgi configuration
5. Canonical static hosting configuration
6. Canonical redirect configuration
7. Auto-reloading maintenance page for reverse-proxy/uwsgi configurations
8. Clean and minimal error pages. They can be customised with a logo using
   `epgen/epgen.py`.


Example usages, using `include_role` for sane variable scoping:

```
- name: Configure nginx
  include_role:
    name: nginx-https-base
  vars:
    admin_email: admin@example.com
    sites:
      - domain: example.com
        template: proxy.conf
        target: http://127.0.0.1:8001

      - domain: www.example.com
        template: domain-redirect.conf
        redirect_to: example.com
```

Use the `location_extra` variable to add more configuration such as static
assets and IP blocking:

```
        location_extra: |
            allow 127.0.0.1;
            deny all;

            location /assets/ {
                alias /var/www/example/;
            }
```


Look at the similarly named template files for `uwsgi` and `static`
configurations.


To install this role, add the following lines to `requirements.yml`:

```
- src: https://github.com/naggie/nginx-https-base
  version: master

```

...and then run `ansible-galaxy install -r requirements.yml`

### Auto reloading maintenance page

Upon a 502 error when running as a reverse proxy or uwsgi gateway,
nginx-https-base is configured to serve a automatically-reloading page to
resume a user's session without losing data.

![autoreload](https://github.com/naggie/nginx-https-base/raw/master/autoreload.gif)

Failed GET and POST requests will be re-attempted. Sometimes this is not what
you want if you are dealing with large POST requests, for example; in which
case, please edit the error page or handler.

