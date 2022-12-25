while true; do
  date=$(date)
  notify-send "$date" -h string:x-canonical-private-synchronous:my-notification
  sleep 1
done