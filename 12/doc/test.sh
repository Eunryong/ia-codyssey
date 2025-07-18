#!/bin/bash

URL="http://127.0.0.1:80"

echo "Sending 4 simultaneous GET requests to $URL..."

# 백그라운드로 4개의 요청 실행
for i in {1..4}
do
  curl -s $URL &
done

wait  # 모든 백그라운드 작업이 끝날 때까지 대기

echo "All 4 requests completed."
