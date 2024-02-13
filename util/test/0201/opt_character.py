opt_character = ' ()+-./01234569ACDFGILQSTWabeghimnoprstuz~°กขคงจฉชซฑณดตถทธนบปผฝพฟภมยรลวศษสหฬอะัาำิีึืุูเแโใไๆ็่้๊์✓'

opt_character = '()+-./01234569ACDFGILQSTWabeghimnoprstuz~°กขคงจฉชซฑณดตถทธนบปผฝพฟภมยรลวศษสหฬอะัาำิีึืุูเแโใไๆ็่้๊์✓'.encode(
        'utf-8').decode('utf-8')

# 두 문자열을 합침
combined_text = "¢£¤¥!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZกขคฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮฤเแโใไะาุูิีืึั่้๊๋็์ำํฺฯๆ0123456789๑๒๓๔๕๖๗๘๙" + \
                    "()+-./01234569ACDFGILQSTWabeghimnoprstuz~°กขคงจฉชซฑณดตถทธนบปผฝพฟภมยรลวศษสหฬอะัาำิีึืุูเแโใไๆ็่้๊์✓"

# 중복 제거
unique_combined_text = ''.join(sorted(set(combined_text), key=combined_text.index))
# ¢£¤¥!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZกขคฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮฤเแโใไะาุูิีืึั่้๊๋็์ำํฺฯๆ0123456789๑๒๓๔๕๖๗๘๙°✓
# 결과 출력
print(unique_combined_text)