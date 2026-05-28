
init python:
    def mg_click():
        store.mg_count += 1
        if store.mg_count >= 30:
            store.mg_state = "success"
            store.mg_result = True
            renpy.restart_interaction()

    def mg_countdown_tick():
        if store.mg_countdown > 1:
            store.mg_countdown -= 1
        else:
            store.mg_state = "playing"
            import time
            store.mg_start_time = time.time()
        renpy.restart_interaction()

    def mg_timer_tick():
        import time
        if store.mg_state == "playing":
            store.mg_time_left = max(0.0, 5.0 - (time.time() - store.mg_start_time))
            if store.mg_time_left <= 0.0:
                store.mg_state = "fail"
                store.mg_result = False
            renpy.restart_interaction()

screen minigame_ep2():
    modal True
    add Solid("#000000AA")

    if mg_state == "countdown":
        timer 1.0 action Function(mg_countdown_tick) repeat True
        text "[mg_countdown]" xalign 0.5 yalign 0.5 size 120 bold True color "#ffffff"
        text "준비하세요!" xalign 0.5 ypos 0.65 size 40 color "#aaaaaa"

    elif mg_state == "playing":
        timer 0.05 action Function(mg_timer_tick) repeat True

        bar value mg_time_left range 5.0 xalign 0.5 yalign 0.1 xsize 600 ysize 30
        text "클릭: [mg_count] / 30" xalign 0.5 ypos 0.15 size 40 bold True color "#ffffff"

        imagebutton:
            xalign 0.5
            yalign 0.5
            idle Frame(Solid("#4488ff"), 200, 200)
            hover Frame(Solid("#66aaff"), 200, 200)
            action Function(mg_click)
            xysize (200, 200)

        text "눌러라!!" xalign 0.5 ypos 0.75 size 36 color "#aaaaaa"

    elif mg_state == "success":
        timer 1.5 action Return()
        text "성공!" xalign 0.5 yalign 0.45 size 100 bold True color "#44ff88"
        text "30회 완료!" xalign 0.5 yalign 0.55 size 40 color "#ffffff"

    elif mg_state == "fail":
        timer 1.5 action Return()
        text "실패..." xalign 0.5 yalign 0.45 size 100 bold True color "#ff4444"
        text "시간 초과" xalign 0.5 yalign 0.55 size 40 color "#ffffff"