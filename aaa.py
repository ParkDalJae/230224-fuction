rubin = 1
print(rubin) #1

rubin = '바보'
print(rubin) #바보

kdt = {
  "삼백오호" : "홀쭉",
  "공욱재" : "안미남",
}
print(kdt["공욱재"]) #안미남

kdt_order = ["우리는","개발자","입니다."]
print(kdt_order[0]) #우리는

for index in kdt_order:
  print(index) #우리는 개발자 입니다.

def percent_calc(real_value, total_value) : 
  result = (real_value/total_value)*100
  return result
print(percent_calc(50,160))