# 불량 판정

```
  post /v1/decision
  Content-type : application/json

```


- Request

변수명| 타입  |required|설명
  ---|-----|---|---|
image_path|String|true|이미지 경로(URI)


- Response

변수명| 타입  |required|설명
  ---|-----|---|---|
class_id|Inteter|true|결과
image_url|String|true|판정 이미지 경로(URI)
