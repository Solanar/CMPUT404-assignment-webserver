import os, sys, urllib, SocketServer
# coding: utf-8

# Copyright 2013 Abram Hindle, Eddie Antonio Santos, Andrew Charles
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/

class MyWebServer(SocketServer.BaseRequestHandler):

  def handle(self):
    self.data = self.request.recv(1024).strip()

    parts = self.data.split()
    url = parts[1]

    self.header = ""
    self.body = ""

    if url == '/':
      self.getFile("/index.html")
    else:
      if (url[0] == '/' and (len(url) > 1)):
        if (url[-1] == '/'):
          self.getFile(url + "index.html")
        else:
          self.getFile(url)

    self.request.sendall(self.header + "\n")
    self.request.sendall(self.body)


  def filetype(self, ext):
    if ext == ".css":
      return "Content-Type: text/css"
    elif ext == ".html":
      return "Content-Type: text/html"
    else:
      raise IOError


  def getFile(self, url):
    root = os.getcwd() + "/www"
    relfilename = root + url
    absfilename = os.path.normpath(relfilename)
    try:
      if not absfilename.startswith(root):
        raise IOError
      f = open(absfilename, "r")
      mimetype = self.filetype(os.path.splitext(absfilename)[1])
      self.header += "HTTP/1.1 200\n"
      self.header += mimetype + "\n"
      self.body += f.read()
      f.close()
    except IOError:
      self.header += "HTTP/1.1 404\n"
      self.body += "Page not found\n"


  def error(self):
    print "Bad request "


if __name__ == "__main__":
  HOST, PORT = "localhost", 8080

  SocketServer.TCPServer.allow_reuse_address = True
  # Create the server, binding to localhost on port 9999
  server = SocketServer.TCPServer((HOST, PORT), MyWebServer)

  # Activate the server; this will keep running until you
  # interrupt the program with Ctrl-C
  server.serve_forever()
