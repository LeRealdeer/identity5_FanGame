# ─────────────────────────────────────
# 캐릭터 선언
# ─────────────────────────────────────
define n = Character("[player_name]", color="#ffffff")
define ng = Character("나이팅게일", color="#c8a2c8")
define pf = Character("조향사", color="#f9a8d4")
define pr = Character("탐사원", color="#93c5fd")
define na = Character("나이아스", color="#6ee7b7")
define se = Character("선지자", color="#fde68a")
define ge = Character("미치코", color="#fca5a5")
define nw = Character("이타콰", color="#a5b4fc")
define th = Character("도둑", color="#d1d5db")
define wc = Character("우는광대", color="#fb923c")
define cb = Character("카우보이", color="#fbbf24")
define aq = Character("골동품 상인", color="#a3e635")
define me = Character("용병", color="#94a3b8")
define fw = Character("포워드", color="#f87171")
define en = Character("주술사", color="#e879f9")
define ps = Character("샤먼", color="#67e8f9")
define ri = Character("리퍼", color="#cbd5e1")
define gk = Character("공장장", color="#fdba74")

# ─────────────────────────────────────
# 변수 선언 (초기값)
# ─────────────────────────────────────
default player_name = "탐정"
default meta_sense = 0
default immersion = 0
default fame = 0
default ep3_hunter_rescue = False

# ─────────────────────────────────────
# 게임 시작
# ─────────────────────────────────────
label start:
    jump opening_title