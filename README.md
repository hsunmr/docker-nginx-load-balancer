### Nginx Load Balancer
| use three flask application to demo nginx load balancer

#### Usage

`docker-compose up -d`

#### Methods


- Round Robin 輪流 (default)

    ```
    upstream flask_app {
        server flask-app1:8000;
        server flask-app2:8000;
        server flask-app3:8000;
    }
    ```

- [Least Connections](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#least_conn) 最少連接數

    ```
    upstream flask_app {
        least_conn;
        server flask-app1:8000;
        server flask-app2:8000;
        server flask-app3:8000;
    }
    ```


- [IP Hash](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#ip_hash)

    ```
    upstream flask_app {
        ip_hash;
        server flask-app1:8000;
        server flask-app2:8000;
        server flask-app3:8000;
    }
    ```

- Generic [Hash](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#hash)

    ```
    upstream flask_app {
        hash $request_uri consistent;
        server flask-app1:8000;
        server flask-app2:8000;
        server flask-app3:8000;
    }
    ```

- Weight 權重

    ```
    upstream flask_app {
        server flask-app1:8000 weight=10;
        server flask-app2:8000 weight=5;
        server flask-app3:8000 weight=1;
    }
    ```

- Backup

    ```
    upstream flask_app {
        server flask-app1:8000;
        server flask-app2:8000;
        server flask-app3:8000 backup;
    }
    ```

- Fair
    ```
    upstream flask_app {
        fair
        server flask-app1:8000;
        server flask-app2:8000;
        server flask-app3:8000;
    }
    ```