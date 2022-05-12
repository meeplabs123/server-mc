bash refresh.sh

bash init.sh
bash authtoken.sh
clear
./ngrok tcp 25565 &
sleep 5
SRVIP=$(curl -s localhost:4040/api/tunnels | jq -r .tunnels[0].public_url | awk '{gsub("tcp://",""); print}')
clear
reset
python3 website.py "$SRVIP" &
echo "Server Ip:"
echo "$SRVIP"
echo ""
java -jar paper-1.18.2-333.jar
clear

bash refresh.sh
