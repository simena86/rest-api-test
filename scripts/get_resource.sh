
curl -u simena86:Seigmann1 -i -X GET http://127.0.0.1:5000/api/resource

curl -X GET http://127.0.0.1:5000/api/users/1

echo ""
echo "with token: "

curl -u simena86:Seigmann1  \
  -i -X GET http://127.0.0.1:5000/api/resource
