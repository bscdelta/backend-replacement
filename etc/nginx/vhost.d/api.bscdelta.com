location ~ ^/socket.io {
    limit_req zone=socketlimit burst=12 nodelay;
    limit_conn socketperip 9;
    proxy_pass https://api.bscdelta.com;
}

location ~ ^/returnTicker {
     limit_req zone=restlimit burst=3 nodelay;
     proxy_pass https://api.bscdelta.com;
}
