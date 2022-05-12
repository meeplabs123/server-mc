for p in $(pgrep -f "python3|tcp")
do
    kill -9 "${p}"
done
