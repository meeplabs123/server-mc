pip install discord
echo " "
echo "Downloading OpenJDK17"
wget https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.3%2B7/OpenJDK17U-jdk_x64_linux_hotspot_17.0.3_7.tar.gz
echo "Untar-gzipping openjdk17..."
tar -xf OpenJDK17U-jdk_x64_linux_hotspot_17.0.3_7.tar.gz
echo "Removing current java installation..."
sudo rm -r /home/gitpod/.sdkman/candidates/java/current
sudo mkdir /home/gitpod/.sdkman/candidates/java/current
echo "Installing new java..."
sudo mv jdk-17.0.3+7/* /home/gitpod/.sdkman/candidates/java/current/
echo "Cleaning Up..."
sudo rm -r jdk-17.0.3+7
sudo rm OpenJDK17U-jdk_x64_linux_hotspot_17.0.3_7.tar.gz
echo "Done!"