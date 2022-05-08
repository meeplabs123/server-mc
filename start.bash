bash authtoken.sh
clear
./ngrok tcp 25565 &
sleep 5
SRVIP=$(curl -s localhost:4040/api/tunnels | jq -r .tunnels[0].public_url | awk '{gsub("tcp://",""); print}')
clear
reset
python website.py "$SRVIP" &
echo "Server Ip:"
echo "$SRVIP"
echo ""
java -jar paper.jar
clear