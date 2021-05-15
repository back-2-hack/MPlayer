play = '''
MDFloatingActionButton:
    icon: "play"
    md_bg_color: app.theme_cls.primary_color
    elevation_normal: 12
    pos_hint  : {'center_x':0.5,'center_y':0.1}
'''
pause = '''
MDFloatingActionButton:
    icon: "pause"
    md_bg_color: app.theme_cls.primary_color
    elevation_normal: 15
    pos_hint  : {'center_x':0.5,'center_y':0.1}
'''
forward = '''
MDFloatingActionButton:
    icon: "step-forward"
    md_bg_color: app.theme_cls.primary_color
    elevation_normal: 12
    pos_hint  : {'center_x':0.7,'center_y':0.1}
'''
backward = '''
MDFloatingActionButton:
    icon: "step-backward"
    md_bg_color: app.theme_cls.primary_color
    elevation_normal: 12
    pos_hint  : {'center_x':0.3,'center_y':0.1}
    pos_hint_x :None
    size:(20,20)
'''
bar = '''
MDProgressBar:
        id: progress
        pos_hint: {"center_y": .6}
        running_duration: 5
        catching_duration: 1.5
'''
msi = '''
MDIcon:
    halign: "center"
    icon: "music"
    size: [50,20]
'''