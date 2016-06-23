# SimpleServerではCGIを実行できないがHTMLを表示させることは可能である。
# CGI機能付きServerを立てることも可能であり、このファイルではそれを実現する。(ただしディレクトリを表示してくれない)

import http.server

server_address = ("",8000)
handler_class = http.server.CGIHTTPRequestHandler
simple_server = http.server.HTTPServer(server_address,handler_class)

simple_server.serve_forever()


