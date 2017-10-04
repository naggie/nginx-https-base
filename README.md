nginx-https-base is an nginx role for andible with the following features:

1. Automatic zero-downtime Let's Encrypt support for automatic transparent
   HTTPS
2. Secure HTTPS related configuration (also redirects from HTTP)
3. Canonical reverse-proxy configuration
4. Canonical uwsgi configuration
5. Canonical static hosting configuration
6. Canonical redirect configuration
7. Auto-reloading maintenance page for reverse-proxy/uwsgi configurations
8. Better (minimal) error pages


Example usages, using `include_role` for sane variable scoping:

```
- name: Configure nginx
  include_role:
    name: nginx-https-base
  vars:
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
