import sys, urllib, SocketServer
# coding: utf-8

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
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
    #
    print self.client_address[0]
    print ("Got a request of: %s\n" % self.data)

    parts = self.data.split(' ')
    print parts[0]
    print parts[1]
    print parts[2]

    if ('/' in parts[1]):
      #if (parts[1].length == 1):

      print "Found"
    else:
      error(request, "Not found" + parts[1])


    # f = open('base.css', 'r')
    # for line in f:
    #   self.request.sendall(line)
    # f.close()
    self.request.sendall("Test\n")
    #self.request.sendall("OK")

  #def parse (self, request)

  def error(self, request, msg):
    print "Bad request ", msg


if __name__ == "__main__":
  HOST, PORT = "localhost", 8080

  SocketServer.TCPServer.allow_reuse_address = True
  # Create the server, binding to localhost on port 9999
  server = SocketServer.TCPServer((HOST, PORT), MyWebServer)

  # Activate the server; this will keep running until you
  # interrupt the program with Ctrl-C
  server.serve_forever()
